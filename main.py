import requests
import time

FREQUENCIA = 15  # segundos entre cada verificação

URL = "https://www.studefi.fr/main.php?srv=Residence&op=show&cdGroupe=801G"
TEXTO = "Aucun logement disponible"

TOKEN = "8721057763:AAFTvG9NbWwmyIQMdW6wZDoBw0ojDsnVTZ8"
CHAT_ID = "8547911301"

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers, timeout=10)
    return TEXTO in r.text

ja_notificou = False
count = 0

while True:
    print("Verificando disponibilidade...")
    try:
        indisponivel = check()

        if not indisponivel and not ja_notificou:
            print("🚨 LOGEMENT DISPONÍVEL!!!")
            enviar("🚨 LOGEMENT DISPONÍVEL!!!")
            ja_notificou = True
        if indisponivel:
            print("Nada ainda...")
        if ja_notificou:
            count += 1
            print("Já notificado, contador:", count)
            if count % 3 == 0:  # Reenvia a cada 3 verificações para lembrar
                ja_notificou = False  # reset para permitir nova notificação se voltar a ficar
                count = 0  # reset do contador

    except Exception as e:
        print("Erro:", e)

    time.sleep(FREQUENCIA) 