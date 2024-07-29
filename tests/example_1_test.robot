*** Settings ***
Documentation    Google 1 Tests.
Resource    resources/web.resource

*** Test Cases ***
Search on Google 1
    [Setup]    Given Open chrome browser
    [Teardown]    And Close All Browsers
    [Template]    Then Search in Google
    [Tags]    XSP-65    example1
    Apple Inc.
    Microsoft Corporation
    Alphabet Inc.

Search on Google 2
    [Tags]    XSP-65    example1
    Given Open chrome browser
    Then Search in Google    text=Apple Inc.
    Then Search in Google    text=Microsoft Corporation
    Then Search in Google    text=Alphabet Inc.
    And Close All Browsers