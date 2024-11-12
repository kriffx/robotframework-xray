# Robot Framework Xray

Xray Library, send your execution report to Jira in a simple and straightforward way.

## Installation

```bash
pip install robotframework-xray
```

You must have Python version >= 3.8 & <= 3.12, along with the pip package manager.

### Project setup

> [!NOTE]
> You need to configure the following keys in the environment variables or in the .env file of your project:

```
# Values ​​are merely illustrative
XRAY_DEBUG = false
PROJECT_KEY = XSE
TEST_PLAN = XSE-135
XRAY_API = https://xray.cloud.getxray.app/api/v2
XRAY_CLIENT_ID = 52861E2E5516439A854E8CD0B3B0126F
XRAY_CLIENT_SECRET = f4730cd0e9253ff57a636d093176245265fft9a05d1074f0
CUCUMBER_PATH = C:/Projetos/robotframework-xray
```

### Jira setup

You must use **_Test Plan_** and link your **_Xray Test_** to it.

Remember that your **_Xray Test_** in **_Jira_** must be configured with the following **_Test Type_** as **_Cucumber_**.

## Usage example

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

For more details, access the [**_tests_**](https://github.com/kriffx/robotframework-xray/tree/main/tests) folder of the library and see some implementation examples.

Only the words **_Given_**, **_When_**, **_Then_**, **_And_** and **_But_** will be displayed in the Jira report and the others will be ignored,
