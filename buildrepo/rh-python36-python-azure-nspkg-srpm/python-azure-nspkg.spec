#
# spec file for package rh-python36-python-azure-nspkg
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name azure-nspkg

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
Version:        2.0.0
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Namespace Package [Internal]
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
BuildRequires:  unzip
%if %{with_dnf}
%endif # with_dnf

%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure namespace.

If you are looking to install the Azure client libraries, see the
`azure <https://pypi.python.org/pypi/azure>`__ bundle package.

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
%exclude %{python3_sitelib}/azure/__init__.py
%exclude %{python3_sitelib}/azure/__pycache__
%exclude %{python3_sitelib}/azure/mgmt/__init__.py
%exclude %{python3_sitelib}/azure/mgmt/__pycache__

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.0.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually exclude cross-duplicated files
