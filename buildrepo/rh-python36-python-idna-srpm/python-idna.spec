#
# spec file for package rh-python36-python-idna
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name idna

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
Version:        2.8
Release:        0%{?dist}
Url:            https://github.com/kjd/idna
Summary:        Internationalized Domain Names in Applications (IDNA)
License:        BSD-like (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
Internationalized Domain Names in Applications (IDNA)
=====================================================

Support for the Internationalised Domain Names in Applications
(IDNA) protocol as specified in `RFC 5891 <http://tools.ietf.org/html/rfc5891>`_.
This is the latest version of the protocol and is sometimes referred to as
&#8220;IDNA 2008&#8221;.

This library also provides support for Unicode Technical Standard 46,
`Unicode IDNA Compatibility Processing <http://unicode.org/reports/tr46/>`_.

This acts as a suitable replacement for the &#8220;encodings.idna&#8221; module that
comes with the Python standard library, but only supports the
old, deprecated IDNA specification (`RFC 3490 <http://tools.ietf.org/html/rfc3490>`_).

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.8-0
- Update .spec from py2pack
