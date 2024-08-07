Installation instructions
=========================

These instructions cover installing `robotframework-xray <https://github.com/kriffx/robotframework-xray>`_
and its preconditions on different operating systems. If you already have
`python <http://python.org>`_ and `robotframework <https://robotframework.org>`_ installed, you can install Robot Framework using
the standard package manager `pip <https://pip.pypa.io>`_::

    pip install robotframework-xray

.. contents::
   :depth: 2
   :local:

.. START USER GUIDE IGNORE
.. Installation instructions are included also in the User Guide.
.. Following content is excluded when the UG is built.
.. default-role:: code
.. role:: file(emphasis)
.. role:: option(code)
.. END USER GUIDE IGNORE

Python installation
-------------------

`Xray Library`_ is implemented using Python_, and a precondition to install it
is having Python or its alternative implementation `PyPy <https://pypy.org>`_
installed. Another recommended precondition is having the pip_ package manager
available.

Xray Library requires Python 3.8 or newer. The latest version that supports
Python 3.6 and 3.7 is `Xray Library 4.3.0`__.

__ https://github.com/kriffx/robotframework-xray/blob/v4.3.0/INSTALL.rst

Installing Python on Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~

On Linux you should have suitable Python installation with pip_ available
by default. If not, you need to consult your distributions documentation
to learn how to install them. This is also true if you want to use some other
Python version than the one provided by your distribution by default.

To check what Python version you have installed, you can run `python --version`
command in a terminal:

.. code:: bash

  $ python --version
  Python 3.10.13

Notice that if your distribution provides also older Python 2, running `python`
may use that. To use Python 3, you can use `python3` command or even more version
specific command like `python3.8`. You need to use these version specific variants
also if you have multiple Python 3 versions installed and need to pinpoint which
one to use:

.. code:: bash

  $ python3.11 --version
  Python 3.11.7
  $ python3.12 --version
  Python 3.12.1

Installing Robot Framework directly under the system provided Python
has a risk that possible problems can affect the whole Python installation
used also by the operating system itself. Nowadays
Linux distributions typically use `user installs`__ by default to avoid such
problems, but users can also themselves decide to use `virtual environments`_.

__ https://pip.pypa.io/en/stable/user_guide/#user-installs

Installing Python on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Windows Python is not available by default, but it is easy to install.
The recommended way to install it is using the official Windows installers available
at http://python.org. For other alternatives, such as installing from the
Microsoft Store, see the `official Python documentation`__.

When installing Python on Windows, it is recommended to add Python to PATH_
to make it and tools like pip and Robot Framework easier to execute from
the command line. When using the `official installer`__, you just need
to select the `Add Python 3.x to PATH` checkbox on the first dialog.

To make sure Python installation has been successful and Python has been
added to `PATH`, you can open the command prompt and execute `python --version`:

.. code:: batch

  C:\>python --version
  Python 3.10.9

If you install multiple Python versions on Windows, the version that is used
when you execute `python` is the one first in `PATH`. If you need to use others,
the easiest way is using the `py launcher`__:

.. code:: batch

  C:\>py --version
  Python 3.10.9
  C:\>py -3.12 --version
  Python 3.12.1

__ https://docs.python.org/3/using/windows.html
__ https://docs.python.org/3/using/windows.html#windows-full
__ https://docs.python.org/3/using/windows.html#launcher

Installing Python on macOS
~~~~~~~~~~~~~~~~~~~~~~~~~~

MacOS does not provide Python 3 compatible Python version by default, so it
needs to be installed separately. The recommended  approach is using the official
macOS installers available at http://python.org. If you are using a package
manager like `Homebrew <https://brew.sh/>`_, installing Python via it is
possible as well.

You can validate Python installation on macOS using `python --version` like on
other operating systems.

PyPy installation
~~~~~~~~~~~~~~~~~

PyPy_ is an alternative Python implementation. Its main advantage over the
standard Python implementation is that it can be faster and use less memory,
but this depends on the context where and how it is used. If execution speed
is important, at least testing PyPy is probably a good idea.

Installing PyPy is a straightforward procedure and you can find both installers
and installation instructions at http://pypy.org. To validate that PyPy installation
was successful, run `pypy --version` or `pypy3 --version`.

.. note:: Using Robot Framework with PyPy is officially supported only on Linux.

Configuring `PATH`
~~~~~~~~~~~~~~~~~~

The `PATH environment variable`__ lists directories where commands executed in
a system are searched from. To make using Python, pip_ and Robot Framework easier
from the command line, it is recommended to add the Python installation directory
as well as the directory where commands like `pip` and `robot` are installed
into `PATH`.

__ https://en.wikipedia.org/wiki/PATH_(variable)

