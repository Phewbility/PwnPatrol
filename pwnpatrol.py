import argparse
import shutil
import os
import pyfiglet
from utils.colors import print_colored, print_section, init_colors
from utils.find_functions import find_functions
from utils.assembly_code import display_assembly
from utils.decompiled_code import display_decompiled
from utils.find_libraries import trace_lib_calls
from utils.check_security import check_security, check_hardening
from colorama import Fore, Style, init

def print_banner():
    init(autoreset=True)
    banner = pyfiglet.figlet_format("PwnPatrol", font="slant")
    width = shutil.get_terminal_size().columns
    border_line = "#" * width
    empty_line = "#" + " " * (width - 2) + "#"
    info_line = "PwnPatrol created by Phewbility".center(width - 4)
    version_line = "Version 1.0".center(width - 4)

    colored_banner = f"{Fore.RED}{border_line}\n"
    for line in banner.splitlines():
        padding_left = (width - len(line) - 2) // 2
        padding_right = width - len(line) - 2 - padding_left
        colored_line = Fore.BLUE + line
        colored_banner += f"{Fore.RED}#{' ' * padding_left}{colored_line}{' ' * padding_right}{Fore.RED}#\n"

    colored_banner += f"{Fore.RED}#{' ' * (width - 2)}{Fore.RED}#\n"
    colored_banner += f"{Fore.RED}#{Fore.YELLOW}{info_line.center(width - 2)}{Fore.RED}#\n"
    colored_banner += f"{Fore.RED}#{Fore.YELLOW}{version_line.center(width - 2)}{Fore.RED}#\n"
    colored_banner += f"{Fore.RED}#{' ' * (width - 2)}{Fore.RED}#\n"
    colored_banner += f"{Fore.RED}{border_line}\n"

    print(colored_banner + Style.RESET_ALL)

def main():
    parser = argparse.ArgumentParser(description="PwnPatrol Analysis Tool")
    parser.add_argument("file", nargs='?', help="Path to the executable file to analyze")
    parser.add_argument("-a", "--assembly", metavar="FUNCTION", help="Show assembly code for the specified function")
    parser.add_argument("-c", "--code", metavar="FUNCTION", help="Show pseudo-code in C for the specified function")
    parser.add_argument("-f", "--functions", action="store_true", help="Show functions")
    parser.add_argument("-s", "--security", action="store_true", help="Run security checks")
    parser.add_argument("-l", "--libraries", action="store_true", help="Trace library calls using ltrace")
    parser.add_argument("-A", "--analyze", action="store_true", help="Perform full analysis (functions, assembly, code, security, libraries)")
    args = parser.parse_args()

    init_colors()
    print_banner()

    if not args.file:
        print_colored(Fore.RED, "ERROR: No file selected for analysis.")
        parser.print_help()
        return

    if not any([args.functions, args.assembly, args.code, args.security, args.libraries, args.analyze]):
        print_colored(Fore.RED, "ERROR: No analysis option specified.")
        parser.print_help()
        return

    if args.analyze:
        args.assembly = "main"
        args.code = "main"
        args.security = True
        args.functions = True
        args.libraries = True

    if args.functions:
        find_functions(args.file)

    if args.assembly:
        display_assembly(args.file, args.assembly)

    if args.code:
        display_decompiled(args.file, args.code)

    if args.security:
        check_security(args.file)
        check_hardening(args.file)

    if args.libraries:
        trace_lib_calls(args.file)

    if os.path.exists("&1"):
        os.remove("&1")

if __name__ == "__main__":
    main()

