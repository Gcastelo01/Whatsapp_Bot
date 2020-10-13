from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from time import sleep


class Web_Browser:

    """Serve para estabelecer a conexão com o Google chrome. Para isso, definimos uma variável de Instância chamada
    _browser. Não altere nada dentro dessa classe. Ela deve ser usada como classe mãe para qualquer outra classe que
    queira abrir um website dentro do google chrome. """

    def __init__(self):
        self._browser = webdriver.Chrome("D:\GABRIEL\Pycharm\Jarvis\drivers\chromedriver_win32\chromedriver.exe")


class Messenger(Web_Browser):
    """Classe filha de Web_Browser. Serve para estabelecer uma conexão com os servidores do Whatsapp."""

    def __get_target__(self, target):

        """Método interno da classe para recuperar o nome do contato do destinatário. Não deve ser utilizado no programa
        principal. Apenas dentro da classe."""

        __barra = self._browser.find_element_by_class_name('_3qx7_')
        __barra.click()
        __barra = self._browser.find_element_by_class_name('_3FRCZ.copyable-text.selectable-text')
        __barra.send_keys(target)
        sleep(0.5)
        self._browser.find_element_by_class_name('_210SC').click()
        self._browser.find_element_by_class_name('_3uMse').click()

    def __get_elements__(self, text):

        """Método interno da Classe. Não deve ser utilizado com ojetos instanciados dentro do programa.
        Serve apenas para dar à classe acessibilidade aos campos adequados dentro da página web."""

        __text_box = self._browser.find_element_by_class_name('_2FVVk._2UL8j')

        for c in text:
            __text_box.send_keys(c)
            __send_button = self._browser.find_element_by_class_name('_1U1xa')
            __send_button.send_keys(Keys.ENTER)
            sleep(1.5)

    def send_text(self, *args):

        """Função responsável por abrir o whatsapp e enviar o texto desejado. O parâmetro *args permite que o usuário do
         código coloque, em sequência, todas as mensagens que deseja enviar, na forma de strings separadas por vírgulas.
         As mensagens serão enviadas separadamente. Não há máximo ou mínimo de número de mensagens."""

        self._browser.get('https://web.whatsapp.com/')
        __cb = self._browser.find_element_by_name('rememberMe')
        __cb.click()
        is_done = True

        while is_done:
            try:
                sleep(8)
                Messenger.__get_elements__(self, args)  # Enviando as mensagens
                self._browser.close()  # Fecha a janela do Chrome que havia sido aberta
                self._browser.quit()  # Encerra a execução do driver do google chrome, que estava rodando em 2º Plano
                is_done = False

            except exceptions.NoSuchElementException:
                print('Favor realizar login e clicar na conversa desejada para continuar.')

    def send_multiple_texts(self, num: int, *args: str):

        """Permite que o usuário mande diversas vezes uma mesma mensagem ou sequência de mensagens para o destinatário.
        No geral, funciona como o send text, mas com a diferença de que agora ele manda mais de uma vez a sequencia de
        mensagens. O parâmetro num define o número de vezes que a mensagem será enviada para o destinatário"""

        self._browser.get('https://web.whatsapp.com/')
        __cb = self._browser.find_element_by_name('rememberMe')
        __cb.click()
        is_done = True

        while is_done:
            try:
                sleep(8)

                for v in range(0, num):  # Enviando a mensagem pelo número de vezes exigido
                    Messenger.__get_elements__(self, args)  # Enviando as mensagens

                self._browser.close()  # Fecha a janela do Chrome que havia sido aberta
                self._browser.quit()  # Encerra a execução do driver do google chrome, que estava rodando em 2º Plano
                is_done = False

            except exceptions.NoSuchElementException:
                print('Favor realizar login e clicar na conversa desejada para continuar.')

    def send_text_to(self, target, *args):
        self._browser.get('https://web.whatsapp.com/')
        __cb = self._browser.find_element_by_name('rememberMe')
        __cb.click()
        is_done = True

        while is_done:
            try:
                sleep(8)
                Messenger.__get_target__(self, target)
                Messenger.__get_elements__(self, args)  # Enviando as mensagens
                self._browser.close()  # Fecha a janela do Chrome que havia sido aberta
                self._browser.quit()  # Encerra a execução do driver do google chrome, que estava rodando em 2º Plano
                is_done = False

            except exceptions.NoSuchElementException:
                print('Favor realizar login e clicar na conversa desejada para continuar.')
