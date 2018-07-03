#!/usr/bin/env python3
import os
import singer
from singer import utils


class IDS(object):
    USERS = 'users'
    TICKETS = 'tickets'
    TICKET_EVENTS = 'ticket_events'
    TICKET_METRIC_EVENTS = 'ticket_metric_events'
    SATISFACTION_RATINGS = 'satisfaction_ratings'


stream_ids = [getattr(IDS, x) for x in dir(IDS)
              if not x.startswith('__')]

PK_FIELDS = {
    IDS.USERS: ['id'],
    IDS.TICKETS: ['id'],
    IDS.TICKET_EVENTS: ['id'],
    IDS.TICKET_METRIC_EVENTS: ['id'],
    IDS.SATISFACTION_RATINGS: ['id'],
}


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


def load_schema(tap_stream_id):
    path = "schemas/{}.json".format(tap_stream_id)
    return utils.load_json(get_abs_path(path))


def load_and_write_schema(tap_stream_id):
    schema = load_schema(tap_stream_id)
    singer.write_schema(tap_stream_id, schema, PK_FIELDS[tap_stream_id])
