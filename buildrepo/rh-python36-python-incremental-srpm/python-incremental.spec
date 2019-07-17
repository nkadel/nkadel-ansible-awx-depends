#
# spec file for package rh-python36-python-incremental
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name incremental

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
Version:        17.5.0
Release:        0%{?dist}
Url:            https://github.com/twisted/incremental
Summary:        Incremental is a small library that versions your Python projects.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
# Manually addded for scripts
Suggests:       %{?scl_prefix}python-click >= 6.0
Suggests:       %{?scl_prefix}python-twisted >= 16.4.0
%endif # with_dnf

%description
Incremental
===========

|travis|
|pypi|
|coverage|

Incremental is a small library that versions your Python projects.

API documentation can be found `here <https://hawkowl.github.io/incremental/docs/>`_.

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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 17.5.0-0
- Update spec file with py2pack
- Manually add Requires for python-click and python-twisted

