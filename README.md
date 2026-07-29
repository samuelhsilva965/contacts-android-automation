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
│   ├── functions/                  # Helpers reutilizáveis (back, click_and_hold, fechar diálogos)
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
| **utils/functions/** | Funções auxiliares de baixo nível (long-press, back com delay, fechar diálogo condicional de "adicionar conta") | Reduz duplicação de tratamento de instabilidades de UI |
| **fixtures/** | Define o `driver` (sessão Appium) e instâncias de Page Objects/Validators com escopo `session` | Sessão única de app por execução — ver seção de riscos abaixo |
| **tests/** | Casos de teste organizados por fluxo e numerados (`1_home`, `2_create`, `3_update`, `4_delete`) | Numeração indica **dependência sequencial** entre suítes — ver seção de riscos |

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
- Adicionar sobrenome, telefone, e-mail e nome a contatos com dados incompletos;
- Editar nome, sobrenome e telefone de um contato já completo;
- Validação da persistência dos dados na lista e na tela de detalhes após cada edição.

### `test_4_delete_contact.py` — Exclusão de contato
- Ícone de exclusão oculto sem seleção;
- Seleção via long-press, contador de seleção múltipla, desmarcação e cancelamento do modo de seleção;
- Cancelar exclusão via diálogo (contato deve permanecer);
- Confirmar exclusão individual e em lote;
- Exclusão a partir da tela de detalhes (via menu "Mais opções" → "Excluir"), com fluxo de cancelar e de confirmar;
- Validação de exibição/fechamento do menu de opções ("Vincular", "Excluir", "Compartilhar", "Criar atalho", "Definir toque").

> ⚠️ **Nota de dependência entre testes:** os arquivos são numerados (`1`, `2`, `3`, `4`) e os testes de atualização/exclusão **reutilizam contatos criados em suítes anteriores** (ex.: `"Maria"`, `"Maria Silva"`, `"maria@gmail.com"`, `"(897) 451-5216"` são originados em `test_2_create_contact.py`). Isso significa que **a suíte não é independente por arquivo** — a execução parcial (ex.: rodar só `test_4`) tende a falhar por pré-condição ausente. Isso deve ser tratado como débito técnico (ver seção "Riscos e recomendações").

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

Como revisor(a), destaco os seguintes pontos de atenção para evolução da suíte:

1. **Independência de testes (isolamento):** os testes de update/delete dependem de estado deixado por testes de create. Recomenda-se migrar para fixtures de setup/teardown (`autouse`) que criem e limpem seus próprios dados, evitando ordem implícita de execução e permitindo paralelização futura.

2. **Uso de `time.sleep()` fixo:** diversos testes usam `time.sleep(1)`/`time.sleep(2)`/`time.sleep(3)` para aguardar transições de tela ou sincronização de toast. Isso é um anti-padrão clássico de automação (waits fixos tornam a suíte lenta e ainda assim instável). Onde possível, substituir por `WebDriverWait` com `expected_conditions` específicas (ex.: invisibilidade do toast anterior, presença do novo elemento).

3. **Retry manual embutido no teste** (`test_select_and_delete_contacts`, em `test_4_delete_contact.py`): há um laço de retry com `time.sleep(3)` dentro do próprio caso de teste para lidar com atraso de re-render da lista. Esse tipo de lógica de retry é mais apropriado na camada de Page Object (como já foi feito, corretamente, em `get_all_contact_names()` com tratamento de `StaleElementReferenceException`) do que espalhado pelos testes.

4. **Validação comentada em `test_delete_contact_from_detail`:** há uma verificação de "home vazia" comentada com a justificativa de comportamento não determinístico observado. Isso é um sinal de **flakiness conhecido e não resolvido** — deveria ser registrado como bug/débito técnico rastreável (ex.: issue no repositório) em vez de permanecer apenas como comentário no código, para não se perder o contexto.

5. **Escopo de fixtures `session`:** `driver`, `home_page`, `create_new_contact`, `new_contact_detail` e `home_with_contact` têm escopo `session`, ou seja, o app não é reiniciado entre testes (`noReset: True`). Isso é adequado para performance, mas reforça o ponto 1 — o estado do app é cumulativo entre todos os testes da sessão.

6. **Cobertura futura sugerida:**
   - Validação de campos obrigatórios com caracteres especiais/emoji no nome;
   - Testes negativos de formato de e-mail/telefone inválidos;
   - Testes de rotação de tela e app em background/foreground (estado de formulário preservado);
   - Testes de acessibilidade (TalkBack) para os principais fluxos.

---

## 📄 Licença

Distribuído sob licença MIT — ver [`LICENSE`](./LICENSE).
