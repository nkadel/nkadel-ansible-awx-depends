#
# spec file for package rh-python36-python-attrs
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name attrs

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
Version:        17.4.0
Release:        0%{?dist}
Url:            http://www.attrs.org/
Summary:        Classes Without Boilerplate
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
%if %{with_dnf}
# Manually added for dev
Suggests:       %{?scl_prefix}python-coverage
Suggests:       %{?scl_prefix}python-hypothesis
Suggests:       %{?scl_prefix}python-pympler
Suggests:       %{?scl_prefix}python-pytest
Suggests:       %{?scl_prefix}python-six
Suggests:       %{?scl_prefix}python-sphinx
Suggests:       %{?scl_prefix}python-zope.interface
# Manually added for docs
#Suggests:       %{?scl_prefix}python-sphinx
#Suggests:       %{?scl_prefix}python-zope.interface
# Manually added for tests
#Suggests:       %{?scl_prefix}python-coverage
#Suggests:       %{?scl_prefix}python-hypothesis
#Suggests:       %{?scl_prefix}python-pympler
#Suggests:       %{?scl_prefix}python-pytest
#Suggests:       %{?scl_prefix}python-six
#Suggests:       %{?scl_prefix}python-zope.interface
%endif # with_dnf

%description
``attrs`` is the Python package that will bring back the **joy** of **writing classes** by relieving you from the drudgery of implementing object protocols (aka `dunder <https://nedbatchelder.com/blog/200605/dunder.html>`_ methods).

Its main goal is to help you to write **concise** and **correct** software without slowing down your code.

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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com>
- Update .spec file with py2pack
- Manually add  dependencies
