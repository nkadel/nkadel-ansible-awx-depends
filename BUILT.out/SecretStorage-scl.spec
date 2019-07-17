%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name SecretStorage
%define version 2.3.1
%define unmangled_version 2.3.1
%define unmangled_version 2.3.1
%define release 1

Summary: Python bindings to FreeDesktop.org Secret Service API
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}SecretStorage
Version: %{version}
Release: %{release}
Source0: SecretStorage-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/SecretStorage-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Dmitry Shachnev <mitya57@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/mitya57/secretstorage


%description

.. image:: https://api.travis-ci.org/mitya57/secretstorage.svg
   :target: https://travis-ci.org/mitya57/secretstorage
   :alt: Travis CI status

Module description
==================

This module provides a way for securely storing passwords and other secrets.

It uses D-Bus `Secret Service`_ API that is supported by GNOME Keyring
(since version 2.30) and KSecretsService.

The main classes provided are ``secretstorage.Item``, representing a secret
item (that has a *label*, a *secret* and some *attributes*) and
``secretstorage.Collection``, a place items are stored in.

SecretStorage supports most of the functions provided by Secret Service,
including creating and deleting items and collections, editing items,
locking and unlocking collections (asynchronous unlocking is also supported).

The documentation can be found on `secretstorage.readthedocs.io`_.

.. _`Secret Service`: https://specifications.freedesktop.org/secret-service/
.. _`secretstorage.readthedocs.io`: https://secretstorage.readthedocs.io/en/latest/

Building the module
===================

.. note::
   SecretStorage supports Python 2.7 and all versions of Python since 3.3.
   Here we assume that your Python version is 3.x.

SecretStorage requires these packages to work:

* `dbus-python`_
* `python-cryptography`_

To build SecretStorage, use this command::

   python3 setup.py build

If you have Sphinx_ installed, you can also build the documentation::

   python3 setup.py build_sphinx

.. _`dbus-python`: https://www.freedesktop.org/wiki/Software/DBusBindings/#dbus-python
.. _`python-cryptography`: https://pypi.python.org/pypi/cryptography
.. _Sphinx: http://sphinx-doc.org/

Testing the module
==================

First, make sure that you have the Secret Service daemon installed.
The `GNOME Keyring`_ is the reference server-side implementation for the
Secret Service specification.

.. _`GNOME Keyring`: https://download.gnome.org/sources/gnome-keyring/

Then, start the daemon and unlock the ``default`` collection, if needed.
The testsuite will fail to run if the ``default`` collection exists and is
locked. If it does not exist, the testsuite can also use the temporary
``session`` collection, as provided by the GNOME Keyring.

Then, run the Python unittest module::

   python3 -m unittest discover -s tests

If you want to run the tests in an isolated or headless environment, run
this command in a D-Bus session::

   dbus-run-session -- python3 -m unittest discover -s tests

Get the code
============

SecretStorage is available under BSD license. The source code can be found
on GitHub_.

.. _GitHub: https://github.com/mitya57/secretstorage



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n SecretStorage-%{unmangled_version} -n SecretStorage-%{unmangled_version}
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
