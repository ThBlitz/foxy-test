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
    
    PWD = arguments[-3]
    VIRTUAL_ENV_VAR = arguments[-2]
    ENVS_PATH = arguments[-1]

    args = []
    for arg in arguments[:-3]:
        if arg == None:
            break
        args.append(arg)
    
    args_obj = parser.Arguments(args)
    print(args_obj.validate_arguments())
    # queue = deque()
    # queue.append(root)
    # queue.append(None)

    # while queue[0] != None:
    #     node = queue.popleft()
    #     for x in node.fetch_linked_nodes():
    #         queue.append(x)

    #     if queue[0] == None:
    #         queue.popleft()
    #         print([x.arg for x in queue])
    #         queue.append(None)
        
    # parser.Arguments_Tree.closest_args(args_obj.arg_tree, args)

    env_obj = env_class.ENV_CLASS(VIRTUAL_ENV_VAR, ENVS_PATH, PWD)

    permissions = ('o', 'i', 'a') # inside, outside, anywhere

    list_of_commands = operations.list_of_commands
    
    if VIRTUAL_ENV_VAR == "__none__":
        VIRTUAL_ENV_VAR = None 

    if command not in list_of_commands:
        if command not in ('activate', 'deactivate'):
            stdout.print_error(0)
    else:
        eval(f'operations.{command}(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH)')
    
    
        


    



