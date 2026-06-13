from pages.create_contact_pages import CreateContactPage
from pages.home_pages import ContactsPage
from utils.validations.validations_new_contact import ValidationNewCrateContact

class TestHomeContact:

    def test_create_contact_with_all_fields_filled(self, driver, create_new_contact: CreateContactPage, validator_new_contact: ValidationNewCrateContact):
        create_new_contact.fill_contact_form("Maria", "Silva", "8974515216", "maria@gmail.com")
        create_new_contact.click_btn_save()
        validator_new_contact.validate_create_new_contact("Maria", "Silva", "8974515216", "maria@gmail.com")
        driver.back()

    def test_create_contact_with_firt_name_only(self, driver, create_new_contact: CreateContactPage, home_page: ContactsPage, validator_new_contact: ValidationNewCrateContact):
        home_page.click_btn_create_new_contact()
        create_new_contact.fill_input_first_name("Maria")
        create_new_contact.click_btn_save()
        validator_new_contact.validate_create_new_contact("Maria")