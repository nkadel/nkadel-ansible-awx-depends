%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name keyring
%define version 15.1.0
%define unmangled_version 15.1.0
%define unmangled_version 15.1.0
%define release 1

Summary: Store and access your passwords safely.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}keyring
Version: %{version}
Release: %{release}
Source0: keyring-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/keyring-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jason R. Coombs <jaraco@jaraco.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/jaraco/keyring


%description
.. image:: https://img.shields.io/pypi/v/keyring.svg
   :target: https://pypi.org/project/keyring

.. image:: https://img.shields.io/pypi/pyversions/keyring.svg

.. image:: https://img.shields.io/travis/jaraco/keyring/master.svg
   :target: https://travis-ci.org/jaraco/keyring

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/keyring/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/keyring/branch/master

.. image:: https://readthedocs.org/projects/keyring/badge/?version=latest
   :target: https://keyring.readthedocs.io/en/latest/?badge=latest

=======================================
Installing and Using Python Keyring Lib
=======================================

.. contents:: **Table of Contents**

---------------------------
What is Python keyring lib?
---------------------------

The Python keyring lib provides an easy way to access the system keyring service
from python. It can be used in any application that needs safe password storage.

The keyring library is licensed under both the `MIT license
<http://opensource.org/licenses/MIT>`_ and the PSF license.

These recommended keyring backends are supported by the Python keyring lib:

* macOS `Keychain
  <https://en.wikipedia.org/wiki/Keychain_%28software%29>`_
* Freedesktop `Secret Service
  <http://standards.freedesktop.org/secret-service/>`_ supports many DE including 
  GNOME (requires `secretstorage <https://pypi.python.org/pypi/secretstorage>`_)
* KDE4 & KDE5 `KWallet <https://en.wikipedia.org/wiki/KWallet>`_
  (requires `dbus <https://pypi.python.org/pypi/dbus-python>`_)
* `Windows Credential Locker
  <https://docs.microsoft.com/en-us/windows/uwp/security/credential-locker>`_

Other keyring implementations are available through `Third-Party Backends`_.

-------------------------
Installation Instructions
-------------------------

Install from Index
==================

Install using your favorite installer. For example:

    $ pip install keyring

Linux
-----

On Linux, the recommended keyring relies on SecretStorage, which in
turn relies on dbus-python, but dbus-python does not install correctly
when using the Python installers, so dbus-python must be installed
as a system package. See `the SecretStorage GitHub repo
<https://github.com/mitya57/secretstorage>`_ for details.

-------------
Using Keyring
-------------

The basic usage of keyring is pretty simple: just call `keyring.set_password`
and `keyring.get_password`:

    >>> import keyring
    >>> keyring.set_password("system", "username", "password")
    >>> keyring.get_password("system", "username")
    'password'

Command-line Utility
====================

Keyring supplies a ``keyring`` command which is installed with the
package. After installing keyring in most environments, the
command should be available for setting, getting, and deleting
passwords. For more information on usage, invoke with no arguments
or with ``--help`` as so::

    $ keyring --help
    $ keyring set system username
    Password for 'username' in 'system':
    $ keyring get system username
    password

The command-line functionality is also exposed as an executable
package, suitable for invoking from Python like so::

    $ python -m keyring --help
    $ python -m keyring set system username
    Password for 'username' in 'system':
    $ python -m keyring get system username
    password

--------------------------
Configure your keyring lib
--------------------------

The python keyring lib contains implementations for several backends. The
library will
automatically choose the keyring that is most suitable for your current
environment. You can also specify the keyring you like to be used in the
config file or by calling the ``set_keyring()`` function.

Customize your keyring by config file
=====================================

This section describes how to change your option in the config file.

Config file path
----------------

The configuration of the lib is stored in a file named "keyringrc.cfg". This
file must be found in a platform-specific location. To determine
where the config file is stored, run the following::

    python -c "import keyring.util.platform_; print(keyring.util.platform_.config_root())"

