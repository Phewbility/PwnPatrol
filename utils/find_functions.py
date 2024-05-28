import r2pipe
from utils.colors import print_colored, print_section
from colorama import Fore

def find_functions(file):
    print_section("[Functions Found]")
    try:
        r2 = r2pipe.open(file, flags=["-e", "bin.relocs.apply=true", "-e", "bin.cache=true"])
        r2.cmd('aaa > /dev/null 2>&1')

        functions_info = r2.cmdj('aflj')

        if not functions_info:
            print_colored(Fore.RED, "No functions found.")
            return

        for function in functions_info:
            func_name = function.get('name')
            func_addr = function.get('offset')
            print_colored(Fore.MAGENTA, f"Function: {func_name} @ {hex(func_addr)}")

        r2.quit()
    except Exception as e:
        print_colored(Fore.RED, str(e))
