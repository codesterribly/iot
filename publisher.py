#!/usr/bin/env python

import json
import awsiot
import logging


if __name__ == "__main__":
    parser = awsiot.iot_arg_parser()
    args = parser.parse_args()

    publisher = awsiot.MQTT(args.endpoint, args.rootCA, args.cert, args.key)

    logging.basicConfig(filename=awsiot.LOG_FILE, level=args.log_level, format=awsiot.LOG_FORMAT)

    message = {'foo': 'bar'}
    for t in args.topic:
        publisher.publish(t, json.dumps(message))

