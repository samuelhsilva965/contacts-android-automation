import pytest

from pages.home_pages import ContactsPage
from pages.create_contact_pages import CreateContactPage
from pages.contact_detail_page import ContactDetailPage
from utils.validations.validations_home_not_contact import ValidationHomeNotContact
from utils.validations.validations_new_contact import ValidationNewCreateContact

@pytest.fixture(scope="session")
def home_page(driver) -> ContactsPage:
    return ContactsPage(driver)

@pytest.fixture(scope="session")
def create_new_contact(driver) -> CreateContactPage:
    return CreateContactPage(driver)

@pytest.fixture(scope="session")
def new_contact_detail(driver) -> ContactDetailPage:
    return ContactDetailPage(driver)

@pytest.fixture
def cleanup_contact(driver):
    yield
    driver.back()

@pytest.fixture(scope="session")
def validator_home_empty(driver) -> ValidationHomeNotContact:
    return ValidationHomeNotContact(driver)

@pytest.fixture(scope="session")
def validator_new_contact(driver) -> ValidationNewCreateContact:
    return ValidationNewCreateContact(driver)

