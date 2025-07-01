import xml.etree.ElementTree as ET;

def parse_nmap_services(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    services = []
    for host in root.findall('host'):
        for port in host.findall(".//port"):
            protocol = port.attrib['protocol']
            portid = port.attrib['portid']
            service = port.find("service")
            if service is not None:
                name = service.attrib.get('name', '')
                version = service.attrib.get('version', '')
                product = service.attrib.get('product', '')
                services.append({
                    "port": portid,
                    "protocol": protocol,
                    "name": name,
                    "product": product,
                    "version": version,
                })
    return services