import time
import sys
from scanner.network import get_local_network, calculate_network, get_hostname
from scanner.discovery import discover_hosts_arp
from scanner.lookup import get_company
from scanner.ports import run_port_scan



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
    found_ips = {host["ip"] for host in active_hosts_data}

    print(f"{'IP ADDRESS':15} | {'HOSTNAME':25} | {'MAC ADDRESS':17} | {'COMPANY'}")
    print("-" * 85)

    for host in active_hosts_data:

        ip_encontrado = host["ip"]
        mac_encontrado = host["mac"]

        name = get_hostname(ip_encontrado)
        company = get_company(mac_encontrado)

        print(f"{ip_encontrado:15} | {name:25} | {mac_encontrado:17} | {company}")

    while True:
        print("\n" + "="*85)
        print("MENU DE OPÇÕES:")
        print("- Introduza um ou mais IPs separados por vírgula (ex: xxx.xxx.x.x, xxx.xxx.x.x)")
        print("- Introduza 's' para sair do programa")

        entrada = input("\nEscolha a sua opção: ").strip()

        if entrada.lower() == 's':
            print("\nA encerrar o programa.")
            break

        if not entrada:
            continue

        target_ips = [ip.strip() for ip in entrada.split(",")]

        for target_ip in target_ips:
            if target_ip in found_ips:

                open_ports = run_port_scan(target_ip)

                if open_ports:
                    print(f"\nPortas abertas detetadas em {target_ip}:")
                    print(f"    {'PORTA':<10} | {'SERVIÇO'}")
                    print(f"    {'-'*25}")

                    for port, service in open_ports:
                        print(f"    {port:<10} | {service}")

                else:
                    print(f"\nNenhuma das portas comuns está aberta em {target_ip}.")

            else:
                print(f"\nErro: O IP {target_ip} não pertence à lista de dispositivos detetados.")

if __name__ == "__main__":

    try:
        main()
        
    except KeyboardInterrupt:
        print("\n\n[!] Programa interrompido pelo utilizador.")
        
        sys.exit()