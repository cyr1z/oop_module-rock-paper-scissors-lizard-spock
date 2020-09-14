def cli_color(string, color='g'):
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