#
# spec file for package rh-python36-python-botocore
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name botocore

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
Version:        1.3.3
Release:        0%{?dist}
Url:            https://github.com/boto/botocore
Summary:        Low-level, data-driven core of boto 3.
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

# Manually added
Requires:       %{?scl_prefix}python-docutils >= 0.10
Requires:       %{?scl_prefix}python-jmespath < 1.0.0
Requires:       %{?scl_prefix}python-jmespath >= 0.7.1
Requires:       %{?scl_prefix}python-mock = 1.0.1
#Requires:       %{?scl_prefix}python-nose = 1.3.0
Requires:       %{?scl_prefix}python-nose >= 1.3.0
Requires:       %{?scl_prefix}python-python-dateutil < 3.0.0
Requires:       %{?scl_prefix}python-python-dateutil >= 2.1
Requires:       %{?scl_prefix}python-tox = 1.4
#Requires:       %{?scl_prefix}python-wheel = 0.24.0
Requires:       %{?scl_prefix}python-wheel >= 0.24.0

#[:python_version=="2.6"]
#Requires:       %{?scl_prefix}python-ordereddict = 1.1
#Requires:       %{?scl_prefix}python-simplejson = 3.3.0

%if %{with_dnf}
%endif # with_dnf

%description
botocore
========

A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the
`AWS CLI <https://github.com/aws/aws-cli>`__ as well as
`boto3 <https://github.com/boto/boto3>`__.

`Documentation <https://botocore.readthedocs.org/en/latest/>`__

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
