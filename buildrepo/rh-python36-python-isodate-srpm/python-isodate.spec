#
# spec file for package rh-python36-python-isodate
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name isodate

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
Version:        0.6.0
Release:        0%{?dist}
Url:            https://github.com/gweis/isodate/
Summary:        An ISO 8601 date/time/duration parser and formatter
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-six
%if %{with_dnf}
%endif # with_dnf

%description
ISO 8601 date/time parser
=========================

This module implements ISO 8601 date, time and duration parsing.
The implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is not
mentioned there, then it is treated as non existent, and not as an allowed
option.

For instance, ISO8601:2004 never mentions 2 digit years. So, it is not
intended by this module to support 2 digit years. (while it may still
be valid as ISO date, because it is not explicitly forbidden.)
Another example is, when no time zone information is given for a time,
then it should be interpreted as local time, and not UTC.

As this module maps ISO 8601 dates/times to standard Python data types, like
*date*, *time*, *datetime* and *timedelta*, it is not possible to convert
all possible ISO 8601 dates/times. For instance, dates before 0001-01-01 are
not allowed by the Python *date* and *datetime* classes. Additionally
fractional seconds are limited to microseconds. That means if the parser finds
for instance nanoseconds it will round it to microseconds.

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.6.0-0
- Update .spec file with py2pack
- Manuall add Requires and Suggests
