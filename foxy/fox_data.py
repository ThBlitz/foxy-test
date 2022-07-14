import datetime
import time

class Env_Meta:

    def __init__(self, env_name, ENV_PATH = None):
        
        if ENV_PATH == None:
            self.env_name = env_name
            self.created_unix_epoch = time.time()
            self.total_versions = 0
            self.versions = [
                [
                    time.time(), 
                    f'virtualenv {env_name}',
                    '0.0.0'
                ]
            ]
        else:
            pass
        return 

    def add_version(self, package_name, package_version):

        self.versions.append(
            [
                time.time(),
                package_name,
                package_version
            ]
        )
        return 

    def save_meta(self, env_name):
        return

    def load_meta(self, ):
        return 