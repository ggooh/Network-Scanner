import psutil
import ipaddress 
import uuid
import socket



def get_local_mac():
    """
    Obtém o MAC address da própria máquina
    """

    mac_hex = iter(hex(uuid.getnode())[2:].zfill(12))
    return ":".join(a + b for a, b in zip(mac_hex, mac_hex))




def get_local_network():
    """
    Descobrir o IP local e máscara ativa
    """

    interfaces = psutil.net_if_addrs()

    for interface_name, addresses in interfaces.items():
        for address in addresses:

            # AF_INET = IPv4
            if address.family.name == "AF_INET":    
                ip = address.address
                mask = address.netmask

                if ip.startswith("127."):
                    continue

                if ip.startswith("169.254"):
                    continue

                return ip, mask
    
    return None, None





def calculate_network(ip, mask):
    """
    Calcula a rede e os Hosts possíveis.
    """
    
    network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
    hosts = list(network.hosts())
    
    return network, hosts



def get_hostname(ip):
    """
    Tenta obter o nome do dispositivo através do IP.
    """

    try:
        
        return socket.gethostbyaddr(str(ip))[0]     # socket.gethostbyaddr devolve (name, aliaslist, addresslist)
    
    except (socket.herror, socket.gaierror, IndexError):
        return "Unknown"