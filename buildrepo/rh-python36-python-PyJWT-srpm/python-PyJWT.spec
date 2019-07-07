#
# spec file for package rh-python36-python-PyJWT
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name PyJWT

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
Version:        1.7.1
Release:        0%{?dist}
Url:            http://github.com/jpadilla/pyjwt
Summary:        JSON Web Token implementation in Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
# Manually added for crypto
Suggests:       %{?scl_prefix}python-cryptography >= 1.4
# Manually added for flake8
Suggests:       %{?scl_prefix}python-import-order
Suggests:       %{?scl_prefix}python-pep8-making
# Manually added for testytest
Suggests:       %{?scl_prefix}python-pytest < 5.0.0
Suggests:       %{?scl_prefix}python-pytest >= 4.0.1
Suggests:       %{?scl_prefix}python-pytest-cov < 3.0.0
Suggests:       %{?scl_prefix}python-pytest-cov >= 2.6.0
Suggests:       %{?scl_prefix}python-pytest-runner < 5.0.0
Suggests:       %{?scl_prefix}python-pytest-runner >= 4.2
%endif # with_dnf

%description
PyJWT
=====

A Python implementation of `RFC 7519
<https://tools.ietf.org/html/rfc7519>`_. Original implementation was
written by `@progrium <https://github.com/progrium>`_.

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
