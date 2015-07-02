# -*- coding: utf-8 -*-

from time import sleep
from .daemon import Daemon
from .config import Config
from .task import Task

import subprocess
import requests
import urllib2
import json

def launch(config):
    interval = config.interval
    tasks = Task(config)

    while True:
        # update from server
        tasks.get_updates() # check whether have new updates

        # run tasks
        # run all task (including old tasks) & save result
        tasks.handle_tasks()

        # send result to center
        tasks.send_back_result()

        # set interval for next run
        interval = tasks.get_interval()
        tasks.set_interval(interval)
        tasks.sleep()

class EmpireAgent(Daemon):
    def run(self, config):
        launch(config)
