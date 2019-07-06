#
# spec file for package rh-python36-python-tacacs_plus
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name tacacs_plus

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
Version:        1.0
Release:        0%{?dist}
Url:            http://github.com/ansible/tacacs_plus
Summary:        A client for interacting with TACACS+ servers
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Added manually
BuildRequires:  %{?scl_prefix}python-pytest-runner
Requires:       %{?scl_prefix}python-six
%if %{with_dnf}
# Testing modules added manually
Suggests:       %{?scl_prefix}python-pytest
Suggests:       %{?scl_prefix}python-pytest-csv
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
# Added manually
%{_bindir}/*

%changelog
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.0-0
- Update .spec file with py2pack
- Add _bindir manually
