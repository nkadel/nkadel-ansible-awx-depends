#
# spec file for package rh-python36-python-jsonpointer
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name jsonpointer

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
Version:        2.0
Release:        0%{?dist}
Url:            https://github.com/stefankoegl/python-json-pointer
Summary:        Identify specific nodes in a JSON document (RFC 6901)
License:        Modified BSD License (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
python-json-pointer
===================

|PyPI version| |Supported Python versions| |Build Status| |Coverage
Status|

Resolve JSON Pointers in Python
-------------------------------

Library to resolve JSON Pointers according to `RFC
6901 <http://tools.ietf.org/html/rfc6901>`__

See source code for examples \* Website:
https://github.com/stefankoegl/python-json-pointer \* Repository:
https://github.com/stefankoegl/python-json-pointer.git \* Documentation:
https://python-json-pointer.readthedocs.org/ \* PyPI:
https://pypi.python.org/pypi/jsonpointer \* Travis CI:
https://travis-ci.org/stefankoegl/python-json-pointer \* Coveralls:
https://coveralls.io/r/stefankoegl/python-json-pointer

.. |PyPI version| image:: https://img.shields.io/pypi/v/jsonpointer.svg
   :target: https://pypi.python.org/pypi/jsonpointer/
.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/jsonpointer.svg
   :target: https://pypi.python.org/pypi/jsonpointer/
.. |Build Status| image:: https://travis-ci.org/stefankoegl/python-json-pointer.png?branch=master
   :target: https://travis-ci.org/stefankoegl/python-json-pointer
.. |Coverage Status| image:: https://coveralls.io/repos/stefankoegl/python-json-pointer/badge.png?branch=master
   :target: https://coveralls.io/r/stefankoegl/python-json-pointer?branch=master




%prep
%setup -q -n %{pypi_name}-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
%{py_build}
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%{py_install}
%{?scl:EOF}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/*

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually add _bindir
