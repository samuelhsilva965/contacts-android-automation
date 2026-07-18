import pytest
import time
import allure
from pages.contact_detail_page import ContactDetailPage
from pages.home_pages import ContactsPage
from pages.home_with_contact_page import HomeWithContactPage
from utils.functions.click_and_holder import click_and_hold
from utils.validations.validations_home_not_contact import ValidationHomeNotContact


class TestDeleteContact:

    @allure.feature("Delete Contact")
    @allure.story("Ícone de lixeira não visível sem seleção")
    @allure.title("Verificar que o ícone de lixeira não está visível sem seleção")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_icon_not_visible_without_selection(self, driver, home_with_contact: HomeWithContactPage):
        """
        Verifica que o ícone de lixeira não está visível na barra de ação sem nenhum contato selecionado.

        Cenário: Usuário está na tela de lista de contatos sem nenhum contato selecionado.
        Resultado esperado: O ícone de lixeira não deve estar visível na barra de ação.
        """
        with allure.step("Verificar que o ícone de lixeira não está visível sem nenhum contato selecionado"):
            assert not home_with_contact.is_btn_delete_visible(), "O botão de exclusão está visível sem nenhum contato selecionado"

    @allure.feature("Delete Contact")
    @allure.story("Desmarcar seleção e cancelar modo de seleção múltipla")
    @allure.title("Desmarcar seleção e cancelar modo de seleção múltipla")
    @allure.severity(allure.severity_level.NORMAL)
    def test_unselect_and_cancel_selection(self, driver, home_with_contact: HomeWithContactPage, home_page: ContactsPage):
        """
        Desmarcar seleção e cancelar modo de seleção múltipla.

        Cenário: Usuário selecionou o contato "Maria Editada" na lista.
        Resultado esperado: Contato é desmarcado e modo de seleção múltipla é encerrado.
        """
        with allure.step("Selecionar contato 'Maria Editada' e verificar seleção"):
            element = home_with_contact.get_contact_row_by_name("Maria Editada")
            click_and_hold(driver, element, duration=2000)
            assert home_with_contact.is_checkbox_selected_by_name("Maria Editada"), "O checkbox do contato 'Maria Editada' não está selecionado"

        with allure.step("Verificar contador de seleção exibe 1"):
            selection_count = home_with_contact.get_selection_count_value()
            assert selection_count == "1", f"Esperado '1' mas obteve '{selection_count}'"

        with allure.step("Fechar modo de seleção"):
            home_with_contact.click_btn_close_selection()

        with allure.step("Verificar que a barra de ação padrão foi restaurada"):
            assert not home_with_contact.is_btn_delete_visible(), "O botão de exclusão ainda está visível"
            assert home_page.get_text_toolbar_title().text == "Contatos", "O título da barra de ferramentas não está correto"

    @allure.feature("Delete Contact")
    @allure.story("Atualizar contador de seleção")
    @allure.title("Verificar atualização do contador ao selecionar e desselecionar contatos")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_selection_count(self, driver, home_with_contact: HomeWithContactPage):
        """
        Verificar atualização do contador ao selecionar e desselecionar contatos.

        Cenário: Usuário está no modo de seleção múltipla.
        Resultado esperado: Contador exibe a quantidade correta de contatos selecionados.
        """
        with allure.step("Selecionar contato 'Maria Oliveira' e verificar contador"):
            element = home_with_contact.get_contact_row_by_name("Maria Oliveira")
            click_and_hold(driver, element, duration=2000)
            selection_count = home_with_contact.get_selection_count_value()
            assert selection_count == "1", f"Esperado '1' mas obteve '{selection_count}'"

        with allure.step("Selecionar também o contato 'Samuel Teste' e verificar contador"):
            home_with_contact.select_contacts(["Samuel Teste"])
            selection_count = home_with_contact.get_selection_count_value()
            assert selection_count == "2", f"Esperado '2' mas obteve '{selection_count}'"

        with allure.step("Desmarcar contato 'Maria Oliveira' e verificar contador"):
            home_with_contact.click_checkbox_by_name("Maria Oliveira")
            selection_count = home_with_contact.get_selection_count_value()
            assert selection_count == "1", f"Esperado '1' mas obteve '{selection_count}'"
            home_with_contact.click_btn_close_selection()

    @allure.feature("Delete Contact")
    @allure.story("Cancelar exclusão de contato")
    @allure.title("Cancelar exclusão de contato e verificar que não foi removido")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cancel_delete_contact(self, driver, home_with_contact: HomeWithContactPage):
       
        with allure.step("Selecionar contato 'Maria Editada'"):
            element = home_with_contact.get_contact_row_by_name("Maria Editada")
            click_and_hold(driver, element, duration=2000)

        with allure.step("Clicar no ícone de lixeira"):
            home_with_contact.get_btn_delete().click()

        with allure.step("Cancelar a confirmação de exclusão"):
            home_with_contact.click_btn_cancel_delete_dialog()

        with allure.step("Verificar que o contato não foi removido e a seleção foi mantida"):
            assert home_with_contact.get_contact_row_by_name("Maria Editada").is_displayed(), "O contato 'Maria Editada' foi removido"
            assert home_with_contact.is_checkbox_selected_by_name("Maria Editada"), "O checkbox do contato 'Maria Editada' não está selecionado"
            assert home_with_contact.get_selection_count_value() == "1", "A seleção não foi mantida"
            home_with_contact.click_btn_close_selection()

    @allure.feature("Delete Contact")
    @allure.story("Confirmar exclusão de contato")
    @allure.title("Confirmar exclusão de contato e verificar remoção")
    @allure.severity(allure.severity_level.NORMAL)
    def test_confirm_delete_contact(self, driver, home_page: ContactsPage, home_with_contact: HomeWithContactPage):
        """
        Testa a confirmação da exclusão de contato.

        Cenário: Usuário clica no botão de criar contato e depois cancela sem preencher nenhum campo. - #Precisa ajustar
        Resultado esperado: Retorna à tela inicial e nenhum contato é criado. - #Precisa ajustar
        """
        with allure.step("Selecionar contato 'Maria Editada' e verificar botão de exclusão"):
            element = home_with_contact.get_contact_row_by_name("Maria Editada")
            click_and_hold(driver, element, duration=2000)
            assert home_with_contact.get_btn_delete(), "Botão de exclusão não está visível após o clique longo."
            assert home_with_contact.get_selection_count_value() == '1'
        with allure.step("Clicar no ícone de lixeira"):
            home_with_contact.click_btn_delete()

        with allure.step("Verificar mensagem de confirmação de exclusão"):
            confirmation_message = home_with_contact.get_text_delete_confirmation_message().text
            assert "Excluir este contato?" in confirmation_message, f"Mensagem de confirmação incorreta: {confirmation_message}"

        with allure.step("Confirmar a exclusão e verificar remoção"):
            home_with_contact.click_btn_confirm_delete_dialog()
            remaining_contacts = home_with_contact.get_all_contact_names()
            time.sleep(3)
            for name in ["Maria Editada"]:
                assert name not in remaining_contacts, f"Contato '{name}' ainda está presente na lista: {remaining_contacts}"

    @allure.feature("Delete Contact")
    @allure.story("Selecionar e excluir múltiplos contatos em lote")
    @allure.title("Selecionar múltiplos contatos e excluir em lote")
    @allure.severity(allure.severity_level.NORMAL)
    def test_select_and_delete_contacts(self, driver, home_with_contact: HomeWithContactPage):
        """
        Seleciona múltiplos contatos e exclui em lote.

        Cenário: Usuário seleciona os contatos "Maria Oliveira" e "Samuel Teste".
        Resultado esperado: Contato é criado e validado com sucesso.
        """
        with allure.step("Selecionar contato 'Maria Oliveira' e verificar botão de exclusão"):
            element = home_with_contact.get_contact_row_by_name("Maria Oliveira")
            click_and_hold(driver, element, duration=2000)
            assert home_with_contact.get_btn_delete(), "Botão de exclusão não está visível após o clique longo."
            home_with_contact.select_contacts(["Samuel Teste"])
        with allure.step("Verificar contador de seleção"):
            selection_count = home_with_contact.get_selection_count_value()
            assert selection_count == "2", f"Esperado '2' mas obteve '{selection_count}'"
        with allure.step("Clicar no ícone de lixeira e verificar mensagem de confirmação"):
            home_with_contact.click_btn_delete()
            confirmation_message = home_with_contact.get_text_delete_confirmation_message().text
            assert "Excluir contatos selecionados?" in confirmation_message, f"Mensagem de confirmação incorreta: {confirmation_message}"
        with allure.step("Confirmar exclusão e verificar remoção dos contatos"):
            home_with_contact.click_btn_confirm_delete_dialog()

            for name in ["Maria Oliveira", "Samuel Teste"]:
                tentativa = 0
                remaining_contacts = home_with_contact.get_all_contact_names()
                while name in remaining_contacts and tentativa < 3:
                    time.sleep(3)
                    remaining_contacts = home_with_contact.get_all_contact_names()
                    tentativa += 1
                if name in remaining_contacts:
                    home_with_contact.click_contact_row_by_name("Ana Villalobos")
                    driver.back()
                    remaining_contacts = home_with_contact.get_all_contact_names()
                assert name not in remaining_contacts, f"Contato '{name}' ainda está presente na lista: {remaining_contacts}"

    @allure.feature("Delete Contact")
    @allure.story("Excluir contato da tela de detalhes com cancelamento")
    @allure.title("Excluir contato da tela de detalhes e cancelar a exclusão")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_contact_from_detail_cancel(self, driver, home_with_contact: HomeWithContactPage, new_contact_detail: ContactDetailPage):
        """
        Excluir um contato a partir da tela de detalhes do contato e cancelar a exclusão.

        Cenário: Usuário está na tela de detalhes do contato "Ana Villalobos".
        Resultado esperado: Contato não é excluído e o usuário permanece na tela de detalhes.
        """
        with allure.step("Navegar para a tela de detalhes do contato 'Ana Villalobos'"):
            home_with_contact.click_contact_row_by_name("Ana Villalobos")
            assert new_contact_detail.get_text_contact_name().text == "Ana Villalobos", "O nome do contato não é 'Ana Villalobos'"

        with allure.step("Abrir menu de opções e verificar opções"):
            new_contact_detail.click_btn_more_options()
            options = ["Vincular", "Excluir", "Compartilhar", "Criar atalho", "Definir toque"]
            for option in options:
                assert new_contact_detail.is_option_visible(option), f"A opção '{option}' não está visível no menu de opções"

        with allure.step("Clicar em 'Excluir' e cancelar confirmação"):
            new_contact_detail.click_btn_excluir()
            confirmation_message = new_contact_detail.get_text_delete_contact_message().text
            assert "Excluir este contato?" in confirmation_message, f"Mensagem de confirmação incorreta: {confirmation_message}"
            new_contact_detail.click_btn_cancelar_dialog()

        with allure.step("Voltar para listagem e verificar que contato não foi removido"):
            driver.back()
            remaining_contacts = home_with_contact.get_all_contact_names()
            assert "Ana Villalobos" in remaining_contacts, f"Contato 'Ana Villalobos' foi removido"

    @allure.feature("Delete Contact")
    @allure.story("Menu de opções na tela de detalhes")
    @allure.title("Verificar exibição e fechamento do menu de opções na tela de detalhes")
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact_detail_menu(self, driver, home_with_contact: HomeWithContactPage, new_contact_detail: ContactDetailPage):
        """
        Verifica que o menu de opções é exibido e fechado corretamente.

        Cenário: Usuário está na tela de detalhes do contato "Ana Villalobos".
        Resultado esperado: Menu de opções é exibido e fechado ao tocar fora dele.
        """
        with allure.step("Navegar para a tela de detalhes do contato 'Ana Villalobos'"):
            home_with_contact.click_contact_row_by_name("Ana Villalobos")
            assert new_contact_detail.get_text_contact_name().text == "Ana Villalobos", "O nome do contato não é 'Ana Villalobos'"

        with allure.step("Abrir menu de opções e verificar todas as opções"):
            new_contact_detail.click_btn_more_options()
            options = ["Vincular", "Excluir", "Compartilhar", "Criar atalho", "Definir toque"]
            for option in options:
                assert new_contact_detail.is_option_visible(option), f"A opção '{option}' não está visível no menu de opções"

        with allure.step("Fechar o menu tocando fora e verificar se foi fechado"):
            driver.back()
            assert not new_contact_detail.is_option_visible("Excluir", 2), "O menu não foi fechado ao tocar fora dele"
            assert new_contact_detail.get_text_contact_name().text == "Ana Villalobos", "O usuário saiu da tela de detalhes do contato"

        with allure.step("Voltar para a tela de listagem de contatos"):
            driver.back()

    @allure.feature("Delete Contact")
    @allure.story("Excluir contato da tela de detalhes com confirmação")
    @allure.title("Excluir contato da tela de detalhes e verificar remoção")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_contact_from_detail(self, driver, home_with_contact: HomeWithContactPage, new_contact_detail: ContactDetailPage, validator_home_empty: ValidationHomeNotContact):
        """
        Excluir um contato a partir da tela de detalhes do contato.

        Cenário: Usuário está na tela de detalhes do contato "Ana Villalobos".
        Resultado esperado: Contato é excluído e removido da lista de contatos.
        """
        with allure.step("Navegar para a tela de detalhes do contato 'Ana Villalobos'"):
            home_with_contact.click_contact_row_by_name("Ana Villalobos")
            assert new_contact_detail.get_text_contact_name().text == "Ana Villalobos", "O nome do contato não é 'Ana Villalobos'"

        with allure.step("Abrir menu de opções e verificar todas as opções"):
            new_contact_detail.click_btn_more_options()
            options = ["Vincular", "Excluir", "Compartilhar", "Criar atalho", "Definir toque"]
            for option in options:
                assert new_contact_detail.is_option_visible(option), f"A opção '{option}' não está visível no menu de opções"

        with allure.step("Clicar em 'Excluir' e confirmar exclusão"):
            new_contact_detail.click_btn_excluir()
            confirmation_message = new_contact_detail.get_text_delete_contact_message().text
            assert "Excluir este contato?" in confirmation_message, f"Mensagem de confirmação incorreta: {confirmation_message}"
            new_contact_detail.click_btn_excluir_dialog()

        with allure.step("Verificar que a home está vazia (sem contatos)"):
            validator_home_empty.validate_home_not_contact()
