#!/usr/bin/env python

from daemon import Daemon
from time import sleep
import subprocess
import requests
import urllib2
import json
import os

def Task():
    def __init__(self, token):
        self.token = token
    return True
def Config():
    return True

def start(config):
    interval = config.interval
    tasks = Task(config.token)

    while True:
        # update from server
        tasks.get_updates() # check whether have new updates

        # run tasks
        # run all task (including old tasks) & save result
        tasks.run_and_save_result()

        # send result to center
        if tasks.send_back_result() is False:
            times = 1;
            while (times < 10):
                sleep(10 + 2 * 10)
                if tasks.send_again():
                    break

        # set interval for next run
        interval = tasks.get_interval()
        config.set_interval(interval)
        sleep(interval)

if __name__ == '__main__':
    # run empire as daemon
    class Empire(Daemon):
        def run(self):
            start(config)

    config = Config('/path/to/config')
    pid_file = config.pid_file
    empire = Empire(pid_file)
    if os.path.isfile(pid_file):
        print 'Exit...'
        empire.stop()
    else:
        print 'Start...'
        empire.start()
