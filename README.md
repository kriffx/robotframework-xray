# Robot Framework Xray

Biblioteca Xray, envie seu relatorio de execução para Jira de forma simples e descomplicada.

## Instalação

```bash
pip install robotframework-xray
```

Obviamente é necessário possuir a versão do Python >= 3.8 e <= 3.12, junto com o gerenciador de pacotes pip do Python.

## Exemplo de uso

<details>
    <summary>Importante (Leia-me)</summary>
    > [!Importante]
    > Necessário configurar na variaveis de ambiente ou no arquivo .env de seu projeto seguintes chaves:
    ```text
    # Valores são meramente ilustrativos
    XRAY_DEBUG = false
    PROJECT_KEY = XSE
    TEST_PLAN = XSE-135
    XRAY_API = https://xray.cloud.getxray.app/api/v2
    XRAY_CLIENT_ID = 52861E2E5516439A854E8CD0B3B0126F
    XRAY_CLIENT_SECRET = f4730cd0e9253ff57a636d093176245265fft9a05d1074f0
    CUCUMBER_PATH = C:/Projetos/robotframework-xray
    ```
</details>

```robotframework
*** Settings ***
Documentation    Xray Library Test Automation
Library    Xray

*** Test Cases ***
Search for the Robot Framework Xray library in the PyPi repository
    [Tags]    XSE-60
    Given I go to PyPi
    When I search on PyPi
    Then I preview the result
    And I close the browser
```

Para mais detalhes, acesse a pasta [**_tests_**](https://github.com/kriffx/robotframework-xray/tree/main/tests) da biblioteca e veja alguns exemplos de implementação.
