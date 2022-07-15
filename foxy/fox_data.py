import datetime
import time

class Env_Meta:

    def __init__(self, env_name):
        
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
        
        return 

    def add_version(self, package_name, package_version):

        self.versions.append(
            [
                time.time(),
                package_name,
                package_version
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


