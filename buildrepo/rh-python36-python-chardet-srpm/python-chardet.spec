#
# spec file for package rh-python36-python-chardet
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name chardet

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
Version:        3.0.4
Release:        0%{?dist}
Url:            https://github.com/chardet/chardet
Summary:        Universal encoding detector for Python 2 and 3
License:        LGPL (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
Chardet: The Universal Character Encoding Detector
--------------------------------------------------

This is a continuation of Mark Pilgrim's excellent chardet. Previously, two
versions needed to be maintained: one that supported python 2.x and one that
supported python 3.x.  We've recently merged with `Ian Cordasco <https://github.com/sigmavirus24>`_'s
`charade <https://github.com/sigmavirus24/charade>`_ fork, so now we have one
coherent version that works for Python 2.6+.

:maintainer: Dan Blanchard

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
