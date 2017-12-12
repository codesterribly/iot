#!/usr/bin/env python

import argparse
import json
import awsiot
import logging

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--endpoint", required=True, help="Your AWS IoT custom endpoint")
    parser.add_argument("-r", "--rootCA", required=True, help="Root CA file path")
    parser.add_argument("-c", "--cert", required=True, help="Certificate file path")
    parser.add_argument("-k", "--key", required=True, help="Private key file path")
    parser.add_argument("-n", "--thing", help="Targeted thing name")

    parser.add_argument("-g", "--groupCA", default=None, help="Group CA file path")
    parser.add_argument("-m", "--mqttHost", default=None, help="Targeted mqtt host")

    parser.add_argument("-t", "--topic", default="/test", help="Targeted topic")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    publisher = awsiot.Publisher(args.endpoint, args.rootCA, args.cert, args.key)

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
        publisher.log_level = logging.DEBUG

    message = {}
    message['foo'] = 'bar'
    messageJson = json.dumps(message)
    logging.info("Publish {} to {}".format(messageJson, args.topic))
    publisher.publish(args.topic, messageJson)

