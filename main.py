import requests
import os

URL = "https://www.studefi.fr/main.php?srv=Residence&op=show&cdGroupe=801G"
TEXTO = "Aucun logement disponibles"

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    
    print("Status code:", response.status_code)
    print("Resposta:", response.text)

def check():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers, timeout=10)
    return TEXTO in r.text

print("Verificando disponibilidade...")

try:
    indisponivel = check()

    if not indisponivel:
        print("🚨 LOGEMENT DISPONÍVEL!!!")
        enviar("🚨 LOGEMENT DISPONÍVEL!!!")

    else:
        print("Nada ainda...")

except Exception as e:
    print("Erro:", e)
