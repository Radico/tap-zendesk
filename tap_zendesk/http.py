from datetime import datetime
import base64

import singer
import requests
from singer import metrics
import backoff

logger = singer.get_logger()

BASE_URL = 'https://{domain}.zendesk.com/api/{version}/{resource}.json'
INCREMENTAL_URL = 'https://{domain}.zendesk.com/api/{version}/incremental/{resource}.json'


class RateLimitException(Exception):
    pass


def _join(a, b):
    return a.rstrip("/") + "/" + b.lstrip("/")


class Client(object):
    MAX_ITEMS = 1000
    API_VERSION = 'v2'
    RATE_LIMIT_PAUSE = 30

    def __init__(self, config):
        self.api_token = config.get("api_token")
        self.email = config.get("email")
        self.domain = self.clean_domain(config)
        self.session = requests.Session()

    def prepare_and_send(self, request):
        request.headers["Authorization"] = "Basic %s" % self.auth_tuple()

        return self.session.send(request.prepare())

    def clean_domain(self, config):
        return config.get('domain').split('.')[0]

    def url(self, resource):

        if resource == 'satisfaction_ratings':
            url_to_format = BASE_URL
        else:
            url_to_format = INCREMENTAL_URL

        return url_to_format.format(
            domain=self.domain,
            version=self.API_VERSION,
            resource=resource
        )

    def auth_tuple(self):
        """
        {email_address}/token:{api_token}
        then base64 encoded and sent as
        Authorization: Basic b64_encoded_str
        :return:
        """
        return base64.b64encode(
            '{email_address}/token:{api_token}'.format(
                email_address=self.email,
                api_token=self.api_token
            ).encode('ascii')).decode("utf-8")

    def create_get_request(self, path, params):
        return requests.Request(method="GET", url=self.url(path),
                                params=params)

    @backoff.on_exception(backoff.expo,
                          RateLimitException,
                          max_tries=10,
                          factor=2)
    def request_with_handling(self, request, tap_stream_id):
        with metrics.http_request_timer(tap_stream_id) as timer:
            response = self.prepare_and_send(request)
            timer.tags[metrics.Tag.http_status_code] = response.status_code
        if response.status_code in [429, 503]:
            raise RateLimitException()
        response.raise_for_status()
        return response.json()

    def GET(self, path, params, *args, **kwargs):
        req = self.create_get_request(path, params)
        return self.request_with_handling(req, *args, **kwargs)
