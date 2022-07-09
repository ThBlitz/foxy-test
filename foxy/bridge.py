import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':

    command = str(sys.argv[1])
    arg_2 = str(sys.argv[2])
    arg_3 = str(sys.argv[3])

    list_of_commands = [
        'info',
        'commands',
        'lsit_envs',
        'env_info',
        'create',
        'remove',
        'clone',
        'rename',
        'list_versions',
        'clone_version',
        'change_version',
        'settings'
    ]
    
    all_commands = set(list_of_commands)

    
        


    



