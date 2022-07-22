from collections import defaultdict, deque

args_to_operations = {
    'info': ('', 'info'),
    'commands': ('', 'commands'),
    'list envs': ('', 'list_envs'),
    'env info': ('i', 'env_info'),
    'info <>': ('', 'env_info'),
    'create <>': ('o', 'create'),
    'create <> overwrite': ('o', 'create'),
    'remove <>': ('o', 'remove'),
    'install <> <>': ('i', 'install'),
    'list versions': ('i', 'list_versions'),
    'clone <> to <>': ('o', 'clone'),
    'clone <> from <>': ('o', 'clone'),
    'clone <> upto version <> as <>': ('o', 'clone'),
    'clone <> upto version <> from <>': ('o', 'clone'),
    'rename <> as <>': ('o', 'rename'),
    'export <>': ('', 'export'),
    'build <> to <>': ('o', 'build'),
    'build <> from <>': ('o', 'build')
}

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


class Arguments:

    def __init__(self, arguments = None):
        self.arg_tree = self.load_tree()
        self.arguments = arguments

    def load_tree(self):
        root = Arguments_Tree(arg = 'fox')
        for args in args_to_operations:
            args = args.split(' ')
            Arguments_Tree.fill_tree(root, args)
        return root

    def validate_arguments(self):
        return Arguments_Tree.validate_args(self.arg_tree, self.arguments)


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
    