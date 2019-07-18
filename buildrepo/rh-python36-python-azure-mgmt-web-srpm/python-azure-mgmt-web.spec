#
# spec file for package rh-python36-python-azure-mgmt-web
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name azure-mgmt-web

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
Version:        0.32.0
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Web Apps Resource Management Client Library for Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  unzip
# Manually added from requires.txt
#Requires:       %{?scl_prefix}python-msrestazure~=0.4.7
#Requires:       %{?scl_prefix}python-azure-common~=1.1.5
Requires:       %{?scl_prefix}python-msrestazure >= 0.4.7
Requires:       %{?scl_prefix}python-azure-common >= 1.1.5
%if %{with_dnf}
%endif # with_dnf

%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Web Apps Resource Management Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.3, 3.4 and 3.5.

For the older Azure Service Management (ASM) libraries, see
`azure-servicemanagement-legacy <https://pypi.python.org/pypi/azure-servicemanagement-legacy>`__ library.

For a more complete set of Azure libraries, see the `azure <https://pypi.python.org/pypi/azure>`__ bundle package.


Compatibility
=============

**IMPORTANT**: If you have an earlier version of the azure package
(version < 1.0), you should uninstall it before installing this package.

You can check the version using pip:

.. code:: shell

    pip freeze

If you see azure==0.11.0 (or any version below 1.0), uninstall it first:

.. code:: shell

    pip uninstall azure


Usage
=====

For code examples, see `Web Apps Resource Management 
<https://azure-sdk-for-python.readthedocs.org/en/latest/resourcemanagementapps.html>`__
on readthedocs.org.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

0.32.0 (2017-04-26)
+++++++++++++++++++

* Support list web runtime stacks
* Expose non resource based model type for SiteConfig, SiteAuthSettings, etc, to be used as property
* Support list linux web available regions

0.31.1 (2017-04-20)
+++++++++++++++++++

This wheel package is now built with the azure wheel extension

0.31.0 (2017-02-13)
+++++++++++++++++++

* Major refactoring and breaking changes
* New API Version

0.30.0 (2016-10-17)
+++++++++++++++++++

* Initial release

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
%exclude %{python3_sitelib}/azure/__init__.py
%exclude %{python3_sitelib}/azure/__pycache__
%exclude %{python3_sitelib}/azure/mgmt/__init__.py
%exclude %{python3_sitelib}/azure/mgmt/__pycache__

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.32.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually exclude cross-duplicated files
