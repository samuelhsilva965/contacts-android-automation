import allure
import time
from selenium.common.exceptions import TimeoutException

from pages.home_pages import ContactsPage
from pages.home_with_contact_page import HomeWithContactPage
from pages.create_contact_pages import CreateContactPage
from utils.functions.back import back
from utils.functions.close_dialog_add_account import click_btn_cancel_dialog_adicionar_conta_if_present
from utils.functions.ensure_on_home import ensure_on_contacts_home


# Contatos esperados ao final de test_2_create_contact (pré-condição do test_3).
REQUIRED_CONTACTS_FOR_UPDATE = [
    {
        "display_name": "Maria",
        "first_name": "Maria",
        "last_name": "",
        "phone": "",
        "email": "",
    },
    {
        "display_name": "(897) 451-5216",
        "first_name": "",
        "last_name": "",
        "phone": "8974515216",
        "email": "",
    },
    {
        "display_name": "maria@gmail.com",
        "first_name": "",
        "last_name": "",
        "phone": "",
        "email": "maria@gmail.com",
    },
    {
        "display_name": "Maria Silva",
        "first_name": "Maria",
        "last_name": "Silva",
        "phone": "8974515216",
        "email": "maria@gmail.com",
    },
]

# Contatos usados pelos testes de exclusão (independente do test_3).
REQUIRED_CONTACTS_FOR_DELETE = [
    {
        "display_name": "Maria Editada",
        "first_name": "Maria Editada",
        "last_name": "",
        "phone": "",
        "email": "",
    },
    {
        "display_name": "Maria Oliveira",
        "first_name": "Maria",
        "last_name": "Oliveira",
        "phone": "",
        "email": "",
    },
    {
        "display_name": "Samuel Teste",
        "first_name": "Samuel Teste",
        "last_name": "",
        "phone": "",
        "email": "",
    },
    {
        "display_name": "Ana Villalobos",
        "first_name": "Ana",
        "last_name": "Villalobos",
        "phone": "",
        "email": "",
    },
]


def _get_existing_contact_names(
    home_page: ContactsPage,
    home_with_contact: HomeWithContactPage,
) -> list[str]:
    """Retorna os nomes visíveis na lista, ou [] se a lista estiver vazia."""
    if home_page.is_contacts_list_empty():
        return []
    try:
        return home_with_contact.get_all_contact_names()
    except TimeoutException:
        return []


def _create_contact(
    driver,
    home_page: ContactsPage,
    create_new_contact: CreateContactPage,
    contact: dict,
) -> None:
    """Cria um único contato a partir da home e volta para a lista."""
    ensure_on_contacts_home(driver)
    home_page.click_btn_create_new_contact()
    click_btn_cancel_dialog_adicionar_conta_if_present(driver)

    create_new_contact.fill_contact_form(
        first_name=contact["first_name"],
        last_name=contact["last_name"],
        phone=contact["phone"],
        email=contact["email"],
    )
    create_new_contact.click_btn_save()
    time.sleep(1)
    back(driver, delay=1)
    ensure_on_contacts_home(driver)


def ensure_required_contacts(
    driver,
    home_page: ContactsPage,
    home_with_contact: HomeWithContactPage,
    create_new_contact: CreateContactPage,
    required_contacts: list[dict],
) -> None:
    """
    Garante que todos os contatos informados existam na lista.

    - Garante que está na home de Contatos
    - Lista os contatos atuais
    - Identifica quais estão presentes e quais faltam
    - Cria apenas os faltantes
    - Revalida que todos estão na lista
    """
    expected_names = [c["display_name"] for c in required_contacts]

    with allure.step("Garantir que está na home de Contatos"):
        ensure_on_contacts_home(driver)

    with allure.step("Listar contatos atuais na tela inicial"):
        existing = _get_existing_contact_names(home_page, home_with_contact)
        allure.attach(
            "\n".join(existing) if existing else "(nenhum contato)",
            name="Contatos atuais",
            attachment_type=allure.attachment_type.TEXT,
        )

    present = [name for name in expected_names if name in existing]
    missing = [c for c in required_contacts if c["display_name"] not in existing]
    missing_names = [c["display_name"] for c in missing]

    with allure.step("Validar quais contatos necessários já existem"):
        allure.attach(
            "\n".join(present) if present else "(nenhum)",
            name="Contatos presentes",
            attachment_type=allure.attachment_type.TEXT,
        )
        allure.attach(
            "\n".join(missing_names) if missing_names else "(nenhum)",
            name="Contatos faltantes",
            attachment_type=allure.attachment_type.TEXT,
        )

        if not missing:
            allure.attach(
                "Todos os contatos necessários já estão criados.",
                name="Resultado da validação",
                attachment_type=allure.attachment_type.TEXT,
            )
            return

        allure.attach(
            f"Faltam {len(missing)} contato(s). Serão criados agora: {', '.join(missing_names)}",
            name="Resultado da validação",
            attachment_type=allure.attachment_type.TEXT,
        )

    for contact in missing:
        with allure.step(f"Criar contato faltante: '{contact['display_name']}'"):
            _create_contact(driver, home_page, create_new_contact, contact)

    with allure.step("Revalidar que todos os contatos necessários estão na lista"):
        final_names = _get_existing_contact_names(home_page, home_with_contact)
        still_missing = [name for name in expected_names if name not in final_names]

        allure.attach(
            "\n".join(final_names) if final_names else "(nenhum contato)",
            name="Contatos após criação",
            attachment_type=allure.attachment_type.TEXT,
        )

        assert not still_missing, (
            f"Após tentar criar os contatos faltantes, ainda estão ausentes: {still_missing}. "
            f"Contatos atuais: {final_names}"
        )


def ensure_required_contacts_for_update(
    driver,
    home_page: ContactsPage,
    home_with_contact: HomeWithContactPage,
    create_new_contact: CreateContactPage,
    required_contacts: list[dict] | None = None,
) -> None:
    """Garante os contatos necessários para os testes de atualização."""
    ensure_required_contacts(
        driver=driver,
        home_page=home_page,
        home_with_contact=home_with_contact,
        create_new_contact=create_new_contact,
        required_contacts=required_contacts or REQUIRED_CONTACTS_FOR_UPDATE,
    )


def contacts_for_delete(*display_names: str) -> list[dict]:
    """Retorna a definição dos contatos de exclusão pelos display names."""
    by_name = {c["display_name"]: c for c in REQUIRED_CONTACTS_FOR_DELETE}
    missing_keys = [name for name in display_names if name not in by_name]
    if missing_keys:
        raise KeyError(f"Contatos de exclusão desconhecidos: {missing_keys}")
    return [by_name[name] for name in display_names]


def ensure_required_contacts_for_delete(
    driver,
    home_page: ContactsPage,
    home_with_contact: HomeWithContactPage,
    create_new_contact: CreateContactPage,
    required_contacts: list[dict] | None = None,
) -> None:
    """Garante os contatos necessários para os testes de exclusão."""
    ensure_required_contacts(
        driver=driver,
        home_page=home_page,
        home_with_contact=home_with_contact,
        create_new_contact=create_new_contact,
        required_contacts=required_contacts or REQUIRED_CONTACTS_FOR_DELETE,
    )
