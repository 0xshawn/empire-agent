# -*- coding: utf-8 -*-

"""
    The core service, do the main business.
"""

from time import sleep


class Eventloop(object):

    def __init__(self, config):
        self.config = config
        self.unfinished = []
        self.finished = []

    def check_for_updates(self):
        """
        Check for new update and sync to local DB
        """
        pass

    def handle_tasks(self):
        """
        Execute the tasks on localhost
        """
        pass

    def send_back_data(self):
        """
        send all result, produced by tasks
        """
        pass

    def sleep(self):
        """
        Sleep for every loop
        """
        sleep(1)
        print 'sleep 1'
        pass

    def event_loop(self):
        while(True):
            self.check_for_updates()
            self.handle_tasks()
            self.send_back_data()
            self.sleep()
