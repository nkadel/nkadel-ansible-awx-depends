#
# spec file for package rh-python36-python-tempora
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name tempora

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
Version:        1.10
Release:        0%{?dist}
Url:            https://github.com/jaraco/tempora
Summary:        Objects and routines pertaining to date and time (tempora)
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-setuptools_scm
# Manually added
Requires:       %{?scl_prefix}python-six
Requires:       %{?scl_prefix}python-pytz
Requires:       %{?scl_prefix}python-sphinx
Requires:       %{?scl_prefix}python-jaraco.packaging >= 3.2
Requires:       %{?scl_prefix}python-rst.linker >= 1.9

%if %{with_dnf}
Suggests:       %{?scl_prefix}python-pytest >= 2.8
Suggests:       %{?scl_prefix}python-pytest-sugar
Suggests:       %{?scl_prefix}python-collective.checkdocs
Suggests:       %{?scl_prefix}python-backports.unittest_mock
%endif # with_dnf

%description
.. image:: https://img.shields.io/pypi/v/tempora.svg
   :target: https://pypi.org/project/tempora

.. image:: https://img.shields.io/pypi/pyversions/tempora.svg

.. image:: https://img.shields.io/travis/jaraco/tempora/master.svg
   :target: http://travis-ci.org/jaraco/tempora

Objects and routines pertaining to date and time (tempora).

Modules include:

 - tempora (top level package module) contains miscellaneous
   utilities and constants.
 - timing contains routines for measuring and profiling.
 - schedule contains an event scheduler.




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
# Manually added
%{_bindir}/*

%changelog
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.10-0
- Update spec file with py2pack
- Manually add _bindir
