

args_to_operations = {
    'info': ('', ('info')),
    'commands': ('', ('commands')),
    'install <1> <2>': ('i', ('install')),
    'create <1>': ('o', ('create'))
}

class args_Tree:
    def __init__(self, arg = 0, next_nodes = None):
        self.arg = arg
        self.next = next_nodes



class Parse_Arguments:
    def __init__(self, arguments):
        self.arguments = arguments
        self.permissions = set(('a', 'o', 'i'))
        for args in args_to_operations.keys():
            arg = args.split(' ')
            if arg[0] == arguments[0]:
                print(arg[1].format(i = 'formated'), arg[2]) 
    

