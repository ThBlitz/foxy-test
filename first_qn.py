
import collections

def SOLUTION(board , word):

    rows = len(board)
    cols = len(board[0])
    word_len = len(word)
    directions = [
        (1, 0), (-1, 0), (0, 1), 
        (0, -1), (1, 1), (-1, -1), 
        (1, -1), (-1, 1)
    ]

    def Depth_First_Search(x, y, given_word):

        stack = collections.deque()
        visited_cells = set()
        stack.append((x, y, 1))
        visited_cells.add((x, y))

        while stack:
            x, y, current_len = stack.pop()
            if current_len == word_len:
                break
            for x_direc, y_direc in directions:
                i = x_direc + x
                j = y_direc + y
                if (i, j) not in visited_cells:
                    if i >= 0 and j >= 0 and i < rows and j < cols and board[i][j] == given_word[current_len]:
                        stack.append((i, j, current_len + 1))
                        visited_cells.add((i, j))

        return current_len == word_len, x, y

    visited_words = set()
    num_of_words = 0
    reversed_word = word[::-1]
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited_words:
                if board[i][j] == word[0]:
                    word_exists, x, y = Depth_First_Search(i, j, word)
                    if word_exists:
                        num_of_words += 1
                        visited_words.add((x, y))
                elif board[i][j] == reversed_word[0]:
                    word_exists, x, y = Depth_First_Search(i, j, reversed_word)
                    if word_exists:
                        num_of_words += 1
                        visited_words.add((x, y))

    return num_of_words


##########  TEST CASE 1  ##########
board = [
    ['c','a','l'],
    ['e','g','j'],
    ['l','f','l']
]
word = 'agl'

## 3 possible words 
print('TEST CASE 1 :', SOLUTION(board, word))

##########  TEST CASE 2  ##########
board = [
    ['a', 'i', 'h', 'l', 'l'],
    ['n', 'f', 'e', 'e', 'n']
]
word = 'hell'

# two possible words
print('TEST CASE 2 :', SOLUTION(board, word))

