import requests
import os
import time

URL = "https://www.studefi.fr/main.php?srv=Residence&op=show&cdGroupe=801G"
TEXTO = "test"

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers, timeout=10)
    return TEXTO in r.text

print("Iniciando monitoramento...")

try:
    for i in range(29):  # 29 vezes = quase 5 min se usar 10s
        print(f"Check {i+1}/30")

        indisponivel = check()

        if not indisponivel:
            print("🚨 LOGEMENT DISPONÍVEL!!!")
            enviar("🚨 LOGEMENT DISPONÍVEL!!!")
            break  # para imediatamente se achar vaga

        time.sleep(10)

    print("Loop finalizado")

except Exception as e:
    print("Erro:", e)
