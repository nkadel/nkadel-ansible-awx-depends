#
# spec file for package rh-python36-python-python-memcached
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name python-memcached

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
Version:        1.59
Release:        0%{?dist}
Url:            https://github.com/linsomniac/python-memcached
Summary:        Pure python memcached client
License:        Python-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-six >= 1.4.0
%if %{with_dnf}
# Manually added for tests
Suggests:       %{?scl_prefix}python-
Suggests:       %{?scl_prefix}python-nose
Suggests:       %{?scl_prefix}python-coverage
Suggests:       %{?scl_prefix}python-hacking
Suggests:       %{?scl_prefix}python-mock
%endif # with_dnf

%description
[![Build
Status](https://travis-ci.org/linsomniac/python-memcached.svg)](https://travis-ci.org/linsomniac/python-memcached)

## Overview

This software is a 100% Python interface to the memcached memory cache
daemon.  It is the client side software which allows storing values
in one or more, possibly remote, memcached servers.  Search google for
memcached for more information.

This package was originally written by Evan Martin of Danga.  Please do
not contact Evan about maintenance.  Sean Reifschneider of tummy.com,
ltd. has taken over maintenance of it.

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
* Fri Jul 12 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.59-0
- Update with py2pack
- Manually add Requires for python-sex, testing Requires
