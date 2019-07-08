#
# spec file for package rh-python36-python-paramiko
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name paramiko

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
Version:        2.4.0
Release:        0%{?dist}
Url:            https://github.com/paramiko/paramiko/
Summary:        SSH2 protocol library
License:        LGPL (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-bcrypt >= 3.1.3
Requires:       %{?scl_prefix}python-cryptography >= 1.5
Requires:       %{?scl_prefix}python-pynacl >= 1.0.1
Requires:       %{?scl_prefix}python-pyasn1 >= 0.1.7
%if %{with_dnf}
%endif # with_dnf

%description
This is a library for making SSH2 connections (client or server).
Emphasis is on using SSH2 as an alternative to SSL for making secure
connections between python scripts.  All major ciphers and hash methods
are supported.  SFTP client and server mode are both supported too.

Required packages:
    Cryptography

To install the development version, ``pip install -e
git+https://github.com/paramiko/paramiko/#egg=paramiko``.




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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.4.0-0
- Update .spec file with py2pack
- Manually add Requires
