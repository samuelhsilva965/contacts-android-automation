from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.home_elements import ContactsElements


class ContactsPage:

    def __init__(self, driver, platform: str = "android", timeout: int = 10):
        self.driver = driver
        self.platform = platform.lower()
        self.wait = WebDriverWait(driver, timeout)
        self.elements = ContactsElements

    # -------------------------
    # Getters
    # -------------------------

    def get_btn_open_navigation_drawer(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_OPEN_NAVIGATION_DRAWER[self.platform]
            )
        )

    def get_text_toolbar_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_TOOLBAR_TITLE[self.platform]
            )
        )

    def get_text_empty_contacts_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_EMPTY_CONTACTS_MESSAGE[self.platform]
            )
        )

    def get_btn_add_account(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_ADD_ACCOUNT[self.platform]
            )
        )

    def get_btn_import_contacts(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_IMPORT_CONTACTS[self.platform]
            )
        )

    def get_btn_create_new_contact(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_CREATE_NEW_CONTACT[self.platform]
            )
        )

    def get_icon_empty_contacts(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.ICON_EMPTY_CONTACTS[self.platform]
            )
        )

    # -------------------------
    # Actions / Clicks
    # -------------------------

    def click_btn_open_navigation_drawer(self):
        self.get_btn_open_navigation_drawer().click()

    def click_btn_add_account(self):
        self.get_btn_add_account().click()

    def click_btn_import_contacts(self):
        self.get_btn_import_contacts().click()

    def click_btn_create_new_contact(self):
        self.get_btn_create_new_contact().click()

    # -------------------------
    # Validations
    # -------------------------

    def is_contacts_list_empty(self) -> bool:
        """Verifica se a mensagem de lista vazia está visível."""
        try:
            return self.get_text_empty_contacts_message().is_displayed()
        except Exception:
            return False

    def get_toolbar_title_text(self) -> str:
        """Retorna o texto do título da toolbar."""
        return self.get_text_toolbar_title().text

