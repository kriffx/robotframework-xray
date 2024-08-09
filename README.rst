Robot Framework
===============

.. contents::
   :local:

Introduction
------------



Installation
------------

If you already have Python with `pip <https://pip.pypa.io>`_ installed,
you can simply run::

    pip install robotframework-xray

For more detailed installation instructions, including installing Python, see
`<INSTALL.rst>`__.

Example
-------

Below is a simple example test case for testing login to some system.

.. code:: robotframework

    *** Settings ***
    Documentation     A test suite with a single test for valid login.
    ...
    ...               This test has a workflow that is created using keywords in
    ...               the imported resource file.
    Library           Xray

    *** Test Cases ***
    Valid Login
        [Tags]    EXE-123
        Open Browser To Login Page
        Input Username    demo
        Input Password    mode
        Submit Credentials
        Welcome Page Should Be Open
        [Teardown]    Close Browser

Usage
-----

.. code:: robotframework

    *** Settings ***
    Library           Xray

It is necessary to set the following parameters in the system variables or in the .env file:

XRAY_DEBUG = false # true/false
PROJECT_KEY = EXE # Project Key
XRAY_API = https://xray.cloud.getxray.app/api/v2
XRAY_CLIENT_ID = F55438AAACD34B4A921DAA0010957CA0
XRAY_CLIENT_SECRET = 57e5bb417c10d4ee152d77a424a2511e3866ea952bccced3b05c2b04ffa67eff
CUCUMBER_PATH = /projects/

In Jira create an Xray Test and set the TEST-TYPE to Cucumber.