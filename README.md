# VulnScan CLI

A command-line vulnerability scanner that uses RustScan and Nmap to detect open ports and running services, then queries NVD for known CVEs based on service version information.

## Features

- Runs RustScan with Nmap to detect open ports and service versions
- Parses Nmap XML output to extract services
- Queries NVD's public CVE API using service product and version
- Generates a JSON report of detected services and known vulnerabilities

## Requirements

- Python 3.8+
- RustScan
- Nmap

## Install Dependencies

```bash
sudo apt update
sudo apt install nmap
```
Install RustScan:

# Recommended (via snap)
sudo snap install rustscan

Make sure it's available in your PATH:

```bash
rustscan -V
```
# Usage

```bash
python3 cli.py scan --target <IP_ADDRESS> --top-ports <NUM_PORTS>
```
# Example

```bash
python3 cli.py scan --target 192.168.1.1 --top-ports 1000
```
# Output

    Raw Nmap XML saved in ./results/scan_output_<timestamp>.xml

    JSON report saved in ./results/report_<timestamp>.json

# Directory Structure

.
├── cli.py
├── parsing/
│   └── parse.py
├── tool/
│   └── scan.py
├── matching/
│   └── matching.py
├── report/
│   └── report.py
└── results/

# Notes

    CVE results are based on basic keyword search using product and version. Manual verification is recommended.

    Only top 5 CVEs per service are returned for brevity.


---

Let me know if you want to add a license, contribution guidelines, or install via `pip`/Makefile.