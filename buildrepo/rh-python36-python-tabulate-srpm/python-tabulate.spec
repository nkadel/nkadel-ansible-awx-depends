#
# spec file for package rh-python36-python-tabulate
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name tabulate

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
Version:        0.7.7
Release:        0%{?dist}
Url:            https://bitbucket.org/astanin/python-tabulate
Summary:        Pretty-print tabular data
License:        Copyright (c) 2011-2016 Sergey Astanin (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
Pretty-print tabular data in Python, a library and a command-line
utility.

The main use cases of the library are:

* printing small tables without hassle: just one function call,
  formatting is guided by the data itself

* authoring tabular data for lightweight plain-text markup: multiple
  output formats suitable for further editing or transformation

* readable presentation of mixed textual and numeric data: smart
  column alignment, configurable number formatting, alignment by a
  decimal point


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
# Added manually
%{_bindir}/*

%changelog
