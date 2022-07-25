import sys
import os
import stdout
import operations
import env_class
import parser
from collections import defaultdict, deque

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

    user_args = []
    for arg in arguments[:-3]:
        if arg == None:
            break
        user_args.append(arg)
    
    arg_tree = parser.args_Tree()
    for arg in operations.args_to_operations:
        method = operations.args_to_operations[arg]
        arg = arg.split(' ')
        arg_tree.add(arg, method)

    validity = arg_tree.validate(user_args)
    
    if validity == False:
        stdout.print_error(0)
        recommends = arg_tree.recommend(user_args)[:6]
        recommends = [' fox ' + ' '.join(x) for x in recommends]
        stdout.print_messg(['suggestions ...'] + recommends, lambda x:x, False, True) 
        __EXIT__ = True
    

    if __EXIT__ == False:
        method, args = arg_tree.extract_args(user_args)
        permission, operation = method[0], method[1]
        env_obj = env_class.ENV(VIRTUAL_ENV_VAR, ENVS_PATH, PWD)
        if permission == 'o' and env_obj.is_active() == True:
            stdout.print_error(1)
        elif permission == 'i' and env_obj.is_active() == False:
            stdout.print_error(4)
        else:
            eval(f'operations.{operation}(env_obj, args, arg_tree, user_args)')

    
    
        


    



