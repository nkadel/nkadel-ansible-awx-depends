#
# spec file for package rh-python36-python-channels
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name channels

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
Version:        1.1.8
Release:        0%{?dist}
Url:            http://github.com/django/channels
Summary:        Brings event-driven capabilities to Django with a channel system. Django 1.8 and up only.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:  %{?scl_prefix}python-Django >= 1.8
#Requires:  %{?scl_prefix}python-asgiref ~= 1.1
Requires:  %{?scl_prefix}python-asgiref >= 1.1
#Requires:  %{?scl_prefix}python-daphne ~= 1.3
Requires:  %{?scl_prefix}python-daphne >= 1.3

%if %{with_dnf}
# Manually added for tests
Suggests:  %{?scl_prefix}python-coverage
Suggests:  %{?scl_prefix}python-flake8 < 3.0
Suggests:  %{?scl_prefix}python-flake8 >= 2.0
Suggests:  %{?scl_prefix}python-isort
# Manually added for tests on python 3.0
Suggests:  %{?scl_prefix}python-mock
%endif # with_dnf

%description


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
