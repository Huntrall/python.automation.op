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

if funcao_escolhida == "1":
    print("dinossauro")