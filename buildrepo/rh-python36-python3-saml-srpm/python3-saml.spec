#
# spec file for package rh-python36-python-python3-saml
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name python3-saml

%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name python-%{pypi_name}}

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Common SRPM package
# Use python3-saml module name, rather than python-pypi_name
#Name:           %{?scl_prefix}python-%{pypi_name}
Name:           %{?scl_prefix}%{pypi_name}
Version:        1.4.0
Release:        0%{?dist}
Url:            https://github.com/onelogin/python3-saml
Summary:        Onelogin Python Toolkit. Add SAML support to your Python software using this library
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-isodate >= 0.5.0
Requires:       %{?scl_prefix}python-xmlsec >= 0.6.0
Requires:       %{?scl_prefix}python-defusedxml = 0.5.0
%if %{with_dnf}
#[test]
Suggests:       %{?scl_prefix}python-coverage = 3.7.1
Suggests:       %{?scl_prefix}python-freezegun = 0.3.5
Suggests:       %{?scl_prefix}python-pylint = 1.3.1
Suggests:       %{?scl_prefix}python-pep8 = 1.5.7
Suggests:       %{?scl_prefix}python-pyflakes = 0.8.1
Suggests:       %{?scl_prefix}python-coveralls = 0.4.4
%endif # with_dnf

%description
Add SAML support to your Python software using this library.
Forget those complicated libraries and use the open source library provided
and supported by OneLogin Inc.

This version supports Python3, There is a separate version that only support Python2: [python-saml](https://pypi.python.org/pypi/python-saml)

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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.4.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Use python3-saml instead python-python3-saml name

