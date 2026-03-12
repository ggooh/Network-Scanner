from scapy.all import ARP, Ether, srp



def discover_hosts_arp(network_range):
    """
    Descobre quais os hosts que estão ativos
    usando ARP Broadcast.
    """

    arp_request = ARP(pdst=str(network_range))
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    print(f"Broadcast ARP para {network_range}...")

    answered_list = srp(packet, timeout = 3, verbose = False)[0]

    active_hosts = []
    for sent, received in answered_list:

        active_hosts.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return active_hosts