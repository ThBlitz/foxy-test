import datetime
import time
import os
import sys
import json


class Env_Meta:

    def __init__(self, env_name, type_ = 'new'):
        
        if type_ == 'new':
            self.env_name = env_name
            self.created = time.time()
            self.python_version = sys.version
            self.total_versions = 0
            self.versions = [
                [
                    time.time(), 
                    f'virtualenv {env_name}',
                    '0.0.0'
                ]
            ]

        elif type_ == 'path':
            env_meta = {}
            with open(env_name, 'r') as file:
                dict = json.load(file)
            env_meta = dict
            self.env_name = env_meta['env_name']
            self.created = env_meta['created']
            self.python_version = env_meta['python_version']
            self.total_versions = env_meta['total_versions']
            self.versions = env_meta['versions']

        return 

    def add_version(self, package_name, package_version):

        self.versions.append(
            [
                time.time(),
                package_name,
                str(package_version)
            ]
        )
        self.total_versions = len(self.versions) - 1
        return 

    def json(self):

        return {
            'env_name':self.env_name,
            'created':self.created,
            'python_version':self.python_version,
            'total_versions':self.total_versions,
            'versions':self.versions
        }

    def save(self, path):

        with open(path, 'w') as f:
            json.dump(self.json(), f, indent = 4)

        return


