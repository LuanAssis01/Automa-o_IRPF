import pyautogui
import time

pyautogui.PAUSE = 0.3

# Funções de tela
# print(pyautogui.position())
# print(pyautogui.size())


time.sleep(3)
# Funções do mouse
#pyautogui.click(x=1342, y=789, button="right", clicks=1)
pyautogui.moveTo(x=634, y=205, duration=1)
pyautogui.click(x=865, y=290, button="left", clicks=1)

pyautogui.write("Olá")
pyautogui.hotkey("ctrl", "c") # Atalhos doteclado
pyautogui.press("enter") # preciona alguma tecla  