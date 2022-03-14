# -*- coding: utf-8 -*-

from time import sleep
from time import time
from multiprocessing.dummy import Pool as ThreadPool
import subprocess
import urllib2
import json
import socket
import traceback
import pickle
import requests
import os.path


class Task(object):

    def __init__(self, config):
        self.config = config
        self.tasks = []
        self.unfinished_tasks = []

    def get_updates(self):
        """get update and save to self.tasks"""
        if self.config.server is None:
            print 'config error'
            exit(0)

        request_tasks_url = 'http://' + self.config.server + '/api/tasks/new'
        print 'start request'
        start = time()
        req = False
        req = Task.get(request_tasks_url)
        if (req is not None):
            response = json.load(req)

        print 'duration: ', int(end - start)

        self.tasks = []
        if os.path.isfile(self.config.cache_file):
            try:
                self.unfinished_tasks = self.load_obj(
                    self.config.cache_file)
            except:
                print 'load object from file error'
        self.tasks.extend(self.unfinished_tasks)
        if response:
            self.tasks.extend(response)
        self.unfinished_tasks = []

    def handle_tasks(self):
        pool = ThreadPool(10)
        pool.map(self.run_command, self.tasks)
        pool.close()
        pool.join()

        return True

    def run_command(self, task):
        # TODO: handle task run fail
        """run command"""
        file = task.get('file', None)
        finished = task.get('finished', None)
        if file:
            (output, err) = subprocess.Popen(
                task['file'], stdout=subprocess.PIPE, shell=True).communicate()
            task['result'] = output
        return True

    def send_back_result(self):
        """send back to server immediatelly"""
        print 'we have ' + str(len(self.tasks)) + ' tasks'
        while(len(self.tasks) > 0):
            task = self.tasks.pop()
            data = {"_id": task['_id'], 'result': task['result']}
            headers = {'Content-type': 'application/json'}
            url = "http://" + self.config.server + "/api/tasks/" + task['_id']
            response = requests.patch(
                url, data=json.dumps(data), headers=headers)
            print response.status_code
            if(response.status_code is 200):
                print 'remove task'
            else:
                self.unfinished_tasks.append(task)
        self.save_obj(self.unfinished_tasks, self.config.cache_file)
        print 'sent_back_result'
        print len(self.tasks)
        return True

    def get_interval(self):
        return 10

    def set_interval(self, interval):
        self.config.interval = int(interval)

    def sleep(self):
        sleep(self.config.interval)

    def send_again(self):
        print 'send_again'
        return True

    def save_obj(self, obj, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    def load_obj(self, file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)

    def post_data_to_server(self, url, data):
        return True
