#
# spec file for package rh-python36-python-bcrypt
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name bcrypt

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
Version:        3.1.4
Release:        0%{?dist}
Url:            https://github.com/pyca/bcrypt/
Summary:        Modern password hashing for your software and your servers
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added for compilation
BuildRequires:  %{?scl_prefix}python-cffi >= 1.1
BuildRequires:  libffi-devel
# Manually added
Requires:       %{?scl_prefix}python-cffi >= 1.1
Requires:       %{?scl_prefix}python-six >= 1.4.1
%if %{with_dnf}
#[tests]
Suggests:       %{?scl_prefix}python-pytest >= 3.2.1
%endif # with_dnf

%description
bcrypt
======

.. image:: https://img.shields.io/pypi/v/bcrypt.svg
    :target: https://pypi.python.org/pypi/bcrypt/
    :alt: Latest Version

.. image:: https://travis-ci.org/pyca/bcrypt.svg?branch=master
    :target: https://travis-ci.org/pyca/bcrypt

Modern password hashing for your software and your servers


Installation
============

To install bcrypt, simply:

.. code:: bash

    $ pip install bcrypt

Note that bcrypt should build very easily on Linux provided you have a C compiler, headers for Python (if you are not using pypy), and headers for the libffi libraries available on your system.

For Debian and Ubuntu, the following command will ensure that the required dependencies are installed:

.. code:: bash

    $ sudo apt-get install build-essential libffi-dev python-dev

For Fedora and RHEL-derivatives, the following command will ensure that the required dependencies are installed:

.. code:: bash

    $ sudo yum install gcc libffi-devel python-devel

Usage
-----

Password Hashing
~~~~~~~~~~~~~~~~

Hashing and then later checking that a password matches the previous hashed
password is very simple:

.. code:: pycon

    >>> import bcrypt
    >>> password = b"super secret password"
    >>> # Hash a password for the first time, with a randomly-generated salt
    >>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    >>> # Check that an unhashed password matches one that has previously been
    >>> # hashed
    >>> if bcrypt.checkpw(password, hashed):
    ...     print("It Matches!")
    ... else:
    ...     print("It Does not Match :(")

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
%{python3_sitearch}/*

%changelog
