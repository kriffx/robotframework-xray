*** Settings ***
Library    SeleniumLibrary    run_on_failure=Capture Page Screenshot    screenshot_root_directory=EMBED
Library    Xray
# Library    ../src/Xray/ListenerV2.py

*** Test Cases ***
Adicionar produto no carrinho
    [Tags]    XSP-105
    [Teardown]    Close All Browsers
    Given I access the Pingo Doce store
    And Capture Page Screenshot    filename=EMBED
    And I accept cookies
    When I set my location
    Then I do a product search
    And I select the product
    And I add product to cart

*** Keywords ***
I access the Pingo Doce store
    Open Browser    url=https://mercadao.pt/store/pingo-doce     browser=chrome
    Maximize Browser Window
    Set Selenium Speed    value=0.3

I accept cookies
    Wait Until Element Is Visible    locator=id:onetrust-accept-btn-handler
    Click Button    locator=id:onetrust-accept-btn-handler

I set my location
    Click Element    locator=xpath://div[2]/pdo-container/ul/li[2]/pdo-navbar-top/div/ul[2]/li[3]/a
    Wait Until Element Is Visible    locator=id:postalCode
    Input Text    locator=id:postalCode    text=4560-132    clear=True
    Capture Page Screenshot    filename=EMBED
    Click Button    locator=xpath://pdo-enter-postal-code//button

I do a product search
    Input Text    locator=xpath://pdo-navbar-right//input[@id='search']    text=Tablete de Chocolate Teasers Malteasers    clear=True
    Capture Page Screenshot    filename=EMBED
    Press Keys    None    ENTER

I select the product
    Wait Until Element Is Visible    locator=xpath://pdo-product-item[1]//h3
    ${PRODUCT_TITLE}=    Get Text    locator=xpath://pdo-product-item[1]//h3
    Should Be Equal    first=Tablete de Chocolate Teasers Malteasers    second=${PRODUCT_TITLE}
    Capture Page Screenshot
    Click Element    locator=xpath://pdo-product-item[1]//h3

I add product to cart
    Wait Until Element Is Visible    locator=xpath://pdo-cart-button/button
    Capture Page Screenshot    filename=EMBED
    Click Button    locator=xpath://pdo-cart-button/button
    Wait Until Element Is Not Visible    locator=xpath://pdo-cart-button/button