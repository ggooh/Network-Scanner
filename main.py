import time
from scanner.network import get_local_network, calculate_network, get_hostname
from scanner.discovery import discover_hosts_arp
from scanner.lookup import get_company

def main():

    ip, mask = get_local_network()

    if not ip:
        print("[-] Não foi possível detetar uma rede ativa.")
        return

    print(f"Local IP: {ip} | Mask: {mask}" )

    network, hosts = calculate_network(ip, mask)

    print(f"Network: {network} ({len(hosts)} hosts possíveis)")
    print("\nScanning network...\n")

    active_hosts_data = discover_hosts_arp(network)

    print(f"{'IP ADDRESS':15} | {'HOSTNAME':25} | {'MAC ADDRESS':17} | {'COMPANY'}")
    print("-" * 80)

    for host in active_hosts_data:

        ip_encontrado = host["ip"]
        mac_encontrado = host["mac"]

        name = get_hostname(ip_encontrado)
        company = get_company(mac_encontrado)

        print(f"{ip_encontrado:15} | {name:25} | {mac_encontrado:17} | {company}")

if __name__ == "__main__":
    main()