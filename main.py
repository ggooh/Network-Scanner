import time
from scanner.network import get_local_network, calculate_network, get_local_mac
from scanner.discovery import discover_hosts_arp
from scanner.arp import get_mac_from_ip
from scanner.lookup import get_company

def main():

    ip, mask = get_local_network()

    print(f"Local IP: {ip}")
    print(f"Subnet Mask: {mask}")

    network, hosts = calculate_network(ip, mask)

    print(f"Network: {network}")
    print(f"Total hosts: {len(hosts)}")

    print("\nScanning network...\n")

    active_hosts_data = discover_hosts_arp(network)

    print("Devices found:\n")

    for host in active_hosts_data:

        ip_encontrado = host["ip"]
        mac_encontrado = host["mac"]
    
        company = get_company(mac_encontrado)

        print(f"{ip_encontrado:15} | MAC: {mac_encontrado:17} | Vendor: {company}")

if __name__ == "__main__":
    main()