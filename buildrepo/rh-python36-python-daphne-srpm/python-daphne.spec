#
# spec file for package rh-python36-python-daphne
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name daphne

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
Version:        1.3.0
Release:        0%{?dist}
Url:            https://github.com/django/daphne
Summary:        Django ASGI (HTTP/WebSocket) server
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:  %{?scl_prefix}python-asgiref = 1.1
Requires:  %{?scl_prefix}python-twisted >= 17.1
Requires:  %{?scl_prefix}python-autobahn>=0.18
%if %{with_dnf}
# Manually added for tests
Suggests:  %{?scl_prefix}python-hypothesis
Suggests:  %{?scl_prefix}python-tox
%endif # with_dnf

%description
daphne
======

Daphne is a HTTP, HTTP2 and WebSocket protocol server for
`ASGI <https://channels.readthedocs.io/en/latest/asgi.html>`_, and developed
to power Django Channels.

It supports automatic negotiation of protocols; there is no need for URL
prefixing to determine WebSocket endpoints versus HTTP endpoints.

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
%{_bindir}/*

%changelog
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.3.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests and _bindir
