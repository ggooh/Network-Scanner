# Network Scanner 

Um scanner de rede local eficiente desenvolvido em Python, utilizando o protocolo **ARP** para descoberta de dispositivos, resolução de **Hostnames**, identificação de fabricantes **OUI Lookup** e o protocolo **TCP** para auditoria de portas, permitindo identificar serviços ativos em múltiplos alvos simultaneamente.


## Funcionalidades

- **Descoberta Ativa:** Utiliza o Scapy para enviar pacotes ARP Broadcast.

- **Identificação de Fabricante:** Base de dados local com mais de 39.000 registos do IEEE (OUI).

- **Resolução de Nomes:** Identifica os nomes dos dispositivos (Hostnames) na rede.

- **Auditoria de Portas (Multi-Port Scan):** - Interface interativa para selecionar um ou mais IPs.
  - Varredura paralela (Multi-threading) para máxima performance.
  - Mapeamento automático de portas para serviços comuns (HTTP, SSH, RDP, SMB, etc.).

- **Auto-Configuração:** Deteta automaticamente o teu IP local e calcula a máscara de rede.


## Instalação

1. **Clone o repositório:**
    ```bash
    git clone [https://github.com/ggooh/network_scanner.git](https://github.com/ggooh/network_scanner.git)
    cd network_scanner
    

2. **Crie e ative um ambiente virtual:**
    python -m venv venv
    No Windows: .\venv\Scripts\activate


4. **Instale as dependências:**
    pip install -r requirements.txt

## Como Usar

**Nota:** Este programa requer privilégios de Administrador para enviar pacotes ARP.

1. **Atualize a base de dados de fabricantes (OUI):**
    python utils/update_oui.py

2. **Execute o scanner:**
    Execute python main.py

3. **Port Scanner:**
    Após o varrimento inicial, introduza os IPs desejados separados por vírgula para auditar as portas:
    Exemplo: xxx.xxx.x.x, xxx.xxx.x.x

## Licença
    Este projeto está sob a licença MIT.
