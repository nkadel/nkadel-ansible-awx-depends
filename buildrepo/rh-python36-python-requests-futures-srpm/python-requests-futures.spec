#
# spec file for package rh-python36-python-requests-futures
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name requests-futures

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
Version:        0.9.7
Release:        0%{?dist}
Url:            https://github.com/ross/requests-futures
Summary:        Asynchronous Python HTTP for Humans.
License:        Apache License v2 (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-requests >= 1.2.0
# Disable requirement on pyton > 3.0
#Requires:       %{?scl_prefix}python-futures >= 2.1.3
%if %{with_dnf}
%endif # with_dnf

%description
Asynchronous Python HTTP Requests for Humans
============================================

Small add-on for the python requests_ http library. Makes use of python 3.2
`concurrent.futures`_ or the backport_ for prior versions of python.

The additional API and changes are minimal and strives to avoid surprises.

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com>
- Update .spec file with py2pack
- Manually add Requires
- Disable Requires for python-futures on python > 3.0-
