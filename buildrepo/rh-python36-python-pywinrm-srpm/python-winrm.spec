#
# spec file for package rh-python36-python-pywinrm
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pywinrm

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
Version:        0.3.0
Release:        0%{?dist}
Url:            http://github.com/diyan/pywinrm/
Summary:        Python library for Windows Remote Management
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-xmltodict
Requires:       %{?scl_prefix}python-requests >= 2.9.1
Requires:       %{?scl_prefix}python-requests_ntlm >= 0.3.0
Requires:       %{?scl_prefix}python-six
%if %{with_dnf}
#[credssp]
Suggests:       %{?scl_prefix}python-requests-credssp >= 0.0.1
#[kerberos]
Suggests:       %{?scl_prefix}python-requests-kerberos >= 0.10.0
%endif # with_dnf

%description
# pywinrm 
pywinrm is a Python client for the Windows Remote Management (WinRM) service.
It allows you to invoke commands on target Windows machines from any machine
that can run Python.

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
