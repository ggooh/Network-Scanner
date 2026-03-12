import urllib.request
import json
import re
import os

def update_oui_json():
    url = "http://standards-oui.ieee.org/oui/oui.txt"
    json_path = os.path.join(os.path.dirname(__file__), "..", "scanner", "oui.json")
    
    print("[+] A descarregar lista oficial do IEEE... (pode demorar)")

    # Criação de um "User-Agent" para o servidor não bloquear
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:

        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            
        oui_list = []
        pattern = re.compile(r'^([0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2})\s+\(hex\)\s+(.*)$', re.MULTILINE)
        matches = pattern.findall(data)
        
        for match in matches:
            prefix = match[0].replace("-", "") 
            company = match[1].strip()
            oui_list.append({"oui": prefix, "company": company})
            
        with open(json_path, 'w', encoding='utf-8') as f:

            json.dump(oui_list, f, indent=4)
        print(f"[+] Sucesso! {len(oui_list)} fabricantes guardados em {json_path}")

    except Exception as e:
        print(f"[-] Erro ao atualizar: {e}")

if __name__ == "__main__":
    update_oui_json()