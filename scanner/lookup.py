import json 
import os
import requests



JSON_PATH = os.path.join(os.path.dirname(__file__), "oui.json")
OUI_CACHE = {}


def load_oui_database():
    """
    Carrega o JSON e transforma-o num dicionário { 'OUI': 'Empresa' }
    para buscas instantâneas.
    """
    global OUI_CACHE
    
    if not OUI_CACHE and os.path.exists(JSON_PATH):

        try:

            with open(JSON_PATH, "r", encoding = "utf-8") as f:

                data = json.load(f)
                OUI_CACHE = {item['oui']: item['company'] for item in data}
            print(f"[i] Base de dados OUI carregada: {len(OUI_CACHE)} registos.") 

        except Exception as e:
            print(f"[-] Erro ao carregar base de dados local: {e}")


def normalize_mac(mac):
    """
    Transforma 'aa:bb:cc:11:22:33' em 'AABBCC' para busca.
    """

    if not mac:
        return ""
    
    clean_mac = mac.replace(":", "").replace("-", "").upper()

    return clean_mac[:6]



def get_company_online(mac):
    """
    Tenta usar uma API como último recurso
    """

    try:

        response = requests.get(f"https://api.macvendors.com/{mac}", timeout = 2)
        if response.status_code == 200:
            return response.text
        
    except:
        pass
    return None




def get_company(mac):
    """
    Função chamada pelo main.py
    """

    load_oui_database()
    prefix = normalize_mac(mac)
    company = OUI_CACHE.get(prefix)

    if company:
        return company
    
    company = get_company_online(mac)

    if company:
        return f"{company} (Online)"
    
    return "Fabricante Desconhecido"