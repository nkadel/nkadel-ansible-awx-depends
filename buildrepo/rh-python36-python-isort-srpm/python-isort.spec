#
# spec file for package rh-python36-python-isort
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name isort

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
Version:        4.3.4
Release:        0%{?dist}
Url:            https://github.com/timothycrosley/isort
Summary:        A Python utility / library to sort Python imports.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added only for python 2.7
#Requires:  %{?scl_prefix}python-futures
%if %{with_dnf}
%endif # with_dnf

%description
isort your python imports for you so you do not have to.

isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections.
It provides a command line utility, Python library and `plugins for various editors <https://github.com/timothycrosley/isort/wiki/isort-Plugins>`_ to quickly sort all your imports.
It currently cleanly supports Python 2.7 - 3.6 without any dependencies.

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
%{_bindir}/*

%changelog
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 4.3.4-0
- Update .spec from py2pack
- Manually add Requires and Suggests and _bindir
