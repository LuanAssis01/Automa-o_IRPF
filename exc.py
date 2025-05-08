import pyautogui
import time

pyautogui.PAUSE = 1.0

# Abre o programa
pyautogui.press("win")
pyautogui.write("IRPF 2025")
pyautogui.press("enter")

time.sleep(5)

# Clica no botão (Declaração)
pyautogui.moveTo(x=48, y=34, duration=1)
pyautogui.click(x=48, y=34, button="left", clicks=1)

# Clica no botão (Novo)
pyautogui.moveTo(x=37, y=61, duration=1)
pyautogui.click(x=37, y=61, button="left", clicks=1)

# Clica no botão (Iniciar declaração em branco)
pyautogui.moveTo(x=1244, y=635, duration=1)
pyautogui.click(x=1244, y=635, button="left", clicks=1)

# Troca para a aba do navegador
# pyautogui.hotkey("alt", "tab") 
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

pyautogui.write("https://www.4devs.com.br/gerador_de_cpf")
pyautogui.press("enter")

# Aperta em gerar CPF
pyautogui.moveTo(x=1094, y=419, duration=1)
pyautogui.click(x=1094, y=419, button="left", clicks=1)

# Copia o CPF gerado
pyautogui.moveTo(x=1061, y=512, duration=1)
pyautogui.click(x=1061, y=512, button="left", clicks=1)

time.sleep(2)

# Volta para o programa
pyautogui.hotkey("alt", "tab") 

time.sleep(2)

# Colo o CPF gerado
pyautogui.moveTo(x=800, y=741, duration=1)
pyautogui.click(x=800, y=741, button="left", clicks=1)
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

time.sleep(2)

# Troca para a aba do navegador
pyautogui.hotkey("alt", "tab")

time.sleep(2)

# Abro a aba do gerador de CNPJ
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://www.4devs.com.br/gerador_de_cnpj")
pyautogui.hotkey("enter")

# Aperta em gerar CNPJ
pyautogui.moveTo(x=1083, y=390, duration=1)
pyautogui.click(x=1083, y=390, button="left", clicks=1)

# Copia o CNPJ gerado
pyautogui.moveTo(x=1064, y=483, duration=1)
pyautogui.click(x=1064, y=483, button="left", clicks=1)

# Volta para o programa
pyautogui.hotkey("alt", "tab") 

# Aperto em Rendimentos Tributáveis REcebidos PJ
pyautogui.moveTo(x=836, y=2722, duration=1)
pyautogui.click(x=836, y=272, button="left", clicks=1)

# Aperto em Novo
pyautogui.moveTo(x=1649, y=953, duration=1)
pyautogui.click(x=1649, y=953, button="left", clicks=1)

# Colo o CNPJ gerado
pyautogui.moveTo(x=448, y=279, duration=1)
pyautogui.click(x=448, y=279, button="left", clicks=1)
pyautogui.hotkey("ctrl", "v") 

# Insiro o nome da fonte pagadora
pyautogui.hotkey("tab")
pyautogui.write("CEIA")

# Aperto em OK
pyautogui.moveTo(x=1650, y=1007, duration=1)
pyautogui.click(x=1650, y=1007, button="left", clicks=1)

# Volto em Inicio
pyautogui.moveTo(x=414, y=98, duration=1)
pyautogui.click(x=414, y=98, button="left", clicks=1)

# Aperto em Imprimir declaração
pyautogui.moveTo(x=1224, y=296, duration=1)
pyautogui.click(x=1224, y=296, button="left", clicks=1)

# Aperto em Ok
pyautogui.moveTo(x=1120, y=484, duration=1)
pyautogui.click(x=1120, y=484, button="left", clicks=1)

time.sleep(5)

# Clico no icone de salvamento
pyautogui.moveTo(x=478, y=219, duration=1)
pyautogui.click(x=478, y=219, button="left", clicks=2)

time.sleep(3)

# Aperto em salvar
pyautogui.moveTo(x=1093, y=699, duration=1)
pyautogui.click(x=1093, y=699, button="left", clicks=1)





