#
# spec file for package rh-python36-python-os-client-config
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name os-client-config

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
Version:        1.29.0
Release:        0%{?dist}
Url:            https://docs.openstack.org/os-client-config/latest
Summary:        OpenStack Client Configuation Library
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added for undocumented build requirement
BuildRequires:  %{?scl_prefix}python-pbr
# Manually added
Requires:       %{?scl_prefix}python-PyYAML >= 3.10
Requires:       %{?scl_prefix}python-appdirs >= 1.3.0
Requires:       %{?scl_prefix}python-keystoneauth1 >= 3.3.0
Requires:       %{?scl_prefix}python-requestsexceptions >= 1.2.0

%if %{with_dnf}
# Manually added for doc
Suggests:       %{?scl_prefix}python-docutils >= 0.11 
Conflicts:       %{?scl_prefix}python-sphinx =1.6.6
Suggests:       %{?scl_prefix}python-sphinx >= 1.6.2
Suggests:       %{?scl_prefix}python-openstackdocstheme >= 1.18.1
Suggests:       %{?scl_prefix}python-reno >= 2.5.0 
# Manually added for test
Conflicts:      %{?scl_prefix}python-hacking = 0.13
Suggests:       %{?scl_prefix}python-hacking < 0.14
Suggests:       %{?scl_prefix}python-hacking >= 0.12.0
Conflicts:       %{?scl_prefix}python-coverage = 4.4
Suggests:       %{?scl_prefix}python-coverage >= 4.0 # Apache-2.0
Suggests:       %{?scl_prefix}python-extras >= 1.0.0
Suggests:       %{?scl_prefix}python-fixtures >= 3.0.0
Suggests:       %{?scl_prefix}python-jsonschema < 3.0.0
Suggests:       %{?scl_prefix}python-jsonschema >= 2.6.0
Suggests:       %{?scl_prefix}python-mock >= 2.0.0
Suggests:       %{?scl_prefix}python-python-glanceclient >= 2.8.0
Suggests:       %{?scl_prefix}python-python-subunit >= 1.0.0
Suggests:       %{?scl_prefix}python-oslotest >= 3.2.0
Suggests:       %{?scl_prefix}python-stestr >= 1.0.0
Suggests:       %{?scl_prefix}python-testscenarios >= 0.4
Suggests:       %{?scl_prefix}python-testtools >= 2.2.0
%endif # with_dnf

%description
================
os-client-config
================

.. image:: http://governance.openstack.org/badges/os-client-config.svg
    :target: http://governance.openstack.org/reference/tags/index.html

`os-client-config` is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want to
put in a config file. It will read environment variables and config files,
and it also contains some vendor specific default values so that you do not
have to know extra info to use OpenStack

* If you have a config file, you will get the clouds listed in it
* If you have environment variables, you will get a cloud named `envvars`
* If you have neither, you will get a cloud named `defaults` with base defaults

Source
------

* Free software: Apache license
* Documentation: http://docs.openstack.org/os-client-config/latest
* Source: http://git.openstack.org/cgit/openstack/os-client-config
* Bugs: http://bugs.launchpad.net/os-client-config


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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.10-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Add unlisted pyton-pbr to BuildRequires
