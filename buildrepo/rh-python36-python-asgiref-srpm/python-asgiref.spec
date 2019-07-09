#
# spec file for package rh-python36-python-asgiref
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name asgiref

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
Version:        3.1.4
Release:        0%{?dist}
Url:            http://github.com/django/asgiref/
Summary:        ASGI specs, helper code, and adapters
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
# [tests]
Suggests:       %{?scl_prefix}python-pytest = 4.3.0
Suggests:       %{?scl_prefix}python-pytest-asyncio = 0.10.0
%endif # with_dnf

%description
asgiref
=======

ASGI is a standard for Python asynchronous web apps and servers to communicate
with each other, and positioned as an asynchronous successor to WSGI. You can
read more at https://asgi.readthedocs.io/en/latest/

This package includes ASGI base libraries, such as:

* Sync-to-async and async-to-sync function wrappers, ``asgiref.sync``
* Server base classes, ``asgiref.server``
* A WSGI-to-ASGI adapter, in ``asgiref.wsgi``

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

%changelog
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 3.1.4-0
- Update .spec from py2pack
- Manually add Requires and Suggests
