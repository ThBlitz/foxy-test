import stdout
import time
import subprocess
import os
import shutil
import sys
import json
import get_versions
import fox_data

args_to_operations = {
    'info': ('', 'info'),
    'commands': ('', 'commands'),
    'list envs': ('', 'list_envs'),
    'env info': ('i', 'env_info'),
    'env info more': ('i', 'env_info_more'),
    'info <env_name>': ('', 'env_info_outside'),
    'info <env_name> more': ('', 'env_info_outside_more'),
    'create <env_name>': ('o', 'create'),
    'create <env_name> overwrite': ('o', 'create_overwrite'),
    'remove <env_name>': ('o', 'remove'),
    'install <package_name> <package_version>': ('i', 'install'),
    'install <package_name>': ('i', 'install'),
    'clone <current_env> to <new_env>': ('o', 'clone'),
    'clone <new_env> from <current_env>': ('o', 'clone'),
    'clone <current_env> upto version <version_number> as <new_env>': ('o', 'clone'),
    'clone <new_env> upto version <version_number> from <current_env>': ('o', 'clone'),
    'export <file_name>': ('', 'export'),
    'build <file_path> to <env_name>': ('o', 'build'),
    'build <env_name> from <file_path>': ('o', 'build')
}


def info(env_obj, args, arg_tree, user_args):
    stdout.print_info(0)
    return

def commands(env_obj, args, arg_tree, user_args):
    recommends = arg_tree.recommend(['fox'])
    stdout.print_messg(recommends, lambda x: 'fox ' + ' '.join(x)) 
    return

def list_envs(env_obj, args, arg_tree, user_args):
    envs = [x.name for x in env_obj.envs_dir_list]
    stdout.print_messg(envs)
    return 

def env_info(env_obj, args, arg_tree, user_args):
    if env_obj.initialize() == True:
        if len(args) == 0:
            env_obj.env_meta.stdout_info()
        elif args[0] == 'more':
            env_obj.env_meta.stdout_info('versions')
    return

def env_info_more(env_obj, args, arg_tree, user_args):
    args.append('more')
    env_info(env_obj, args, arg_tree, user_args)

def env_info_outside(env_obj, args, arg_tree, user_args):
    if env_obj.env_exists(args[0]):
        env_obj.initialize(args[0])
        if len(args) == 1:
            env_obj.env_meta.stdout_info()
        elif args[1] == 'more':
            env_obj.env_meta.stdout_info('versions')
    else:
        stdout.print_error(2)
    return

def env_info_outside_more(env_obj, args, arg_tree, user_args):
    args.append('more')
    env_info_outside(env_obj, args, arg_tree, user_args)
    return 

def _create_(env_obj):
    final_path = os.path.join(env_obj.ENVS_PATH, env_obj.env_meta.env_name)
    output = subprocess.run(
        f'virtualenv --clear {final_path}',
        shell=True, stdout=subprocess.PIPE 
    ).stdout.decode('utf-8')
    env_obj.env_meta.save(os.path.join(final_path, 'env_meta.json'))
    return 

def create(env_obj, args, arg_tree, user_args):
    if args[0] in [x.name for x in env_obj.envs_dir_list]:
        stdout.print_error(6)
    else:
        env_obj.initialize(args[0])
        _create_(env_obj)
    return

def create_overwrite(env_obj, args, arg_tree, user_args):
    env_obj.initialize(args[0])
    _create_(env_obj)
    return

def create__DEAD__(env_obj, args, arg_tree, user_args):
    
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

def remove(env_obj, args, arg_tree, user_args):
    if env_obj.env_exists(args[0]):
        env_obj.initialize(args[0])
        shutil.rmtree(os.path.join(env_obj.ENVS_PATH, args[0]))
    else:
        stdout.print_error(2)
    
def remove__DEAD__(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH):

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

def install(env_obj, args, arg_tree, user_args):
    pip_command = [f'{env_obj.VIRTUAL_ENV_VAR}/bin/pip', 'install']
    if len(args) == 1:
        pip_command.append(args[0])
        args.append(get_versions.get_version(args[0]))
    else:
        pip_command.append(args[0] + '==' + args[1])
    
    pip_command.append('--no-cache-dir')

    subprocess.run(
        pip_command
    )
    env_obj.initialize()
    env_obj.env_meta.add_version(args[0], args[1])
    env_obj.env_meta.save(os.path.join(env_obj.ENVS_PATH, env_obj.env_meta.env_name, 'env_meta.json'))
    return

def install__DEAD__(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH):

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

        import env_class 
        env_obj = env_class.ENV_CLASS(VIRTUAL_ENV_VAR, ENVS_PATH)
        env_obj.initialize()
        print(env_obj.is_active())
        print(env_obj.is_active())
        env_obj.env_meta.export(ENVS_PATH)

        env_meta.add_version(arg_2, arg_3)

        # env_meta.save(os.path.join(VIRTUAL_ENV_VAR, 'env_meta.json'))

    else:
        stdout.print_error(1)

    return
 
## IMPLEMENTATION LATER
def _rename_(current_name, new_name, envs_path):
    os.rename(os.path.join(envs_path, current_name), os.path.join(envs_path, new_name))
    return

def rename(env_obj, args, arg_tree, user_args):
    _rename_(args[0], args[1], env_obj.ENVS_PATH)
    return

def _clone_(current_env, new_env):
    
    return

def _export_():
    return

def export(env_obj, args, arg_tree, user_args):
    return

def _build_(file_path):
    return

def build(env_obj, args, arg_tree, user_args):
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

