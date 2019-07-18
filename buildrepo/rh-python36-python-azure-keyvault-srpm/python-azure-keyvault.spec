#
# spec file for package rh-python36-python-azure-keyvault
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name azure-keyvault

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
Version:        1.1.0
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Key Vault Client Library for Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-msrestazure >= 0.4.15
Requires:       %{?scl_prefix}python-msrestazure < 2.0.0
# Original stanza msrest >= 0.4.17azure-common~=1.1.5
Requires:       %{?scl_prefix}python-msrest >= 0.5.0
Requires:       %{?scl_prefix}python-azure-common >= 1.1.5
Requires:       %{?scl_prefix}python-cryptography >= 2.1.4
Requires:       %{?scl_prefix}python-requests >= 2.18.4
%if %{with_dnf}
%endif # with_dnf

%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Key Vault Client Library.

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

For code examples, see `Key Vault
<https://azure-sdk-for-python.readthedocs.org/en/latest/sample_azure-keyvault.html>`__
on readthedocs.org.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============
1.0.0a1 (2018-01-25)
++++++++++++++++++++
* Added message encryption support for message encryption enabled vaults

0.3.7 (2017-09-22)
++++++++++++++++++

* Workaround for Azure Stack ADFS authentication issue https://github.com/Azure/azure-cli/issues/4448

0.3.6 (2017-08-16)
++++++++++++++++++

* Updated KeyVaultClient to accept both KeyVaultAuthentication and azure.common.credentials instances for authentication

0.3.5 (2017-06-23)
++++++++++++++++++

* Fix: https://github.com/Azure/azure-sdk-for-python/issues/1159
* KeyVaultId refactoring
  - adding object specific id classes to make usage more uniform with other key vault SDKs
  - added storage account id and storage sas definition id parsing and formatting

0.3.4 (2017-06-07)
++++++++++++++++++

* Adding Preview Features
  - Managed Storage Account keys for managing storage credentials and provisioning SAS tokens
  - Key Vault "Soft Delete" allowing for recovery of deleted keys, secrets and certificates
  - Secret Backup and Restore for secret recovery and migration

0.3.3 (2017-05-10)
++++++++++++++++++

* Reverting to 0.3.0, since behavior of 0.3.2 is not satisfaying either.

0.3.2 (2017-05-09)
++++++++++++++++++

* Fix critical regression on 0.3.1 (#1157)
* Now the client respects 'REQUESTS_CA_BUNDLE' and 'CURL_CA_BUNDLE'

0.3.1 (2017-05-09)
++++++++++++++++++

* Support for REQUESTS_CA_BUNDLE (#1154)

0.3.0 (2017-05-08)
++++++++++++++++++

* Moving KeyVaultClient class to the azure.keyvault namespace
* Moving model classes to the azure.keyvault.models namespace
* Deprecating 'generated' namespaces azure.keyvault.generated and azure.keyvault.generated.models
* Exposed KeyVaultId class through azure.keyvault namespace
* Moving identifier parsing methods to static methods on KeyVaultId class
* Removing convenience overridden methods from KeyVaultClient
  - update_key(self, key_identifier, ...
  - get_key(self, key_identifier, ...
  - encrypt(self, key_identifier, ...
  - decrypt(self, key_identifier, ...
  - sign(self, key_identifier, ...
  - verify(self, key_identifier, ...
  - wrap_key(self, key_identifier, ...
  - unwrap_key(self, key_identifier, ...
  - update_secret(self, secret_identifer, ...
  - get_secret(self, secret_identifer, ...
  - get_certificate(self, certificate_identifier, ...

0.2.0 (2017-04-19)
++++++++++++++++++

**Bugfixes**

- Fix possible deserialization error, but updating from list<enumtype> to list<str> when applicable

**Notes**

- This wheel package is now built with the azure wheel extension

0.1.0 (2016-12-29)
++++++++++++++++++

* Initial Release




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

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.1.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- python-azure-common updated to >= 1.1.5 from = 1.1.5
- Manually exclude cross-duplicated files
