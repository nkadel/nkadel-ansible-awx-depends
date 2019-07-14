#
# spec file for package rh-python36-python-vine
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name vine
%{?scl:%scl_package python-vine}
%{!?scl:%global pkg_name python-vine}

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Common SRPM package
Name:           %{?scl_prefix}python-vine
Version:        1.2.0
Release:        0%{?dist}
Url:            http://github.com/celery/vine
Summary:        Promises, promises, promises.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=vine; echo ${n:0:1})/vine/vine-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
=====================================================================
 vine - Python Promises
=====================================================================

|build-status| |coverage| |license| |wheel| |pyversion| |pyimp|

:Version: 1.2.0
:Web: https://vine.readthedocs.io/
:Download: https://pypi.org/project/vine/
:Source: http://github.com/celery/vine/
:Keywords: promise, async, future

About
=====


.. |build-status| image:: https://secure.travis-ci.org/celery/vine.png?branch=master
    :alt: Build status
    :target: https://travis-ci.org/celery/vine

.. |coverage| image:: https://codecov.io/github/celery/vine/coverage.svg?branch=master
    :target: https://codecov.io/github/celery/vine?branch=master

.. |license| image:: https://img.shields.io/pypi/l/vine.svg
    :alt: BSD License
    :target: https://opensource.org/licenses/BSD-3-Clause

.. |wheel| image:: https://img.shields.io/pypi/wheel/vine.svg
    :alt: Vine can be installed via wheel
    :target: https://pypi.org/project/vine/

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/vine.svg
    :alt: Supported Python versions.
    :target: https://pypi.org/project/vine/

.. |pyimp| image:: https://img.shields.io/pypi/implementation/vine.svg
    :alt: Support Python implementations.
    :target: https://pypi.org/project/vine/





%prep
%setup -q -n vine-%{version}

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