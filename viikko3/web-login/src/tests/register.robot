*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  anna
    Set Password  anna1234
    Set Password Confirmation  anna1234
    Submit Registering Credentials
    Registering Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  anna1234
    Set Password Confirmation  anna1234
    Submit Registering Credentials
    Registering Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  anna
    Set Password  a1
    Set Password Confirmation  a1
    Submit Registering Credentials
    Registering Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
    Set Username  anna
    Set Password  annaanna
    Set Password Confirmation  annaanna
    Submit Registering Credentials
    Registering Should Fail With Message  Password should contain atleast two different types of characters


Register With Nonmatching Password And Password Confirmation
    Set Username  anna
    Set Password  annaSusanna123
    Set Password Confirmation  annaanna111
    Submit Registering Credentials
    Registering Should Fail With Message  Given passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  anna1234
    Set Password Confirmation  anna1234
    Submit Registering Credentials
    Registering Should Fail With Message  User with username kalle already exists

Login After Successful Registration
    Register With Valid Username And Password
    Logout After Registeration
    Logout Should Succeed
    Set Username  anna
    Set Password  anna1234
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Register With Unvalid Username And Password
    Click Link    Login
    Set Username  anna
    Set Password  anna1234
    Submit Login Credentials
    Login Should Fail With Message    Invalid username or password


*** Keywords ***

Register With Unvalid Username And Password
    Set Username  a
    Set Password  a
    Set Password Confirmation  a
    Submit Registering Credentials
    Registering Should Fail


Logout After Registeration
    Click Link  Continue to main page
    Click Button  Logout

Logout Should Succeed
    Title Should Be    Login

Register With Valid Username And Password
    Set Username  anna
    Set Password  anna1234
    Set Password Confirmation  anna1234
    Submit Registering Credentials
    Registering Should Succeed

Registering Should Fail
    Title Should Be    Register

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Login Credentials
    Click Button  Login


Submit Registering Credentials
    Click Button  Register

*** Keywords ***

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page