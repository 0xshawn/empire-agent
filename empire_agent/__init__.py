# -*- coding: utf-8 -*-

from .system import *
from .core import *


class EmpireAgent(system.daemon.Daemon):

    def run(self, config):
        app = core.produce.Eventloop(config)
        app.event_loop()
