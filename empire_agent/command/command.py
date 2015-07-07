# -*- coding: utf-8 -*-

import subprocess


def exec_command(command):
    # TODO: handle task run fail
    """run command"""
    (output, err) = subprocess.Popen(
        command, stdout=subprocess.PIPE, shell=True).communicate()
    return output
