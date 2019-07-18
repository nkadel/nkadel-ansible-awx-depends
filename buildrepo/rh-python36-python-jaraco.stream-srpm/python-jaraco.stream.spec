#
# spec file for package rh-python36-python-jaraco.stream
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name jaraco.stream

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
Version:        1.1.2
Release:        0%{?dist}
Url:            https://github.com/jaraco/jaraco.stream
Summary:        routines for dealing with data streams
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-setuptools_scm >= 1.15.0
Requires:       %{?scl_prefix}python-six
%if %{with_dnf}
# Manually added for docs
Suggests:       %{?scl_prefix}python-rst.linker
# Manually added for tests
Suggests:       %{?scl_prefix}python-pytest >= 2.8
Suggests:       %{?scl_prefix}python-more_itertools
# Manually added for tests on pyton 2.6
#Suggests:  %{?scl_prefix}python-subprocess32; python_version=="2.6"
%endif # with_dnf

%description
Routines for handling streaming data, including a
set of generators for loading gzip data on the fly.

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
%exclude %{python3_sitelib}/jaraco/__init__.py
%exclude %{python3_sitelib}/jaraco/__pycache__

%changelog
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.1.2-0
- Update .spec with py2pack
- Manually add Requires
- Manually exclude cross-duplicated files
