import stdOut

# class Args_Pack:
#     def __init__(self, PWD, VIRTUAL_ENV_VAR, ENVS_PATH, args_list):
#         self.PWD = PWD
#         self.VIRTUAL_ENV_VAR = VIRTUAL_ENV_VAR
#         self.ENVS_PATH = ENVS_PATH
#         self.args_list = args_list

def commands(pack):
    recommends = pack.breakout_trie.recommend()
    stdOut.print_messg(recommends)
    return

def info(pack):
    stdOut.print_info(0)
    return

def commands(args):
    recommends = args['arg_tree'].recommend(['fox'])
    stdOut.print_messg(recommends, lambda x: 'fox ' + ' '.join(x)) 
    return

def info(args):
    stdOut.print_info(0)
    return

def list_envs(args):
    envs = [x.name for x in args['env_obj'].envs_dir_list]
    stdOut.print_messg(envs)
    return 

def env_info(args):
    if args['env_obj'].initialize() == True:
        if len(args) == 0:
            args['env_obj'].env_meta.stdout_info()
        elif args[0] == 'more':
            args['env_obj'].env_meta.stdout_info('versions')
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
        stdOut.print_error(2)
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

def remove(env_obj, args, arg_tree, user_args):
    if env_obj.env_exists(args[0]):
        env_obj.initialize(args[0])
        shutil.rmtree(os.path.join(env_obj.ENVS_PATH, args[0]))
    else:
        stdout.print_error(2)

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

        stdOut.print_messg(pip_command)

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
                stdOut.print_error(2)

        else:
            stdOut.print_error(3)
    
    else:
        stdOut.print_error(1)
    
    return




