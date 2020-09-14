"""
simple colorize cli with bash aliases
https://gist.github.com/vratiu/9780109#file-bash_aliases
"""


def cli_color(string, color='g'):
    """
    string color
    :param string: colored string
    :param color: color literal
    :return: string with cli color prefix end reset cli color postfix
    """
    colors = {
        'c': '[034m',
        'b': '[035m',
        'y': '[034m',
        'g': '[032m',
        'r': '[031m',
        'w': '[0m',
    }
    result = chr(27) + colors[color] + string + chr(27) + colors['w']
    return result
