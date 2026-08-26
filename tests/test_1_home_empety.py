import allure
from utils.validations.validations_home_not_contact import ValidationHomeNotContact


class TestHomeContact:

    @allure.feature("Home sem contatos")
    @allure.story("Verificar elementos da tela inicial vazia")
    @allure.title("Tela inicial vazia - verificar elementos")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_home_screen_elements(self, validator_home_empty: ValidationHomeNotContact):
        with allure.step("Validar que a tela inicial não possui contatos"):
            validator_home_empty.validate_home_not_contact()
