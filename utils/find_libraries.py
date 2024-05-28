import pexpect
from utils.colors import print_colored, print_section
from colorama import Fore, Style

def trace_lib_calls(file):
    print_section("[Library Calls Found]")
    child = pexpect.spawn(f'ltrace -f {file}', timeout=0.01)
    
    libcalls = []
    timeout_retries = 0
    max_retries = 5
    try:
        while True:
            index = child.expect([pexpect.EOF, pexpect.TIMEOUT, r'\[(pid \d+)\] (\w+)\((.*?)\) += +(.+)'])
            if index == 0:
                # print_colored(Fore.YELLOW, "pexpect.EOF reached.")
                break
            elif index == 1:
                # print_colored(Fore.YELLOW, "pexpect.TIMEOUT reached.")
                timeout_retries += 1
                if timeout_retries >= max_retries:
                    # print_colored(Fore.RED, "Maximum TIMEOUT retries reached. Exiting.")
                    break
                continue
            elif index == 2:
                pid = child.match.group(1).decode('utf-8')
                libcall = child.match.group(2).decode('utf-8')
                args = child.match.group(3).decode('utf-8')
                retval = child.match.group(4).decode('utf-8')
                libcalls.append((pid, libcall, args, retval))
                print_colored(Fore.GREEN + Style.BRIGHT, f"PID: {pid}")
                print_colored(Fore.CYAN, f"  Library Call: {libcall}")
                print_colored(Fore.YELLOW, f"  Args: {args}")
                print_colored(Fore.CYAN, f"  Return Value: {retval}\n")
                timeout_retries = 0
    except pexpect.exceptions.EOF:
        print_colored(Fore.RED, "Caught pexpect.exceptions.EOF")
    except pexpect.exceptions.TIMEOUT:
        print_colored(Fore.RED, "Caught pexpect.exceptions.TIMEOUT")
    except Exception as e:
        print_colored(Fore.RED, f"Exception in trace_lib_calls: {str(e)}")
    finally:
        child.close(force=True)

    return libcalls

