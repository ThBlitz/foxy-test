


error_messages = {
    0: [
        'invalid command',
        'please enter ~ $fox OR $fox commands',
        'for more information'
    ]
}

def print_messg(messg):
    for line in messg:
        print(line)
    return

def format_messg(messg):
    
    return messg

def print_error(error_code):
    print_messg(error_messages[error_code])
    return

def print_(print_type):
    return 