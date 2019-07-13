#
# spec file for package rh-python36-python-keystoneauth1
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name keystoneauth1

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
Version:        3.4.0
Release:        0%{?dist}
Url:            https://docs.openstack.org/keystoneauth/latest/
Summary:        Authentication Library for OpenStack Identity
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-pbr >= 2.0.0
Conflicts:      %{?scl_prefix}python-pbr = 2.1.0
Requires:       %{?scl_prefix}python-pbr >= 2.0.0
Requires:       %{?scl_prefix}python-iso8601 >= 0.1.11
Requires:       %{?scl_prefix}python-requests >= 2.14.2
Requires:       %{?scl_prefix}python-six >= 1.10.0
Requires:       %{?scl_prefix}python-stevedore >= 1.20.0
%if %{with_dnf}
#[betamax]
Suggests:       %{?scl_prefix}python-betamax >= 0.7.0
Suggests:       %{?scl_prefix}python-fixtures >= 3.0.0
Suggests:       %{?scl_prefix}python-mock >= 2.0.0
#[kerberos]
Suggests:       %{?scl_prefix}python-requests-kerberos >= 0.6
#[oauth1]
Suggests:       %{?scl_prefix}python-oauthlib >= 0.6.0
#[saml2]
Conflicts:       %{?scl_prefix}python-lxml = 3.7.0
Suggests:       %{?scl_prefix}python-lxml >= 3.4.1
%endif # with_dnf

%description
========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/badges/keystoneauth.svg
    :target: https://governance.openstack.org/reference/tags/index.html

.. Change things from this point on

============
keystoneauth
============

.. image:: https://img.shields.io/pypi/v/keystoneauth1.svg
    :target: https://pypi.python.org/pypi/keystoneauth1/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/keystoneauth1.svg
    :target: https://pypi.python.org/pypi/keystoneauth1/
    :alt: Downloads

This package contains tools for authenticating to an OpenStack-based cloud.
These tools include:

* Authentication plugins (password, token, and federation based)
* Discovery mechanisms to determine API version support
* A session that is used to maintain client settings across requests (based on
  the requests Python library)

Further information:

* Free software: Apache license
* Documentation: https://docs.openstack.org/keystoneauth/latest/
* Source: https://git.openstack.org/cgit/openstack/keystoneauth
* Bugs: https://bugs.launchpad.net/keystoneauth





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
