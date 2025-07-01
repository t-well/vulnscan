import requests

def search_cves(product, version):
    query = f"{product} {version}"
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "keywordSearch": query,
        "resultsPerPage": 5
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        cves = data.get("vulnerabilities", [])
        return [{
            "id": cve["cve"]["id"],
            "description": cve["cve"]["descriptions"][0]["value"]
        } for cve in cves]

    except requests.RequestException as e:
        print(f"[!] CVE API error for {query}: {e}")
        return []