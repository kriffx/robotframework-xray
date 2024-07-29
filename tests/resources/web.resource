*** Settings ***
Library    SeleniumLibrary    run_on_failure=Capture Page Screenshot    screenshot_root_directory=EMBED
Library    Xray

*** Keywords ***
Open chrome browser
    Open Browser    url=https://www.google.com.br    browser=chrome    remote_url=http://localhost:4444/wd/hub
    Maximize Browser Window
    Set Selenium Speed    value=0.3

Search in Google
    [Arguments]    ${text}
    Capture Page Screenshot
    Input Text    locator=name:q    text=${text}    clear=True