#
# spec file for package rh-python36-python-ovirt-engine-sdk-python
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name ovirt-engine-sdk-python

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
Version:        4.2.4
Release:        0%{?dist}
#Url:            
Summary:        Python SDK for oVirt Engine API
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  libxml2-devel
Requires:       %{?scl_prefix}python-pycurl >= 7.19.0
Requires:       %{?scl_prefix}python-six
# Disabled for python > 2.7
#Requires:       %{?scl_prefix}python-enum34
%if %{with_dnf}
%endif # with_dnf

%description
= oVirt Engine API Python SDK

== Introduction

This project contains the Python SDK for the oVirt Engine API.

== Important

Note that most of the code of this SDK is automatically generated. If
you just installed the package then you will have everything already,
but if you downloaded the source then you will need to generate it,
follow the instructions in the `README.adoc` file of the parent
directory.

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
%{python3_sitearch}/*

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.10-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Disable enum34 requirement

