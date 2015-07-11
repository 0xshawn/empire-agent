# -*- coding: utf-8 -*-

"""
    Shell related
"""

import subprocess


def exec_shell_script(command):
    # TODO: handle task run fail
    """run command"""
    (output, err) = subprocess.Popen(
        command, stdout=subprocess.PIPE, shell=True).communicate()
    return output


def parse_args():
    pass
