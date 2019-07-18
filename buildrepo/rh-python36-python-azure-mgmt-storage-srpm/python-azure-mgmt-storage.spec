#
# spec file for package rh-python36-python-azure-mgmt-storage
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name azure-mgmt-storage

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
Version:        1.5.0
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Storage Management Client Library for Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  unzip
#Requires:       %{?scl_prefix}python-msrestazure~=0.4.11
#Requires:       %{?scl_prefix}python-azure-common~=1.1
Requires:       %{?scl_prefix}python-msrestazure >= 0.4.11
Requires:       %{?scl_prefix}python-azure-common >= 1.1

%if %{with_dnf}
%endif # with_dnf

%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Storage Management Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.3, 3.4, 3.5 and 3.6.

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

For code examples, see `Storage Resource Management 
<https://azure-sdk-for-python.readthedocs.org/en/latest/resourcemanagementstorage.html>`__
on readthedocs.org.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

1.5.0 (2017-12-12)
++++++++++++++++++

**Features**

- Add StorageV2 as valid kind
- Add official support for API version 2017-10-01

1.4.0 (2017-09-26)
++++++++++++++++++

**Bug fixes**

- Add skus operations group to the generic client

**Features**

- Add official support for API version 2016-01-01

1.3.0 (2017-09-08)
++++++++++++++++++

**Features**

- Adds list_skus operation (2017-06-01)

**Breaking changes**

- Rename the preview attribute "network_acls" to "network_rule_set"

1.2.1 (2017-08-14)
++++++++++++++++++

**Bugfixes**

- Remove "tests" packaged by mistake (#1365)

1.2.0 (2017-07-19)
++++++++++++++++++

**Features**

- Api version 2017-06-01 is now the default
- This API version adds Network ACLs objects (2017-06-01 as preview)

1.1.0 (2017-06-28)
++++++++++++++++++

- Added support for https traffic only (2016-12-01)

1.0.0 (2017-05-15)
++++++++++++++++++

- Tag 1.0.0rc1 as stable (same content)

1.0.0rc1 (2017-04-11)
+++++++++++++++++++++

**Features**

To help customers with sovereign clouds (not general Azure),
this version has official multi ApiVersion support for 2015-06-15 and 2016-12-01

0.31.0 (2017-01-19)
+++++++++++++++++++

* New `list_account_sas` operation
* New `list_service_sas` operation
* Name syntax are now checked before RestAPI call, not the server (exception changed)

Based on API version 2016-12-01.

0.30.0 (2016-11-14)
+++++++++++++++++++

* Initial release. Based on API version 2016-01-01
  Note that this is the same content as 0.30.0rc6, committed as 0.30.0.

0.20.0 (2015-08-31)
+++++++++++++++++++

* Initial preview release. Based on API version 2015-05-01-preview.




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
# Manually exclude cross-duplicated files
%exclude %{python3_sitelib}/azure/__init__.py
%exclude %{python3_sitelib}/azure/__pycache__
%exclude %{python3_sitelib}/azure/mgmt/__init__.py
%exclude %{python3_sitelib}/azure/mgmt/__pycache__

%changelog
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.5.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually exclude cross-duplicated files
