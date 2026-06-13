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
        self.get_txt_add_phone_number().click()

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
        self.get_btn_add_email().click()

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