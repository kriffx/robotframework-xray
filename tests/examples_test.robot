*** Settings ***
Documentation    Xray Library Test Automation
Resource    resources/web.resource

*** Test Cases ***   
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

Test Logins with several username / password example line 19
    [Tags]    XSE-198
    [Template]    Scenario Outline Test Logins with several username / password
    gerencia    ara-8892-jef    Carnaval0101
    gerencia    ara-8892-jefY    Carnaval0101
    gerencia    ara-8892-jefY1    dsfdsgfds
    gerencia    ara-8892-jefY1    fdsgsdgd

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

Scenario Outline Test Logins with several username / password
    [Arguments]    ${menu}    ${username}    ${password}
    Given I am in the login page
    When I want to login     ${menu}         ${username}         ${password}    
    Then I want to see the Welcome page

I am in the login page
    I go to Google

I want to login
    [Arguments]    ${menu}    ${username}    ${password}
    Log to Console    ${menu} ${username} ${password}
    I search on Google    dbservices

I want to see the Welcome page
    I close the browser