# -*- coding: utf-8 -*-

from time import sleep

class Task(object):
    def __init__(self, config):
        self.config = config

    def get_updates(self):
        print 'get_updates'

    def run_and_save_result(self):
        print 'run_and_save_result'

    def send_back_result(self):
        print 'send_back_result'

    def get_interval(self):
        return self.config.interval

    def set_interval(self, interval):
        self.config.interval = int(interval)

    def sleep(self):
        sleep(self.config.interval)
