import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from elements.home_elements import ContactsElements
from utils.functions.back import back

PACKAGE_NAME = "com.android.contacts"


def restart_contacts_app(driver, settle_seconds: float = 2.0) -> None:
    """Encerra e reabre o app Contatos, aguardando a home estabilizar."""
    driver.terminate_app(PACKAGE_NAME)
    time.sleep(0.5)
    driver.activate_app(PACKAGE_NAME)
    time.sleep(settle_seconds)


def is_on_contacts_home(driver, timeout: float = 2) -> bool:
    """Retorna True se a toolbar 'Contatos' (home) estiver visível."""
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(
                ContactsElements.TEXT_TOOLBAR_TITLE["android"]
            )
        )
        return True
    except TimeoutException:
        return False


def return_to_contacts_home(driver, max_backs: int = 3) -> None:
    """
    Garante retorno à home de Contatos.
    Tenta voltar com back; só reinicia o app se ainda não estiver na home.
    """
    if is_on_contacts_home(driver, timeout=1):
        return

    for _ in range(max_backs):
        back(driver, delay=0.5)
        if is_on_contacts_home(driver, timeout=1):
            return

    restart_contacts_app(driver)

    if not is_on_contacts_home(driver, timeout=10):
        raise AssertionError(
            "Não foi possível retornar à home de Contatos (back + restart)."
        )


def ensure_on_contacts_home(driver) -> None:
    """
    Garante que o app está na home de Contatos antes de iniciar o fluxo do teste.
    Prefere back; reinicia apenas se necessário.
    """
    return_to_contacts_home(driver)
