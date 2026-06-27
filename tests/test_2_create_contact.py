import pytest
import time
from pages.create_contact_pages import CreateContactPage
from pages.home_pages import ContactsPage
from utils.validations.validations_new_contact import ValidationNewCreateContact
from utils.validations.validations_home_not_contact import ValidationHomeNotContact


class TestCreateContact:

    def test_cancel_contact_creation_empty_form(self, create_new_contact: CreateContactPage, home_page: ContactsPage, validator_home_empty: ValidationHomeNotContact):
        """
        Testa o cancelamento da criação de contato com formulário vazio.

        Cenário: Usuário clica no botão de criar contato e depois cancela sem preencher nenhum campo.
        Resultado esperado: Retorna à tela inicial e nenhum contato é criado.
        """

        home_page.click_btn_create_new_contact()

        create_new_contact.click_btn_cancel()

        validator_home_empty.validate_home_not_contact()

    def test_cancel_contact_creation_with_filled_fields(self, create_new_contact: CreateContactPage, home_page: ContactsPage, validator_home_empty: ValidationHomeNotContact):
        """
        Testa o cancelamento da criação com diálogo de confirmação ao ter campos preenchidos.

        Cenário: Usuário preenche o primeiro nome e tenta cancelar, acionando diálogo de confirmação.
        Resultado esperado: Usuário pode confirmar o cancelamento e nenhum contato é criado.
        """

        home_page.click_btn_create_new_contact()

        create_new_contact.fill_input_first_name("Maria")
        create_new_contact.click_btn_cancel()

        create_new_contact.click_btn_cancel_dialog()
        create_new_contact.click_btn_cancel()
        create_new_contact.click_btn_discard_dialog()

        validator_home_empty.validate_home_not_contact()

    def test_create_contact_with_empty_form_fails(self, create_new_contact: CreateContactPage,  home_page: ContactsPage, validator_home_empty: ValidationHomeNotContact):
        """
        Testa que a criação falha com formulário vazio.

        Cenário: Usuário tenta criar contato sem preencher nenhum campo.
        Resultado esperado: Falha na validação e nenhum contato é criado.
        """

        home_page.click_btn_create_new_contact()

        create_new_contact.click_btn_save()

        validator_home_empty.validate_home_not_contact()

    def test_validate_create_contact_screen_placeholders(self, home_page: ContactsPage, validator_new_contact: ValidationNewCreateContact, create_new_contact: CreateContactPage):
        """
        Valida os placeholders da tela de criação de contato.

        Cenário: Usuário acessa a tela de criação de contato.
        Resultado esperado: Todos os placeholders são exibidos corretamente.
        """

        home_page.click_btn_create_new_contact()

        validator_new_contact.validate_placeholder_screen_create_new_contact()

        create_new_contact.click_btn_cancel()
        
    @pytest.mark.parametrize("phone_type_option, expected_text", [
        ("mobile", "Celular"),
        ("work", "Comercial"),
        ("home", "Casa")
    ], ids=["type_work", "type_mobile", "type_home"])
    def test_change_phone_type_shows_correct_label(self, home_page: ContactsPage, create_new_contact: CreateContactPage, phone_type_option, expected_text):
        """
        Valida que a seleção dos tipos de telefone mostra o texto correto na tela,
        utilizando desvios condicionais para cada tipo.
        """

        home_page.click_btn_create_new_contact()

        create_new_contact.click_phone_type_selected()
        
        if phone_type_option == "work":
            create_new_contact.click_opt_work()
            
        elif phone_type_option == "mobile":
            create_new_contact.click_opt_mobile()
            
        elif phone_type_option == "home":
            create_new_contact.click_opt_home()

        phone_type_text = create_new_contact.get_text_phone_type_selected().text
        
        assert phone_type_text == expected_text, f"Esperado '{expected_text}' mas obteve '{phone_type_text}'"

        create_new_contact.click_btn_cancel()

    @pytest.mark.parametrize("email_type_option, expected_text", [
        ("mobile", "Celular"),
        ("work", "Comercial"),
        ("home", "Casa")
    ], ids=["type_work", "type_mobile", "type_home"])
    def test_change_email_type_shows_correct_label(self, driver, home_page: ContactsPage, create_new_contact: CreateContactPage, email_type_option, expected_text):
        """
        Valida que a seleção dos tipos de e-mail mostra o texto correto na tela,
        utilizando desvios condicionais para cada tipo.
        """

        home_page.click_btn_create_new_contact()
        time.sleep(1)  # Pequena pausa para garantir que a tela de criação de contato esteja totalmente carregada
        driver.hide_keyboard()
        create_new_contact.click_element_email_type_spinner()
        
        if email_type_option == "work":
            create_new_contact.click_opt_work()
            
        elif email_type_option == "mobile":
            create_new_contact.click_opt_mobile()
            
        elif email_type_option == "home":
            create_new_contact.click_opt_home()

        email_type_text = create_new_contact.get_text_email_type_selected().text
        
        assert email_type_text == expected_text, f"Esperado '{expected_text}' mas obteve '{email_type_text}'"

        create_new_contact.click_btn_cancel()

    def test_(self, driver, home_page: ContactsPage, create_new_contact: CreateContactPage):
        """
        Valida que a seleção dos tipos de e-mail mostra o texto correto na tela,
        utilizando desvios condicionais para cada tipo.
        """

        home_page.click_btn_create_new_contact()
        is_focused = create_new_contact.get_input_first_name().get_attribute("focused")
        assert is_focused, f"O campo nome não veio em foco '{is_focused}'"
        print(f"Focused: {is_focused}")

        create_new_contact.click_btn_cancel()

    @pytest.mark.parametrize("first_name,last_name,phone,email", [
        ("Maria", "", "", ""),
        ("", "", "8974515216", ""),
        ("", "", "", "maria@gmail.com"),
    ], ids=["first_name_only", "phone_only", "email_only"])
    def test_create_contact_with_partial_data(self, home_page: ContactsPage, create_new_contact: CreateContactPage, validator_new_contact: ValidationNewCreateContact, first_name, last_name, phone, email, cleanup_contact):
        """
        Testa a criação de contato com dados parciais.

        Cenários parametrizados:
        - Apenas primeiro nome preenchido
        - Apenas telefone preenchido
        - Apenas email preenchido

        Resultado esperado: Contato é criado com os dados fornecidos.
        """

        home_page.click_btn_create_new_contact()

        if first_name:
            create_new_contact.fill_input_first_name(first_name)

        if phone:
            create_new_contact.fill_input_phone_number(phone)

        if email:
            create_new_contact.fill_input_email(email)

        create_new_contact.click_btn_save()

        validator_new_contact.validate_create_new_contact(
            first_name,
            last_name,
            phone,
            email
        )

    def test_create_contact_with_all_fields_filled(self, home_page: ContactsPage, create_new_contact: CreateContactPage, validator_new_contact: ValidationNewCreateContact, cleanup_contact):
        """
        Testa a criação completa de contato com todos os campos preenchidos.

        Cenário: Usuário preenche todos os campos (primeiro nome, sobrenome, telefone e email).
        Resultado esperado: Contato é criado e validado com sucesso.
        """

        home_page.click_btn_create_new_contact()

        create_new_contact.fill_contact_form(
            "Maria", "Silva", "8974515216", "maria@gmail.com")
        create_new_contact.click_btn_save()

        validator_new_contact.validate_create_new_contact(
            "Maria", "Silva", "8974515216", "maria@gmail.com")
