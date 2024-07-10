*** Settings ***
Documentation       Test scenarios for Google.

Library             SeleniumLibrary    run_on_failure=Capture Page Screenshot    screenshot_root_directory=EMBED
Library             Xray

*** Test Cases ***
Example 3
    [Documentation]    Google page screenshot
    [Tags]             KT-46    google3
    Given Open Browser                   browser=headless chrome
     When Maximize Browser Window
     Then Set Selenium Speed             value=0.3
      and Go To                          url=https://www.google.com.br
      and Wait Until Element Is Visible  locator=tag:body
      and Title Should Be                title=Google
      and Capture Page Screenshot
      and Close Browser
      