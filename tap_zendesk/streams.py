import pendulum

import singer

from .schemas import IDS

logger = singer.get_logger()


def metrics(tap_stream_id, records):
    with singer.metrics.record_counter(tap_stream_id) as counter:
        counter.increment(len(records))


def write_records(tap_stream_id, records):
    singer.write_records(tap_stream_id, records)
    metrics(tap_stream_id, records)


class BOOK(object):
    USERS = [IDS.USERS, 'updated_at']
    TICKETS = [IDS.TICKETS, 'updated_at']
    SATISFACTION_RATINGS = [IDS.SATISFACTION_RATINGS, 'updated_at']
    TICKET_EVENTS = [IDS.TICKET_EVENTS, 'updated_at']
    TICKET_METRIC_EVENTS =[IDS.TICKET_METRIC_EVENTS, 'updated_ad']

    @classmethod
    def return_bookmark_path(cls, stream):
        return getattr(cls, stream.upper())

    @classmethod
    def get_incremental_syncs(cls):
        syncs = []
        for k, v in cls.__dict__.items():
            if not k.startswith("__") and not isinstance(v, classmethod):
                if len(v) > 1:
                    syncs.append(k)

        return syncs

    @classmethod
    def get_full_syncs(cls):
        syncs = []
        for k, v in cls.__dict__.items():
            if not k.startswith("__") and not isinstance(v, classmethod):
                if len(v) == 1:
                    syncs.append(k)

        return syncs


def sync(context):
    for stream in context.selected_stream_ids:
        if stream.upper() in BOOK.get_incremental_syncs():
            bk = call_stream_incremental(context, stream)
            save_state(context, stream, bk)


def call_stream_incremental(ctx, stream):
    ctx.update_start_date_bookmark(BOOK.return_bookmark_path(stream))
    last_updated = ctx.get_bookmark(BOOK.return_bookmark_path(stream))

    params = {"start_time": pendulum.parse(last_updated).int_timestamp}

    while True:
        logger.info("Extracting users since %s" % timestamp_to_iso8601(
            params['start_time']))

        res = ctx.client.GET(stream, params, stream)

        write_records(stream, res.get(stream))

        if res['count'] == 1000:
            # returns max 1000, if less than 1000 then end of records
            # https://developer.zendesk.com/rest_api/docs/core/incremental_export#pagination
            params['start_time'] = res['end_time']

        else:
            break

    return get_state_to_save(res, last_updated)


def get_state_to_save(res, last_updated):
    if res.get('end_time'):
        return timestamp_to_iso8601(res['end_time'])
    else:
        return last_updated


def timestamp_to_iso8601(ts):
    return pendulum.from_timestamp(int(ts)).to_iso8601_string()

def save_state(context, stream, bk):
    context.set_bookmark(BOOK.return_bookmark_path(stream), bk)
    context.write_state()
