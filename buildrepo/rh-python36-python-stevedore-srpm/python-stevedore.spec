#
# spec file for package rh-python36-python-stevedore
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name stevedore

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
Version:        1.28.0
Release:        0%{?dist}
Url:            https://docs.openstack.org/stevedore/latest/
Summary:        Manage dynamic plugins for Python applications
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-pbr >= 2.0.0
BuildRequires:  %{?scl_prefix}python-pbr >= 2.0.0
Requires:       %{?scl_prefix}python-pbr >= 2.0.0
Conflicts:      %{?scl_prefix}python-pbr 2.1.0
Requires:       %{?scl_prefix}python-six >= 1.10.0
%if %{with_dnf}
# Manually added for docs
Suggests:       %{?scl_prefix}python-openstackdocstheme >= 1.17.0
Suggests:       %{?scl_prefix}python-reno >= 2.5.0
Suggests:       %{?scl_prefix}python-sphinx >= 1.6.2
# Manually added for tests
Suggests:       %{?scl_prefix}python-mock >= 2.0.0
Suggests:       %{?scl_prefix}python-coverage >= 4.0
Conflicts:      %{?scl_prefix}python-coverage = 4.4
Suggests:       %{?scl_prefix}python-testrepository >= 0.0.18
# sphinx is needed for testing the sphinxext module
Suggests:       %{?scl_prefix}python-sphinx >= 1.6.2
# Bandit security code scanner
Suggests:       %{?scl_prefix}python-bandit >= 1.1.0
%endif # with_dnf

%description
===========================================================
stevedore -- Manage dynamic plugins for Python applications
===========================================================

Python makes loading code dynamically easy, allowing you to configure
and extend your application by discovering and loading extensions
("*plugins*") at runtime. Many applications implement their own
library for doing this, using ``__import__`` or ``importlib``.
stevedore avoids creating yet another extension
mechanism by building on top of `setuptools entry points`_. The code
for managing entry points tends to be repetitive, though, so stevedore
provides manager classes for implementing common patterns for using
dynamically loaded extensions.

.. _setuptools entry points: http://setuptools.readthedocs.io/en/latest/pkg_resources.html?#entry-points

* Free software: Apache license
* Documentation: https://docs.openstack.org/stevedore/latest
* Source: https://git.openstack.org/cgit/openstack/stevedore
* Bugs: https://bugs.launchpad.net/python-stevedore

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.28.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
