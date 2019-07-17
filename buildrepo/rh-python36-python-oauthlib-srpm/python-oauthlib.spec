#
# spec file for package rh-python36-python-oauthlib
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name oauthlib

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
Version:        3.0.2
Release:        0%{?dist}
Url:            https://github.com/oauthlib/oauthlib
Summary:        A generic, spec-compliant, thorough implementation of the OAuth request-signing logic
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
# Manually added for rsa
Suggests:       %{?scl_prefix}python-cryptography
# Manually added for signals
Suggests:       %{?scl_prefix}python-blinker
# Manually added for signedtoken
Suggests:       %{?scl_prefix}python-cryptography
Suggests:       %{?scl_prefix}python-pyjwt >= 1.0.0
%endif # with_dnf

%description
OAuthLib - Python Framework for OAuth1 & OAuth2
===============================================

*A generic, spec-compliant, thorough implementation of the OAuth request-signing
logic for Python 2.7 and 3.4+.*

OAuth often seems complicated and difficult-to-implement. There are several
prominent libraries for handling OAuth requests, but they all suffer from one or
both of the following:

1. They predate the `OAuth 1.0 spec`_, AKA RFC 5849.
2. They predate the `OAuth 2.0 spec`_, AKA RFC 6749.
3. They assume the usage of a specific HTTP request library.

.. _`OAuth 1.0 spec`: https://tools.ietf.org/html/rfc5849
.. _`OAuth 2.0 spec`: https://tools.ietf.org/html/rfc6749

OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without
assuming a specific HTTP request object or web framework. Use it to graft OAuth
client support onto your favorite HTTP library, or provide support onto your
favourite web framework. If you are a maintainer of such a library, write a thin
veneer on top of OAuthLib and get OAuth support for very little effort.

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 3.0.2-0
- Update .spec file with py2pack
- Manually add Suggests for feature requirements
