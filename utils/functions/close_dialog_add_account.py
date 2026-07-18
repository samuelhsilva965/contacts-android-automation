from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException


def click_btn_cancel_dialog_adicionar_conta_if_present(driver, timeout=3):
    """
    Fecha o diálogo de 'adicionar conta' se ele estiver visível.
    Usa um timeout curto e próprio, já que esse diálogo só aparece
    condicionalmente (normalmente na primeira execução do app).
    """
    try:
        short_wait = WebDriverWait(driver, timeout)
        button = short_wait.until(
            EC.visibility_of_element_located(
                (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.contacts:id/left_button"]')
            )
        )
        button.click()
    except TimeoutException:
        pass