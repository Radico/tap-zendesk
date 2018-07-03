# tap-zendesk

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from [Zendesk](https://developer.zendesk.com/rest_api/docs/core/introduction)
- Extracts the following resources:
  - [Users](https://developer.zendesk.com/rest_api/docs/core/users)
  - [Tickets](https://developer.zendesk.com/rest_api/docs/core/tickets)
  - [Ticket events](https://developer.zendesk.com/rest_api/docs/core/ticket_metrics)
  - [Ticket metric events](https://developer.zendesk.com/rest_api/docs/core/ticket_metric_events)
  - [Satisfaction ratings](https://developer.zendesk.com/rest_api/docs/core/satisfaction_ratings)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state
