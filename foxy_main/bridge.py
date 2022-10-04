import sys
import stdOut
import arguments_list
import breakout_trie

class Args_Pack:
    def __init__(self, PWD, VIRTUAL_ENV_VAR, ENVS_PATH, args_list, breakout_trie):
        self.PWD = PWD
        self.VIRTUAL_ENV_VAR = VIRTUAL_ENV_VAR
        self.ENVS_PATH = ENVS_PATH
        self.args_list = args_list
        self.breakout_trie = breakout_trie


if __name__ == '__main__':
    arguments = []
    for arg in sys.argv[1:]:
        arguments.append(str(arg))

    PWD = arguments[-3]
    VIRTUAL_ENV_VAR = arguments[-2] if arguments[-2] != '__none__' else None
    ENVS_PATH = arguments[-1]
    if len(arguments) == 3:
        arguments = ['commands'] + arguments

    arg_str = 'fox '
    arg_str += ' '.join(arguments[:-3])

    tree = breakout_trie.Breakout_Trie()
    for arg in arguments_list.arguments:
        tree.add('fox ' + arg[0], arg[1])
    
    args_list = tree.parse(arg_str)
    if len(args_list) == 0:
        stdOut.print_error(0)
        exit()
    elif len(args_list) > 1:
        print('ERROR: MULTIPLE METHODS RETURNED BY TRIE')
        exit()

    pack = Args_Pack(PWD, VIRTUAL_ENV_VAR, ENVS_PATH, args_list[:-1], tree)
    permission, method = args_list[0][-1] 

    if permission == 'o' and pack.VIRTUAL_ENV_VAR != None:
        stdOut.print_error(1)
    elif permission == 'i' and pack.VIRTUAL_ENV_VAR == None:
        stdOut.print_error(4)
    else:
        method(pack)

    