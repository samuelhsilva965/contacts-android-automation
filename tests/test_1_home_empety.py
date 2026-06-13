from pages.home_pages import ContactsPage
from utils.validations.validations_home_not_contact import ValidationHomeNotContact

class TestHomeContact:

    def test_empty_home_screen_elements(self, driver, home_page: ContactsPage, validator_home_empaty: ValidationHomeNotContact):
        validator_home_empaty.validate_home_not_contact()

    