


error_messages = {
    0: [
        'invalid command',
        'please enter ~ `$fox` OR `$fox commands`',
        'for more information'
    ]
}

info_messages = {
    0: [
        'FOXY 2022 (C) COPYRIGHT @ThBlitz',
        '(C) LICENSE        - https://github.com/ThBlitz/Fox/blob/main/LICENSE',
        'MAINTAINER         - https://github.com/ThBlitz'
    ]
}

def print_messg(messg):
    for line in messg:
        print('-', line)
    return

def print_error(error_code):
    print_messg(error_messages[error_code])
    return

def print_info(info_code):
    print_messg(info_messages[info_code])
    return 