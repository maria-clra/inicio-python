import pyautogui
import pyperclip
import time

time.sleep(3)

mensagem = "Olá, tudo bem?\nAqui é a Maria Clara, do setor de SST"

pyperclip.copy(mensagem)      
pyautogui.hotkey("ctrl", "v") 
pyautogui.press("enter")


