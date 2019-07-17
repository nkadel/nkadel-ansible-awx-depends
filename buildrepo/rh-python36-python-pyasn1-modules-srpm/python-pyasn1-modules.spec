#
# spec file for package rh-python36-python-pyasn1-modules
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pyasn1-modules

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
Version:        0.2.1
Release:        0%{?dist}
Url:            https://github.com/etingof/pyasn1-modules
Summary:        A collection of ASN.1-based protocols modules.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires:       %{?scl_prefix}python-pyasn1 >= 0.4.1
Requires:       %{?scl_prefix}python-pyasn1 < 0.5.0
%if %{with_dnf}
%endif # with_dnf
# Manually added
Provides:       %{?scl_prefix}python-pyasn1_modules = %{version}-%{release}
Obsoletes:      %{?scl_prefix}python-pyasn1_modules <= %{version}-%{release}
Conflicts:      %{?scl_prefix}python-pyasn1_modules <= %{version}-%{release}

%description
A collection of ASN.1 modules expressed in form of pyasn1 classes. Includes protocols PDUs definition (SNMP, LDAP etc.) and various data structures (X.509, PKCS etc.).

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.2.1-0
- Update .spec file with py2pack
- Add Requires manually
- Add Provides for python-pyasn1_modules because of mixed case pypi.org names
