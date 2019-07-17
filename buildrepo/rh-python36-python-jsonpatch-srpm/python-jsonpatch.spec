#
# spec file for package rh-python36-python-jsonpatch
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name jsonpatch

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
Version:        1.21
Release:        0%{?dist}
Url:            https://github.com/stefankoegl/python-json-patch
Summary:        Apply JSON-Patches (RFC 6902)
License:        Modified BSD License (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-jsonpointer >= 1.9

%if %{with_dnf}
%endif # with_dnf

%description
python-json-patch |Build Status| |Coverage Status|
==================================================

Applying JSON Patches in Python
-------------------------------

Library to apply JSON Patches according to `RFC
6902 <http://tools.ietf.org/html/rfc6902>`__

See Sourcecode for Examples

-  Website: https://github.com/stefankoegl/python-json-patch
-  Repository: https://github.com/stefankoegl/python-json-patch.git
-  Documentation: https://python-json-patch.readthedocs.org/
-  PyPI: https://pypi.python.org/pypi/jsonpatch
-  Travis-CI: https://travis-ci.org/stefankoegl/python-json-patch
-  Coveralls: https://coveralls.io/r/stefankoegl/python-json-patch

Running external tests
----------------------

To run external tests (such as those from
https://github.com/json-patch/json-patch-tests) use ext\_test.py

::

    ./ext_tests.py ../json-patch-tests/tests.json

.. |Build Status| image:: https://secure.travis-ci.org/stefankoegl/python-json-patch.png?branch=master
   :target: https://travis-ci.org/stefankoegl/python-json-patch
.. |Coverage Status| image:: https://coveralls.io/repos/stefankoegl/python-json-patch/badge.png?branch=master
   :target: https://coveralls.io/r/stefankoegl/python-json-patch?branch=master




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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.21-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually add _bindir
