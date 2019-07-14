#
# spec file for package rh-python36-python-os-service-types
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name os-service-types

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
Version:        1.2.0
Release:        0%{?dist}
Url:            http://www.openstack.org/
Summary:        Python library for consuming OpenStack sevice-types-authority data
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
%if %{with_dnf}
Suggests:       %{?scl_prefix}python-hacking < 0.13
Suggests:       %{?scl_prefix}python-hacking >= 0.12.0

Conflicts:       %{?scl_prefix}python-coverage = 4.4,>=4.0
Suggests:       %{?scl_prefix}python-coverage >= 4.0
Suggests:       %{?scl_prefix}python-python-subunit >= 1.0.0
Conflicts:      %{?scl_prefix}python-sphinx =1.6.6
Suggests:       %{?scl_prefix}python-sphinx >=1.6.2
Suggests:       %{?scl_prefix}python-oslotest >= 3.2.0
Suggests:       %{?scl_prefix}python-testscenarios >= 0.4
Suggests:       %{?scl_prefix}python-requests-mock >= 1.1.0
Suggests:       %{?scl_prefix}python-openstackdocstheme >= 1.18.1
Suggests:       %{?scl_prefix}python-keystoneauth1 >= 3.3.0
# releasenotes
Suggests:       %{?scl_prefix}python-reno >= 2.5.0
%endif # with_dnf

%description
================
os-service-types
================

Python library for consuming OpenStack sevice-types-authority data

The `OpenStack Service Types Authority`_ contains information about official
OpenStack services and their historical ``service-type`` aliases.

The data is in JSON and the latest data should always be used. This simple
library exists to allow for easy consumption of the data, along with a built-in
version of the data to use in case network access is for some reason not
possible and local caching of the fetched data.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/os-service-types
* Source: http://git.openstack.org/cgit/openstack/os-service-types
* Bugs: https://storyboard.openstack.org/#!/project/904

.. _OpenStack Service Types Authority: https://service-types.openstack.org/





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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.2.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
