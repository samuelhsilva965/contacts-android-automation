import allure
from selenium.common.exceptions import TimeoutException
import pytest
import time
from pages.create_contact_pages import CreateContactPage
from pages.home_pages import ContactsPage
from utils.validations.validations_new_contact import ValidationNewCreateContact
from utils.validations.validations_home_not_contact import ValidationHomeNotContact
from utils.functions.close_dialog_add_account import click_btn_cancel_dialog_adicionar_conta_if_present


class TestCreateContact:

    @allure.feature("Criação de Contato")
    @allure.story("Cancelar criação com formulário vazio")
    @allure.title("Cancelar criação de contato com formulário vazio retorna à tela inicial")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cancel_contact_creation_empty_form(self, driver, create_new_contact: CreateContactPage, home_page: ContactsPage, validator_home_empty: ValidationHomeNotContact):
        """
        Testa o cancelamento da criação de contato com formulário vazio.

        Cenário: Usuário clica no botão de criar contato e depois cancela sem preencher nenhum campo.
        Resultado esperado: Retorna à tela inicial e nenhum contato é criado.
        """

        with allure.step("Clicar em criar novo contato"):
            home_page.click_btn_create_new_contact()

        with allure.step("Fechar modal de adicionar conta, se estiver visível"):
            click_btn_cancel_dialog_adicionar_conta_if_present(driver)
            
        with allure.step("Clicar em cancelar"):
            create_new_contact.click_btn_cancel()

        with allure.step("Validar que não há contato na tela inicial"):
            validator_home_empty.validate_home_not_contact()

    @allure.feature("Criação de Contato")
    @allure.story("Cancelar criação com campos preenchidos")
    @allure.title("Cancelar criação com diálogo de confirmação após preencher campo")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cancel_contact_creation_with_filled_fields(self, driver, create_new_contact: CreateContactPage, home_page: ContactsPage, validator_home_empty: ValidationHomeNotContact):
        """
        Testa o cancelamento da criação com diálogo de confirmação ao ter campos preenchidos.

        Cenário: Usuário preenche o primeiro nome e tenta cancelar, acionando diálogo de confirmação.
        Resultado esperado: Usuário pode confirmar o cancelamento e nenhum contato é criado.
        """

        with allure.step("Clicar em criar novo contato"):
            home_page.click_btn_create_new_contact()

        with allure.step("Preencher primeiro nome e cancelar"):
            create_new_contact.fill_input_first_name("Maria")
            create_new_contact.click_btn_cancel()

        with allure.step("Navegar pelo diálogo de confirmação"):
            create_new_contact.click_btn_cancel_dialog()
            create_new_contact.click_btn_cancel()
            create_new_contact.click_btn_discard_dialog()

        with allure.step("Validar que não há contato na tela inicial"):
            validator_home_empty.validate_home_not_contact()

    @allure.feature("Criação de Contato")
    @allure.story("Criar contato com formulário vazio falha")
    @allure.title("Tentar criar contato com formulário vazio resulta em falha")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_contact_with_empty_form_fails(self, driver, create_new_contact: CreateContactPage,  home_page: ContactsPage, validator_home_empty: ValidationHomeNotContact):
        """
        Testa que a criação falha com formulário vazio.

        Cenário: Usuário tenta criar contato sem preencher nenhum campo.
        Resultado esperado: Falha na validação e nenhum contato é criado.
        """

        with allure.step("Clicar em criar novo contato"):
            home_page.click_btn_create_new_contact()

        with allure.step("Clicar em salvar sem preencher campos"):
            create_new_contact.click_btn_save()

        with allure.step("Validar que não há contato na tela inicial"):
            validator_home_empty.validate_home_not_contact()

    @allure.feature("Criação de Contato")
    @allure.story("Validar placeholders da tela de criação")
    @allure.title("Validar placeholders da tela de criação de contato")
    @allure.severity(allure.severity_level.NORMAL)
    def test_validate_create_contact_screen_placeholders(self, driver, home_page: ContactsPage, validator_new_contact: ValidationNewCreateContact, create_new_contact: CreateContactPage):
        """
        Valida os placeholders da tela de criação de contato.

        Cenário: Usuário acessa a tela de criação de contato.
        Resultado esperado: Todos os placeholders são exibidos corretamente.
        """

        with allure.step("Acessar a tela de criação de contato"):
            home_page.click_btn_create_new_contact()

        with allure.step("Validar placeholders"):
            validator_new_contact.validate_placeholder_screen_create_new_contact()

        with allure.step("Cancelar e retornar"):
            create_new_contact.click_btn_cancel()
        
    @allure.feature("Criação de Contato")
    @allure.story("Alterar tipo de telefone e verificar label")
    @allure.title("Selecionar tipo de telefone exibe o texto correto")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("phone_type_option, expected_text", [
        ("mobile", "Celular"),
        ("work", "Comercial"),
        ("home", "Casa")
    ], ids=["type_work", "type_mobile", "type_home"])
    def test_change_phone_type_shows_correct_label(self, driver, home_page: ContactsPage, create_new_contact: CreateContactPage, phone_type_option, expected_text):
        """
        Valida que a seleção dos tipos de telefone mostra o texto correto na tela,
        utilizando desvios condicionais para cada tipo.
        """

        with allure.step("Acessar tela de criação de contato"):
            home_page.click_btn_create_new_contact()

        with allure.step("Selecionar tipo de telefone"):
            create_new_contact.click_phone_type_selected()
        
        if phone_type_option == "work":
            create_new_contact.click_opt_work()
            
        elif phone_type_option == "mobile":
            create_new_contact.click_opt_mobile()
            
        elif phone_type_option == "home":
            create_new_contact.click_opt_home()

        with allure.step("Verificar label do tipo de telefone selecionado"):
            phone_type_text = create_new_contact.get_text_phone_type_selected().text
        
        assert phone_type_text == expected_text, f"Esperado '{expected_text}' mas obteve '{phone_type_text}'"

        with allure.step("Cancelar e retornar"):
            create_new_contact.click_btn_cancel()

    @allure.feature("Criação de Contato")
    @allure.story("Alterar tipo de e-mail e verificar label")
    @allure.title("Selecionar tipo de e-mail exibe o texto correto")
    @allure.severity(allure.severity_level.NORMAL)
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

        with allure.step("Acessar tela de criação de contato"):
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

        with allure.step("Verificar label do tipo de e-mail selecionado"):
            email_type_text = create_new_contact.get_text_email_type_selected().text
        
        assert email_type_text == expected_text, f"Esperado '{expected_text}' mas obteve '{email_type_text}'"

        with allure.step("Cancelar e retornar"):
            create_new_contact.click_btn_cancel()

    @allure.feature("Criação de Contato")
    @allure.story("Verificar foco no campo nome")
    @allure.title("Campo nome recebe foco automaticamente ao abrir tela de criação")
    @allure.severity(allure.severity_level.NORMAL)
    def test_new_contact_first_name_autofocus(self, driver, home_page: ContactsPage, create_new_contact: CreateContactPage):
        """
        Valida que a seleção dos tipos de e-mail mostra o texto correto na tela,
        utilizando desvios condicionais para cada tipo.
        """

        with allure.step("Acessar tela de criação de contato"):
            home_page.click_btn_create_new_contact()
            is_focused = create_new_contact.get_input_first_name().get_attribute("focused")
            assert is_focused, f"O campo nome não veio em foco '{is_focused}'"
            print(f"Focused: {is_focused}")

        with allure.step("Cancelar e retornar"):
            create_new_contact.click_btn_cancel()

    @allure.feature("Criação de Contato")
    @allure.story("Criar contato com dados parciais")
    @allure.title("Criar contato com dados parciais (parametrizado)")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("first_name,last_name,phone,email", [
        ("Maria", "", "", ""),
        ("", "", "8974515216", ""),
        ("", "", "", "maria@gmail.com"),
    ], ids=["first_name_only", "phone_only", "email_only"])
    def test_create_contact_with_partial_data(self, driver, home_page: ContactsPage, create_new_contact: CreateContactPage, validator_new_contact: ValidationNewCreateContact, first_name, last_name, phone, email, cleanup_contact):
        """
        Testa a criação de contato com dados parciais.

        Cenários parametrizados:
        - Apenas primeiro nome preenchido
        - Apenas telefone preenchido
        - Apenas email preenchido

        Resultado esperado: Contato é criado com os dados fornecidos.
        """

        with allure.step("Acessar tela de criação de contato"):
            home_page.click_btn_create_new_contact()

        with allure.step("Preencher campos fornecidos"):
            if first_name:
                create_new_contact.fill_input_first_name(first_name)

            if phone:
                create_new_contact.fill_input_phone_number(phone)

            if email:
                create_new_contact.fill_input_email(email)

        with allure.step("Salvar contato"):
            create_new_contact.click_btn_save()

        with allure.step("Validar criação do contato"):
            validator_new_contact.validate_create_new_contact(
                first_name,
                last_name,
                phone,
                email
            )

    @allure.feature("Criação de Contato")
    @allure.story("Criar contato com todos os campos preenchidos")
    @allure.title("Criar contato completo com todos os dados")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_contact_with_all_fields_filled(self, driver, home_page: ContactsPage, create_new_contact: CreateContactPage, validator_new_contact: ValidationNewCreateContact, cleanup_contact):
        """
        Testa a criação completa de contato com todos os campos preenchidos.

        Cenário: Usuário preenche todos os campos (primeiro nome, sobrenome, telefone e email).
        Resultado esperado: Contato é criado e validado com sucesso.
        """

        with allure.step("Acessar tela de criação de contato"):
            home_page.click_btn_create_new_contact()

        with allure.step("Preencher formulário com todos os dados"):
            create_new_contact.fill_contact_form(
                "Maria", "Silva", "8974515216", "maria@gmail.com")
            create_new_contact.click_btn_save()

        with allure.step("Validar criação do contato"):
            validator_new_contact.validate_create_new_contact(
                "Maria", "Silva", "8974515216", "maria@gmail.com")
