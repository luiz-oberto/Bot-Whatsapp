import webbrowser
import pyautogui
from time import sleep

telefones = [] 

with open('telefones.txt') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(5)
    pyautogui.click(-1012,443, duration=1)
    sleep(2)
    pyautogui.click(-1027,539, duration=1)
    sleep(10)
    pyautogui.click(-1122,993, duration=1)
    sleep(1)
    pyautogui.typewrite('Ola, voce tem interesse em participar do grupo?')
    sleep(1)
    pyautogui.press('enter')
    sleep(20)