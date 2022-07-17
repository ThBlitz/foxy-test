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

    if arg_2 == "__none__":
        arg_2 = None
    
    if arg_3 == "__none__":
        arg_3 = None

    permissions = ('o', 'i', 'a') # inside, outside, anywhere

    list_of_commands = operations.list_of_commands
    
    if VIRTUAL_ENV_VAR == "__none__":
        VIRTUAL_ENV_VAR = None 

    if command not in list_of_commands:
        if command not in ('activate', 'deactivate'):
            stdout.print_error(0)
    else:
        eval(f'operations.{command}(arg_2, arg_3, VIRTUAL_ENV_VAR, ENVS_PATH)')
    
    
        


    



