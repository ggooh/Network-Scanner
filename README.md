# Network Scanner 

Um scanner de rede local eficiente desenvolvido em Python, utilizando o protocolo **ARP** para descoberta de dispositivos, resolução de **Hostnames** e identificação de fabricantes **OUI Lookup**.


## Funcionalidades

- **Descoberta Ativa:** Utiliza o Scapy para enviar pacotes ARP Broadcast.

- **Identificação de Fabricante:** Base de dados local com mais de 39.000 registos do IEEE (OUI).

- **Resolução de Nomes:** Identifica os nomes dos dispositivos (Hostnames) na rede.

- **Auto-Configuração:** Deteta automaticamente o teu IP local e calcula a máscara de rede.


## Instalação

1. **Clone o repositório:**
    ```bash
    git clone [https://github.com/ggooh/network_scanner.git](https://github.com/ggooh/network_scanner.git)
    cd network_scanner

2. **Crie e ative um ambiente virtual:**
    python -m venv venv
    No Windows:
    .\venv\Scripts\activate

3. **Instale as dependências:**
    pip install -r requirements.txt

## Como Usar

**Nota:** Este programa requer privilégios de Administrador (Windows) ou root (Linux/macOS) para enviar pacotes ARP.

1. **Atualize a base de dados de fabricantes (OUI):**
    python utils/update_oui.py

2. **Execute o scanner:**   
    Execute python main.py

## Licença
    Este projeto está sob a licença MIT.