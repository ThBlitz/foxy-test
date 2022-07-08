import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':

    try:
        command = str(sys.argv[1])
    except:
        command = "help"

    try:
        arg_2 = str(sys.argv[2])
    except:
        arg_2 = None 
        pass
    
    try:
        arg_3 = str(sys.argv[3])
    except:
        arg_3 = None
        pass
    
    print(command, arg_2, arg_3)

    



