#
# spec file for package rh-python36-python-netaddr
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name netaddr

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
Version:        0.7.19
Release:        0%{?dist}
Url:            https://github.com/drkjam/netaddr/
Summary:        A network address manipulation library for Python
License:        BSD License (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
Provides support for:

Layer 3 addresses
-----------------

- IPv4 and IPv6 addresses, subnets, masks, prefixes
- iterating, slicing, sorting, summarizing and classifying IP networks
- dealing with various ranges formats (CIDR, arbitrary ranges and globs, nmap)
- set based operations (unions, intersections etc) over IP addresses and subnets
- parsing a large variety of different formats and notations
- looking up IANA IP block information
- generating DNS reverse lookups
- supernetting and subnetting

Layer 2 addresses
-----------------

- representation and manipulation MAC addresses and EUI-64 identifiers
- looking up IEEE organisational information (OUI, IAB)
- generating derived IPv6 addresses

Documentation
-------------

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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.7.19-0
- Update .spec from py2pack
- Manually add Requires and Suggests
