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

    # ── Mais opções ─────────────────────────────────────────

    BTN_VINCULAR = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="Vincular"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Vincular")
    }

    BTN_EXCLUIR = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="Excluir"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Excluir")
    }

    BTN_COMPARTILHAR = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="Compartilhar"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Compartilhar")
    }

    BTN_CRIAR_ATALHO = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="Criar atalho"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Criar atalho")
    }

    BTN_DEFINIR_TOQUE = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="Definir toque"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Definir toque")
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

    TEXT_TOAST_DELETE_CONTACT_MESSAGE = {
        "android": (AppiumBy.ID, "android:id/message"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Excluir este contato?")
    }

    BTN_TOAST_CANCELAR = {
        "android": (AppiumBy.ID, "android:id/button2"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "CANCELAR")
    }

    BTN_TOAST_EXCLUIR = {
        "android": (AppiumBy.ID, "android:id/button1"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "EXCLUIR")
    }