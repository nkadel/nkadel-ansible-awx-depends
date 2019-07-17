#
# spec file for package rh-python36-python-boto
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name boto

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
Version:        2.47.0
Release:        0%{?dist}
Url:            https://github.com/boto/boto/
Summary:        Amazon Web Services Library
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
####
boto
####
boto 2.47.0

Released: 24-May-2017

******
Boto 3
******

`Boto3 <https://github.com/boto/boto3>`__, the next version of Boto, is now
stable and recommended for general use.  It can be used side-by-side with Boto
in the same project, so it is easy to start using Boto3 in your existing
projects as well as new projects. Going forward, API updates and all new
feature work will be focused on Boto3.

To assist users who still depend on Boto and cannot immediately switch over, we
will be triaging and addressing critical issues and PRs in Boto in the short
term. As more users make the switch to Boto3, we expect to reduce our
maintenance involvement over time. If we decide on a cutoff date or any
significant changes to our maintenance plan, we will make pre-announcements
well ahead of schedule to allow ample time for our users to adapt/migrate.


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
