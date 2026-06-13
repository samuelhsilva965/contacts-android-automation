from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.create_contact_elements import CreateContactElements


class CreateContactPage:

    def __init__(self, driver, platform: str = "android", timeout: int = 10):
        self.driver = driver
        self.platform = platform.lower()
        self.wait = WebDriverWait(driver, timeout)
        self.elements = CreateContactElements

    # ── Toolbar ───────────────────────────────────────────────────────────────

    def get_btn_cancel(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_CANCEL[self.platform]
            )
        )

    def click_btn_cancel(self):
        self.get_btn_cancel().click()

    def get_text_toolbar_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_TOOLBAR_TITLE[self.platform]
            )
        )

    def get_btn_save(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_SAVE[self.platform]
            )
        )

    def click_btn_save(self):
        self.get_btn_save().click()

    def get_btn_cancel_dialog(self):
        return self.wait.until(EC.visibility_of_element_located(self.elements.BTN_CANCEL_DIALOG[self.platform]))
    def click_btn_cancel_dialog(self):
        self.get_btn_cancel_dialog().click()
        
    def get_btn_discard_dialog(self):
        return self.wait.until(EC.visibility_of_element_located(self.elements.BTN_DISCARD_DIALOG[self.platform]))

    def click_btn_discard_dialog(self):
        self.get_btn_discard_dialog().click()

    # ── Foto do contato ───────────────────────────────────────────────────────

    def get_btn_add_contact_photo(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_ADD_CONTACT_PHOTO[self.platform]
            )
        )

    def click_btn_add_contact_photo(self):
        self.get_btn_add_contact_photo().click()

    def get_icon_contact_photo(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.ICON_CONTACT_PHOTO[self.platform]
            )
        )

    # ── Conta de destino ──────────────────────────────────────────────────────

    def get_text_save_to_label(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_SAVE_TO_LABEL[self.platform]
            )
        )

    def get_text_account_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_ACCOUNT_NAME[self.platform]
            )
        )

    # ── Campos de nome ────────────────────────────────────────────────────────

    def get_icon_name_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.ICON_NAME_FIELD[self.platform]
            )
        )

    def get_input_first_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.INPUT_FIRST_NAME[self.platform]
            )
        )

    def click_input_first_name(self):
        self.get_input_first_name().click()

    def fill_input_first_name(self, value: str):
        field = self.get_input_first_name()
        field.click()
        #field.clear()
        field.send_keys(value)

    def get_input_last_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.INPUT_LAST_NAME[self.platform]
            )
        )

    def click_input_last_name(self):
        self.get_input_last_name().click()

    def fill_input_last_name(self, value: str):
        field = self.get_input_last_name()
        field.click()
        #field.clear()
        field.send_keys(value)

    def get_btn_expand_name_fields(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_EXPAND_NAME_FIELDS[self.platform]
            )
        )

    def click_btn_expand_name_fields(self):
        self.get_btn_expand_name_fields().click()

    # ── Campos de telefone ────────────────────────────────────────────────────

    def get_icon_phone_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.ICON_PHONE_FIELD[self.platform]
            )
        )

    def get_input_phone_number(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.INPUT_PHONE_NUMBER[self.platform]
            )
        )

    def click_input_phone_number(self):
        self.get_input_phone_number().click()

    def fill_input_phone_number(self, value: str):
        field = self.get_input_phone_number()
        field.click()
        #field.clear()
        field.send_keys(value)

    def get_element_phone_type_spinner(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.ELEMENT_PHONE_TYPE_SPINNER[self.platform]
            )
        )

    def click_element_phone_type_spinner(self):
        self.get_element_phone_type_spinner().click()

    def get_text_phone_type_selected(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_PHONE_TYPE_SELECTED[self.platform]
            )
        )

    # ── Campos de e-mail ──────────────────────────────────────────────────────

    def get_icon_email_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.ICON_EMAIL_FIELD[self.platform]
            )
        )

    def get_input_email(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.INPUT_EMAIL[self.platform]
            )
        )

    def click_input_email(self):
        self.get_input_email().click()

    def fill_input_email(self, value: str):
        field = self.get_input_email()
        field.click()
        #field.clear()
        field.send_keys(value)

    def get_element_email_type_spinner(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.ELEMENT_EMAIL_TYPE_SPINNER[self.platform]
            )
        )

    def click_element_email_type_spinner(self):
        self.get_element_email_type_spinner().click()

    def get_text_email_type_selected(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_EMAIL_TYPE_SELECTED[self.platform]
            )
        )

    # ── Mais campos ───────────────────────────────────────────────────────────

    def get_btn_more_fields(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_MORE_FIELDS[self.platform]
            )
        )

    def click_btn_more_fields(self):
        self.get_btn_more_fields().click()

    # ── Actions compostas ─────────────────────────────────────────────────────

    def fill_contact_form(self, first_name: str = "", last_name: str = "",
                          phone: str = "", email: str = ""):
        """Preenche o formulário completo de criação de contato."""
        if first_name:
            self.fill_input_first_name(first_name)
        if last_name:
            self.fill_input_last_name(last_name)
        if phone:
            self.fill_input_phone_number(phone)
        if email:
            self.driver.back()
            self.fill_input_email(email)

    def save_contact(self):
        """Salva o contato clicando no botão SALVAR."""
        self.click_btn_save()

    def cancel_contact_creation(self):
        """Cancela a criação do contato."""
        self.click_btn_cancel()

    def get_toolbar_title_text(self) -> str:
        """Retorna o texto do título da toolbar."""
        return self.get_text_toolbar_title().text

    def get_account_name_text(self) -> str:
        """Retorna o nome da conta de destino para salvar o contato."""
        return self.get_text_account_name().text

    def get_phone_type_text(self) -> str:
        """Retorna o tipo de telefone atualmente selecionado no spinner."""
        return self.get_text_phone_type_selected().text

    def get_email_type_text(self) -> str:
        """Retorna o tipo de e-mail atualmente selecionado no spinner."""
        return self.get_text_email_type_selected().text
    
    