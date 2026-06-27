from pages.home_pages import ContactsPage
from utils.validations.validations_home_not_contact import ValidationHomeNotContact


class TestHomeContact:

    def test_empty_home_screen_elements(self, validator_home_empty: ValidationHomeNotContact):
        validator_home_empty.validate_home_not_contact()
