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

class ENV_META:

    def __init__(self, env_data = None):

        if env_data != None:
            self.__initialize(env_data)
        else:
            self.env_name = None
            self.created = time.time()
            self.python_version = sys.version
            self.total_versions = 0
            self.versions = [
                [
                    time.time(), 
                    f'virtualenv {self.env_name}',
                    '0.0.0'
                ]
            ]
        return
            
    def __initialize(self, env_data):
        self.env_name = env_data['env_name']
        self.created = env_data['created']
        self.python_version = env_data['python_version']
        self.total_versions = env_data['total_versions']
        self.versions = env_data['versions']
        return 

    def load(self, path):
        env_meta = {}
        with open(path, 'r') as file:
            env_meta = json.load(file)
        self.__initialize(env_meta)
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
    
    def export(self, path):
        lines = []
        lines.append(f'create {self.env_name}')
        for time, package, version in self.versions:
            lines.append(f'install {package} {version}')
        
        with open(path, 'w') as f:
            for line in lines:
                f.write(f"{line}\n")

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


class ENV_CLASS:

    def __init__(self, VIRTUAL_ENV_VAR, ENVS_PATH):
        self.ENVS_PATH = ENVS_PATH
        self.VIRTUAL_ENV_VAR = VIRTUAL_ENV_VAR
        self.env_meta = None

    def env_exists(self, env_name):
        path = os.path.join(self.ENVS_PATH, env_name)
        meta_file_path = os.path.join(path, 'env_meta.json')
        if os.path.isdir(path) and os.path.isfile(meta_file_path):
            return True
        return False
    
    def initialize(self):
        if self.VIRTUAL_ENV_VAR != None:
            env_name = os.path.basename(self.VIRTUAL_ENV_VAR)
            if self.env_exists(env_name):
                self.env_meta = ENV_META()
                meta_file_path = os.path.join(self.VIRTUAL_ENV_VAR, 'env_meta.json')
                self.env_meta.load(meta_file_path)
                return True
        return False

    def create_env_meta(self, env_name):
        self.env_meta = ENV_META()
        self.env_meta.env_name = env_name

    def is_active(self):
        if self.VIRTUAL_ENV_VAR != None:
            env_name = os.path.basename(self.VIRTUAL_ENV_VAR)
            if self.env_meta != None:
                if self.env_exists(env_name) and self.env_meta.env_name == env_name:
                    return True
        return False


