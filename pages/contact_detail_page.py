from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.contact_detail_elements import ContactDetailElements


class ContactDetailPage:

    def __init__(self, driver, platform: str = "android", timeout: int = 10):
        self.driver = driver
        self.platform = platform.lower()
        self.wait = WebDriverWait(driver, timeout)
        self.elements = ContactDetailElements

    # ── Toolbar / Header ──────────────────────────────────────────────────────

    def get_icon_contact_photo(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.ICON_CONTACT_PHOTO[self.platform]
            )
        )

    def click_icon_contact_photo(self):
        self.get_icon_contact_photo().click()

    def get_text_contact_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_CONTACT_NAME[self.platform]
            )
        )

    def get_btn_add_to_favorites(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_ADD_TO_FAVORITES[self.platform]
            )
        )

    def click_btn_add_to_favorites(self):
        self.get_btn_add_to_favorites().click()

    def get_btn_edit(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_EDIT[self.platform]
            )
        )

    def click_btn_edit(self):
        self.get_btn_edit().click()

    def get_btn_more_options(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_MORE_OPTIONS[self.platform]
            )
        )

    def click_btn_more_options(self):
        self.get_btn_more_options().click()

    # ── Mais opções" ─────────────────────────────────────────

    # ---------------- VINCULAR ----------------

    def get_btn_vincular(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_VINCULAR[self.platform]
            )
        )

    def click_btn_vincular(self):
        self.get_btn_vincular().click()

    # ---------------- EXCLUIR ----------------

    def get_btn_excluir(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_EXCLUIR[self.platform]
            )
        )

    def click_btn_excluir(self):
        self.get_btn_excluir().click()

    # ---------------- COMPARTILHAR ----------------

    def get_btn_compartilhar(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_COMPARTILHAR[self.platform]
            )
        )

    def click_btn_compartilhar(self):
        self.get_btn_compartilhar().click()

    # ---------------- CRIAR ATALHO ----------------

    def get_btn_criar_atalho(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_CRIAR_ATALHO[self.platform]
            )
        )

    def click_btn_criar_atalho(self):
        self.get_btn_criar_atalho().click()

    # ---------------- DEFINIR TOQUE ----------------

    def get_btn_definir_toque(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_DEFINIR_TOQUE[self.platform]
            )
        )

    def click_btn_definir_toque(self):
        self.get_btn_definir_toque().click()

    # ── Cartão "sem dados de contato" ─────────────────────────────────────────

    def get_element_no_contact_data_card(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.ELEMENT_NO_CONTACT_DATA_CARD[self.platform]
            )
        )

    def get_text_add_phone_number(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_ADD_PHONE_NUMBER[self.platform]
            )
        )

    def click_text_add_phone_number(self):
        self.get_text_add_phone_number().click()

    def get_text_phone_number(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_PHONE_NUMBER[self.platform]
            )
        )

    def get_text_add_email(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_ADD_EMAIL[self.platform]
            )
        )

    def click_btn_add_email(self):
        self.get_text_add_email().click()

    def get_text_email(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_EMAIL[self.platform]
            )
        )
    
    def get_btn_send_msg(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_SEND_SMS[self.platform]
            )
        )
    
    def click_btn_send_msg(self):
        self.get_btn_send_msg().click()

    # ── Toast de confirmação ──────────────────────────────────────────────────

    def get_text_toast_contact_saved(self):
        return self.wait.until(
            EC.presence_of_element_located(
                self.elements.TEXT_TOAST_CONTACT_SAVED[self.platform]
            )
        )
    
    # ---------------- MENSAGEM DE CONFIRMAÇÃO ----------------

    def get_text_delete_contact_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.TEXT_TOAST_DELETE_CONTACT_MESSAGE[self.platform]
            )
        )

    # ---------------- BOTÃO CANCELAR ----------------

    def get_btn_cancelar_dialog(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_TOAST_CANCELAR[self.platform]
            )
        )

    def click_btn_cancelar_dialog(self):
        self.get_btn_cancelar_dialog().click()

    # ---------------- BOTÃO EXCLUIR ----------------

    def get_btn_excluir_dialog(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.elements.BTN_TOAST_EXCLUIR[self.platform]
            )
        )

    def click_btn_excluir_dialog(self):
        self.get_btn_excluir_dialog().click()

    OPTIONS_MAP = {
        "Vincular": "BTN_VINCULAR",
        "Excluir": "BTN_EXCLUIR",
        "Compartilhar": "BTN_COMPARTILHAR",
        "Criar atalho": "BTN_CRIAR_ATALHO",
        "Definir toque": "BTN_DEFINIR_TOQUE",
    }

    def is_option_visible(self, option: str, timeout: float = 5) -> bool:
        """
        Verifica se uma opção do menu 'Mais opções' está visível na tela.

        :param option: Texto da opção (ex: "Vincular", "Excluir", etc.)
        :param timeout: Tempo máximo (em segundos) de espera pela visibilidade do elemento.
        :return: True se a opção estiver visível, False caso contrário.
        """
        element_attr = self.OPTIONS_MAP.get(option)

        if element_attr is None:
            raise ValueError(f"Opção '{option}' não é reconhecida no OPTIONS_MAP")

        locator = getattr(ContactDetailElements, element_attr)[self.platform]

        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except TimeoutException:
            return False