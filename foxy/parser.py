from collections import defaultdict, deque

args_to_operations = {
    'info': ('', 'info'),
    'commands': ('', 'commands'),
    'list envs': ('', 'list_envs'),
    'env info': ('i', 'env_info'),
    'info <env_name>': ('', 'env_info'),
    'create <env_name>': ('o', 'create'),
    'create <env_name> overwrite': ('o', 'create'),
    'remove <env_name>': ('o', 'remove'),
    'install <package_name> <package_version>': ('i', 'install'),
    'list versions': ('i', 'list_versions'),
    'clone <current_env> to <new_env>': ('o', 'clone'),
    'clone <new_env> from <current_env>': ('o', 'clone'),
    'clone <current_env> upto version <version_number> as <new_env>': ('o', 'clone'),
    'clone <new_env> upto version <version_number> from <current_env>': ('o', 'clone'),
    'rename <current_name> as <new_name>': ('o', 'rename'),
    'export <file_name>': ('', 'export'),
    'build <file_path> to <env_name>': ('o', 'build'),
    'build <env_name> from <file_path>': ('o', 'build')
}

class Args_Tree:

    def __init__(self, arg = None, end = False):
        self.arg = arg
        self.arg_name = arg
        self.user_defined = False
        self.end = end
        if arg[0] == '<' and arg[-1] == '>':
            self.user_defined = True
            self.arg = '<>'
        self.__pointer = defaultdict(self.__default)

    def __default(self):
        return None

    def link_node(self, node):
        self.__pointer[node.arg] = node
    
    def list_links(self):
        return self.__pointer.keys()

    def next_node(self, arg):
        if arg[0] == '<' and arg[-1] == '>':
            return self.__pointer['<>']
        elif arg not in self.__pointer:
            return self.__pointer['<>']
        return self.__pointer[arg]

    def fetch_linked_nodes(self):
        for x in self.list_links():
            yield self.next_node(x)

    def link_exists(self, arg):
        if arg not in self.__pointer:
            return '<>' in self.__pointer
        return True

    @staticmethod
    def fill_tree(node, args):
        
        if len(args) == 0:
            node.end = True
            return

        if node.link_exists(args[0]) == False:
            node.link_node(Args_Tree(args[0]))
        
        Args_Tree.fill_tree(node.next_node(args[0]), args[1:])

    @staticmethod
    def validate_tree(node, args):
        
        if len(args) == 0:
            return node.end
        print(node.list_links(), args[0])
        if node.link_exists(args[0]):
            return Args_Tree.validate_tree(node.next_node(args[0]), args[1:])
        return False


class Arguments_Tree:

    def __init__(self, arg = None):
        self.arg = arg
        self.__pointer = defaultdict(self.__default)
        self.__reverse_pointer = defaultdict(self.__default)

    def __default(self):
        return None
    
    def list_nodes(self):
        return self.__pointer.keys()

    def fetch_nodes(self):
        for x in self.list_nodes():
            yield self.next_node(x)
    
    def add_node(self, node):
        self.__pointer[node.arg] = node
    
    def add_reverse_node(self, node):
        self.__reverse_pointer[node.arg] = node
    
    def next_node(self, arg):
        return self.__pointer[arg]

    def node_exists(self, arg):
        return arg in self.__pointer

    def end(self):
        return True if self.node_exists(None) else False

    @staticmethod
    def fill_tree(node, args):
        if len(args) == 0:
            node.add_node(Arguments_Tree())
            return
        if not node.node_exists(args[0]):
            node.add_node(Arguments_Tree(args[0]))
        Arguments_Tree.fill_tree(node.next_node(args[0]), args[1:])

    @staticmethod
    def validate_args(node, args):
        if len(args) == 0:
            return node.end()
        if node.node_exists(args[0]):
            return Arguments_Tree.validate_args(node.next_node(args[0]), args[1:])
        elif node.node_exists('<>'):
            return Arguments_Tree.validate_args(node.next_node('<>'), args[1:])
        return False

    @staticmethod
    def closest_args(node, args):
        
        def recur(node, args, closest = []):
            if len(args) == 0:
                return node, closest
            if node.node_exists(args[0]):
                closest.append(args[0])
                return recur(node.next_node(args[0]), args[1:], closest)
            elif node.node_exists('<>'):
                closest.append('<>')
                return recur(node.next_node('<>'), args[1:], closest)
            return node, closest
        
        closest = []
        node, close = recur(node, args)
        print(close)
        stack = deque()
        stack.append(node)
        possible_args = []
        close = close[:-1]
        while stack:
            node = stack.pop()
            possible_args.append(node.arg)
            if node.end():
                closest.append(close + possible_args)
                possible_args = []
            
            for x in node.fetch_nodes():
                stack.append(x)
            
        print(closest)


class Arguments:

    def __init__(self, arguments = None):
        self.arg_tree = self.load_tree()
        self.arguments = arguments

    def load_tree(self):
        # root = Arguments_Tree(arg = 'fox')
        root = Args_Tree(arg = 'fox')
        for args in args_to_operations:
            args = args.split(' ')
            Args_Tree.fill_tree(root, args)
        return root

    def validate_arguments(self):
        return Args_Tree.validate_tree(self.arg_tree, self.arguments)


# root = Arguments_Tree(arg = 'fox')
# for args in args_to_operations:
#     args = args.split(' ')
#     Arguments_Tree.fill_tree(root, args)






# args = 'clone test upto version 8 as test_other'
# args = args.split(' ')
# print(args)
# print(Arguments_Tree.validate_args(root, args))

# queue = deque()
# queue.append(root)
# queue.append(None)

# while queue[0] != None:
#     node = queue.popleft()
#     for x in node.fetch_nodes():
#         queue.append(x)

#     if queue[0] == None:
#         queue.popleft()
#         print([x.arg for x in queue])
#         queue.append(None)
    