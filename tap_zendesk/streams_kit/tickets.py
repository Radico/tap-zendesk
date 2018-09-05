from tap_kit.streams import Stream


class TicketsStream(Stream):

    stream = 'tickets'

    meta_fields = dict(
        key_properties=['id'],
        replication_key='updated_at',
        valid_replication_keys=['updated_at'],
        incremental_search_key=['start_time'],
        replication_method='incremental',
        selected_by_default=False
    )
    schema = \
{
  "properties": {
    "organization_id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "requester_id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "is_public": {
      "type": [
        "null",
        "boolean"
      ]
    },
    "description": {
      "type": [
        "null",
        "string"
      ]
    },
    "follower_ids": {
      "items": {
        "type": [
          "null",
          "integer"
        ]
      },
      "type": [
        "null",
        "array"
      ]
    },
    "submitter_id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "generated_timestamp": {
      "type": [
        "null",
        "integer"
      ]
    },
    "brand_id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "group_id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "type": {
      "type": [
        "null",
        "string"
      ]
    },
    "recipient": {
      "type": [
        "null",
        "string"
      ]
    },
    "collaborator_ids": {
      "items": {
        "type": [
          "null",
          "integer"
        ]
      },
      "type": [
        "null",
        "array"
      ]
    },
    "tags": {
      "items": {
        "type": [
          "null",
          "string"
        ]
      },
      "type": [
        "null",
        "array"
      ]
    },
    "has_incidents": {
      "type": [
        "null",
        "boolean"
      ]
    },
    "created_at": {
      "type": [
        "null",
        "string"
      ],
      "format": "date-time"
    },
    "raw_subject": {
      "type": [
        "null",
        "string"
      ]
    },
    "status": {
      "type": [
        "null",
        "string"
      ]
    },
    "updated_at": {
      "type": [
        "null",
        "string"
      ],
      "format": "date-time"
    },
    "custom_fields": {
      "items": {
        "properties": {
          "id": {
            "type": [
              "null",
              "integer"
            ]
          },
          "value": { }
        },
        "type": [
          "null",
          "object"
        ]
      },
      "type": [
        "null",
        "array"
      ]
    },
    "url": {
      "type": [
        "null",
        "string"
      ]
    },
    "allow_channelback": {
      "type": [
        "null",
        "boolean"
      ]
    },
    "allow_attachments": {
      "type": [
        "null",
        "boolean"
      ]
    },
    "due_at": {
      "type": [
        "null",
        "string"
      ],
      "format": "date-time"
    },
    "followup_ids": {
      "items": {
        "type": [
          "null",
          "integer"
        ]
      },
      "type": [
        "null",
        "array"
      ]
    },
    "priority": {
      "type": [
        "null",
        "string"
      ]
    },
    "assignee_id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "subject": {
      "type": [
        "null",
        "string"
      ]
    },
    "external_id": {
      "type": [
        "null",
        "string"
      ]
    },
    "via": {
      "properties": {
        "source": {
          "properties": {
            "from": {
              "properties": {
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "ticket_id": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "address": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "subject": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "to": {
              "properties": {
                "address": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "rel": {
              "type": [
                "null",
                "string"
              ]
            }
          },
          "type": [
            "null",
            "object"
          ]
        },
        "channel": {
          "type": [
            "null",
            "string"
          ]
        }
      },
      "type": [
        "null",
        "object"
      ]
    },
    "ticket_form_id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "satisfaction_rating": {
      "type": [
        "null",
        "object"
      ],
      "properties": {
        "id": {
          "type": ["null", "integer"]
        },
        "assignee_id": {
          "type": ["null", "integer"]
        },
        "group_id": {
          "type": ["null", "integer"]
        },
        "reason_id": {
          "type": ["null", "integer"]
        },
        "requester_id": {
          "type": ["null", "integer"]
        },
        "ticket_id": {
          "type": ["null", "integer"]
        },
        "updated_at": {
            "type": ["null", "string"],
            "format": "date-time"
        },
        "created_at": {
            "type": ["null", "string"],
            "format": "date-time"
        },
        "url": {
            "type": ["null", "string"]
        },
        "score": {
            "type": ["null", "string"]
        },
        "reason": {
            "type": ["null", "string"]
        },
        "comment": {
            "type": ["null", "string"]
        }
      }
    },
    "sharing_agreement_ids": {
      "type": [
        "null",
        "array"
      ],
      "items": {
        "type": [
          "null",
          "integer"
        ]
      }
    },
    "email_cc_ids": {
      "type": [
        "null",
        "array"
      ],
      "items": {
        "type": [
          "null",
          "integer"
        ]
      }
    },
    "problem_id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "forum_topic_id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "satisfaction_rating": {
      "type": [
        "null",
        "object",
        "string"
      ],
      "properties": {}
    }
  },
  "type": [
    "null",
    "object"
  ]
}