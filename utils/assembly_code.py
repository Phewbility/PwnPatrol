import r2pipe
from utils.colors import print_colored, print_section
from colorama import Fore, Style

def display_assembly(file, function_name):
    try:
        r2 = r2pipe.open(file, flags=["-e", "bin.relocs.apply=true", "-e", "bin.cache=true"])
        r2.cmd('aaa > /dev/null 2>&1')

        functions_info = r2.cmdj('aflj')

        func_addr = next((func.get('offset') for func in functions_info if func.get('name') == function_name), None)
        if func_addr is None:
            print_colored(Fore.RED, f"Function {function_name} not found.")
            return

        print_section("[Assembly Code (Detailed)]")
        asm_code_detailed = r2.cmd(f'pdf @ {func_addr}')
        print(Fore.YELLOW + asm_code_detailed + Style.RESET_ALL)

        print_section("[Assembly Code (Simplified)]")
        asm_code_simplified = r2.cmd(f'pdr @ {func_addr}')
        print(Fore.CYAN + asm_code_simplified + Style.RESET_ALL)

        print_section("[Assembly Code (Basic)]")
        asm_code_basic = r2.cmd(f'pda @ {func_addr}')
        print(Fore.GREEN + asm_code_basic + Style.RESET_ALL)

        r2.quit()
    except Exception as e:
        print_colored(Fore.RED, str(e))
