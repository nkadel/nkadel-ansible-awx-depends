#
# spec file for package rh-python36-python-msrest
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name msrest

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
Version:        0.6.8
Release:        0%{?dist}
Url:            https://github.com/Azure/msrest-for-python
Summary:        AutoRest swagger generator Python client runtime.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
#Requires:  %{?scl_prefix}python-requests~=2.16
Requires:  %{?scl_prefix}python-requests >= 2.16
Requires:  %{?scl_prefix}python-requests_oauthlib >= 0.5.0
Requires:  %{?scl_prefix}python-isodate >= 0.6.0
Requires:  %{?scl_prefix}python-certifi >= 2017.4.17
%if %{with_dnf}
#[:python_version<'3.4']
#Suggests:  %{?scl_prefix}python-enum34 >= 1.0.4
#[:python_version<'3.5']
#Suggests:  %{?scl_prefix}python-typing
#[async:python_version>='3.5']
Suggests:  %{?scl_prefix}python-aiohttp >= 3.0
Suggests:  %{?scl_prefix}python-aiodns
%endif # with_dnf

%description
AutoRest: Python Client Runtime
===============================

.. image:: https://travis-ci.org/Azure/msrest-for-python.svg?branch=master
 :target: https://travis-ci.org/Azure/msrest-for-python

.. image:: https://codecov.io/gh/azure/msrest-for-python/branch/master/graph/badge.svg
 :target: https://codecov.io/gh/azure/msrest-for-python

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

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.6.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests

