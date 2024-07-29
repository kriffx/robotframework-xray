*** Settings ***
Documentation    Google 2 Tests.
Resource    resources/web.resource

*** Test Cases ***
Search on Google 2
    [Tags]    KT-192    example2
    When Open Browser    url=https://www.google.com.br    browser=chrome
    Then Maximize Browser Window
    And Set Selenium Speed    value=0.3
    Then Input Text    locator=name:q    text=Microsoft    clear=True
    And Capture Page Screenshot
    And Close All Browsers

Search on Google 3
    [Tags]    XSP-65    example1
    [Setup]    Given Open chrome browser
    [Teardown]    And Close All Browsers
    When Search in Google    Microsoft