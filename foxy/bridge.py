import sys
import os
import stdout
import operations

sys.path.append(os.path.dirname(os.path.abspath(__file__)))




if __name__ == '__main__':

    command = str(sys.argv[1])
    arg_2 = str(sys.argv[2])
    arg_3 = str(sys.argv[3])
    VIRTUAL_ENV_VAR = str(sys.argv[4])
    ENVS_PATH = str(sys.argv[5])

    permissions = ('o', 'i', 'a') # inside, outside, anywhere

    list_of_commands = {
        'info': ('a'),
        'commands': ('a'),
        'list_envs': ('a'),
        'env_info': ('i', 'o'),
        'create': ('o'),
        'remove': ('o'),
        'clone': ('o'),
        'rename': ('o'),
        'list_versions': ('o', 'i'),
        'clone_version': ('o', 'i'),
        'change_version': ('o', 'i'),
        'settings': ('i', 'o')
    }
    
    permission = []
    permission.append('a')
    if VIRTUAL_ENV_VAR == "__none__":
        VIRTUAL_ENV_VAR = None 
        permission.append('o')
    else:
        permission.append('i')

    if command not in list_of_commands:
        stdout.print_error(0)
    else:
        eval(f'operations.{command}(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH)')
        
    
        


    



