#
# spec file for package rh-python36-python-s3transfer
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name s3transfer

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
Version:        0.1.13
Release:        0%{?dist}
Url:            https://github.com/boto/s3transfer
Summary:        An Amazon S3 Transfer Manager
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-botocore < 2.0.0
Requires:       %{?scl_prefix}python-botocore >= 1.3.0
# Manually disabled, python 3.x has library built in
#Requires:       %{?scl_prefix}python-futures < 4.0.0
#Requires:       %{?scl_prefix}python-futures >= 2.2.0
%if %{with_dnf}
# Manually added for test
#Suggests:       %{?scl_prefix}python-nose = 1.3.3
Suggests:       %{?scl_prefix}python-nose >= 1.3.3
Suggests:       %{?scl_prefix}python-mock = 1.3.0
Suggests:       %{?scl_prefix}python-coverage = 4.0.1
Suggests:       %{?scl_prefix}python-wheel = 0.24.0
# Only For python 2.6
#Suggests:       %{?scl_prefix}python-unittest2 = 0.5.1
%endif # with_dnf
%description
=====================================================
s3transfer - An Amazon S3 Transfer Manager for Python
=====================================================

S3transfer is a Python library for managing Amazon S3 transfers.

.. note::

  This project is not currently GA. If you are planning to use this code in
  production, make sure to lock to a minor version as interfaces may break
  from minor version to minor version. For a basic, stable interface of
  s3transfer, try the interfaces exposed in `boto3 <https://boto3.readthedocs.io/en/latest/guide/s3.html#using-the-transfer-manager>`__

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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.1.13-0
- Update .spec file with py2pack
- Add Requires and Suggests for tests manually
