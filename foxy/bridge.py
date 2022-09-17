import sys
import os
import stdOut
import args_dictionary
import env_class
import parser

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':

    arguments = [None] * 10
    for i in range(1, 11):
        arg = str(sys.argv[i])
        if arg != '__none__':
            arguments[i - 1] = arg
    
    __EXIT__ = False

    PWD = arguments[-3]
    VIRTUAL_ENV_VAR = arguments[-2]
    ENVS_PATH = arguments[-1]
    arguments[0] = 'commands' if arguments[0] == None else arguments[0]

    user_args = []
    for arg in arguments[:-3]:
        if arg == None:
            break
        user_args.append(arg)
    
    arg_tree = parser.args_Tree()
    for arg in args_dictionary.args_to_operations:
        method = args_dictionary.args_to_operations[arg]
        arg = arg.split(' ')
        arg_tree.add(arg, method)

    validity = arg_tree.validate(user_args)
    
    if validity == False:
        stdout.print_error(0)
        recommends = arg_tree.recommend(user_args)[:4]
        recommends = [' fox ' + ' '.join(x) for x in recommends]
        stdout.print_messg(['suggestions ...'] + recommends, lambda x:x, False, True) 
        __EXIT__ = True
    

    if __EXIT__ == False:
        method, args = arg_tree.extract_args(user_args)
        permission, operation = method[0], method[1]
        env_obj = env_class.ENV(VIRTUAL_ENV_VAR, ENVS_PATH, PWD)
        if permission == 'o' and env_obj.is_active() != False:
            stdout.print_error(1)
        elif permission == 'i' and env_obj.is_active() == False:
            stdout.print_error(4)
        else:
            Operation_Arguments = {
                'env_obj': env_obj,
                'args': args,
                'arg_tree': arg_tree,
                'user_args': user_args
            }
            operation(Operation_Arguments)
            # eval(f'operations.{operation}(env_obj, args, arg_tree, user_args)')

    
    
        


    