When using Python on Linux or macOS, Python and tools installed with it should be
automatically in `PATH`. If you nevertheless need to update `PATH`, you
typically need to edit some system wide or user specific configuration file.
Which file to edit and how depends on the operating system and you need to
consult its documentation for more details.

On Windows the easiest way to make sure `PATH` is configured correctly is
setting the `Add Python 3.x to PATH` checkbox when `running the installer`__.
To manually modify `PATH` on Windows, follow these steps:

1. Find `Environment Variables` under `Settings`. There are variables affecting
   the whole system and variables affecting only the current user. Modifying
   the former will require admin rights, but modifying the latter is typically
   enough.

2. Select `PATH` (often written like `Path`) and click `Edit`. If you are
   editing user variables and `PATH` does not exist, click `New` instead.

3. Add both the Python installation directory and the :file:`Scripts` directory
   under the installation directory into `PATH`.

4. Exit the dialog with `Ok` to save the changes.

5. Start a new command prompt for the changes to take effect.

__ https://docs.python.org/3/using/windows.html#the-full-installer

Installing using pip
--------------------

These instructions cover installing Robot Framework using pip_, the standard
Python package manager. If you are using some other package manager like
`Conda <https://conda.io>`_, you can use it instead but need to study its
documentation for instructions.

When installing Python, you typically get pip installed automatically. If
that is not the case, you need to check the documentation of that Python
installation for instructions how to install it separately.

Running `pip` command
~~~~~~~~~~~~~~~~~~~~~

Typically you use pip by running the `pip` command, but on Linux you may need
to use `pip3` or even more Python version specific variant like `pip3.8`
instead. When running `pip` or any of its variants, the pip version that is
found first in PATH_ will be used. If you have multiple Python versions
installed, you may need to pinpoint which exact version you want to use.
This is typically easiest done by running `python -m pip` and substituting
`python` with the Python version you want to use.

To make sure you have pip available, you can run `pip --version` or equivalent.

Examples on Linux:

.. code:: bash

  $ pip --version
  pip 23.2.1 from ... (python 3.10)
  $ python3.12 -m pip --version
  pip 23.3.1 from ... (python 3.12)

Examples on Windows:

.. code:: batch

  C:\> pip --version
  pip 23.2.1 from ... (python 3.10)
  C:\> py -m 3.12 -m pip --version
  pip 23.3.2 from ... (python 3.12)

In the subsequent sections pip is always run using the `pip` command. You may
need to use some of the other approaches explained above in your environment.

Installing and uninstalling Xray Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The easiest way to use pip is by letting it find and download packages it
installs from the `Python Package Index (PyPI)`__, but it can also install
packages downloaded from the PyPI separately. The most common usages are
shown below and pip_ documentation has more information and examples.

__ PyPI_

.. code:: bash

    # Install the latest version (does not upgrade)
    pip install robotframework-xray

    # Upgrade to the latest stable version
    pip install --upgrade robotframework-xray

    # Upgrade to the latest version even if it is a pre-release
    pip install --upgrade --pre robotframework-xray

    # Install a specific version
    pip install robotframework-xray==4.3.0

    # Install separately downloaded package (no network connection needed)
    pip install robotframework-xray-4.3.0-py3-none-any.whl

    # Install latest (possibly unreleased) code directly from GitHub
    pip install https://github.com/kriffx/robotframework-xray/archive/master.zip

    # Uninstall
    pip uninstall robotframework-xray

Installing from source
----------------------

Another installation alternative is getting Xray Library source code
and installing it using the provided `setup.py` script. This approach is
recommended only if you do not have pip_ available for some reason.

You can get the source code by downloading a source distribution as a zip
package from PyPI_ and extracting it. An alternative is cloning the GitHub_
repository and checking out the needed release tag.

Once you have the source code, you can install it with the following command:

.. code:: bash

   python setup.py install

The `setup.py` script accepts several arguments allowing, for example,
installation into a non-default location that does not require administrative
rights. It is also used for creating different distribution packages. Run
`python setup.py --help` for more details.

Virtual environments
--------------------

Python `virtual environments`__ allow Python packages to be installed in
an isolated location for a particular system or application, rather than
installing all packages into the same global location. They have
two main use cases:

- Install packages needed by different projects into their own environments.
  This avoids conflicts if projects need different versions of same packages.

- Avoid installing everything under the global Python installation. This is
  especially important on Linux where the global Python installation may be
  used by the distribution itself and messing it up can cause severe problems.

__ https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment

.. _PATH: `Configuring path`_
.. _PyPI: https://pypi.org/project/robotframework
.. _GitHub: https://github.com/kriffx/robotframework-xray