*** Settings ***
Library    SeleniumLibrary    run_on_failure=Capture Page Screenshot    screenshot_root_directory=EMBED
Library    Xray
# Library    ../../src/Xray/ListenerV2.py

*** Keywords ***
Open chrome browser
    Open Browser    url=https://www.google.com.br    browser=chrome
    Maximize Browser Window
    Set Selenium Speed    value=0.3

Search in Google
    [Arguments]    ${text}
    Capture Page Screenshot    filename=EMBED
    Input Text    locator=name:q    text=${text}    clear=True
    Sleep   time_=10