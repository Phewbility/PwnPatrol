from colorama import Fore, Style, init
import shutil

def init_colors():
    init()

def print_colored(color, text):
    print(color + text + Style.RESET_ALL)

def print_section(title):
    width = shutil.get_terminal_size().columns
    separator = '=' * width
    print(Fore.RED + separator + Style.RESET_ALL)
    print(Fore.RED + title.center(width) + Style.RESET_ALL)
    print(Fore.RED + separator + Style.RESET_ALL)
