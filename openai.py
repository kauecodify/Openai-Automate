import pyautogui
import time

def open_browser_and_search():
    # Abre o navegador
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.write('C:\\Users\\Aluno\\AppData\\Local\\Programs\\Opera GX\\launcher.exe\n', interval=0.1)
    time.sleep(3)

    # Aguarda o navegador abrir
    time.sleep(4)

     # acessa site chatgpt
    url = 'https://chatgpt.com'
    pyautogui.write(url + '\n', interval=0.1)
    time.sleep(5)

    # Escreve a pergunta no chatGPT
    search_query = "me mostre 3 jogos de playstation 2 de aventura rpg"
    pyautogui.write(search_query + '\n', interval=0.1)
    time.sleep(5) # aqui aguarda a resposta do chatGPT

if __name__ == "__main__":
    open_browser_and_search()
