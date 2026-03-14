import socket
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Proxy"
}


def check_port(ip, port):
    """
    Tenta abrir uma ligação TCP numa porta específica.
    Retorna a porta e o seu estado
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:        # AF_INET = IPv4     SOCK_STREAM = TCP
       
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))

        if result == 0:
            return port, True
        
    return port, False



def run_port_scan(ip):
    """
    Usa Threads para maior rapidez.
    """

    open_ports = []
    print(f"\nA iniciar Port Scan ao IP: {ip}...")

    with ThreadPoolExecutor(max_workers = 20) as executor:
        
        futures = [executor.submit(check_port, ip, port) for port in COMMON_PORTS.keys()]

        for future in futures:
            port, is_open = future.result()

            if is_open:
                service = COMMON_PORTS.get(port, "Uknown")
                open_ports.append((port, service))

    return open_ports