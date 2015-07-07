# -*- coding: utf-8 -*-

"""
    The core service, do the main business.
"""


class Eventloop(object):

    def __init__(self):
        self.unfinished_tasks = []
        self.finished

    def check_for_updates(self):
        """
        check for new update and sync to local DB
        """
        pass

    def handle_tasks(self):
        """
        exec the tasks on localhost
        """
        pass

    def save_():
        pass

    def event_loop(self):
        while(True):
            print 'EventLoop'
            return True
