*** Settings ***
Library    SeleniumLibrary    run_on_failure=Capture Page Screenshot    screenshot_root_directory=EMBED
Library    ../../src/Xray/ListenerV2.py

*** Keywords ***
Set basic settings
    Maximize Browser Window
    Set Selenium Speed    value=0.3

I go to Google
    Open Browser    url=https://www.google.com.br    browser=headlesschrome
    Set basic settings

I go to PyPi
    Open Browser    url=https://pypi.org    browser=headlesschrome
    Set basic settings

I search on Google
    [Arguments]    ${text}
    Input Text    locator=name:q    text=${text}    clear=True
    Sleep   time_=5
    Page screenshot

Page screenshot
    Capture Page Screenshot    filename=EMBED

I close the browser
    Close All Browsers