import pyautogui
import pyscreeze
from pyautogui import hotkey, write, press
from time import sleep
import os
from functions_reserve import *

OFFSET_X = 1050

# Nessa função nós localizamos e clicamos apenas no fechamento R-2099
def localizar_R2099():
    for conf in [0.80, 0.75, 0.70]:
        try:
            return pyautogui.locateCenterOnScreen(
                "fechamento.png",
                confidence=conf,
                grayscale=True
            )
        except pyautogui.ImageNotFoundException:
            continue
    return None

def clicar_evento_R2099():
    fechamento = localizar_R2099()

    if not fechamento:
        print("Nenhum Fechamento encontrado.")
        return False

    print(f"Procurando Parâmetros 🔎")

    x_botao = fechamento.x + OFFSET_X
    pyautogui.click(x_botao, fechamento.y)
    print(f"Clicando no Evento 🕹️")
    return True

# Nessa função nós localizamos e clicamos apenas no fechamento R-4099
def localizar_R4099():
    for conf in [0.75]:
        try:
            resultados = list(pyautogui.locateAllOnScreen(
                "fechamento.png",
                confidence=conf,
                grayscale=True
            ))
        except (pyautogui.ImageNotFoundException, pyscreeze.ImageNotFoundException):
            return None
    if not resultados:
        return None

    # ordena por Y (posição vertical) e pega o último, ou seja, o mais embaixo
    resultados.sort(key=lambda box: box.top)
    ultimo = resultados[-1]

    centro_x = ultimo.left + ultimo.width // 2
    centro_y = ultimo.top + ultimo.height // 2
    return pyautogui.Point(x=centro_x, y=centro_y)

def clicar_evento_R4099():
    fechamento = localizar_R4099()

    if not fechamento:
        print("Nenhum Fechamento encontrado.")
        return False

    print(f"Procurando Parâmetros 🔎")

    x_botao = fechamento.x + OFFSET_X
    pyautogui.click(x_botao, fechamento.y)
    print(f"Clicando no Evento 🕹️")
    return True

# Nessa função entramos no Acesso Remoto
def acesso_remoto():
    os.startfile("mstsc.exe")
    sleep(3)
    press("enter")
    sleep(4)
    press("enter")
    sleep(2)
    press("tab")
    sleep(1)
    write("Pedrosilva2212", 0.05)
    sleep(1)
    press("enter")
    sleep(3)

# Função para entrar e navegar no sistema Domínio
def system():
    hotkey("alt", "enter")
    sleep(1)
    press("Win")
    sleep(2)
    write("Aplicativos:Dominio Escrita Fiscal.exe", 0.05)
    sleep(6)
    press("enter")
    sleep(10)
    write("Hemera123", 0.05)
    sleep(1)
    press("enter")
    sleep(55)

def navegar_dominio(cod):
    press("F")
    sleep(2)
    sleep(1)
    press('f8')
    sleep(2)
    write(cod)
    sleep(1)
    press("enter")
    sleep(12)
    pyautogui.click(x= 1050, y= 307)
    press("alt")
    sleep(1)
    press('r')
    sleep(2)
    press("N")
    sleep(1.5)
    press("F")
    sleep(1.5)
    press("N")
    sleep(1)
    press("enter")
    sleep(1)
    press("C")
    sleep(2)
    write(f"{datames()}", 0.05)
    sleep(1.5)
    press("tab")
    write(f"{datames()}", 0.05)
    sleep(1)
    press("tab")
    sleep(1)
    press("Up")
    sleep(1)
    press("Tab")
    sleep(1)
    press("L")
    sleep(2)
    press("tab", 11)
    sleep(1)
    press("Right", 5)
    sleep(1)
    press("pagedown")
    sleep(2)

def voltar():
    press("esc", 4)
# Nessa função Imprimimos o Recibo e baixamos na pasta teste por enquanto
def imprimir(cod, nome, evento):
    sleep(3)
    hotkey("Ctrl", "d")
    sleep(4)
    write(f"H:\\B - Obrigacoes Acessorias\\REINF\\{dataano()}\\RECIBOS\\{data()}\\Teste\\{cod} - {nome} - REINF {evento} {datames()}", 0.02)
    sleep(2)
    press("enter")
    sleep(8)
    press("esc")
    sleep(6)

