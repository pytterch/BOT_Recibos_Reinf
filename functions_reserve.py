import datetime
import pyautogui

def mes_anterior():
    agora = datetime.datetime.today()
    return agora.replace(day=1) - datetime.timedelta(days=1)

# Não tirar isso, é o que transforma o return em _string_
competencia = mes_anterior()

def datames():
    return str(competencia.strftime("%m%Y"))

def data():
    return str(competencia.strftime("%m"))

def dataano():
    return str(competencia.strftime("%Y"))

# Lê a mensagem de erro caso apareça na tela
def localizar_erro():
    for conf in [0.80, 0.75, 0.70]:
        try:
            return pyautogui.locateCenterOnScreen(
                "erro.png",
                confidence=conf,
                grayscale=True
            )
        except pyautogui.ImageNotFoundException:
            continue
    return None
