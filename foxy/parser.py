from collections import defaultdict, deque


class args_Node:

    def __init__(self, arg = None):
        self.arg = arg
        self.value = None
        self.normal_children = defaultdict(self.__default)
        self.special_children = defaultdict(self.__default)
        self.end_node = False
        self.method = None
        self.parent = None
        self.special = False

    def __default(self):
        return None

class args_Tree:

    def __init__(self):
        self.root = self.create_node('fox')

    def create_node(self, arg = None):
        return args_Node(arg = arg)
    
    def add(self, args_list, method):

        def recur(node, args):
           
            if len(args) == 0:
                node.end_node = True
                node.method = method
                return 

            if args[0][0] == '<' and args[0][-1] == '>':
                if args[0] not in node.special_children:
                    node.special_children[args[0]] = self.create_node(args[0])
                    node.special_children[args[0]].parent = node
                    node.special_children[args[0]].special = True
                recur(node.special_children[args[0]], args[1:])
            else:
                if args[0] not in node.normal_children:
                    node.normal_children[args[0]] = self.create_node(args[0])
                    node.normal_children[args[0]].parent = node
                recur(node.normal_children[args[0]], args[1:])
            return

        recur(self.root, args_list)
        return
    
    def validate(self, args_list):

        def recur(node, args):

            if len(args) == 0:
                return node.end_node
            
            validation = False
            if args[0] in node.normal_children:
                validation = recur(node.normal_children[args[0]], args[1:])
            else:
                for special_arg in node.special_children:
                    validation = validation or recur(node.special_children[special_arg], args[1:])

            return validation

        return recur(self.root, args_list)

    def recommend(self, args_list):

        self.res = []

        def validate_upto(node, args, correct_args):
        
            if len(args) == 0:
                self.res.append((node, correct_args))
                return
            
            if args[0] in node.normal_children:
                correct_args.append(args[0])
                validate_upto(node.normal_children[args[0]], args[1:], correct_args)
                return 
            elif len(node.special_children) != 0:
                for special_arg in node.special_children:
                    corr = correct_args[:]
                    corr.append(special_arg)
                    validate_upto(node.special_children[special_arg], args[1:], corr)
                return 

            self.res.append((node, correct_args))

        validate_upto(self.root, args_list, correct_args = [])

        max_len = max([len(x[1]) for x in self.res])
        for x in self.res:
            if len(x[1]) != max_len:
                self.res.remove(x)

        def recur(node, correct_args, temp = []):
            if node.end_node:
                self.recommends.append(correct_args + temp)

            for arg in node.normal_children:
                recur(node.normal_children[arg], correct_args, temp + [arg])
            for s_arg in node.special_children:
                recur(node.special_children[s_arg], correct_args, temp + [s_arg])
            return

        self.recommends = []  
        for node, correct_args in self.res:
            recur(node, correct_args)
        
        self.res = []
        return self.recommends
        
    def extract_args(self, args_list):

        self.args_ = None

        def recur(node, args, temp = []):

            if len(args) == 0:
                self.args_ = (node.method, temp)
                return
            
            if args[0] in node.normal_children:
                recur(node.normal_children[args[0]], args[1:], temp)
            else:
                for s_arg in node.special_children:
                    recur(node.special_children[s_arg], args[1:], temp + [args[0]])
            
            return 
        
        recur(self.root, args_list)
        res = self.args_
        self.args_ = None
        return res


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
        
        if node.link_exists(args[0]):
            return Args_Tree.validate_tree(node.next_node(args[0]), args[1:])
        return False

    def closest_tree(node, args):

        def recur(node, args, closest = []):
            if len(args) == 0:
                return node, closest
            if node.link_exists(args[0]):
                closest.append(args[0])
                return recur(node.next_node(args[0]), args[1:], closest)
            return node, closest
        
        closest = []
        node, close = recur(node, args)
        stack = deque()
        stack.append((node, 0))
        res = []
        temp = [(None, 0)]
        while stack:
            node, level = stack.pop()
            if temp[-1][1] > level:
                for _ in range(level):
                    temp.pop()
            temp.append((node.arg_name, level))
            if node.end == True:
                res.append([x[0] for x in temp[1:]])
            for x in node.fetch_linked_nodes():
                stack.append((x, level + 1))
            

        print(res)


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
    