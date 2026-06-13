from appium.webdriver.common.appiumby import AppiumBy


class CreateContactElements:

    # ── Toolbar ──────────────────────────────────────────────────────────────

    BTN_CANCEL = {
        "android": (AppiumBy.ACCESSIBILITY_ID, "Cancelar"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Cancelar")
    }

    TEXT_TOOLBAR_TITLE = {
        "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="Criar novo contato"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Criar novo contato")
    }

    BTN_SAVE = {
        "android": (AppiumBy.ID, "com.android.contacts:id/editor_menu_save_button"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "SALVAR")
    }

    BTN_CANCEL_DIALOG = {
        "android": (AppiumBy.ID, "android:id/button2"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Cancelar")  # Ajuste conforme o padrão do iOS se aplicável
    }

    BTN_DISCARD_DIALOG = {
        "android": (AppiumBy.ID, "android:id/button1"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Descartar")  # Ajuste conforme o padrão do iOS se aplicável
    }

    # ── Foto do contato ───────────────────────────────────────────────────────

    BTN_ADD_CONTACT_PHOTO = {
        "android": (AppiumBy.ACCESSIBILITY_ID, "Adicionar foto do contato"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Adicionar foto do contato")
    }

    ICON_CONTACT_PHOTO = {
        "android": (AppiumBy.ID, "com.android.contacts:id/photo"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "photo")
    }

    # ── Conta de destino ──────────────────────────────────────────────────────

    TEXT_SAVE_TO_LABEL = {
        "android": (AppiumBy.ID, "com.android.contacts:id/account_type"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Salvar em")
    }

    TEXT_ACCOUNT_NAME = {
        "android": (AppiumBy.ID, "com.android.contacts:id/account_name"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Dispositivo")
    }

    # ── Campos de nome ────────────────────────────────────────────────────────

    ICON_NAME_FIELD = {
        "android": (AppiumBy.XPATH,
            '//android.widget.ImageView[@content-desc="Nome" and @resource-id="com.android.contacts:id/kind_icon"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Nome")
    }

    INPUT_FIRST_NAME = {
        "android": (AppiumBy.XPATH,
            '//android.widget.EditText[@hint="Nome"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Nome")
    }

    INPUT_LAST_NAME = {
        "android": (AppiumBy.XPATH,
            '//android.widget.EditText[@hint="Sobrenome"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Sobrenome")
    }

    BTN_EXPAND_NAME_FIELDS = {
        "android": (AppiumBy.ACCESSIBILITY_ID, "Mostrar mais campos de nome"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Mostrar mais campos de nome")
    }

    # ── Campos de telefone ────────────────────────────────────────────────────

    ICON_PHONE_FIELD = {
        "android": (AppiumBy.XPATH,
            '//android.widget.ImageView[@content-desc="Telefone" and @resource-id="com.android.contacts:id/kind_icon"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Telefone")
    }

    INPUT_PHONE_NUMBER = {
        "android": (AppiumBy.XPATH,
            '//android.widget.EditText[@hint="Telefone"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Telefone")
    }

    ELEMENT_PHONE_TYPE_SPINNER = {
        "android": (AppiumBy.XPATH,
            '//android.widget.Spinner[@content-desc="Telefone"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Telefone")
    }

    TEXT_PHONE_TYPE_SELECTED = {
        "android": (AppiumBy.XPATH,
            '//android.widget.Spinner[@content-desc="Telefone"]//android.widget.TextView[@resource-id="android:id/text1"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Celular")
    }

    # ── Campos de e-mail ──────────────────────────────────────────────────────

    ICON_EMAIL_FIELD = {
        "android": (AppiumBy.XPATH,
            '//android.widget.ImageView[@content-desc="E-mail" and @resource-id="com.android.contacts:id/kind_icon"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "E-mail")
    }

    INPUT_EMAIL = {
        "android": (AppiumBy.XPATH,
            '//android.widget.EditText[@hint="E-mail"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "E-mail")
    }

    ELEMENT_EMAIL_TYPE_SPINNER = {
        "android": (AppiumBy.XPATH,
            '//android.widget.Spinner[@content-desc="E-mail"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "E-mail")
    }

    TEXT_EMAIL_TYPE_SELECTED = {
        "android": (AppiumBy.XPATH,
            '//android.widget.Spinner[@content-desc="E-mail"]//android.widget.TextView[@resource-id="android:id/text1"]'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Casa")
    }

    # ── Mais campos ───────────────────────────────────────────────────────────

    BTN_MORE_FIELDS = {
        "android": (AppiumBy.ID, "com.android.contacts:id/more_fields"),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Mais campos")
    }