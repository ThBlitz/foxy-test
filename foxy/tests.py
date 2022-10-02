

class args_trie_node:
    def __init__(self):
        self.children = [None] * 27
        self.special_children = [None] * 27
        self.end_method = None

class args_trie:
    def __init__(self):
        self.root = args_trie_node()

    def index(self, char):
        if char == ' ':
            return 26
        return ord(char) - 97

    def add(self, args, method):
        def recur(i, special, node):
            
            if i < 0:
                node.end_method = method
                return

            if args[i] == '<':
                special = True
                i -= 1
            elif args[i] == '>':
                special = False
                i -= 1

            idx = self.index(args[i])
            if special == True:
                if node.special_children[idx] == None:
                    node.special_children[idx] = args_trie_node()
                recur(i - 1, special, node.special_children[idx])
                return
            if node.children[idx] == None:
                node.children[idx] = args_trie_node()
            
            recur(i - 1, special, node.children[idx])
            return
        args += ' '
        args = args[::-1]
        recur(len(args) - 1, False, self.root)
        return

    def parse(self, args):
        self.params = []
        def recur(i, node, param):

            if i < 0:
                if node.end_method != None:
                    self.params += param
                    self.params.append(node.end_method)
            
            idx = self.index(args[i])
            if node.children[idx] != None:
                recur(i - 1, node.children[idx], param)
             
            arg = ''
            while args[i] != ' ':
                arg += args[i]
                i -= 1
            
            for idx in range(0, 27):
                if node.special_children[idx] != None:
                    recur(i, node.special_children[idx], param + [arg] if len(arg) > 0 else param)
            return 
        args += ' '
        args = args[::-1]
        recur(len(args) - 1, self.root, [])
        return self.params

tree = args_trie()

tree.add('fox create <new env> after', "create new env")
tree.add('fox create <new env> after and', "overwritten env")
tree.add('fox <create> new now', '<ccc>')
tree.add('fox create <new new>', 'create new new')

print(tree.parse('fox create new after and'))