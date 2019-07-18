#
# spec file for package rh-python36-python-azure-mgmt-batch
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name azure-mgmt-batch

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
Version:        4.1.0
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Batch Management Client Library for Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
# Manually added
BuildRequires:  unzip
#Requires:       %{?scl_prefix}python-msrestazure~=0.4.7
#Requires:       %{?scl_prefix}python-azure-common~=1.1.5
Requires:       %{?scl_prefix}python-msrestazure >= 0.4.7
Requires:       %{?scl_prefix}python-azure-common >= 1.1.5
%if %{with_dnf}
%endif # with_dnf

%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Batch Management Client Library.

This package has been tested with Python 2.7, 3.3, 3.4 and 3.5.


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

For code examples, see `the Batch samples repo  
<https://github.com/Azure/azure-batch-samples/tree/master/Python>`__
on GitHub.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

4.1.0 (2017-07-24)
++++++++++++++++++

- New operation to check the availability and validity of a Batch account name.

4.0.0 (2017-05-10)
++++++++++++++++++

- New operation to list the operations available for the Microsoft.Batch provider, includes new `Operation` and `OperationDisplay` models.
- Renamed `AddApplicationParameters` to `ApplicationCreateParameters`.
- Renamed `UpdateApplicationParameters` to `ApplicationUpdateParameters`.
- Removed `core_quota` attribute from `BatchAccount` object, now replaced by separate `dedicated_core_quota` and `low_priority_core_quota`.
- `BatchAccountKeys` object now has additional `account_name` attribute.

3.0.1 (2017-04-19)
++++++++++++++++++

- This wheel package is now built with the azure wheel extension

3.0.0 (2017-03-07)
++++++++++++++++++

- Updated `BatchAccount` model - support for pool allocation in the user's subscription.
- Updated `BatchAccount` model - support for referencing an Azure Key Vault for accounts created with a pool allocation mode of UserSubscription.
- Updated `BatchAccount` model - properties are now read only.
- Updated `ApplicationPackage` model - properties are now read only.
- Updated `BatchAccountKeys` model - properties are now read only.
- Updated `BatchLocationQuota` model - properties are now read only.

2.0.0 (2016-10-04)
++++++++++++++++++

- Renamed `AccountResource` to `BatchAccount`.
- Renamed `AccountOperations` to `BatchAccountOperations`. The `IBatchManagementClient.Account` property was also renamed to `IBatchManagementClient.BatchAccount`.
- Split `Application` and `ApplicationPackage` operations up into two separate operation groups. 
- Updated `Application` and `ApplicationPackage` methods to use the standard `Create`, `Delete`, `Update` syntax. For example creating an `Application` is done via `ApplicationOperations.Create`.
- Renamed `SubscriptionOperations` to `LocationOperations` and changed `SubscriptionOperations.GetSubscriptionQuotas` to be `LocationOperations.GetQuotas`.
- This version targets REST API version 2015-12-01.

1.0.0 (2016-08-09)
++++++++++++++++++

- Initial Release




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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 4.1.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually exclude cross-duplicated files
