# Robot Framework Xray

Biblioteca Xray, envie seu relatorio de execução para Jira de forma simples e descomplicada.

## Instalação

```bash
pip install robotframework-xray
```

É necessário possuir a versão do Python >= 3.8 & <= 3.12, junto com o gerenciador de pacotes pip.

### Configuração no projeto

> [!NOTE]
> Necessário configurar na variaveis de ambiente ou no arquivo .env de seu projeto seguintes chaves:

```
# Valores são meramente ilustrativos
XRAY_DEBUG = false
PROJECT_KEY = XSE
TEST_PLAN = XSE-135
XRAY_API = https://xray.cloud.getxray.app/api/v2
XRAY_CLIENT_ID = 52861E2E5516439A854E8CD0B3B0126F
XRAY_CLIENT_SECRET = f4730cd0e9253ff57a636d093176245265fft9a05d1074f0
CUCUMBER_PATH = C:/Projetos/robotframework-xray
```

### Configurações no Jira

É necessário o uso de **_Test Plan_** e vincular seus **_Xray Test_** ao mesmo.

Lembrando que seu **_Xray Test_** no **_Jira_** precisa estar configurado com seguinte **_Test Type_** como **_Cucumber_**.

## Exemplo de uso

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

Apenas escritas com palavras **_Given_**, **_When_**, **_Then_**, **_And_** e **_But_** serão exibidas no relatório do Jira e as demais serão ignoradas,
