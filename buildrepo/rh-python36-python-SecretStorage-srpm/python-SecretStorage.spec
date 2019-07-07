#
# spec file for package rh-python36-python-SecretStorage
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name SecretStorage

%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name python-%{pypi_name}}

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Common SRPM package
Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.3.1
Release:        0%{?dist}
Url:            https://github.com/mitya57/secretstorage
Summary:        Python bindings to FreeDesktop.org Secret Service API
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires:       %{?scl_prefix}python-dbus
Requires:       %{?scl_prefix}python-cryptography
%if %{with_dnf}
# Manually added for dbus-python
Suggests:       %{?scl_prefix}python-dbus-python
%endif # with_dnf

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
%setup -q -n %{pypi_name}-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
%{__python3} setup.py build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{?scl:EOF}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.3.1-0
= Update .spec file with py2pack
- Manually add Suggests for python-dbus-python
