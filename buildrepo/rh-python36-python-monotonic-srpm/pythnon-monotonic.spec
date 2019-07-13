#
# spec file for package rh-python36-python-monotonic
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name monotonic

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
Version:        1.4
Release:        0%{?dist}
Url:            https://github.com/atdt/monotonic
Summary:        An implementation of time.monotonic() for Python 2 & < 3.3
License:        Apache (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description

monotonic
~~~~~~~~~

This module provides a ``monotonic()`` function which returns the
value (in fractional seconds) of a clock which never goes backwards.

On Python 3.3 or newer, ``monotonic`` will be an alias of
``time.monotonic`` from the standard library. On older versions,
it will fall back to an equivalent implementation:

+------------------+----------------------------------------+
| Linux, BSD, AIX  | ``clock_gettime(3)``                   |
+------------------+----------------------------------------+
| Windows          | ``GetTickCount`` or ``GetTickCount64`` |
+------------------+----------------------------------------+
| OS X             | ``mach_absolute_time``                 |
+------------------+----------------------------------------+

If no suitable implementation exists for the current platform,
attempting to import this module (or to import from it) will
cause a ``RuntimeError`` exception to be raised.



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