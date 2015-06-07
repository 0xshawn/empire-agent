# -*- coding: utf-8 -*-

import json

class Config(object):
    def __init__(self, config_path):
        with open(config_path) as file_content:
             config_json = json.load(file_content)
        self.interval = config_json.get('interval', 300) # interval default: 5 mins
        self.pid_file = config_json.get('pid_file', '/tmp/empire-agent.pid')
