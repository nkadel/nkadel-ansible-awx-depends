#
# spec file for package rh-python36-python-selenium
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name selenium

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
Version:        3.141.0
Release:        0%{?dist}
Url:            https://github.com/SeleniumHQ/selenium/
Summary:        Python bindings for Selenium
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-urllib3
%if %{with_dnf}
%endif # with_dnf

%description
======================
Selenium Client Driver
======================

Introduction
============

Python language bindings for Selenium WebDriver.

The `selenium` package is used to automate web browser interaction from Python.

+-----------+--------------------------------------------------------------------------------------+
| **Home**: | http://www.seleniumhq.org                                                            |
+-----------+--------------------------------------------------------------------------------------+
| **Docs**: | `selenium package API <https://seleniumhq.github.io/selenium/docs/api/py/api.html>`_ |
+-----------+--------------------------------------------------------------------------------------+
| **Dev**:  | https://github.com/SeleniumHQ/Selenium                                               |
+-----------+--------------------------------------------------------------------------------------+
| **PyPI**: | https://pypi.org/project/selenium/                                                   |
+-----------+--------------------------------------------------------------------------------------+
| **IRC**:  | **#selenium** channel on freenode                                                    |
+-----------+--------------------------------------------------------------------------------------+

Several browsers/drivers are supported (Firefox, Chrome, Internet Explorer), as well as the Remote protocol.

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
# Despite not being noarch, use sitelib
%{python3_sitelib}/*

%changelog
* Sat Jul 13 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 3.141.0-0
- Update .spec file with py2pack
- Add Requires for urllib3
