# -*- coding: utf-8 -*-

from empire_agent.network.request import http_get, http_patch
from empire_agent.system import shell
from empire_agent.util import save_obj, load_obj
from multiprocessing.dummy import Pool as ThreadPool
from time import time, sleep
import json
import os


class Task(object):

    def __init__(self, config):
        self.config = config
        self.unfinished_tasks = []
        self.finished_tasks = []
        self.tasks = []

    def check_for_updates(self):
        """
        Check for new update and sync to local DB
        TODO: if self.config.server is None, try to log
        """
        if self.config.server is None:
            print 'config error'
            return None

        request_tasks_url = 'http://' + self.config.server + '/api/tasks/new'
        print 'start request'
        start = time()
        response = False
        response = http_get(request_tasks_url)
        if (response is not None):
            self.tasks.extend(response)
        end = time()
        print 'duration: ', int(end - start)

        if os.path.isfile(self.config.cache_file):
            try:
                self.unfinished_tasks = load_obj(self.config.cache_file)
            except:
                print 'load object from file error'
        self.tasks.extend(self.unfinished_tasks)
        self.unfinished_tasks = []

    def handle(self):
        """
        Execute the tasks on localhost
        """
        pool = ThreadPool(10)
        pool.map(self.run_command, self.tasks)
        pool.close()
        pool.join()
        pass

    def run_command(self, task):
        # TODO: handle task run fail
        file = task.get('file', None)
        finished = task.get('finished', None)
        if file:
            task['result'] = shell.exec_shell_script(file)

    def send_back_data(self):
        """
        send all result, produced by tasks
        """
        while(len(self.tasks) > 0):
            task = self.tasks.pop()
            data = {"_id": task['_id'], 'result': task['result']}
            headers = {'Content-type': 'application/json'}
            url = "http://" + self.config.server + "/api/tasks/" + task['_id']
            response = http_patch(url, data, headers)
            if response is None:
                self.unfinished_tasks.append(task)
            else:
                if(response.status_code is 200):
                    print 'remove task'
                else:
                    self.unfinished_tasks.append(task)

        save_obj(self.unfinished_tasks, self.config.cache_file)
        print 'len unfinished_tasks: ', len(self.unfinished_tasks)
        print 'sent_back_result'

    def sleep(self):
        """
        Sleep for every loop
        """
        sleep(1)
        # sleep(self.config.interval)
        print 'sleep 1'
        pass
