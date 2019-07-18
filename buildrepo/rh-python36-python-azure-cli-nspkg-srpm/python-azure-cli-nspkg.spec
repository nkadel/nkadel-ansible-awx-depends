#
# spec file for package rh-python36-python-azure-cli-nspkg
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name azure-cli-nspkg

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
Version:        3.0.2
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-cli
Summary:        Microsoft Azure CLI Namespace Package
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-azure-nspkg >= 2.0.0

%if %{with_dnf}
%endif # with_dnf

%description
Microsoft Azure CLI Namespace Package
=====================================

This is the Microsoft Azure CLI namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure cli namespaces.


.. :changelog:

Release History
===============

3.0.2
+++++
* minor fixes

3.0.1
+++++
* minor fixes

3.0.0 (2016-04-28)
++++++++++++++++++

* New nspkg structure.

2.0.0 (2016-02-27)
++++++++++++++++++

* GA release.

0.1.2 (2016-01-30)
++++++++++++++++++

* Support Python 3.6.

0.1.1 (2016-01-17)
++++++++++++++++++

* Stable release (no code changes since previous version).

0.1.0b11 (2016-12-12)
+++++++++++++++++++++

* Preview release.




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
%exclude %{python3_sitelib}/azure/cli/__init__.py
%exclude %{python3_sitelib}/azure/cli/__pycache__

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 3.0.2-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually exclude cross-duplicated files
