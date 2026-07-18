from appium.webdriver.common.appiumby import AppiumBy

class ContactsElements:

    BTN_OPEN_NAVIGATION_DRAWER = {
        "android": (AppiumBy.ACCESSIBILITY_ID, "Abrir gaveta de navegação"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Abrir gaveta de navegação")
    }

    TEXT_TOOLBAR_TITLE = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="Contatos"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Contatos")
    }

    TEXT_EMPTY_CONTACTS_MESSAGE = {
        "android": (AppiumBy.ID, "com.android.contacts:id/message"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Sua lista de contatos está vazia")
    }

    BTN_ADD_ACCOUNT = {
        "android": (AppiumBy.ID, "com.android.contacts:id/add_account_button"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "ADICIONAR CONTA")
    }

    BTN_IMPORT_CONTACTS = {
        "android": (AppiumBy.ID, "com.android.contacts:id/import_contacts_button"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "IMPORTAR")
    }

    BTN_CREATE_NEW_CONTACT = {
        "android": (AppiumBy.ACCESSIBILITY_ID, "Criar novo contato"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Criar novo contato")
    }

    ICON_EMPTY_CONTACTS = {
        "android": (AppiumBy.ID, "com.android.contacts:id/empty_image"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "empty_image")
    }