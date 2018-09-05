from tap_kit import TapExecutor, BaseClient, main_method
import base64

from .streams_kit import STREAMS

REQUIRED_CONFIG_KEYS = ["start_date", "domain", "email", 'api_token']


class ZendeskTap(TapExecutor):
    url = 'https://{domain}.zendesk.com/api/v2/{stream}.json'
    pagination_type = 'precise'
    replication_key_format = 'timestamp'
    res_json_key = 'STREAM'
    auth_type = 'custom'

    def generate_api_url(self, stream):
        if stream.stream == 'satisfaction_ratings':
            url_to_format = 'https://{domain}.zendesk.com/api/v2/incremental/{stream}.json'
        else:
            url_to_format = self.url

        return url_to_format.format(
            domain=self.clean_domain(self.config),
            stream=stream.stream
        )

    def clean_domain(self, config):
        return config.get('domain').split('.')[0]

    def generate_auth(self):
        return base64.b64encode(
            '{email_address}/token:{api_token}'.format(
                email_address=self.config['email'],
                api_token=self.config['api_token']
            ).encode('ascii')).decode("utf-8")


def main():
    main_method(
        REQUIRED_CONFIG_KEYS,
        ZendeskTap,
        BaseClient,
        STREAMS
    )


if __name__ == '__main__':
    main()
