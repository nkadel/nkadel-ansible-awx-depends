#
# spec file for package rh-python36-python-PyJWT
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name PyJWT

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
Version:        1.7.1
Release:        0%{?dist}
Url:            http://github.com/jpadilla/pyjwt
Summary:        JSON Web Token implementation in Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
PyJWT
=====

.. image:: https://travis-ci.com/jpadilla/pyjwt.svg?branch=master
   :target: http://travis-ci.com/jpadilla/pyjwt?branch=master

.. image:: https://ci.appveyor.com/api/projects/status/h8nt70aqtwhht39t?svg=true
   :target: https://ci.appveyor.com/project/jpadilla/pyjwt

.. image:: https://img.shields.io/pypi/v/pyjwt.svg
   :target: https://pypi.python.org/pypi/pyjwt

.. image:: https://coveralls.io/repos/jpadilla/pyjwt/badge.svg?branch=master
   :target: https://coveralls.io/r/jpadilla/pyjwt?branch=master

.. image:: https://readthedocs.org/projects/pyjwt/badge/?version=latest
   :target: https://pyjwt.readthedocs.io

A Python implementation of `RFC 7519 <https://tools.ietf.org/html/rfc7519>`_. Original implementation was written by `@progrium <https://github.com/progrium>`_.

Sponsor
-------

+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |auth0-logo| | If you want to quickly add secure token-based authentication to Python projects, feel free to check Auth0's Python SDK and free plan at `auth0.com/overview <https://auth0.com/overview?utm_source=GHsponsor&utm_medium=GHsponsor&utm_campaign=pyjwt&utm_content=auth>`_. |
+--------------+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |auth0-logo| image:: https://user-images.githubusercontent.com/83319/31722733-de95bbde-b3ea-11e7-96bf-4f4e8f915588.png

Installing
----------

Install with **pip**:

.. code-block:: sh

    $ pip install PyJWT


Usage
-----

.. code:: python

    >>> import jwt
    >>> encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg'

    >>> jwt.decode(encoded, 'secret', algorithms=['HS256'])
    {'some': 'payload'}


Command line
------------

Usage::

    pyjwt [options] INPUT

Decoding examples::

    pyjwt --key=secret decode TOKEN
    pyjwt decode --no-verify TOKEN

See more options executing ``pyjwt --help``.


Documentation
-------------

View the full docs online at https://pyjwt.readthedocs.io/en/latest/


Tests
-----

You can run tests from the project root after cloning with:

.. code-block:: sh

    $ python setup.py test




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