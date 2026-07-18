from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from elements.home_with_contact_elements import ContactListElements
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import time


class HomeWithContactPage:
    """
    Page Object for the Contact List Selection screen.

    Covers:
      - Individual contact row interaction (tap to open / toggle selection)
      - Checkbox selection per contact
      - Toolbar actions: close selection, share, delete
      - Dynamic helpers for any contact by name
    """

    def __init__(self, driver, platform: str = "android", timeout: int = 10):
        """
        :param driver:   Appium WebDriver instance.
        :param platform: "android" or "ios".
        :param timeout:  Explicit wait timeout in seconds.
        """
        self.driver = driver
        self.platform = platform.lower()
        self.wait = WebDriverWait(driver, timeout)

    # ----------------------------------------------------------
    # Private helper
    # ----------------------------------------------------------

    def _locate(self, locator_dict: dict):
        """Resolve the correct (by, value) tuple for the current platform."""
        return locator_dict[self.platform]

    # ===========================================================
    # Toolbar
    # ===========================================================

    def get_btn_close_selection(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.BTN_CLOSE_SELECTION)
            )
        )

    def click_btn_close_selection(self):
        """Close multi-selection mode without performing any action."""
        self.get_btn_close_selection().click()

    # -----------------------------------------------------------

    def get_text_selection_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.TEXT_SELECTION_COUNT)
            )
        )

    def get_selection_count_value(self) -> str:
        """Returns the current selection counter as a string (e.g. '1', '3')."""
        return self.get_text_selection_count().text

    # -----------------------------------------------------------

    def get_btn_share(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.BTN_SHARE)
            )
        )

    def click_btn_share(self):
        """Tap the Share button in the toolbar."""
        self.get_btn_share().click()

    # -----------------------------------------------------------

    def get_btn_delete(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.BTN_DELETE)
            )
        )

    def click_btn_delete(self):
        """Tap the Delete (trash) button in the toolbar to trigger deletion flow."""
        self.get_btn_delete().click()

    # ===========================================================
    # Contact List
    # ===========================================================

    def get_contact_list(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.ELEMENT_CONTACT_LIST)
            )
        )

    # ===========================================================
    # Contact — Maria
    # ===========================================================

    def get_contact_row_maria(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.ELEMENT_CONTACT_ROW_MARIA)
            )
        )

    def click_contact_row_maria(self):
        """Tap the Maria contact row (opens detail or toggles selection)."""
        self.get_contact_row_maria().click()

    def get_text_contact_name_maria(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.TEXT_CONTACT_NAME_MARIA)
            )
        )

    def get_checkbox_maria(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.ELEMENT_CHECKBOX_MARIA)
            )
        )

    def click_checkbox_maria(self):
        """Toggle the checkbox for contact Maria."""
        self.get_checkbox_maria().click()

    def is_checkbox_maria_selected(self) -> bool:
        return self.get_checkbox_maria().is_selected()

    # ===========================================================
    # Contact — Maria Silva
    # ===========================================================

    def get_contact_row_maria_silva(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.ELEMENT_CONTACT_ROW_MARIA_SILVA)
            )
        )

    def click_contact_row_maria_silva(self):
        """Tap the Maria Silva contact row."""
        self.get_contact_row_maria_silva().click()

    def get_text_contact_name_maria_silva(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.TEXT_CONTACT_NAME_MARIA_SILVA)
            )
        )

    def get_checkbox_maria_silva(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.ELEMENT_CHECKBOX_MARIA_SILVA)
            )
        )

    def click_checkbox_maria_silva(self):
        """Toggle the checkbox for contact Maria Silva."""
        self.get_checkbox_maria_silva().click()

    def is_checkbox_maria_silva_selected(self) -> bool:
        return self.get_checkbox_maria_silva().is_selected()

    # ===========================================================
    # Contact — maria@gmail.com
    # ===========================================================

    def get_contact_row_maria_email(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.ELEMENT_CONTACT_ROW_MARIA_EMAIL)
            )
        )

    def click_contact_row_maria_email(self):
        """Tap the maria@gmail.com contact row."""
        self.get_contact_row_maria_email().click()

    def get_text_contact_name_maria_email(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.TEXT_CONTACT_NAME_MARIA_EMAIL)
            )
        )

    def get_checkbox_maria_email(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.ELEMENT_CHECKBOX_MARIA_EMAIL)
            )
        )

    def click_checkbox_maria_email(self):
        """Toggle the checkbox for contact maria@gmail.com."""
        self.get_checkbox_maria_email().click()

    def is_checkbox_maria_email_selected(self) -> bool:
        return self.get_checkbox_maria_email().is_selected()

    # ===========================================================
    # Contact — (897) 451-5216
    # ===========================================================

    def get_contact_row_phone(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.ELEMENT_CONTACT_ROW_PHONE)
            )
        )

    def click_contact_row_phone(self):
        """Tap the phone-number contact row."""
        self.get_contact_row_phone().click()

    def get_text_contact_name_phone(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.TEXT_CONTACT_NAME_PHONE)
            )
        )

    def get_checkbox_phone(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.ELEMENT_CHECKBOX_PHONE)
            )
        )

    def click_checkbox_phone(self):
        """Toggle the checkbox for the phone-number contact."""
        self.get_checkbox_phone().click()

    def is_checkbox_phone_selected(self) -> bool:
        return self.get_checkbox_phone().is_selected()

    # ===========================================================
    # Dynamic helpers — interact with any contact by name
    # ===========================================================

    def get_contact_row_by_name(self, name: str):
        """
        Returns the contact row WebElement for the given display name.

        Usage:
            page.get_contact_row_by_name("Maria Silva")
        """
        locator = ContactListElements.contact_row_by_name(name)[self.platform]
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_contact_row_by_name(self, name: str):
        """Tap any contact row by its display name."""
        self.get_contact_row_by_name(name).click()

    def get_checkbox_by_name(self, name: str):
        """
        Returns the checkbox WebElement for the given contact display name.

        Usage:
            page.get_checkbox_by_name("Maria Silva")
        """
        locator = ContactListElements.checkbox_by_name(name)[self.platform]
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_checkbox_by_name(self, name: str):
        """Toggle the checkbox for any contact by its display name."""
        self.get_checkbox_by_name(name).click()

    def is_checkbox_selected_by_name(self, name: str) -> bool:
        """Returns True if the checkbox for the given contact name is checked."""
        return self.get_checkbox_by_name(name).get_attribute("checked") == "true"
    
    def is_btn_delete_visible(self, timeout: int = 2) -> bool:
        """Retorna True se o botão de excluir estiver visível dentro do timeout informado."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self._locate(ContactListElements.BTN_DELETE))
            )
            return True
        except TimeoutException:
            return False

    # ===========================================================
    # Composite / high-level actions
    # ===========================================================

    def get_all_contact_names(self, retries: int = 3, delay: float = 0.5) -> list[str]:
        """
        Returns the display names of all contacts currently visible in the list.

        Retries on StaleElementReferenceException, since the list may still be
        re-rendering right after an action (e.g. deleting a contact), which can
        invalidate the cached element references between the search and reading
        their text.

        Usage:
            names = page.get_all_contact_names()
            assert "Maria" not in names
        """
        locator = self._locate(ContactListElements.ELEMENT_ALL_CONTACT_NAMES)

        for attempt in range(retries):
            try:
                elements = self.wait.until(EC.presence_of_all_elements_located(locator))
                return [el.text for el in elements]
            except StaleElementReferenceException:
                if attempt == retries - 1:
                    raise
                time.sleep(delay)

    def select_contacts(self, names: list):
        """
        Select multiple contacts by their display names.

        :param names: List of contact display names to check.

        Usage:
            page.select_contacts(["Maria", "Maria Silva", "maria@gmail.com"])
        """
        for name in names:
            if not self.is_checkbox_selected_by_name(name):
                self.click_checkbox_by_name(name)

    def delete_selected_contacts(self):
        """
        Tap the Delete button in the toolbar.
        Assumes at least one contact is already selected.
        """
        self.click_btn_delete()

    def select_and_delete_contacts(self, names: list):
        """
        Select the given contacts and then tap Delete.

        :param names: List of contact display names to delete.

        Usage:
            page.select_and_delete_contacts(["Maria Silva"])
        """
        self.select_contacts(names)
        self.delete_selected_contacts()

    def get_text_delete_confirmation_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.TEXT_DELETE_CONFIRMATION_MESSAGE)
            )
        )

    def get_btn_confirm_delete_dialog(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.BTN_CONFIRM_DELETE_DIALOG)
            )
        )

    def click_btn_confirm_delete_dialog(self):
        """Confirma a exclusão no diálogo (botão positivo)."""
        self.get_btn_confirm_delete_dialog().click()

    def get_btn_cancel_delete_dialog(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self._locate(ContactListElements.BTN_CANCEL_DELETE_DIALOG)
            )
        )

    def click_btn_cancel_delete_dialog(self):
        """Cancela a exclusão no diálogo (botão negativo)."""
        self.get_btn_cancel_delete_dialog().click()