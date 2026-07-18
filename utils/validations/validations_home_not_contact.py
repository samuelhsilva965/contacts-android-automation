from pages.home_pages import ContactsPage


class ValidationHomeNotContact:

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.home_page = ContactsPage(self.driver)

    def validate_home_not_contact(self):

        assert self.home_page.get_toolbar_title_text() == "Contatos"
        assert self.home_page.get_btn_open_navigation_drawer().is_enabled
        assert self.home_page.get_icon_empty_contacts()
        assert self.home_page.get_text_empty_contacts_message().text == "Sua lista de contatos está vazia"
        assert self.home_page.get_btn_add_account().is_enabled()
        assert self.home_page.get_btn_import_contacts().is_enabled()
        assert self.home_page.get_btn_add_account().text == "ADICIONAR CONTA"
        assert self.home_page.get_btn_import_contacts().text == "IMPORTAR"
        assert self.home_page.get_btn_create_new_contact().is_enabled()
