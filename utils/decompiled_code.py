import r2pipe
from utils.colors import print_colored, print_section
from colorama import Fore,Style

def display_decompiled(file, function_name):
    try:
        r2 = r2pipe.open(file, flags=["-e", "bin.relocs.apply=true", "-e", "bin.cache=true"])
        r2.cmd('aaa > /dev/null 2>&1')

        function_info = r2.cmdj(f'afij @ {function_name}')

        if not function_info:
            print_colored(Fore.RED, f"Function {function_name} not found.")
            return

        print_section(f"[Fast Decompiled Code for {function_name}]")

        func_addr = function_info[0].get('offset')
        c_code = r2.cmd(f'pdd @ {func_addr}')
        print(Fore.GREEN + c_code + Style.RESET_ALL)

        print_section(f"[Complete Decompiled Code for {function_name}]")

        func_addr = function_info[0].get('offset')
        c_code = r2.cmd(f'pdg @ {func_addr}')
        print(Fore.CYAN + c_code + Style.RESET_ALL)

        r2.quit()
    except Exception as e:
        print_colored(Fore.RED, str(e))

