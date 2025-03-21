import pyautogui as pyau
import time
import cv2
import os

pyau.press("win")
time.sleep(1)

pyau.write("react")
time.sleep(1)

pyau.press("enter")
time.sleep(2)

email = pyau.locateOnScreen("images\\email.png", confidence=0.8)
pyau.click(email)
time.sleep(1)

pyau.write("henrique.bento@delphostec.com.br")
time.sleep(1)

password = pyau.locateOnScreen("images\\password.png", confidence=0.8)
pyau.click(password)
time.sleep(1)

pyau.write("D@r1us@123")
pyau.press("enter")
time.sleep(3)

try:
    buttoncontinue = pyau.locateOnScreen("images\\continue.png", confidence=0.8)
    if buttoncontinue:
        pyau.click(buttoncontinue)
        time.sleep(70)
        abrircomputador = pyau.locateOnScreen("images\\abrircomputador.png", confidence=0.8)
        pyau.click(abrircomputador)
except pyau.ImageNotFoundException:
    print("Imagem 'images\\continue.png' não encontrada, seguindo para o próximo passo...")

time.sleep(2)

try:
    abrircomputador = pyau.locateOnScreen("images\\abrircomputador.png", confidence=0.8)
    pyau.click(abrircomputador)
except pyau.ImageNotFoundException:
    print("Erro: 'images\\brircomputador.png' não encontrada.")

time.sleep(25)

abrirsarwin = pyau.locateOnScreen("images\\arwin.png", confidence=0.8)
pyau.click(abrirsarwin, clicks=2)

time.sleep(2)

abriremp = pyau.locateOnScreen("images\\emp.png", confidence=0.8)
pyau.click(abriremp, clicks=2)

time.sleep(2)

abrirdespesa = pyau.locateOnScreen("images\\despesa.png", confidence=0.8)
pyau.click(abrirdespesa, clicks=2)

time.sleep(4)

pyau.write("erminio.nicolleti")
pyau.press("tab")
pyau.write("160796")
pyau.press("enter")

time.sleep(7)

abrirprocesso = pyau.locateOnScreen("images\\processo.png", confidence=0.8)
pyau.click(abrirprocesso, clicks=2)

time.sleep(1)

importadespesa = pyau.locateOnScreen("images\\importadespesa.png", confidence=0.8)
pyau.click(importadespesa)

time.sleep(1)

clicaplanilha = pyau.locateOnScreen("images\\planilha.png", confidence=0.8)
pyau.click(clicaplanilha)

clicaabrirarquivo = pyau.locateOnScreen("images\\abrirarquivo.png", confidence=0.8)
pyau.click(clicaabrirarquivo)

time.sleep(2)

clicaestecomputador = pyau.locateOnScreen("images\\estecomputador.png", confidence=0.8)
pyau.click(clicaestecomputador)

time.sleep(1)

screen_width, screen_height = pyau.size()

center_x = screen_width // 2
center_y = screen_height // 2

pyau.moveTo(center_x, center_y)

pyau.scroll(-500)

time.sleep(2)

clicasetores = pyau.locateOnScreen("images\\setores.png", confidence=0.8)
pyau.click(clicasetores, clicks=2)

time.sleep(0.5)

clicati = pyau.locateOnScreen("images\\TI.png", confidence=0.8)
pyau.click(clicati, clicks=2)

time.sleep(0.5)

clicaautoop = pyau.locateOnScreen("images\\autoop.png", confidence=0.8)
pyau.click(clicaautoop, clicks=2)

pasta = r"\\192.168.100.245\\Setores\\TI\\automacaoop"

arquivos = os.listdir(pasta)

diretorioarquivo = pyau.locateOnScreen("images\\diretorioarquivo.png", confidence=0.8)
pyau.click(diretorioarquivo)

pyau.write("H:\TI\AUTOMACAOOP\ ")
pyau.press("backspace")
pyau.write(arquivos[0])