Some keyrings also store the keyring data in the file system. To determine
where the data files are stored, run this command::

    python -c "import keyring.util.platform_; print(keyring.util.platform_.data_root())"


Config file content
-------------------

To specify a keyring backend, set the **default-keyring** option to the
full path of the class for that backend, such as
``keyring.backends.OS_X.Keyring``.

If **keyring-path** is indicated, keyring will add that path to the Python
module search path before loading the backend.

For example, this config might be used to load the SimpleKeyring from the demo
directory in the project checkout::

    [backend]
    default-keyring=simplekeyring.SimpleKeyring
    keyring-path=/home/kang/pyworkspace/python-keyring-lib/demo/

Third-Party Backends
====================

In addition to the backends provided by the core keyring package for
the most common and secure use cases, there
are additional keyring backend implementations available for other
use-cases. Simply install them to make them available:

- `keyrings.cryptfile <https://pypi.org/project/keyrings.cryptfile>`_
  - Encrypted text file storage.
- `keyring_jeepney <https://pypi.org/project/keyring_jeepney>`__ - a
  pure Python backend using the secret service DBus API for desktop
  Linux.
- `keyrings.alt <https://pypi.org/project/keyrings.alt>`_ - "alternate",
  possibly-insecure backends, originally part of the core package, but
  available for opt-in.
- `gsheet-keyring <https://pypi.org/project/gsheet-keyring>`_
  - a backend that stores secrets in a Google Sheet. For use with
  `ipython-secrets <https://pypi.org/project/ipython-secrets>`_.

Write your own keyring backend
==============================

The interface for the backend is defined by ``keyring.backend.KeyringBackend``.
Every backend should derive from that base class and define a ``priority``
attribute and three functions: ``get_password()``, ``set_password()``, and
``delete_password()``.

See the ``backend`` module for more detail on the interface of this class.

Keyring employs entry points to allow any third-party package to implement
backends without any modification to the keyring itself. Those interested in
creating new backends are encouraged to create new, third-party packages
in the ``keyrings`` namespace, in a manner modeled by the `keyrings.alt
package <https://github.com/jaraco/keyrings.alt>`_. See the ``setup.py`` file
in that project for a hint on how to create the requisite entry points.
Backends that prove essential may be considered for inclusion in the core
library, although the ease of installing these third-party packages should
mean that extensions may be readily available.

If you've created an extension for Keyring, please submit a pull request to
have your extension mentioned as an available extension.

Set the keyring in runtime
==========================

Keyring additionally allows programmatic configuration of the
backend calling the api ``set_keyring()``. The indicated backend
will subsequently be used to store and retrieve passwords.

Here's an example demonstrating how to invoke ``set_keyring``::

    # define a new keyring class which extends the KeyringBackend
    import keyring.backend

    class TestKeyring(keyring.backend.KeyringBackend):
        """A test keyring which always outputs same password
        """
        priority = 1

        def set_password(self, servicename, username, password):
            pass

        def get_password(self, servicename, username):
            return "password from TestKeyring"

        def delete_password(self, servicename, username, password):
            pass

    # set the keyring for keyring lib
    keyring.set_keyring(TestKeyring())

    # invoke the keyring lib
    try:
        keyring.set_password("demo-service", "tarek", "passexample")
        print("password stored successfully")
    except keyring.errors.PasswordSetError:
        print("failed to store password")
    print("password", keyring.get_password("demo-service", "tarek"))


Using Keyring on Ubuntu 16.04
=============================

The following is a complete transcript for installing keyring in a
virtual environment on Ubuntu 16.04.  No config file was used.::

  $ sudo apt install python3-venv libdbus-glib-1-dev
  $ cd /tmp
  $ pyvenv py3
  $ source py3/bin/activate
  $ pip install -U pip
  $ pip install secretstorage dbus-python
  $ pip install keyring
  $ python
  >>> import keyring
  >>> keyring.get_keyring()
  <keyring.backends.SecretService.Keyring object at 0x7f9b9c971ba8>
  >>> keyring.set_password("system", "username", "password")
  >>> keyring.get_password("system", "username")
  'password'


