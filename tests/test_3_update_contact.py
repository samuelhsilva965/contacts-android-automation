import allure
import pytest
import time
from pages.create_contact_pages import CreateContactPage
from pages.home_with_contact_page import HomeWithContactPage
from pages.contact_detail_page import ContactDetailPage


class TestUpdateContact:

    @allure.feature("Atualizar Contato")
    @allure.story("Adicionar sobrenome a contato existente")
    @allure.title("Adicionar sobrenome a contato que possui apenas nome")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_surname_to_existing_contact(self, driver, home_with_contact: HomeWithContactPage,
                                             create_new_contact: CreateContactPage,
                                             new_contact_detail: ContactDetailPage):
        """
        Adicionar sobrenome a um contato que possui apenas nome.

        Cenário: Usuário edita o contato "Maria" e adiciona o sobrenome "Silva".
        Resultado esperado: O contato é exibido como "Maria Silva" na lista de contatos.
        """

        with allure.step("Abrir o contato 'Maria' e tocar no ícone de editar"):
            home_with_contact.click_contact_row_by_name("Maria")
            new_contact_detail.click_btn_edit()

        with allure.step("Preencher sobrenome e salvar"):
            create_new_contact.fill_input_last_name("Oliveira")
            create_new_contact.click_btn_save()
            time.sleep(1)

        with allure.step("Voltar para a lista de contatos e verificar o resultado"):
            driver.back()
            remaining_contacts = home_with_contact.get_all_contact_names()
            assert "Maria" not in remaining_contacts, (
                f"O contato 'Maria' ainda aparece na lista sem sobrenome: {remaining_contacts}"
            )

            assert "Maria Silva" in remaining_contacts, (
                f"O contato 'Maria Silva' não foi encontrado na lista: {remaining_contacts}"
            )

    @allure.feature("Atualizar Contato")
    @allure.story("Adicionar telefone a contato com apenas nome")
    @allure.title("Adicionar número de telefone a contato que possui apenas nome")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_phone_to_contact_with_only_name(self, driver, home_with_contact: HomeWithContactPage, new_contact_detail: ContactDetailPage, create_new_contact: CreateContactPage):
        """
        Adicionar número de telefone a um contato que possui apenas nome.

        Cenário: Usuário abre o contato "Maria", adiciona um telefone e salva.
        Resultado esperado: O telefone informado é exibido na tela de detalhes.
        """

        with allure.step("Abrir o contato 'Maria Oliveira' e tocar em 'Adicionar número de telefone'"):
            home_with_contact.get_contact_row_by_name("Maria Oliveira").click()
            new_contact_detail.click_text_add_phone_number()

        with allure.step("Informar telefone e salvar"):
            phone_number = "(11) 99999-0000"
            create_new_contact.fill_input_phone_number(phone_number)
            create_new_contact.click_btn_save()

        with allure.step("Aguardar e verificar se o telefone é exibido nos detalhes"):
            time.sleep(1)
            phone_displayed = new_contact_detail.get_text_phone_number()
            assert phone_displayed.is_displayed(), "O campo de telefone não está visível na tela de detalhes"
            assert phone_number in phone_displayed.text, f"Esperado '{phone_number}' no telefone, mas obteve '{phone_displayed.text}'"

    @allure.feature("Atualizar Contato")
    @allure.story("Adicionar e-mail a contato com apenas nome")
    @allure.title("Adicionar e-mail a contato que possui apenas nome")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_email_to_contact_with_only_name(self, driver,
                                                 home_with_contact: HomeWithContactPage,
                                                 new_contact_detail: ContactDetailPage,
                                                 create_new_contact: CreateContactPage):
        """
        Adicionar e-mail a um contato que possui apenas nome.

        Cenário:
          Dado que o usuário está no contato "Maria"
          Quando tocar em "Editar"
          E informar um e-mail válido
          E tocar no botão "SALVAR"
          Então o e-mail informado deverá ser exibido na tela de detalhes do contato
        """

        with allure.step("Verificar que está na tela de detalhes do contato 'Maria Oliveira'"):
            assert new_contact_detail.get_text_contact_name().text == "Maria Oliveira", \
                "A tela de detalhes do contato 'Maria Oliveira' não está sendo exibida"

        with allure.step("Editar, preencher e-mail e salvar"):
            new_contact_detail.click_btn_edit()
            email_valido = "maria.teste@exemplo.com"
            create_new_contact.fill_input_email(email_valido)
            create_new_contact.click_btn_save()

        with allure.step("Aguardar e verificar se o e-mail é exibido nos detalhes"):
            time.sleep(2)
            email_exibido = new_contact_detail.get_text_email().text
            assert email_exibido == email_valido, \
                f"E-mail exibido ('{email_exibido}') é diferente do esperado ('{email_valido}')"
            
            driver.back()

    @allure.feature("Atualizar Contato")
    @allure.story("Adicionar nome a contato com apenas e-mail")
    @allure.title("Adicionar nome a contato que possui apenas e-mail")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_name_to_contact_with_email(self, driver, home_with_contact: HomeWithContactPage, new_contact_detail: ContactDetailPage):
        """
        Adicionar nome a um contato que possui apenas e-mail.

        Cenário: Usuário abre o contato "maria@gmail.com" na lista, toca em editar,
                 preenche o campo "Nome" com um valor válido e salva.
        Resultado esperado: O contato passa a ser exibido pelo nome informado na lista de contatos.
        """

        with allure.step("Abrir contato 'maria@gmail.com' e verificar o nome"):
            home_with_contact.click_contact_row_by_name("maria@gmail.com")
            assert new_contact_detail.get_text_contact_name().text == "maria@gmail.com", "O nome do contato não é 'maria@gmail.com'"

        with allure.step("Editar, preencher nome e salvar"):
            new_contact_detail.click_btn_edit()
            create_contact_page = CreateContactPage(driver)
            nome_informado = "Maria Editada"
            create_contact_page.fill_input_first_name(nome_informado)
            create_contact_page.click_btn_save()

        with allure.step("Aguardar, voltar para lista e verificar o nome"):
            time.sleep(2)
            driver.back()
            remaining_contacts = home_with_contact.get_all_contact_names()
            assert nome_informado in remaining_contacts, f"Contato '{nome_informado}' não encontrado na lista: {remaining_contacts}"

    @allure.feature("Atualizar Contato")
    @allure.story("Adicionar nome a contato com apenas telefone")
    @allure.title("Adicionar nome a contato que possui apenas telefone")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_name_to_phone_only_contact(self, driver, home_with_contact: HomeWithContactPage,
                                            new_contact_detail: ContactDetailPage,
                                            create_new_contact: CreateContactPage):
        """
        Adicionar nome a um contato que possui apenas telefone.

        Cenário: Usuário abre o contato '(897) 451-5216', edita, preenche o nome e salva.
        Resultado esperado: O contato passa a ser exibido pelo nome informado na lista.
        """

        with allure.step("Abrir contato '(897) 451-5216' e verificar o nome"):
            home_with_contact.click_contact_row_by_name("(897) 451-5216")
            assert new_contact_detail.get_text_contact_name().text == "(897) 451-5216", \
                "O contato aberto não é o esperado"

        with allure.step("Editar, preencher nome e salvar"):
            new_contact_detail.click_btn_edit()
            create_new_contact.fill_input_first_name("Samuel Teste")
            create_new_contact.click_btn_save()
            time.sleep(1)

        with allure.step("Voltar para lista e verificar o nome"):
            driver.back()
            remaining_contacts = home_with_contact.get_all_contact_names()
            assert "Samuel Teste" in remaining_contacts, \
                f"O nome 'Samuel Teste' não foi encontrado na lista de contatos: {remaining_contacts}"

    @allure.feature("Atualizar Contato")
    @allure.story("Editar nome de contato completo")
    @allure.title("Alterar o nome de um contato completo")
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_contact_name(self, driver, home_with_contact: HomeWithContactPage,
                               new_contact_detail: ContactDetailPage,
                               create_new_contact: CreateContactPage):
        """
        Alterar o nome de um contato completo.

        Cenário:
          Dado que o usuário abre o contato "Maria Silva"
          Quando tocar no ícone de editar
          E alterar o campo "Nome" para um novo valor válido
          E tocar no botão "SALVAR"
          Então o contato deverá ser exibido com o novo nome na lista de contatos
        """

        with allure.step("Abrir contato 'Maria Silva' e verificar detalhes"):
            home_with_contact.click_contact_row_by_name("Maria Silva")
            assert new_contact_detail.get_text_contact_name().text == "Maria Silva", \
                "Não está na tela de detalhes do contato 'Maria Silva'"

        with allure.step("Editar, alterar nome para 'Ana' e salvar"):
            new_contact_detail.click_btn_edit()
            create_new_contact.fill_input_first_name("Ana")
            create_new_contact.click_btn_save()
            time.sleep(1)

        with allure.step("Voltar para lista e verificar se 'Ana Silva' está presente"):
            driver.back()
            remaining_contacts = home_with_contact.get_all_contact_names()
            assert "Ana Silva" in remaining_contacts, \
                f"O contato 'Ana Silva' não foi encontrado na lista. Contatos atuais: {remaining_contacts}"

    @allure.feature("Atualizar Contato")
    @allure.story("Editar sobrenome de contato completo")
    @allure.title("Alterar o sobrenome de um contato completo")
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_contact_last_name(self, driver, home_with_contact: HomeWithContactPage,
                                    new_contact_detail: ContactDetailPage,
                                    create_new_contact: CreateContactPage):
        """
        Alterar o sobrenome de um contato completo.

        Cenário: Usuário altera o sobrenome do contato "Ana Silva" para "Villalobos".
        Resultado esperado: O contato é exibido com o novo sobrenome na lista de contatos.
        """

        with allure.step("Abrir contato 'Ana Silva'"):
            home_with_contact.click_contact_row_by_name("Ana Silva")

        with allure.step("Editar, alterar sobrenome para 'Villalobos' e salvar"):
            new_contact_detail.click_btn_edit()
            create_new_contact.fill_input_last_name("Villalobos")
            create_new_contact.click_btn_save()
            time.sleep(1)

        with allure.step("Voltar para lista e verificar se 'Ana Villalobos' está presente"):
            driver.back()
            remaining_contacts = home_with_contact.get_all_contact_names()
            assert "Ana Villalobos" in remaining_contacts, f"Contato 'Ana Villalobos' não encontrado na lista: {remaining_contacts}"

    @allure.feature("Atualizar Contato")
    @allure.story("Editar telefone de contato completo")
    @allure.title("Alterar o telefone de um contato completo")
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_contact_phone(self, driver, home_with_contact: HomeWithContactPage, new_contact_detail: ContactDetailPage, create_new_contact: CreateContactPage):
        """
        Alterar o telefone de um contato completo.

        Cenário: Usuário altera o telefone do contato "Ana Villalobos".
        Resultado esperado: Novo telefone é exibido na tela de detalhes.
        """

        with allure.step("Abrir contato 'Ana Villalobos' e verificar detalhes"):
            home_with_contact.click_contact_row_by_name("Ana Villalobos")
            assert new_contact_detail.get_text_contact_name().text == "Ana Villalobos", "O nome do contato não corresponde"

        with allure.step("Editar, alterar telefone e salvar"):
            new_contact_detail.click_btn_edit()
            novo_telefone = "+5511987654321"
            create_new_contact.fill_input_phone_number(novo_telefone)
            create_new_contact.click_btn_save()
            time.sleep(1)

        with allure.step("Verificar novo telefone na tela de detalhes e voltar"):
            assert new_contact_detail.get_text_contact_name().text == "Ana Villalobos", "Não retornou à tela de detalhes"
            telefone_exibido = new_contact_detail.get_text_phone_number().text
            assert "+55 11 98765-4321" in telefone_exibido, f"Telefone esperado '{novo_telefone}' não encontrado em '{telefone_exibido}'"

            driver.back()
