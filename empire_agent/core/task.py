# -*- coding: utf-8 -*-

class Task(object):
    def __init__(self, config):
        self.config = config

        self.task = Task(self.config)

        self.unfinished_tasks = []
        self.finished_tasks = []

    def check_for_updates(self):
        """
        Check for new update and sync to local DB
        """
        # self.unfinished = task.
        pass

    def handle(self):
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
    def __init__(self, ):
        pass