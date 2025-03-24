import pyautogui as pyau
import time
import cv2
import os

pasta = r"\\192.168.100.245\\Setores\\TI\\automacaoop"

arquivos = os.listdir(pasta)

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

time.sleep(2)

finaldireita = pyau.locateOnScreen("images\\finaldireita.png", confidence=0.8)
pyau.click(finaldireita)

for arquivo in arquivos:
    caminho_completo = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho_completo):
        print(f"processando: {arquivo}")

        clicaop = pyau.locateOnScreen("images\\clicaop.png", confidence=0.8)
        pyau.click(clicaop)
        
        time.sleep(10)

        clicaimpressora = pyau.locateOnScreen("images\\clicaimpressora.png", confidence=0.8)
        pyau.click(clicaimpressora)

        time.sleep(5)

        pyau.write("ss")

        time.sleep(5)

        pyau.press("enter")

        time.sleep(3)

        movaesquerda = pyau.locateOnScreen("images\\movaesquerda.png", confidence=0.8)
        pyau.click(movaesquerda)

        time.sleep(3)