# 📇 Contacts Android Automation

Suíte de testes E2E (end-to-end) para o **app nativo de Contatos do Android** (`com.android.contacts`), construída com **Appium + Selenium + Pytest**, seguindo o padrão **Page Object Model (POM)**.

O projeto cobre os principais fluxos de CRUD de contato — criação, leitura/validação de tela, atualização e exclusão (individual e em lote) — incluindo cenários de cancelamento, validações de formulário e estados de confirmação/diálogo.

---

## 🎯 Objetivo do projeto

Validar, de ponta a ponta, o comportamento funcional do app de Contatos em português (pt-BR), garantindo que:

- A tela inicial reflita corretamente o estado "sem contatos";
- A criação de contatos respeite validações obrigatórias e opcionais (nome, telefone, e-mail, tipos de campo);
- A edição de contatos existentes atualize corretamente nome, sobrenome, telefone e e-mail;
- A exclusão (individual, em lote, e a partir da tela de detalhes) remova o contato e trate corretamente confirmação/cancelamento;
- Fluxos de cancelamento (com e sem dados preenchidos) não gerem contatos indevidos.

---

## 🧱 Arquitetura da automação

O projeto segue o **Page Object Model (POM)**, com separação clara de responsabilidades:

```
contacts-android-automation/
├── conftest.py                     # Registro dos plugins de fixtures (pytest_plugins)
├── requirements.txt                # Dependências do projeto
│
├── elements/                       # Camada de localizadores (locators) por tela
│   ├── home_elements.py
│   ├── home_with_contact_elements.py
│   ├── create_contact_elements.py
│   └── contact_detail_elements.py
│
├── pages/                          # Camada de Page Objects (ações da UI)
│   ├── home_pages.py
│   ├── home_with_contact_page.py
│   ├── create_contact_pages.py
│   └── contact_detail_page.py
│
├── utils/
│   ├── functions/                  # Helpers (back, long-press, home, pré-condições de contatos)
│   └── validations/                # Classes de validação (assertions agrupadas por contexto)
│
├── fixtures/                       # Fixtures de pytest (driver e page objects)
│   ├── driver_fixtures.py
│   └── pages_fixtures.py
│
├── tests/                          # Casos de teste (Pytest + Allure)
│   ├── test_1_home_empety.py
│   ├── test_2_create_contact.py
│   ├── test_3_update_contact.py
│   └── test_4_delete_contact.py
│
└── .github/workflows/
    └── appium-tests.yml            # Pipeline CI (emulador Android + Appium + Allure)
```

### Camadas e responsabilidades

