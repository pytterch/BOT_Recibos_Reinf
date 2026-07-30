import datetime
import psutil

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

def VPN(nome_processo):
    for processo in psutil.process_iter(["name"]):
        if nome_processo.lower() in processo.info["name"].lower():
            return True
    return False