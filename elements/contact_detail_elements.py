from appium.webdriver.common.appiumby import AppiumBy


class ContactDetailElements:

    # ── Toolbar / Header ──────────────────────────────────────────────────────

    ICON_CONTACT_PHOTO = {
        "android": (AppiumBy.ID, "com.android.contacts:id/photo"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "photo")
    }

    TEXT_CONTACT_NAME = {
        "android": (AppiumBy.ID, "com.android.contacts:id/large_title"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "large_title")
    }

    BTN_ADD_TO_FAVORITES = {
        "android": (AppiumBy.ACCESSIBILITY_ID, "Adicionar aos favoritos"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Adicionar aos favoritos")
    }

    BTN_EDIT = {
        "android": (AppiumBy.ACCESSIBILITY_ID, "Editar"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Editar")
    }

    BTN_MORE_OPTIONS = {
        "android": (AppiumBy.ACCESSIBILITY_ID, "Mais opções"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Mais opções")
    }

    # ── Cartão "sem dados de contato" ─────────────────────────────────────────

    ELEMENT_NO_CONTACT_DATA_CARD = {
        "android": (AppiumBy.ID, "com.android.contacts:id/no_contact_data_card"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "no_contact_data_card")
    }

    TEXT_ADD_PHONE_NUMBER = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.android.contacts:id/header" and @text="Adicionar número de telefone"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Adicionar número de telefone")
    }

    TEXT_PHONE_NUMBER = {
        "android": (AppiumBy.XPATH, '//android.widget.RelativeLayout[contains(@content-desc, "Celular")]//android.widget.TextView[@resource-id="com.android.contacts:id/header"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Adicionar número de telefone")
    }

    TEXT_ADD_EMAIL = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.android.contacts:id/header" and @text="Adicionar e-mail"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Adicionar e-mail")
    }

    TEXT_EMAIL = {
        "android": (AppiumBy.XPATH, '//android.widget.RelativeLayout[contains(@content-desc, "Casa")]//android.widget.TextView[@resource-id="com.android.contacts:id/header"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Adicionar e-mail")
    }

    BTN_SEND_SMS = {
    "android": (AppiumBy.XPATH,
        '//android.widget.ImageView[@resource-id="com.android.contacts:id/icon_alternate" and contains(@content-desc, "Enviar mensagem de texto para")]'),
    "ios": (
        AppiumBy.ACCESSIBILITY_ID, "Enviar mensagem de texto")
    }

    # ── Toast de confirmação ──────────────────────────────────────────────────

    TEXT_TOAST_CONTACT_SAVED = {
        "android": (AppiumBy.XPATH, '//android.widget.Toast[contains(@text, "Contato salvo")]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Contato salvo")
    }