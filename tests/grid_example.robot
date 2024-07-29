*** Settings ***
Library  SeleniumLibrary
Library  output_video_url.py
Library  Xray

*** Variables ***
${remote_url}       http://localhost:4444/wd/hub

*** Keywords ***
Open Test Page
    Open Browser    https://gridlastic.com/?demo
    ...    remote_url=${remote_url}
    ...    options=&{DESIRED}
    Maximize Browser Window
    Sleep    10s

*** Test Cases ***
Run Test
    [Tags]    XSP-65
    Given Open Test Page
    When output video url
    [Teardown]  Then Close Browser