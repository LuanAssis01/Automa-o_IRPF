import pyautogui
import time
import webbrowser

# Configurações iniciais
pyautogui.PAUSE = 1.0
pyautogui.FAILSAFE = True  # Permite abortar movendo o mouse para canto superior esquerdo

def click_position(x, y, clicks=1, button="left", duration=0.5):
    """Função para mover e clicar em uma posição"""
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click(x=x, y=y, button=button, clicks=clicks)

def open_program(program_name):
    """Abre um programa usando o menu iniciar"""
    pyautogui.press("win")
    pyautogui.write(program_name)
    pyautogui.press("enter")
    time.sleep(3)

def generate_and_copy_from_4devs(url, generate_button, copy_button):
    """Gera e copia um valor (CPF/CNPJ) do site 4devs"""
    webbrowser.open(url)
    time.sleep(5) 
    
    click_position(*generate_button)
    time.sleep(2)
    click_position(*copy_button)
    time.sleep(2)

# Coordenadas definidas como constantes para fácil manutenção
COORDS = {
    "irpf": {
        "declaracao": (48, 34),
        "novo": (37, 61),
        "iniciar_branco": (1244, 635),
        "cpf_field": (800, 741),
        "rendimentos_pj": (836, 272),
        "novo_rendimento": (1649, 953),
        "cnpj_field": (448, 279),
        "ok_rendimento": (1650, 1007),
        "inicio": (414, 98),
        "imprimir": (1224, 296),
        "ok_imprimir": (1120, 484),
        "salvar_icone": (478, 219),
        "salvar_botao": (1093, 699)
    },
    "4devs": {
        "cpf": {
            "generate": (1094, 419),
            "copy": (1061, 512)
        },
        "cnpj": {
            "generate": (1083, 390),
            "copy": (1064, 483)
        }
    }
}

# Fluxo principal
def main():
    try:
        # Abre o programa IRPF
        open_program("IRPF 2025")
        time.sleep(5)

        # Clica nos botões para nova declaração
        click_position(*COORDS["irpf"]["declaracao"])
        click_position(*COORDS["irpf"]["novo"])
        click_position(*COORDS["irpf"]["iniciar_branco"])

        # Gera e insere CPF
        generate_and_copy_from_4devs(
            "https://www.4devs.com.br/gerador_de_cpf",
            COORDS["4devs"]["cpf"]["generate"],
            COORDS["4devs"]["cpf"]["copy"]
        )
        
        pyautogui.hotkey("alt", "tab")
        time.sleep(2)
        
        click_position(*COORDS["irpf"]["cpf_field"])
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        
        # Insere nome e confirma
        pyautogui.hotkey("tab")
        pyautogui.write("Luan Silva")
        pyautogui.hotkey("tab")
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)

        # Gera e insere CNPJ
        generate_and_copy_from_4devs(
            "https://www.4devs.com.br/gerador_de_cnpj",
            COORDS["4devs"]["cnpj"]["generate"],
            COORDS["4devs"]["cnpj"]["copy"]
        )
        
        pyautogui.hotkey("alt", "tab")
        
        # Preenche rendimentos PJ
        click_position(*COORDS["irpf"]["rendimentos_pj"])
        click_position(*COORDS["irpf"]["novo_rendimento"])
        
        click_position(*COORDS["irpf"]["cnpj_field"])
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey("tab")
        pyautogui.write("CEIA")
        
        click_position(*COORDS["irpf"]["ok_rendimento"])
        
        # Finaliza declaração
        click_position(*COORDS["irpf"]["inicio"])
        click_position(*COORDS["irpf"]["imprimir"])
        click_position(*COORDS["irpf"]["ok_imprimir"])
        
        time.sleep(5)
        click_position(*COORDS["irpf"]["salvar_icone"], clicks=2)
        time.sleep(3)
        click_position(*COORDS["irpf"]["salvar_botao"])
        
        print("Processo concluído com sucesso!")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        print("Posição atual do mouse:", pyautogui.position())

if __name__ == "__main__":
    main()