#
# spec file for package rh-python36-python-Twisted
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name Twisted

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
Version:        17.9.0
Release:        0%{?dist}
Url:            http://twistedmatrix.com/
Summary:        An asynchronous networking framework written in Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.bz2

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Added manuall
BuildRequires:  %{?scl_prefix}python-incremental >= 16.10.1
%if %{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python-%{pypi_name}}

%description
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

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
%{python3_sitearch}/*
%{_bindir}/*

%changelog
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 17.9.0-0
- Update spec file from py2pack
- Manually switch tarball to bz2

