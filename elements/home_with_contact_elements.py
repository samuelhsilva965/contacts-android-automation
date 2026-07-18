from appium.webdriver.common.appiumby import AppiumBy

# ============================================================
# Contact List Selection Screen — Elements
# ============================================================


class ContactListElements:

    # ----------------------------------------------------------
    # Toolbar / Action Bar
    # ----------------------------------------------------------

    BTN_CLOSE_SELECTION = {
        "android": (AppiumBy.ACCESSIBILITY_ID, "fechar"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "fechar"),
    }

    TEXT_SELECTION_COUNT = {
        "android": (AppiumBy.ID, "com.android.contacts:id/selection_count_text"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "selection_count_text"),
    }

    BTN_SHARE = {
        "android": (AppiumBy.ID, "com.android.contacts:id/menu_share"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Compartilhar"),
    }

    BTN_DELETE = {
        "android": (AppiumBy.ID, "com.android.contacts:id/menu_delete"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Excluir"),
    }

    # ----------------------------------------------------------
    # Contact List (container)
    # ----------------------------------------------------------

    ELEMENT_CONTACT_LIST = {
        "android": (AppiumBy.ID, "android:id/list"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "contact_list"),
    }

    # ----------------------------------------------------------
    # All contact names (usado para listar/validar todos os contatos)
    # ----------------------------------------------------------

    ELEMENT_ALL_CONTACT_NAMES = {
        "android": (AppiumBy.ID, "com.android.contacts:id/cliv_name_textview"),
        "ios": (
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeStaticText[`name CONTAINS "cliv_name"`]',
        ),
    }

    # ----------------------------------------------------------
    # Contact Item — Maria (index 1)
    # ----------------------------------------------------------

    ELEMENT_CONTACT_ROW_MARIA = {
        "android": (
            AppiumBy.XPATH,
            '//android.widget.ListView[@resource-id="android:id/list"]'
            '/android.view.ViewGroup[.//android.widget.TextView[@content-desc="Maria"]]',
        ),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Maria"),
    }

    TEXT_CONTACT_NAME_MARIA = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Maria" and @resource-id="com.android.contacts:id/cliv_name_textview"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Maria"),
    }

    ELEMENT_CHECKBOX_MARIA = {
        "android": (
            AppiumBy.XPATH,
            '//android.widget.ListView[@resource-id="android:id/list"]'
            '/android.view.ViewGroup[.//android.widget.TextView[@content-desc="Maria"]]'
            '//android.widget.CheckBox',
        ),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "checkbox_Maria"),
    }

    # ----------------------------------------------------------
    # Contact Item — Maria Silva (index 2)
    # ----------------------------------------------------------

    ELEMENT_CONTACT_ROW_MARIA_SILVA = {
        "android": (
            AppiumBy.XPATH,
            '//android.widget.ListView[@resource-id="android:id/list"]'
            '/android.view.ViewGroup[.//android.widget.TextView[@content-desc="Maria Silva"]]',
        ),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Maria Silva"),
    }

    TEXT_CONTACT_NAME_MARIA_SILVA = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Maria Silva" and @resource-id="com.android.contacts:id/cliv_name_textview"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Maria Silva"),
    }

    ELEMENT_CHECKBOX_MARIA_SILVA = {
        "android": (
            AppiumBy.XPATH,
            '//android.widget.ListView[@resource-id="android:id/list"]'
            '/android.view.ViewGroup[.//android.widget.TextView[@content-desc="Maria Silva"]]'
            '//android.widget.CheckBox',
        ),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "checkbox_Maria_Silva"),
    }

    # ----------------------------------------------------------
    # Contact Item — maria@gmail.com (index 3)
    # ----------------------------------------------------------

    ELEMENT_CONTACT_ROW_MARIA_EMAIL = {
        "android": (
            AppiumBy.XPATH,
            '//android.widget.ListView[@resource-id="android:id/list"]'
            '/android.view.ViewGroup[.//android.widget.TextView[@content-desc="maria@gmail.com"]]',
        ),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "maria@gmail.com"),
    }

    TEXT_CONTACT_NAME_MARIA_EMAIL = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="maria@gmail.com" and @resource-id="com.android.contacts:id/cliv_name_textview"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "maria@gmail.com"),
    }

    ELEMENT_CHECKBOX_MARIA_EMAIL = {
        "android": (
            AppiumBy.XPATH,
            '//android.widget.ListView[@resource-id="android:id/list"]'
            '/android.view.ViewGroup[.//android.widget.TextView[@content-desc="maria@gmail.com"]]'
            '//android.widget.CheckBox',
        ),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "checkbox_maria_email"),
    }

    # ----------------------------------------------------------
    # Contact Item — (897) 451-5216 (index 4)
    # ----------------------------------------------------------

    ELEMENT_CONTACT_ROW_PHONE = {
        "android": (
            AppiumBy.XPATH,
            '//android.widget.ListView[@resource-id="android:id/list"]'
            '/android.view.ViewGroup[.//android.widget.TextView[@content-desc="(897) 451-5216"]]',
        ),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "(897) 451-5216"),
    }

    TEXT_CONTACT_NAME_PHONE = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="(897) 451-5216" and @resource-id="com.android.contacts:id/cliv_name_textview"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "(897) 451-5216"),
    }

    ELEMENT_CHECKBOX_PHONE = {
        "android": (
            AppiumBy.XPATH,
            '//android.widget.ListView[@resource-id="android:id/list"]'
            '/android.view.ViewGroup[.//android.widget.TextView[@content-desc="(897) 451-5216"]]'
            '//android.widget.CheckBox',
        ),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "checkbox_phone"),
    }

    # ----------------------------------------------------------
    # Diálogo de confirmação de exclusão
    # ----------------------------------------------------------

    TEXT_DELETE_CONFIRMATION_MESSAGE = {
        "android": (AppiumBy.ID, "android:id/message"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "delete_confirmation_message"),
    }

    BTN_CONFIRM_DELETE_DIALOG = {
        "android": (AppiumBy.ID, "android:id/button1"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Excluir"),
    }

    BTN_CANCEL_DELETE_DIALOG = {
        "android": (AppiumBy.ID, "android:id/button2"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Cancelar"),
    }

    # ----------------------------------------------------------
    # Generic / dynamic locators (used by helper methods)
    # ----------------------------------------------------------

    @staticmethod
    def contact_row_by_name(name: str) -> dict:
        """Returns a locator dict for any contact row matched by display name."""
        return {
            "android": (
                AppiumBy.XPATH,
                f'//android.widget.ListView[@resource-id="android:id/list"]'
                f'/android.view.ViewGroup[.//android.widget.TextView[@content-desc="{name}"]]',
            ),
            "ios": (AppiumBy.ACCESSIBILITY_ID, name),
        }

    @staticmethod
    def checkbox_by_name(name: str) -> dict:
        """Returns a locator dict for the checkbox of a contact matched by display name."""
        return {
            "android": (
                AppiumBy.XPATH,
                f'//android.widget.ListView[@resource-id="android:id/list"]'
                f'/android.view.ViewGroup[.//android.widget.TextView[@content-desc="{name}"]]'
                f'//android.widget.CheckBox',
            ),
            "ios": (AppiumBy.ACCESSIBILITY_ID, f"checkbox_{name.replace(' ', '_')}"),
        }