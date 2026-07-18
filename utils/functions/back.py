import time
def back(driver, delay: float = 1):
        """
        Aguarda um pequeno delay antes de navegar para trás,
        garantindo que a tela atual finalize suas transições/animações
        antes do comando 'back' ser disparado.
        """
        time.sleep(delay)
        driver.back()