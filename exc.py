import pyautogui
import time

pyautogui.PAUSE = 1.0

# Abre o programa
pyautogui.press("win")
pyautogui.write("IRPF 2025")
pyautogui.press("enter")

time.sleep(2)

# Clica no botão (Declaração)
pyautogui.moveTo(x=22, y=77, duration=1)
pyautogui.click(x=22, y=77, button="left", clicks=1)

# Clica no botão (Novo)
pyautogui.moveTo(x=44, y=102, duration=1)
pyautogui.click(x=44, y=102, button="left", clicks=1)

# Clica no botão (Iniciar declaração em branco)
pyautogui.moveTo(x=1261, y=678, duration=1)
pyautogui.click(x=1261, y=678, button="left", clicks=1)

# Troca para a aba do navegador
# pyautogui.hotkey("alt", "tab") 
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

# Aperta na aba do site gerador de CPF
pyautogui.moveTo(x=150, y=57, duration=1)
pyautogui.click(x=150, y=57, button="left", clicks=1)


# Aperta em gerar CPF
pyautogui.moveTo(x=1100, y=496, duration=1)
pyautogui.click(x=1100, y=496, button="left", clicks=1)

# Copia o CPF gerado
pyautogui.moveTo(x=1062, y=579, duration=1)
pyautogui.click(x=1062, y=579, button="left", clicks=1)

time.sleep(2)

# Volta para o programa
pyautogui.hotkey("alt", "tab") 

time.sleep(2)

# Colo o CPF gerado
pyautogui.moveTo(x=794, y=786, duration=1)
pyautogui.click(x=794, y=786, button="left", clicks=1)
pyautogui.hotkey("ctrl", "v") 

time.sleep(2)

# Insiro o nome da pesso
pyautogui.hotkey("tab")
pyautogui.write("Luan Silva")

# Aperto o botão OK
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
time.sleep(2)
pyautogui.hotkey("enter")

# Troca para a aba do navegador
pyautogui.hotkey("alt", "tab")

# Aperta na aba do CNPJ
pyautogui.moveTo(x=262, y=56, duration=1)
pyautogui.click(x=262, y=56, button="left", clicks=1)

# Aperta em gerar CNPJ
pyautogui.moveTo(x=1102, y=460, duration=1)
pyautogui.click(x=1102, y=460, button="left", clicks=1)

# Copia o CNPJ gerado
pyautogui.moveTo(x=1057, y=555, duration=1)
pyautogui.click(x=1057, y=555, button="left", clicks=1)

# Volta para o programa
pyautogui.hotkey("alt", "tab") 

# Aperto em Rendimentos Tributáveis REcebidos PJ
pyautogui.moveTo(x=824, y=252, duration=1)
pyautogui.click(x=824, y=252, button="left", clicks=1)

# Aperto em Novo
pyautogui.moveTo(x=1645, y=999, duration=1)
pyautogui.click(x=1645, y=999, button="left", clicks=1)

# Colo o CNPJ gerado
pyautogui.moveTo(x=510, y=224, duration=1)
pyautogui.click(x=510, y=224, button="left", clicks=1)
pyautogui.hotkey("ctrl", "v") 

# Insiro o nome da fonte pagadora
pyautogui.hotkey("tab")
pyautogui.write("CEIA")

# Aperto em OK
pyautogui.moveTo(x=1652, y=1059, duration=1)
pyautogui.click(x=1652, y=1059, button="left", clicks=1)

# Aperto em Importar arquivo
pyautogui.moveTo(x=1656, y=1058, duration=1)
pyautogui.click(x=1656, y=1058, button="left", clicks=1)

# Aperto em Ok
pyautogui.moveTo(x=1086, y=724, duration=1)
pyautogui.click(x=1086, y=724, button="left", clicks=1)



















