*** Settings ***
Documentation       Test scenarios for Google.

Library             SeleniumLibrary    run_on_failure=Capture Page Screenshot    screenshot_root_directory=EMBED
Library             ../src/Xray/ListenerV2.py

*** Test Cases ***
Google page test
    [Documentation]    Google page screenshot
    [Tags]    KT-1    google
    Open Browser    browser=chrome
    Maximize Browser Window
    Set Selenium Speed    value=0.3
    Go To    url=https://www.google.com.br
    Wait Until Element Is Visible    locator=tag:body
    Title Should Be    title=Google
    Capture Page Screenshot
    Close Browser

Google page test 2
    [Documentation]    Google page screenshot
    [Tags]    kt-2    google2
    [Setup]    Open Browser    browser=chrome
    Maximize Browser Window
    Set Selenium Speed    value=0.3
    Go To    url=https://www.google.com.br
    Wait Until Element Is Visible    locator=tag:body
    Title Should Be    title=Google
    Capture Page Screenshot
    [Teardown]    Close Browser
