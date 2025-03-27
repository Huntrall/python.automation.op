import pyautogui as pyau
import time
import cv2
import os

funcao_escolhida = None

opcoesempresas = {"1", "2", "3"}


while True:
    print("\nEscolha a empresa que irá fazer a operação:")
    print("1 - emp")
    print("2 - serv")    
    print("3 - vig")

    escolha = input("Digite o número da opção: ")  
    
    if escolha in opcoesempresas:
        funcao_escolhida = escolha
        break  
    else:
        print("Opção inválida! Tente novamente.")

emaildigita = input(str("Digite seu email: "))
senhadigita = input("Digite a sua senha: ")
usuariosarwin = input("Digite o usuário do sarwin: ")
senhasarwin = input("Digite a senha do sarwin: ")

pyau.press("win")
time.sleep(1)

pyau.write("react")
time.sleep(1)

pyau.press("enter")
time.sleep(1)

while True:
    try:
        email = pyau.locateOnScreen("images\\email.png", confidence=0.8)
        if email:
            pyau.click(email)
            break
    except Exception as e:
        pass
    time.sleep(1)

pyau.write(emaildigita)
time.sleep(1)

password = pyau.locateOnScreen("images\\password.png", confidence=0.8)
pyau.click(password)
time.sleep(1)

pyau.write(senhadigita)
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

while True:
    try:
        abrirsarwin = pyau.locateOnScreen("images\\sarwin.png", confidence=0.8)
        if abrirsarwin:
            pyau.click(abrirsarwin, clicks=2)
            break
    except Exception as e:
        pass
    time.sleep(1)

time.sleep(2)

while True:
    try:
        abriremp = pyau.locateOnScreen("images\\emp.png", confidence=0.8)
        if funcao_escolhida == "1":
            pyau.click(abriremp, clicks=2)
        elif funcao_escolhida == "2":
            abrirserv = pyau.locateOnScreen("images\\serv.png", confidence=0.8)
            pyau.click(abrirserv, clicks=2)
        elif funcao_escolhida == "3":
            abrirvig = pyau.locateOnScreen("images\\vig.png", confidence=0.8)
            pyau.click(abrirvig, clicks=2)
        break
    except Exception as e:
        pass
    time.sleep(1)


time.sleep(2)

abrirdespesa = pyau.locateOnScreen("images\\despesa.png", confidence=0.8)
pyau.click(abrirdespesa, clicks=2)

time.sleep(4)

pyau.write(usuariosarwin)
pyau.press("tab")
pyau.write(senhasarwin)
pyau.press("enter")

while True:
    try:
        abrirprocesso = pyau.locateOnScreen("images\\processo.png", confidence=0.8)
        if abrirprocesso:
            pyau.click(abrirprocesso, clicks=2)
            importadespesa = pyau.locateOnScreen("images\\importadespesa.png", confidence=0.8)
            pyau.click(importadespesa)
            break
    except Exception as e:
        pass
    time.sleep(1)

while True:
    try:
        clicaplanilha = pyau.locateOnScreen("images\\planilha.png", confidence=0.8)
        if clicaplanilha:
            pyau.click(clicaplanilha)
            break
    except Exception as e:
        pass
    time.sleep(1)

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

        while True:
            try:
                okprocesso = pyau.locateOnScreen("images\\okprocesso.png", confidence=0.8)
                if abrirprocesso:
                    pyau.click(okprocesso)
                    break
            except Exception as e:
                pass
            time.sleep(1)

        time.sleep(4)

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

time.sleep(2)

try:
    finaldireita = pyau.locateOnScreen("images\\finaldireita.png", confidence=0.8)
    if finaldireita:
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

                pyau.write("s")
                    
                sigame = pyau.locateOnScreen("images\\sigame.png", confidence=0.8)
                pyau.click(sigame)

                time.sleep(5)

                pyau.press("enter")

                time.sleep(3)

                movaesquerda = pyau.locateOnScreen("images\\movaesquerda.png", confidence=0.8)
                pyau.click(movaesquerda)

                time.sleep(3)
except pyau.ImageNotFoundException:
    print("Aparentemente só tem 1 op")

time.sleep(2)

try:
    clicaop = pyau.locateOnScreen("images\\clicaop.png", confidence=0.8)
    pyau.click(clicaop)
                    
    time.sleep(10)

    clicaimpressora = pyau.locateOnScreen("images\\clicaimpressora.png", confidence=0.8)
    pyau.click(clicaimpressora)

    time.sleep(5)

    pyau.write("s")
                    
    sigame = pyau.locateOnScreen("images\\sigame.png", confidence=0.8)
    pyau.click(sigame)

    time.sleep(5)

    pyau.press("enter")
except pyau.ImageNotFoundException:
    print("Não tem op.")