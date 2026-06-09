from pages.create_contact_pages import CreateContactPage

class ValidationNewCrateContact:

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.new_contact_page = CreateContactPage(self.driver)

    def validate_create_new_contact(self, first_name: str = "Maria", last_name: str = "Silva",
                          phone: str = "11999999999", email: str = "maria@email.com"):

        self.new_contact_page.fill_contact_form(first_name, last_name, phone, email)