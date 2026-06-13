from pages.create_contact_pages import CreateContactPage
from pages.contact_detail_page import ContactDetailPage
import re

class ValidationNewCrateContact:

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.new_contact_page = CreateContactPage(self.driver)
        self.contact_detail_page = ContactDetailPage(self.driver)

    def validate_create_new_contact(self, first_name: str = "", last_name: str = "", phone: str = "", email: str = ""):
       
        assert self.contact_detail_page.get_btn_add_to_favorites().is_enabled()
        assert self.contact_detail_page.get_btn_edit().is_enabled()
        assert self.contact_detail_page.get_btn_more_options().is_enabled()
        if phone == "":
            assert self.contact_detail_page.get_text_add_phone_number().text == "Adicionar número de telefone"
        else:
            phone_clean_from_screen = re.sub(r'\D', '', self.contact_detail_page.get_text_phone_number().text)
            assert phone_clean_from_screen == phone
            assert self.contact_detail_page.get_btn_send_msg().is_enabled()
        if email == "":
            assert self.contact_detail_page.get_text_add_email().text == "Adicionar e-mail"
        else:
            assert self.contact_detail_page.get_text_email().text == email
        if last_name == "":
            assert self.contact_detail_page.get_text_toast_contact_saved().text == f"Contato salvo: {first_name}"

        elif first_name != "" and last_name != "":
            assert self.contact_detail_page.get_text_toast_contact_saved().text == f"Contato salvo: {first_name} {last_name}"

        elif first_name == "" and last_name != "":
            assert self.contact_detail_page.get_text_toast_contact_saved().text == f"Contato salvo: {last_name}"