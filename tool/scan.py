import subprocess;
from datetime import datetime, timezone;
import os;

def rust_scan(target, top_ports):
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S");
    output_file = f"./results/scan_output_{timestamp}.xml";
    print(f"[*] Running RustScan on {target} (top {top_ports} ports)...");

    os.makedirs("results", exist_ok=True);

    try:
        subprocess.run([
            "rustscan", 
            "-a", target, 
            "--ulimit", "5000", 
            "--", "-sV", "-T4", f"--top-ports {top_ports}", 
            "-oX", output_file
        ], check=True);
        print(f"[*] Scan complete. Output saved to {output_file}");
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running RustScan: {e}");