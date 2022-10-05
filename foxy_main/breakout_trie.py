

class breakout_trie_node:
    def __init__(self):
        # 26 + '_' + ' ' + 10 
        self.children = [None] * 40
        self.end = None
        self.len = 40

    def index(self, char):
        # 0 node, 1 _, 2 ' ', a - z, 0 - 9
        num = ord(char)
        if num <= 57 and num >= 48:
            return num - 48 + 29
        elif num >= 97 and num <= 122:
            return num - 97 + 3
        elif num == 95:
            return 1
        elif num == 32:
            return 2
        return math.inf  

    def character(self, idx):
        if idx >= 29 and idx <= 37:
            return chr(idx + 48 - 29)
        elif idx >= 3 and idx <= 28:
            return chr(idx + 97 - 3)
        elif idx == 1:
            return chr(95)
        elif idx == 2:
            return chr(32)
        return -1 * math.inf 


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
        self.suggestions = ''
        def recur(i, node, bag):
            self.count += 1
            self.suggestions += args[i]
            if i < 0:
                if node.end != None:
                    self.collect.append(bag + [node.end])
                return 
            idx = node.index(args[i])
            if node.children[idx] != None:
                recur(i - 1, node.children[idx], bag)
            elif node.children[0] != None:
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

    def get_all(self, node):
        self.all = []
        def recur(node, args = ''):
            if node.end != None:
                self.all.append(args[:])
            
            for idx in range(1, node.len):
                if node.children[idx] != None:
                    recur(node.children[idx], args + node.character(idx))
            if node.children[0] != None:
                recur(node.children[0], args + '`')

        recur(node)        
        return self.all

    def suggest(self, args):
        self.correct_ones = []
        def recur(i, node, bag):
            if i < 0:
                self.correct_ones.append((node, bag[:]))
                return
            idx = node.index(args[i])
            if node.children[idx] != None:
                recur(i - 1, node.children[idx], bag + args[i])
            elif node.children[0] != None:
                arg = '`'
                while i >= 0 and args[i] != ' ':
                    arg += args[i]
                    i -= 1
                arg += '`'
                for breakout in self.get_leaves(node.children[0]):
                    recur(i, breakout, bag + arg)
            else:
                self.correct_ones.append((node, bag[:]))            
            return
        args = args[::-1]
        recur(len(args) - 1, self.root, '')
        suggestions = []
        for node, correct_args in self.correct_ones:
            for rest_args in self.get_all(node):
                suggestions.append(correct_args + rest_args)
        return suggestions
    


