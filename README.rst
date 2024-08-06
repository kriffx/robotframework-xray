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

