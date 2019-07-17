#
# spec file for package rh-python36-python-tox
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name tox

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
Version:        1.4.2
Release:        0%{?dist}
Url:            http://tox.readthedocs.org
Summary:        tox is a generic virtualenv management and test command line tool
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added, not in requires files
BuildRequires:  unzip
# Manually added
Requires:  %{?scl_prefix}python-virtualenv >= 1.7
Requires:  %{?scl_prefix}python-py >= 1.4.9
%if %{with_dnf}
%endif # with_dnf

%description
# tox automation project

**Command line driven CI frontend and development task automation tool**

At its core tox povides a convenient way to run arbitrary commands in
isolated environments to serve as a single entry point for build, test
and release activities.

tox is highly
[configurable](https://tox.readthedocs.io/en/latest/config.html) and
[pluggable](https://tox.readthedocs.io/en/latest/plugins.html).

## Example: run tests with Python 2.7 and Python 3.7

tox is mainly used as a command line tool and needs a `tox.ini` or a
`tool.tox` section in `pyproject.toml` containing the configuration.

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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.4.2-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Adjust virtualenv dependency to python-virtualenv
