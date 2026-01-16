from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    try:
        # Cria uma instância do Navegador
        bot = webdriver.Firefox()

        # Acessa página Practice Test Automation
        bot.get("https://practicetestautomation.com/practice-test-login/")

        # Dados de acesso
        username = "student"
        password = "Password123"

        # Busca pelo elemento input de nome de usuário
        input_username = bot.find_element(By.ID, "username")
        # Ação de digitar
        input_username.send_keys(username)

        # Busca pelo elemento input de senha
        input_password = bot.find_element(By.ID, "password")
        # Ação de digitar
        input_password.send_keys(password)

        # Busca pelo elemento botão submit
        input_button = bot.find_element(By.ID, "submit")
        # Ação de clicar
        input_button.click()

        # Aguarda 3 segundos para garantir que carregou a página com resultado
        sleep(3)

        # Busca pela confirmação de login
        logged = bot.find_element(By.CSS_SELECTOR, ".post-title")
        # Imprime o texto da confirmação
        print(logged.text)        

        # Busca pelo elemento botão log out
        logout = bot.find_element(By.CSS_SELECTOR, ".wp-block-button__link")
        # Ação de clicar
        logout.click()

        # Busca pelo titulo login para garantir que fez o logout
        bot.find_element(By.CSS_SELECTOR, "#login > h2:nth-child(1)")

    except Exception as ex:
        # Busca pelo elemento de mensagem de erro
        error_alert = bot.find_element(By.ID, "error")
        print(error_alert.text)

        # Grava uma captura de tela
        bot.save_screenshot("captura.png")

    finally:
        # Finaliza fechando o navegador
        bot.quit()

        # Imprime mensagem de finalização
        print("Finalizado")

if __name__ == "__main__":
    main()
