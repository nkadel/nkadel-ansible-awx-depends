#
# spec file for package rh-python36-python-django-auth-ldap
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name django-auth-ldap

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
Version:        1.7.0
Release:        0%{?dist}
Url:            https://github.com/django-auth-ldap/django-auth-ldap
Summary:        Django LDAP authentication backend
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:  %{?scl_prefix}python-Django >= 1.11
Requires:  %{?scl_prefix}python-python-ldap >= 3.1
%if %{with_dnf}
%endif # with_dnf

%description
================================
Django Authentication Using LDAP
================================

This is a Django authentication backend that authenticates against an LDAP
service. Configuration can be as simple as a single distinguished name
template, but there are many rich configuration options for working with users,
groups, and permissions.

* Documentation: https://django-auth-ldap.readthedocs.io/
* PyPI: https://pypi.org/project/django-auth-ldap/
* Repository: https://github.com/django-auth-ldap/django-auth-ldap
* Tests: http://travis-ci.org/pypa/django-auth-ldap
* License: BSD 2-Clause

This version is supported on Python 2.7 and 3.4+; and Django 1.11+. It requires
`python-ldap`_ >= 3.0.

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.7.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