Using Keyring on headless Linux systems
=======================================

It is possible to use the SecretService backend on Linux systems without
X11 server available (only D-Bus is required). To do that, you need the
following:

* Install the `GNOME Keyring`_ daemon.
* Start a D-Bus session, e.g. run ``dbus-run-session -- sh`` and run
  the following commands inside that shell.
* Run ``gnome-keyring-daemon`` with ``--unlock`` option. The description of
  that option says:

      Read a password from stdin, and use it to unlock the login keyring
      or create it if the login keyring does not exist.

  When that command is started, enter your password into stdin and
  press Ctrl+D (end of data). After that the daemon will fork into
  background (use ``--foreground`` option to prevent that).
* Now you can use the SecretService backend of Keyring. Remember to
  run your application in the same D-Bus session as the daemon.

.. _GNOME Keyring: https://wiki.gnome.org/Projects/GnomeKeyring

-----------------------------------------------
Integrate the keyring lib with your application
-----------------------------------------------

API interface
=============

The keyring lib has a few functions:

* ``get_keyring()``: Return the currently-loaded keyring implementation.
* ``get_password(service, username)``: Returns the password stored in the
  active keyring. If the password does not exist, it will return None.
* ``set_password(service, username, password)``: Store the password in the
  keyring.
* ``delete_password(service, username)``: Delete the password stored in
  keyring. If the password does not exist, it will raise an exception.

In all cases, the parameters (``service``, ``username``, ``password``)
should be Unicode text. On Python 2, these parameters are accepted as
simple ``str`` in the default encoding as they will be implicitly
decoded to text. Some backends may accept ``bytes`` for these parameters,
but such usage is discouraged.


Exceptions
==========

The keyring lib raises following exceptions:

* ``keyring.errors.KeyringError``: Base Error class for all exceptions in keyring lib.
* ``keyring.errors.InitError``: Raised when the keyring can't be initialized.
* ``keyring.errors.PasswordSetError``: Raise when password can't be set in the keyring.
* ``keyring.errors.PasswordDeleteError``: Raised when the password can't be deleted in the keyring.

------------
Get involved
------------

Python keyring lib is an open community project and highly welcomes new
contributors.

* Repository: https://github.com/jaraco/keyring/
* Bug Tracker: https://github.com/jaraco/keyring/issues/
* Mailing list: http://groups.google.com/group/python-keyring

Making Releases
===============

This project makes use of automated releases via Travis-CI. The
simple workflow is to tag a commit and push it to Github. If it
passes tests on a late Python version, it will be automatically
deployed to PyPI.

Other things to consider when making a release:

 - first ensure that tests pass (preferably on Windows and Linux)
 - check that the changelog is current for the intended release

Running Tests
=============

Tests are `continuously run <https://travis-ci.org/#!/jaraco/keyring>`_ using
Travis-CI.

To run the tests yourself, you'll want keyring installed to some environment
in which it can be tested. Recommended technique is described below.

Using tox
---------

Keyring prefers use of `tox <https://pypi.org/project/tox>`_ to run tests.
Simply install and invoke ``tox``.

This technique is the one used by the Travis-CI script.

----------
Background
----------

The project was based on Tarek Ziade's idea in `this post`_. Kang Zhang
initially carried it out as a `Google Summer of Code`_ project, and Tarek
mentored Kang on this project.

.. _this post: http://tarekziade.wordpress.com/2009/03/27/pycon-hallway-session-1-a-keyring-library-for-python/
.. _Google Summer of Code: http://socghop.appspot.com/


.. image:: https://badges.gitter.im/jaraco/keyring.svg
   :alt: Join the chat at https://gitter.im/jaraco/keyring
   :target: https://gitter.im/jaraco/keyring?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n keyring-%{unmangled_version} -n keyring-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
