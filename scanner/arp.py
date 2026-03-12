from scapy.all import ARP, Ether, srp




def get_mac_from_ip(ip):
    """
    Envia um pacote ARP Request para obter o MAC de um IP específico.
    """

    arp_request = ARP(pdst=str(ip))
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request             

    try:

        answered = srp(packet, timeout = 2, verbose = False)[0]

        if answered:

            return answered[0][1].hwsrc             # Retorna endereço de hardware (hwsrc) da resposta
        
    except Exception as e:
        print(f"Erro ao obter MAC para {ip}: {e}")
        pass

    return None