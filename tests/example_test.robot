*** Settings ***
Documentation    Test scenarios for example.
Library     Xray
Library     SeleniumLibrary        run_on_failure=Capture Page Screenshot       screenshot_root_directory=EMBED
Library     ScreenCapLibrary

*** Tasks ***
Click for JS Alert
    [Documentation]    Click for JS Alert
    [Tags]      KT-1        Example1
    Given Vou para The Internet
    When Abro o alerta
    Then Valido a mensagem

*** Keywords ***
Vou para The Internet
    Start Video Recording
    Open Browser    browser=chrome
    Maximize Browser Window
    Set Selenium Speed    value=0.3
    Go To    url=https://the-internet.herokuapp.com/javascript_alerts
    Wait Until Element Is Visible    locator=tag:body
    Title Should Be    title=The Internet
    Capture Page Screenshot

Abro o alerta
    Click Button    locator=xpath://*[@id="content"]/div/ul/li[1]/button
    Handle Alert    action=ACCEPT

Valido a mensagem
    Wait Until Element Contains    locator=id:result    text=You successfully clicked an alert
    Close Browser
    Stop Video Recording