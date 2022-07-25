


error_messages = {
    0: [
        'invalid command (error 0)',
        'please enter ~ `$fox` OR `$fox commands` for more information'
    ],
    1: [
        'permission denied (error 1)',
        'The command must be executed OUTSIDE the env'
    ],
    2: [
        'specified env not found in the directory (error 2)',
        'enter the right env name OR check for the right envs path in path_settings.foxy file'
    ],
    3: [
        'required arguments are missing (error 3)',
        'enter the right arguments'
    ],
    4: [
        'permission denied (error 4)',
        'The command must be executed INSIDE an env'
    ],
    5: [
        'invalid entry of arguments (error 5)',
        'The scope for the entered argument cannot be found'
    ]

}

info_messages = {
    0: [
        'FOXY 2022 (C) COPYRIGHT @ThBlitz',
        '(C) LICENSE        - https://github.com/ThBlitz/Fox/blob/main/LICENSE',
        'MAINTAINER         - https://github.com/ThBlitz'
    ],
    1: [
        'envs present:'
    ]
}

prompt_messages = {
    0: {
        0: ['env already exists (prompt 0)'],
        1: '- do you want to overwrite ? [y/n] : '
    },
    1: {
        0: ['env will be removed from the directory'],
        1: '- do you want to remove the env ? [y/n] : '
    }
}

def print_messg(messg, x = lambda x:x, upper_buffer = True, lower_buffer = True):
    if upper_buffer == True:
        print(' ')
    for line in messg:
        print('-', x(line))
    if lower_buffer == True:
        print(' ')
    return

def print_error(error_code):
    print_messg(error_messages[error_code])
    return

def print_info(info_code):
    print_messg(info_messages[info_code])
    return 

def print_prompt(prompt_code):
    print_messg(prompt_messages[prompt_code][0])
    res = input(prompt_messages[prompt_code][1])
    return res