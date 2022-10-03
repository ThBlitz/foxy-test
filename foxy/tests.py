import collections

class breakout_trie_node:
    def __init__(self):
        self.children = [None] * 28
        self.end = None

    def index(self, char):
        if char == ' ':
            return 27
        return ord(char) - 96 


# class breakout_trie_node:
#     def __init__(self):
#         self.children = [None] * 27
#         self.end = None

#     def index(self, char):
#         if char == ' ':
#             return 26
#         return ord(char) - 97
    
#     def next(self, char):
#         return self.children[index(char)]

#     def insert(self, char, node):
#         self.children[index(char)] = node
#         return

class Breakout_Trie:
    def __init__(self):
        self.root = breakout_trie_node()
        self.len = 0
        self.size = 0
    
    def add(self, args, method):
        def recur(i, node):
            if i < 0:
                if node.end == None:
                    node.end = method
                    self.len += 1
                    return True
                return False
            if args[i] == '<' or args[i] == '>':
                if node.children[0] == None:
                    node.children[0] = breakout_trie_node()
                    self.size += 1
                return recur(i - 1, node.children[0])
            idx = node.index(args[i])
            if node.children[idx] == None:
                node.children[idx] = breakout_trie_node()
                self.size += 1
            return recur(i - 1, node.children[idx])
        args = args[::-1]
        return recur(len(args) - 1, self.root)

    def get_leaves(self, node):
        self.leaves = []
        def recur(node):
            if node.children[0] != None:
                return self.leaves.append(node.children[0])
            return [recur(node) for node in node.children[1:] if node != None]
        recur(node)
        return self.leaves

    def parse(self, args):
        self.collect = []
        self.count = 0
        def recur(i, node, bag):
            self.count += 1
            if i < 0:
                if node.end != None:
                    self.collect.append(bag + [node.end])
                    return 
            idx = node.index(args[i])
            if node.children[idx] != None:
                recur(i - 1, node.children[idx], bag)
            if node.children[0] != None:
                arg = ''
                while i >= 0 and args[i] != ' ':
                    arg += args[i]
                    i -= 1
                for breakout in self.get_leaves(node.children[0]):
                    recur(i, breakout, bag + [arg])
            return 
        args = args[::-1]
        recur(len(args) - 1, self.root, [])
        return self.collect
    


class args_trie:
    def __init__(self):
        self.root = args_trie_node()

    def index(self, char):
        if char == ' ':
            return 27
        return ord(char) - 96
    
    def character(self, num):
        if num == 27:
            return ' '
        return chr(num + 96)

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
        self.count = 0
        def recur(i, node, param):
            self.count += 1
            if i < 0:
                if node.end_method != None:
                    param.append(node.end_method)
                    self.params.append(param)
                    return True
                return False
            
            idx = self.index(args[i])
            valid = False
            if node.children[idx] != None:
                valid = recur(i - 1, node.children[idx], param)
        
            arg = ''
            while args[i] != ' ':
                arg += args[i]
                i -= 1
            
            for idx in range(0, 27):
                if node.special_children[idx] != None:
                    valid = recur(i, node.special_children[idx], param + [arg] if len(arg) > 0 else param)
            return valid 
        args += ' '
        args = args[::-1]
        recur(len(args) - 1, self.root, [])
        print(self.count)
        return self.params

    def print(self):
        queue = collections.deque()
        queue.append(self.root)
        levels = []
        count = 1
        while queue:
            level = [[], []]
            for _ in range(len(queue)):
                node = queue.popleft()
                count += 1
                for idx in range(27):
                    if node.children[idx] != None:
                        level[0].append(self.character(idx))
                        queue.append(node.children[idx])
                for idx in range(27):
                    if node.special_children[idx] != None:
                        level[1].append(self.character(idx))
                        queue.append(node.special_children[idx])
            levels.append(level)
        for level in levels:
            print(level)
        print(count)

tree = Breakout_Trie()

# tree.add('fox create <new env> after', "create new env")
# tree.add('fox create <old> after', "overwritten env")
# tree.add('fox <create> crr caa', '<ccc>')
# tree.add('fox create <new new>', 'create new new')
# tree.add('fox build <new env> <now>', 'new build')
# tree.add('fox build new nnn', 'new None')

# print(tree.parse('fox build new nnn'))

import args_dictionary

operations = args_dictionary.args_to_operations

for op in operations:
    tree.add('fox ' + op, operations[op])

print(tree.parse('fox clone old_env upto version eighty_nine as new_env'), tree.count, tree.size, tree.len)
