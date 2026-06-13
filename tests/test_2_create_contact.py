from pages.create_contact_pages import CreateContactPage
from pages.home_pages import ContactsPage
from utils.validations.validations_new_contact import ValidationNewCrateContact
from utils.validations.validations_home_not_contact import ValidationHomeNotContact

class TestHomeContact:

    def test_cancel_contact_creation_empty_form(self, driver, create_new_contact: CreateContactPage, home_page: ContactsPage, validator_home_empaty: ValidationHomeNotContact):
        home_page.click_btn_create_new_contact()
        create_new_contact.click_btn_cancel()
        validator_home_empaty.validate_home_not_contact()

    def test_cancel_contact_creation_with_filled_fields(self, driver, create_new_contact: CreateContactPage, home_page: ContactsPage, validator_home_empaty: ValidationHomeNotContact):
        home_page.click_btn_create_new_contact()
        create_new_contact.fill_input_first_name("Maria")
        create_new_contact.click_btn_cancel()
        create_new_contact.click_btn_cancel_dialog() #validar botão de cancelar da dialog
        create_new_contact.click_btn_cancel()
        create_new_contact.click_btn_discard_dialog()
        validator_home_empaty.validate_home_not_contact()

    def test_create_contact_with_empty_form_fails(self, driver, create_new_contact: CreateContactPage,  home_page: ContactsPage, validator_home_empaty: ValidationHomeNotContact):
        home_page.click_btn_create_new_contact()
        create_new_contact.click_btn_save()
        validator_home_empaty.validate_home_not_contact()
    
    def test_validate_create_contact_screen_placeholders(self, driver, create_new_contact: CreateContactPage,  home_page: ContactsPage, validator_new_contact: ValidationNewCrateContact):
        home_page.click_btn_create_new_contact()
        validator_new_contact.validate_placeholder_screen_create_new_contact()

    def test_create_contact_with_all_fields_filled(self, driver, create_new_contact: CreateContactPage,  home_page: ContactsPage, validator_new_contact: ValidationNewCrateContact):
        create_new_contact.fill_contact_form("Maria", "Silva", "8974515216", "maria@gmail.com")
        create_new_contact.click_btn_save()
        validator_new_contact.validate_create_new_contact("Maria", "Silva", "8974515216", "maria@gmail.com")
        driver.back()

    def test_create_contact_with_firt_name_only(self, driver, create_new_contact: CreateContactPage, home_page: ContactsPage, validator_new_contact: ValidationNewCrateContact):
        home_page.click_btn_create_new_contact()
        create_new_contact.fill_input_first_name("Maria")
        create_new_contact.click_btn_save()
        validator_new_contact.validate_create_new_contact("Maria")
        driver.back()

    def test_create_contact_with_phone_only(self, driver, create_new_contact: CreateContactPage, home_page: ContactsPage, validator_new_contact: ValidationNewCrateContact):
        home_page.click_btn_create_new_contact()
        create_new_contact.fill_input_phone_number("8974515216")
        create_new_contact.click_btn_save()
        validator_new_contact.validate_create_new_contact("", "", "8974515216", "")
        driver.back()

    def test_create_contact_with_email_only(self, driver, create_new_contact: CreateContactPage, home_page: ContactsPage, validator_new_contact: ValidationNewCrateContact):
        home_page.click_btn_create_new_contact()
        create_new_contact.fill_input_email("maria@gmail.com")
        create_new_contact.click_btn_save()
        validator_new_contact.validate_create_new_contact("", "", "", "maria@gmail.com")
        driver.back()