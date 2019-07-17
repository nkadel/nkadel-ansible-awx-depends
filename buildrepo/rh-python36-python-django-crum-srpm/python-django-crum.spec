#
# spec file for package rh-python36-python-django-crum
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name django-crum

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
Version:        0.7.2
Release:        0%{?dist}
Url:            https://github.com/ninemoreminutes/django-crum/
Summary:        Django middleware to capture current request and user.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-pytest-runner
Requires:       %{?scl_prefix}python-django
%if %{with_dnf}
%endif # with_dnf

%description
|Build Status| |PyPI Version| |PyPI License| |Python Versions|

Django-CRUM
===========

Django-CRUM (Current Request User Middleware) captures the current request and
user in thread local storage.

It enables apps to check permissions, capture audit trails or otherwise access
the current request and user without requiring the request object to be passed
directly. It also offers a context manager to allow for temporarily
impersonating another user.

It provides a signal to extend the built-in function for getting the current
user, which could be helpful when using custom authentication methods or user
models.

It is tested against:
 * Django 1.8 (Python 2.7, 3.3, 3.4 and 3.5)
 * Django 1.9 (Python 2.7, 3.4 and 3.5)
 * Django 1.10 (Python 2.7, 3.4 and 3.5)
 * Django 1.11 (Python 2.7, 3.4, 3.5 and 3.6)
 * Django master/2.0 (Python 3.5 and 3.6)

.. |Build Status| image:: http://img.shields.io/travis/ninemoreminutes/django-crum.svg
   :target: https://travis-ci.org/ninemoreminutes/django-crum
.. |PyPI Version| image:: https://img.shields.io/pypi/v/django-crum.svg
   :target: https://pypi.python.org/pypi/django-crum/
.. |PyPI License| image:: https://img.shields.io/pypi/l/django-crum.svg
   :target: https://pypi.python.org/pypi/django-crum/
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/django-crum.svg
   :target: https://pypi.python.org/pypi/django-crum/

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.7.2-0
- Update .spec from py2pack
- Manually add Requires and Suggests
