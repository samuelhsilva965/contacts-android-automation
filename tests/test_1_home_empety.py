from pages.home_pages import ContactsPage
from utils.validations.validations_home_not_contact import ValidationHomeNotContact
class TestHomeContact:

    def test(self, driver, home_page, validator_home_empaty):

        validator_home_empaty.validate_home_not_contact()
        home_page.click_btn_create_new_contact()

    