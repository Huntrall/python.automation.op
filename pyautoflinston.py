import pyautogui as pyau
import time
import cv2
import os
"""
pyau.press("win")
time.sleep(1)

pyau.write("react")
time.sleep(1)

pyau.press("enter")
time.sleep(2)

email = pyau.locateOnScreen("email.png", confidence=0.8)
pyau.click(email)
time.sleep(1)

pyau.write("henrique.bento@delphostec.com.br")
time.sleep(1)

password = pyau.locateOnScreen("password.png", confidence=0.8)
pyau.click(password)
time.sleep(1)

pyau.write("D@r1us@123")
pyau.press("enter")
time.sleep(3)

try:
    buttoncontinue = pyau.locateOnScreen("continue.png", confidence=0.8)
    if buttoncontinue:
        pyau.click(buttoncontinue)
        time.sleep(70)
        abrircomputador = pyau.locateOnScreen("abrircomputador.png", confidence=0.8)
        pyau.click(abrircomputador)
except pyau.ImageNotFoundException:
    print("Imagem 'continue.png' não encontrada, seguindo para o próximo passo...")

time.sleep(2)

try:
    abrircomputador = pyau.locateOnScreen("abrircomputador.png", confidence=0.8)
    pyau.click(abrircomputador)
except pyau.ImageNotFoundException:
    print("Erro: 'abrircomputador.png' não encontrada.")

time.sleep(25)

abrirsarwin = pyau.locateOnScreen("sarwin.png", confidence=0.8)
pyau.click(abrirsarwin, clicks=2)

time.sleep(2)

abriremp = pyau.locateOnScreen("emp.png", confidence=0.8)
pyau.click(abriremp, clicks=2)

time.sleep(2)

abrirdespesa = pyau.locateOnScreen("despesa.png", confidence=0.8)
pyau.click(abrirdespesa, clicks=2)

time.sleep(4)

pyau.write("erminio.nicolleti")
pyau.press("tab")
pyau.write("160796")
pyau.press("enter")

time.sleep(7)

abrirprocesso = pyau.locateOnScreen("processo.png", confidence=0.8)
pyau.click(abrirprocesso, clicks=2)

time.sleep(1)

importadespesa = pyau.locateOnScreen("importadespesa.png", confidence=0.8)
pyau.click(importadespesa)

time.sleep(1)

clicaplanilha = pyau.locateOnScreen("planilha.png", confidence=0.8)
pyau.click(clicaplanilha)

clicaabrirarquivo = pyau.locateOnScreen("abrirarquivo.png", confidence=0.8)
pyau.click(clicaabrirarquivo)

time.sleep(2)

clicaestecomputador = pyau.locateOnScreen("estecomputador.png", confidence=0.8)
pyau.click(clicaestecomputador)

time.sleep(1)

screen_width, screen_height = pyau.size()

center_x = screen_width // 2
center_y = screen_height // 2

pyau.moveTo(center_x, center_y)

pyau.scroll(-500)

time.sleep(2)

clicasetores = pyau.locateOnScreen("setores.png", confidence=0.8)
pyau.click(clicasetores, clicks=2)

time.sleep(0.5)

clicati = pyau.locateOnScreen("TI.png", confidence=0.8)
pyau.click(clicati, clicks=2)

time.sleep(0.5)

clicaautoop = pyau.locateOnScreen("autoop.png", confidence=0.8)
pyau.click(clicaautoop, clicks=2)

"""

pasta = r"\\192.168.100.245\\Setores\\TI\\automacaoop"

arquivos = os.listdir(pasta)

diretorioarquivo = pyau.locateOnScreen("images\\diretorioarquivo.png", confidence=0.8)
pyau.click(diretorioarquivo)

pyau.write("H:\TI\AUTOMACAOOP\ ")
pyau.press("backspace")
pyau.write(arquivos[0])