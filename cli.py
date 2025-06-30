import sys;
import ipaddress;
from tool.scan import rust_scan;

# TEST COMMAND: python3 cli.py scan --target 192.168.1.1 --top-ports 1000

def input_checks():
    if len(sys.argv) == 6:
        target = sys.argv[3];
        top_ports = sys.argv[5];
        try:
            ipaddress.ip_address(target);
            rust_scan(target, top_ports);
        except ValueError:
            print(f"[!] '{target}' is not a valid IP address.");
            sys.exit();
    else:
        print("Usage Example: python3 cli.py scan --target 192.168.1.1 --top-ports 1000");
        sys.exit(1);


if __name__ == '__main__':
    input_checks();