import sys
import os
import stdout

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':

    command = str(sys.argv[1])
    arg_2 = str(sys.argv[2])
    arg_3 = str(sys.argv[3])
    virtual_env_var = str(sys.argv[4])
    envs_path = str(sys.argv[5])

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
    if virtual_env_var == "__none__":
        virtual_env_var = None 
        permission.append('o')
    else:
        permission.append('i')

    if command not in list_of_commands:
        stdout.print_error(0)
    else:
        print('right command')
    
        


    



