*** Settings ***
Documentation    Automation test for Desktop.

# Library    ../src/Xray/ListenerV2.py
Library    Xray
Library    Screenshot

*** Test Cases ***
Execute automation test for Desktop
    [Tags]    XSP-58    example3
    Given Log To Console    message=Essa é uma mensagem de início
    When Take Screenshot Without Embedding
    Then Log To Console    message=Essa é uma mensagem de fim