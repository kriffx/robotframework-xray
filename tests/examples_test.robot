*** Settings ***
Documentation    Xray Library Test Automation
Resource    resources/web.resource

*** Test Cases ***
Search for the three largest companies in the world
    [Setup]    Given I go to Google
    [Teardown]    And I close the browser
    [Template]    Then I search on Google
    [Tags]    XSE-59
    Apple Inc.
    Microsoft Corporation
    Alphabet Inc.
    
Search for the Robot Framework Xray library in the PyPi repository
    [Tags]    XSE-60
    Given I go to PyPi
    When I search on PyPi
    Then I preview the result
    And I close the browser

Run test with error
    [Tags]    XSE-99
    Given I go to Google
    When I search on Google    Python
    Then I do not exist
    And I close the browser

Fast test
    [Tags]    XSE-177
    Log to Console    test

*** Keywords ***
I search on PyPi
    Input Text    locator=id:search    text=robotframework-xray    clear=True
    Press Keys    None    ENTER
    I validate the search result

I validate the search result
    ${text}=    Get Text    locator=xpath://*[@id="content"]/div/div/div[2]/form/div[3]/ul/li[1]/a/h3/span[1]
    Should Be Equal As Strings    first=${text}    second=robotframework-xray
    Page screenshot

I preview the result
    Click Element    locator=xpath://*[@id="content"]/div/div/div[2]/form/div[3]/ul/li[1]/a/h3/span[1]
    Sleep   time_=5
    Page screenshot