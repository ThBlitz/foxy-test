import stdout
import time
import subprocess
import os
import shutil
import sys
import json
import get_versions
import fox_data

list_of_commands = {
        'info': ('a'),
        'commands': ('a'),
        'list_envs': ('a'),
        'env_info': ('i', 'o'),
        'create': ('o'),
        'install': ('i'),
        'remove': ('o'),
        'clone': ('o'),
        'rename': ('o'),
        'list_versions': ('o', 'i'),
        'clone_version': ('o', 'i'),
        'change_version': ('o', 'i'),
        'settings': ('i', 'o')
}

env_meta = {
    'env_name':None,
    'python_version':None,
    'total_versions':0,
    'versions':[
        {
            'created': None,
            'created_unix_epoch':None,
            'pip_list': [None]
        }
    ]
}

def get_envs_dir_list(ENVS_PATH):
    envs_dir_list = set([x for x in os.scandir(ENVS_PATH) if x.is_dir() ])
    return envs_dir_list

def info(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH):
    stdout.print_info(0)
    return

def commands(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH):
    stdout.print_messg(list_of_commands.keys(), lambda x: 'fox ' + x)
    return

def list_envs(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH):
    envs_dir_list = get_envs_dir_list(ENVS_PATH)
    envs = [x.name for x in envs_dir_list]
    stdout.print_messg(envs)
    return 
    
def env_info(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH):
    print('needs implementation')
    return

def create(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH):
    
    if VIRTUAL_ENV_VAR == None:
        final_path = os.path.join(ENVS_PATH, arg_2)
        y_or_n = None
        for x in get_envs_dir_list(ENVS_PATH): 
            if final_path in x.path:
                y_or_n = stdout.print_prompt(0)
                break

        if y_or_n == None or y_or_n == 'y': 

            if y_or_n == 'y':
                remove(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH)
            
            output = subprocess.run(
                f'virtualenv --clear {final_path}',
                shell=True, stdout=subprocess.PIPE
            ).stdout.decode('utf-8')
            
            env_meta = fox_data.Env_Meta(arg_2)

            final_path = os.path.join(final_path, 'env_meta.json')

            with open(final_path, 'w') as f:
                json.dump(env_meta.json(), f, indent = 4)

            ####################
            print(output)
            ####################
    else:
        stdout.print_error(1)
    return

def remove(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH):

    if VIRTUAL_ENV_VAR == None:
        final_path = os.path.join(ENVS_PATH, arg_2)
        y_or_n = None
        for x in get_envs_dir_list(ENVS_PATH): 
            if final_path in x.path:
                y_or_n = stdout.print_prompt(1)
                break
        
        if y_or_n == 'y':
            shutil.rmtree(final_path)
            os.remove(os.path.join(ENVS_PATH, f'{arg_2}.json'))

        elif y_or_n == None:
            stdout.print_error(2)

    else:
        stdout.print_error(1)

def build(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH):
    # fox build arg_2(new env_name) arg_3(file path)

    if arg_2 != None and arg_3 != None:
        if arg_3 == '.':
            #.fox files 
            pass
    else:
        stdout.print_error(3)

    # create
    # update
    return 

def clone(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH):
    
    if VIRTUAL_ENV_VAR == None:
        if arg_2 != None and arg_3 != None:
            final_path = os.path.join(ENVS_PATH, arg_2)
            env_exists = False
            for x in get_envs_dir_list(ENVS_PATH): 
                if final_path in x.path:
                    env_exists = True
                    break
            if env_exists:
                pass
                # create(arg_3, None, VIRTUAL_ENV_VAR, ENVS_PATH)
            else:
                stdout.print_error(2)

        else:
            stdout.print_error(3)
    
    else:
        stdout.print_error(1)
    
    return

def install(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH):

    if VIRTUAL_ENV_VAR != None:
        
        if arg_3 == None:
            pip_command = [f'{VIRTUAL_ENV_VAR}/bin/pip', 'install', arg_2, '--no-cache-dir']
            arg_3 = get_versions.get_version(arg_2)
        else:
            pip_command = [f'{VIRTUAL_ENV_VAR}/bin/pip', 'install', f'{arg_2}=={arg_3}', '--no-cache-dir']

        stdout.print_messg(pip_command)

        # subprocess.run(
        #     pip_command
        # )

        env_meta = fox_data.Env_Meta(
            os.path.join(VIRTUAL_ENV_VAR, 'env_meta.json'), 
            type_ = 'path'
        )

        env_meta.add_version(arg_2, arg_3)

        # env_meta.save(os.path.join(VIRTUAL_ENV_VAR, 'env_meta.json'))

    else:
        stdout.print_error(1)

    return