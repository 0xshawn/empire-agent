# -*- coding: utf-8 -*-

"""
    Provide command `empire`
"""

from empire_agent import EmpireAgent
from empire_agent.config import Config
import os


def main():
    print 'start empire'
    config = Config('/etc/empire-agent.json')
    pid_file = config.pid_file
    empire = EmpireAgent(pid_file)

    empire.run(config)

    # if os.path.isfile(pid_file):
    #     empire.stop()
    # else:
    #     empire.start(config)


if __name__ == '__main__':
    main()