#
# spec file for package rh-python36-python-pbr
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pbr

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
Version:        5.1.1
Release:        0%{?dist}
Url:            https://docs.openstack.org/pbr/latest/
Summary:        Python Build Reasonableness
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-sphinx >= 1.6.2
Conflicts:      %{?scl_prefix}python-sphinx = 1.6.6
Conflicts:      %{?scl_prefix}python-sphinx = 1.6.7
Requires:       %{?scl_prefix}python-openstackdocstheme >= 1.18.1
Requires:       %{?scl_prefix}python-reno >= 2.5.0

%if %{with_dnf}
# The order of packages is significant, because pip processes them in the order
# of appearance. Changing the order has an impact on the overall integration
# process, which may cause wedges in the gate later.
Suggests:       %{?scl_prefix}python-wheel >= 0.32.0
Suggests:       %{?scl_prefix}python-fixtures >= 3.0.0
Conflicts:      %{?scl_prefix}python-hacking = 0.13.0
Suggests:       %{?scl_prefix}python-hacking  < 0.14
Suggests:       %{?scl_prefix}python-hacking >=0.12.0
Suggests:       %{?scl_prefix}python-mock >= 2.0.0
Suggests:       %{?scl_prefix}python-six >= 1.10.0
Suggests:       %{?scl_prefix}python-stestr >= 2.1.0
Suggests:       %{?scl_prefix}python-testresources >= 2.0.0
Suggests:       %{?scl_prefix}python-testscenarios >= 0.4
Suggests:       %{?scl_prefix}python-testtools >= 2.2.0
Suggests:       %{?scl_prefix}python-virtualenv >= 14.0.6
Conflicts:      %{?scl_prefix}python-coverage = 4.4
Suggests:       %{?scl_prefix}python-coverage >= 4.0

# optionally exposed by distutils commands
Suggests:       %{?scl_prefix}python-sphinx >= 1.6.2 # BSD
Conflicts:      %{?scl_prefix}python-sphinx =1.6.6
Conflicts:      %{?scl_prefix}python-sphinx =1.6.7
Suggests:       %{?scl_prefix}python-testrepository >= 0.0.18

# test requirements
# For python 2.6
#Suggests:       %{?scl_prefix}python-ordereddict
Suggests:       %{?scl_prefix}python-requests-mock

%endif # with_dnf

%description
Introduction
============

.. image:: https://img.shields.io/pypi/v/pbr.svg
    :target: https://pypi.python.org/pypi/pbr/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/pbr.svg
    :target: https://pypi.python.org/pypi/pbr/
    :alt: Downloads

PBR is a library that injects some useful and sensible default behaviors
into your setuptools run. It started off life as the chunks of code that
were copied between all of the `OpenStack`_ projects. Around the time that
OpenStack hit 18 different projects each with at least 3 active branches,
it seemed like a good time to make that code into a proper reusable library.

PBR is only mildly configurable. The basic idea is that there's a decent
way to run things and if you do, you should reap the rewards, because then
it's simple and repeatable. If you want to do things differently, cool! But
you've already got the power of Python at your fingertips, so you don't
really need PBR.

PBR builds on top of the work that `d2to1`_ started to provide for declarative
configuration. `d2to1`_ is itself an implementation of the ideas behind
`distutils2`_. Although `distutils2`_ is now abandoned in favor of work towards
`PEP 426`_ and Metadata 2.0, declarative config is still a great idea and
specifically important in trying to distribute setup code as a library
when that library itself will alter how the setup is processed. As Metadata
2.0 and other modern Python packaging PEPs come out, PBR aims to support
them as quickly as possible.

* License: Apache License, Version 2.0
* Documentation: https://docs.openstack.org/pbr/latest/
* Source: https://git.openstack.org/cgit/openstack-dev/pbr
* Bugs: https://bugs.launchpad.net/pbr
* Change Log: https://docs.openstack.org/pbr/latest/user/history.html

.. _d2to1: https://pypi.python.org/pypi/d2to1
.. _distutils2: https://pypi.python.org/pypi/Distutils2
.. _PEP 426: http://legacy.python.org/dev/peps/pep-0426/
.. _OpenStack: https://www.openstack.org/





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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 5.1.1-0
- Update .spec from py2pack
- Manually add Requires and Suggests

