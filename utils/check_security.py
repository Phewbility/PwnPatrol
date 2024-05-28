import subprocess
from utils.colors import print_colored, print_section
from colorama import Fore, Style

def check_security(file):
    print_section("[Checksec]")
    try:
        result = subprocess.run(['checksec', '--file=' + file])
        print(result.stdout)
    except Exception as e:
        print_colored(Fore.RED, str(e))

def check_hardening(file):
    print_section("[Hardening Check]")
    try:
        result = subprocess.run(['hardening-check', file], capture_output=True, text=True)
        output_lines = result.stdout.splitlines()
        for line in output_lines:
            if "yes" in line:
                print_colored(Fore.GREEN, line)
            elif "no" in line:
                print_colored(Fore.RED, line)
            else:
                print_colored(Fore.YELLOW, line)
    except Exception as e:
        print_colored(Fore.RED, str(e))

