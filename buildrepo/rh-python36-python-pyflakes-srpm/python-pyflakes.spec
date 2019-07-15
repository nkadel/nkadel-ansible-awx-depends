#
# spec file for package rh-python36-python-pyflakes
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pyflakes

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
Version:        2.1.1
Release:        0%{?dist}
Url:            https://github.com/PyCQA/pyflakes
Summary:        passive checker of Python programs
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
========
Pyflakes
========

A simple program which checks Python source files for errors.

Pyflakes analyzes programs and detects various errors.  It works by
parsing the source file, not importing it, so it is safe to use on
modules with side effects.  It is also much faster.

It is `available on PyPI <https://pypi.org/project/pyflakes/>`_
and it supports all active versions of Python: 2.7 and 3.4 to 3.7.


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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.1.1-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually add _bindir

