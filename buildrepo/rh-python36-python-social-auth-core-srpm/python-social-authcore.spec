#
# spec file for package rh-python36-python-social-auth-core
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name social-auth-core

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
Version:        3.0.0
Release:        0%{?dist}
Url:            https://github.com/python-social-auth/social-core
Summary:        Python social authentication made simple.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:  %{?scl_prefix}python-PyJWT >= 1.4.0
Requires:  %{?scl_prefix}python-oauthlib >= 1.0.3
Requires:  %{?scl_prefix}python-requests-oauthlib >= 0.6.1
Requires:  %{?scl_prefix}python-requests >= 2.9.1
Requires:  %{?scl_prefix}python-six >= 1.10.0
# Manually added for python3
Requires:  %{?scl_prefix}defusedxml >= 0.5.0rc1
Requires:  %{?scl_prefix}python3-openid >= 3.0.10
# For python2
#Requires:  %{?scl_prefix}python2-openid >= 3.0.10

%if %{with_dnf}
Suggests:       %{?scl_prefix}python-python3-saml >= 1.2.1
Suggests:       %{?scl_prefix}python-jose >= 3.0.0
Suggests:       %{?scl_prefix}python-cryptography >= 2.1.1
# For python2
#Suggests:       %{?scl_prefix}python-python2-saml >= 1.2.1
%endif # with_dnf

%description
# Python Social Auth - Core

[![Build Status](https://travis-ci.org/python-social-auth/social-core.svg?branch=master)](https://travis-ci.org/python-social-auth/social-core)
[![Donate](https://img.shields.io/badge/Donate-PayPal-orange.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=matiasaguirre%40gmail%2ecom&lc=US&item_name=Python%20Social%20Auth&no_note=0&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHostedGuest)

Python Social Auth is an easy to setup social authentication/registration
mechanism with support for several frameworks and auth providers.

## Description

This is the core component of the python-social-auth ecosystem, it
implements the common interface to define new authentication backends
to third parties services, implement integrations with web frameworks
and storage solutions.

## Documentation

Project documentation is available at http://python-social-auth.readthedocs.org/.

## Setup

```shell
$ pip install social-auth-core
```

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) document for details.

## Versioning

This project follows [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html).

## License

This project follows the BSD license. See the [LICENSE](LICENSE) for details.

## Donations

This project is maintened on my spare time, consider donating to keep
it improving.

[![Donate](https://img.shields.io/badge/Donate-PayPal-orange.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=matiasaguirre%40gmail%2ecom&lc=US&item_name=Python%20Social%20Auth&no_note=0&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHostedGuest)


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
