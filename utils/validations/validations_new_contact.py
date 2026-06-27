from pages.create_contact_pages import CreateContactPage
from pages.contact_detail_page import ContactDetailPage
import re


class ValidationNewCreateContact:

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.new_contact_page = CreateContactPage(self.driver)
        self.contact_detail_page = ContactDetailPage(self.driver)

    def validate_create_new_contact(self, first_name: str = "", last_name: str = "", phone: str = "", email: str = ""):

        # --- 1. VALIDAÇÃO DO TOAST (Sempre a primeira linha, pois some rápido!) ---
        full_name = f"{first_name} {last_name}".strip()
        toast_text = self.contact_detail_page.get_text_toast_contact_saved().text

        if full_name == "" and phone != "":
            # Se salvou sem nome o Android usa o telefone formatado como título
            screen_phone = self.contact_detail_page.get_text_phone_number().text
            expected_toast = f"Contato salvo: {screen_phone}"
        elif full_name == "" and email != "" and phone == "":
            # Se salvou apenas com o email o Android usa o email como título
            screen_email = self.contact_detail_page.get_text_email().text
            expected_toast = f"Contato salvo: {screen_email}"
        else:
            expected_toast = f"Contato salvo: {full_name}"

        assert toast_text == expected_toast, f"Erro no Toast: Esperava '{expected_toast}', mas leu '{toast_text}'"

        # --- 2. VALIDAÇÃO DOS BOTÕES FIXOS DO TOPO ---
        assert self.contact_detail_page.get_btn_add_to_favorites(
        ).is_enabled(), "O botão de Favoritos não está habilitado"
        assert self.contact_detail_page.get_btn_edit(
        ).is_enabled(), "O botão de Editar não está habilitado"
        assert self.contact_detail_page.get_btn_more_options(
        ).is_enabled(), "O botão de Mais Opções não está habilitado"

        # --- 3. VALIDAÇÃO DO CAMPO DE TELEFONE ---
        if phone != "":
            phone_from_screen = self.contact_detail_page.get_text_phone_number().text
            # Remove parênteses e traços
            phone_clean = re.sub(r'\D', '', phone_from_screen)

            assert phone_clean == phone, f"Telefone incorreto: Esperava '{phone}', mas leu '{phone_clean}'"
            assert self.contact_detail_page.get_btn_send_msg(
            ).is_enabled(), "Botão de enviar SMS não está habilitado"

        # --- 4. VALIDAÇÃO DO CAMPO DE E-MAIL ---

        if email != "":
            email_from_screen = self.contact_detail_page.get_text_email().text
            assert email_from_screen == email, f"E-mail incorreto: Esperava '{email}', mas leu '{email_from_screen}'"

        # --- 5. VALIDAÇÃO EMAIL E FONE VAZIO ---

        if email == "" and phone == "":
            phone_placeholder = self.contact_detail_page.get_text_add_phone_number().text
            email_placeholder = self.contact_detail_page.get_text_add_email().text
            assert phone_placeholder == "Adicionar número de telefone", f"Texto do telefone incorreto: '{phone_placeholder}'"
            assert email_placeholder == "Adicionar e-mail", f"Texto de e-mail incorreto: '{email_placeholder}'"

    def validate_placeholder_screen_create_new_contact(self):
        assert self.new_contact_page.get_input_first_name().text == "Nome"
        assert self.new_contact_page.get_input_last_name().text == "Sobrenome"
        assert self.new_contact_page.get_input_phone_number().text == "Telefone"
