# -*- coding: utf-8 -*-


import json


class Config(object):

    def __init__(self, config_path):
        with open(config_path) as file_content:
            config_json = json.load(file_content)
        # interval default: 5 mins
        self.interval = config_json.get('interval', 300)

        self.pid_file = config_json.get('pid_file', '/tmp/empire-agent.pid')
        self.server = config_json.get('server', None)
        self.cache_file = config_json.get('cache', '/tmp/empire-agent.cache')

        # TODO: config from shell args
        self.debug = True
