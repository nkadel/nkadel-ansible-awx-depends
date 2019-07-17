%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name pbr
%define version 5.1.1
%define unmangled_version 5.1.1
%define unmangled_version 5.1.1
%define release 1

Summary: Python Build Reasonableness
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}pbr
Version: %{version}
Release: %{release}
Source0: pbr-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/pbr-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: OpenStack <openstack-dev@lists.openstack.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://docs.openstack.org/pbr/latest/


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
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n pbr-%{unmangled_version} -n pbr-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
