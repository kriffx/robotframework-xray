*** Settings ***
Documentation    Google 1 Tests.
Resource    resources/web.resource

*** Test Cases ***
Search on Google 1
    [Setup]    Given Open chrome browser
    [Teardown]    And Close All Browsers
    [Template]    Then Search in Google
    [Tags]    XSP-65    example1
    Apple Inc.
    Microsoft Corporation
    Alphabet Inc.
    
Search on Google 2
    [Tags]    XSP-65
    Given Open Browser    url=https://pypi.org/    browser=chrome
    Then Maximize Browser Window
    Then Set Selenium Speed    value=0.3
    Then Input Text    locator=id:search    text=robotframework-xray    clear=True
    Then Press Keys    None    ENTER
    ${text}=    Then Get Text    locator=xpath://*[@id="content"]/div/div/div[2]/form/div[3]/ul/li[1]/a/h3/span[1]
    Then Should Be Equal As Strings    first=${text}    second=robotframework-xray
    Then Click Element    locator=xpath://*[@id="content"]/div/div/div[2]/form/div[3]/ul/li[1]/a/h3/span[1]
    And Capture Page Screenshot    filename=EMBED
    And Close All Browsers