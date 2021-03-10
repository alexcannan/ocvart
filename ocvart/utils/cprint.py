"""
Author: Alex Cannan
Date Created: 2021-3-10
Purpose: This module contains a cprint method, which lets you print in COLOR! (Imagine this in color)
"""

bcolors = {
    "HEADER": '\033[95m',
    "OKBLUE": '\033[94m',
    "OKCYAN": '\033[96m',
    "OKGREEN": '\033[92m',
    "WARNING": '\033[93m',
    "FAIL": '\033[91m',
    "ENDC": '\033[0m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m',
}

color_map = {
    "PURPLE": "HEADER",
    "BLUE": "OKBLUE",
    "LIGHTBLUE": "OKCYAN",
    "GREEN": "OKGREEN",
    "RED": "FAIL",
}

def cprint(message, color="HEADER"):
    color = color.upper()
    if color in color_map:
        color = color_map[color]
    message = str(message)
    if color not in bcolors:
        raise ValueError("Invalid color selection. Try one of {}" \
                         .format("|".join(list(color_map.keys()) \
                                         +list(bcolors.keys()))))
    print(bcolors[color]+message+bcolors["ENDC"])


if __name__ == '__main__':
    cprint("Sup yo")