import pyautogui as pyau
import time
import cv2
import os

pyau.press("win")
time.sleep(1)

pyau.write("react")
time.sleep(1)

pyau.press("enter")
time.sleep(4)

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
    print("Erro: 'images\\abrircomputador.png' não encontrada.")

time.sleep(25)

abrirsarwin = pyau.locateOnScreen("images\\sarwin.png", confidence=0.8)
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

time.sleep(2)

pasta = r"\\192.168.100.245\\Setores\\TI\\automacaoop"

arquivos = os.listdir(pasta)


for arquivo in arquivos:
    caminho_completo = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho_completo):
        print(f"processando: {arquivo}")
        diretorioarquivo = pyau.locateOnScreen("images\\diretorioarquivo.png", confidence=0.8)
        pyau.click(diretorioarquivo)

        pyau.write("H:\TI\AUTOMACAOOP\ ")
        pyau.press("backspace")
        pyau.write(arquivo)

        time.sleep(6)
        
        confirma = pyau.locateOnScreen("images\\confirma.png", confidence=0.8)
        pyau.click(confirma)

        time.sleep(4)

        okprocesso = pyau.locateOnScreen("images\\okprocesso.png", confidence=0.8)
        pyau.click(okprocesso)

        time.sleep(2)

        pyau.press("tab", presses=4)
        pyau.press("backspace")

        time.sleep(4)

sairprocesso = pyau.locateOnScreen("images\\sairprocesso.png", confidence=0.8)
pyau.click(sairprocesso)

time.sleep(2)

cadastro = pyau.locateOnScreen("images\\cadastro.png", confidence=0.8)
pyau.click(cadastro)

time.sleep(2)

despesacadastro = pyau.locateOnScreen("images\\despesacadastro.png", confidence=0.8)
pyau.click(despesacadastro)

time.sleep(2)

departamento = pyau.locateOnScreen("images\\departamento.png", confidence=0.8)
pyau.click(departamento)

time.sleep(1)

pyau.write("26")

time.sleep(1)

pyau.press("enter")