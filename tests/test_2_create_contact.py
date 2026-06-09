

class TestHomeContact:

    def test_criar_contato_com_todos_os_campos_preenchidos(self, driver, criar_novo_contato, validator_new_contact):


        validator_new_contact.validate_create_new_contact()