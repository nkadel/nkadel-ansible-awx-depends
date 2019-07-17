#
# spec file for package rh-python36-python-requests-kerberos
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name requests-kerberos

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
Version:        0.12.0
Release:        0%{?dist}
Url:            https://github.com/requests/requests-kerberos
Summary:        A Kerberos authentication handler for python-requests
License:        ISC
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
# Manually added
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires:       %{?scl_prefix}python-requests >= 1.1.0
Requires:       %{?scl_prefix}python-cryptography >= 1.3
# For win32
#winkerberos >= 0.5.0; sys.platform == 'win32'
#pykerberos >= 1.1.8, < 2.0.0; sys.platform != 'win32'
#cryptography >= 1.3
#cryptography>=1.3; python_version!="3.3"
#cryptography>=1.3, <2; python_version=="3.3"

%if %{with_dnf}
%endif # with_dnf

%description
requests Kerberos/GSSAPI authentication library
===============================================

Requests is an HTTP library, written in Python, for human beings. This library
adds optional Kerberos/GSSAPI authentication support and supports mutual
authentication.

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.12.0-0
- Update .spec file with py2pack
- Manually add Requires

