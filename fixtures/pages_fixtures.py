import pytest

from pages.home_pages import ContactsPage
from pages.create_contact_pages import CreateContactPage
from utils.validations.validations_home_not_contact import ValidationHomeNotContact
from utils.validations.validations_new_contact import ValidationNewCrateContact

@pytest.fixture(scope="session")
def home_page(driver) -> ContactsPage:
    return ContactsPage(driver)

@pytest.fixture(scope="session")
def criar_novo_contato(driver) -> CreateContactPage:
    return CreateContactPage(driver)

@pytest.fixture(scope="session")
def validator_home_empaty(driver) -> ValidationHomeNotContact:
    return ValidationHomeNotContact(driver)

@pytest.fixture(scope="session")
def validator_new_contact(driver) -> ValidationNewCrateContact:
    return ValidationNewCrateContact(driver)