| Camada | Responsabilidade | Observação de QA |
|---|---|---|
| **elements/** | Centraliza os localizadores, por plataforma (`android`/`ios`), em dicionários (`{"android": (...), "ios": (...)}`) | Estrutura já preparada para expansão multiplataforma, embora hoje apenas Android seja executado |
| **pages/** | Encapsula ações (`click_*`, `fill_*`) e getters (`get_*`) sobre os elementos, sem lógica de asserção | Boa prática de POM: Page Objects não devem conter `assert` |
| **utils/validations/** | Concentra os `assert` de negócio, desacoplando a verificação da interação | Facilita reuso das validações em múltiplos testes e leitura dos casos de teste |
| **utils/functions/** | Helpers de UI e de pré-condição (`ensure_required_contacts`, `ensure_on_home`, long-press, back, fechar diálogo de conta) | Isola setup reutilizável e reduz duplicação entre módulos de teste |
| **fixtures/** | Define o `driver` (sessão Appium) e instâncias de Page Objects/Validators com escopo `session` | Sessão única de app por execução — ver seção de observações abaixo |
| **tests/** | Casos de teste organizados por fluxo e numerados (`1_home`, `2_create`, `3_update`, `4_delete`) | Update e delete garantem os próprios contatos via fixtures/helpers; a numeração organiza a suíte, sem impor ordem obrigatória |

---

## ✅ Cobertura de testes

### `test_1_home_empety.py` — Home vazia
- Validação de elementos da tela inicial sem contatos (título, ícone, mensagem, botões "Adicionar conta" e "Importar").

### `test_2_create_contact.py` — Criação de contato
- Cancelamento de criação com formulário vazio;
- Cancelamento com campos preenchidos (fluxo de diálogo de confirmação de descarte);
- Tentativa de salvar formulário vazio (deve falhar);
- Validação de placeholders da tela de criação;
- Seleção de tipo de telefone/e-mail (Celular, Comercial, Casa) — parametrizado;
- Autofoco no campo "Nome" ao abrir a tela;
- Criação com dados parciais (somente nome / somente telefone / somente e-mail) — parametrizado;
- Criação com todos os campos preenchidos.

### `test_3_update_contact.py` — Atualização de contato
- Fixture de módulo garante os contatos necessários antes da suíte (`ensure_required_contacts_for_update`);
- Adicionar sobrenome, telefone, e-mail e nome a contatos com dados incompletos;
- Editar nome, sobrenome e telefone de um contato já completo;
- Validação da persistência dos dados na lista e na tela de detalhes após cada edição;
- Pós-condição: cada teste retorna à home de Contatos.

### `test_4_delete_contact.py` — Exclusão de contato
- Pré-condições criam apenas os contatos usados por cada cenário (`ensure_required_contacts_for_delete`);
- Ícone de exclusão oculto sem seleção;
- Seleção via long-press, contador de seleção múltipla, desmarcação e cancelamento do modo de seleção;
- Cancelar exclusão via diálogo (contato deve permanecer);
- Confirmar exclusão individual e em lote;
- Exclusão a partir da tela de detalhes (via menu "Mais opções" → "Excluir"), com fluxo de cancelar e de confirmar;
- Validação de exibição/fechamento do menu de opções ("Vincular", "Excluir", "Compartilhar", "Criar atalho", "Definir toque").

---

## 🔧 Stack técnica

| Ferramenta | Uso |
|---|---|
| **Python 3.11** | Linguagem base |
| **Pytest** | Test runner |
| **Appium-Python-Client** | Driver de automação mobile (protocolo WebDriver) |
| **Selenium** | `WebDriverWait` / `expected_conditions` para esperas explícitas |
| **Allure (allure-pytest)** | Relatório de execução, com `@allure.feature`, `@allure.story`, `@allure.step` |
| **UiAutomator2** | Automation engine do Appium para Android |
| **GitHub Actions + reactivecircus/android-emulator-runner** | CI com emulador Android real (AVD) |

Dependências completas em [`requirements.txt`](./requirements.txt).

---

## ▶️ Como executar localmente

### Pré-requisitos
- Python 3.11+
- Node.js 18+ (para o Appium)
- Android SDK configurado, com um emulador ou dispositivo físico disponível
- App de Contatos nativo instalado e com permissões `READ_CONTACTS`/`WRITE_CONTACTS` concedidas

### Passo a passo

```bash
# 1. Instalar dependências Python
pip install -r requirements.txt

# 2. Instalar o Appium e o driver do Android
npm install -g appium
appium driver install uiautomator2

# 3. Subir o servidor Appium
appium

# 4. Em outro terminal, garantir que o emulador/dispositivo esteja ativo
adb devices

# 5. Rodar os testes
pytest tests/ --alluredir=allure-results -v

# 6. (Opcional) Gerar e visualizar o relatório Allure
allure serve allure-results
```

> A fixture `driver` está configurada com `appium:udid: "emulator-5554"` e idioma `pt-BR` fixos (`fixtures/driver_fixtures.py`). Para rodar em outro dispositivo/emulador, ajuste esse capability antes da execução.

---

## 🤖 Pipeline de CI/CD

O workflow [`appium-tests.yml`](./.github/workflows/appium-tests.yml) automatiza toda a execução em GitHub Actions:

1. Sobe um emulador Android (API 31, `google_apis`, `x86_64`, perfil `pixel_6`) com locale pt-BR;
2. Usa **cache de AVD com snapshot** para acelerar execuções subsequentes;
3. Concede as permissões de contatos via `adb shell pm grant`;
4. Instala Appium + driver UiAutomator2;
5. Executa a suíte via `pytest` com saída em `--junitxml` e `--alluredir`;
6. Gera relatório Allure e publica no **GitHub Pages** (branch `gh-pages`).

Disparado em `push`/`pull_request` para `main`, e também via `workflow_dispatch` com input opcional `test_path` (permite rodar um subconjunto específico de testes manualmente).

---

## 🔍 Observações e recomendações de QA

Pontos de atenção para evolução da suíte:

1. **Uso de `time.sleep()` fixo:** diversos testes ainda usam `time.sleep(1)`/`time.sleep(2)`/`time.sleep(3)` para aguardar transições de tela ou sincronização de toast. Waits fixos deixam a suíte mais lenta e ainda assim instável. Preferir `WebDriverWait` com `expected_conditions` específicas (ex.: presença do novo elemento, retorno à home).

2. **Retry / polling de lista:** em exclusão, há esperas com polling para confirmar remoção dos nomes na lista. Essa lógica funciona, mas o ideal é concentrá-la em helpers/Page Objects (como em `get_all_contact_names()` com tratamento de `StaleElementReferenceException`), em vez de espalhar sleeps nos testes.

3. **Escopo de fixtures `session`:** `driver` e Page Objects usam escopo `session` com `noReset: True` — o app não reinicia entre testes. Isso melhora performance; o estado da agenda é gerenciado pelas pré-condições de update/delete, mas limpeza explícita entre módulos ainda pode ser útil para execuções parciais e paralelização futura.

4. **Cobertura futura sugerida:**
   - Validação com caracteres especiais/emoji no nome;
   - Testes negativos de formato de e-mail/telefone inválidos;
   - Rotação de tela e app em background/foreground (estado de formulário preservado);
   - Acessibilidade (TalkBack) nos principais fluxos.

---

## 📄 Licença

Distribuído sob licença MIT — ver [`LICENSE`](./LICENSE).
