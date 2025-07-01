import subprocess;
from datetime import datetime, timezone;
import os;
from parsing.parse import parse_nmap_services;
from matching.matching import search_cves;
from report.report import json_report;

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
        parsing_result = parse_nmap_services(f'{output_file}');
        for service in parsing_result:
            product = service["product"];
            version = service["version"];
            if product and version:
                cves = search_cves(product, version);
            if cves:
                print(f"\n[+] CVEs for {product} {version}:");
                service['cve_found'] = True;
                for cve in cves:
                    print(f"- {cve['id']}: {cve['description']}");
            else:
                service['cve_found'] = False;
                print(f'{product} {version}: No CVEs Found');
        json_report(parsing_result, timestamp);


    except subprocess.CalledProcessError as e:
        print(f"[!] Error running RustScan: {e}");