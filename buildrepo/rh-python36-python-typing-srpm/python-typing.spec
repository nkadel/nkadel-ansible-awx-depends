#
# spec file for package rh-python36-python-typing
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name typing

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
Version:        3.7.4
Release:        0%{?dist}
Url:            https://docs.python.org/3/library/typing.html
Summary:        Type Hints for Python
License:        Python-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
Typing -- Type Hints for Python

This is a backport of the standard library typing module to Python
versions older than 3.5.  (See note below for newer versions.)

Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a
concise, standard format, and it has been designed to also be used by
static and runtime type checkers, static analyzers, IDEs and other
tools.

NOTE: in Python 3.5 and later, the typing module lives in the stdlib,
and installing this package has NO EFFECT.  To get a newer version of
the typing module in Python 3.5 or later, you have to upgrade to a
newer Python (bugfix) version.  For example, typing in Python 3.6.0 is
missing the definition of 'Type' -- upgrading to 3.6.2 will fix this.

Also note that most improvements to the typing module in Python 3.7
will not be included in this package, since Python 3.7 has some
built-in support that is not present in older versions (See PEP 560.)




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