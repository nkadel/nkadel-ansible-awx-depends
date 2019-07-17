#
# spec file for package rh-python36-python-azure-mgmt-sql
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name azure-mgmt-sql

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
Version:        0.7.1
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure SQL Management Client Library for Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  unzip
#Requires:       %{?scl_prefix}python-azure-common~=1.1.5
#Requires:       %{?scl_prefix}python-msrestazure~=0.4.8
Requires:       %{?scl_prefix}python-azure-common >= 1.1.5
Requires:       %{?scl_prefix}python-msrestazure >= 0.4.8

%if %{with_dnf}
%endif # with_dnf

%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure SQL Management Client Library.

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

For code examples, see `SQL Management
<https://azure-sdk-for-python.readthedocs.org/en/latest/sample_azure-mgmt-sql.html>`__
on readthedocs.org.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

0.7.1 (2017-06-30)
++++++++++++++++++

- Added support for server connection policies
- Fixed error in databases_operations.create_or_update_threat_detection_policy

0.7.0 (2017-06-28)
++++++++++++++++++

**features**

- Backup/Restore related: RecoverableDatabase, RestorableDroppedDatabase, BackupLongTermRetentionVault, BackupLongTermRetentionPolicy, and GeoBackupPolicy
- Data Masking rules and policies
- Server communication links

**Breaking changes**

- Renamed enum RestorePointTypes to RestorePointType
- Renamed VnetFirewallRule and related operations to VirtualNetworkRule

0.6.0 (2017-06-13)
++++++++++++++++++

- Updated Servers api version from 2014-04-01 to 2015-05-01-preview, which is SDK compatible and includes support for server managed identity
- Added support for server keys and encryption protectors
- Added support for check server name availability
- Added support for virtual network firewall rules
- Updated server azure ad admin from swagger
- Minor nonfunctional updates to database blob auditing
- Breaking changes DatabaseMetrics and ServerMetrics renamed to DatabaseUsage and ServerUsage. These were misleadingly named because metrics is a different API.
- Added database metrics and elastic pool metrics

0.5.3 (2017-06-01)
++++++++++++++++++

- Update minimal dependency to msrestazure 0.4.8

0.5.2 (2017-05-31)
++++++++++++++++++

**Features**

- Added support for server active directory administrator, failover groups, and virtual network rules
- Minor changes to database auditing support

0.5.1 (2017-04-28)
++++++++++++++++++

**Bugfixes**

- Fix return exception in import/export

0.5.0 (2017-04-19)
++++++++++++++++++

**Breaking changes**

- `SqlManagementClient.list_operations` is now `SqlManagementClient.operations.list`

**New features**

- Added elastic pool capabilities to capabilities API.

**Notes**

* This wheel package is now built with the azure wheel extension

0.4.0 (2017-03-22)
++++++++++++++++++

Capabilities and security policy features.

Also renamed several types and operations for improved clarify and
consistency.

Additions:

* BlobAuditingPolicy APIs (e.g. databases.create_or_update_blob_auditing_policy)
* ThreatDetectionPolicy APIs (e.g. databases.create_or_update_threat_detection_policy)
* databases.list_by_server now supports $expand parameter
* Capabilities APIs (e.g. capabilities.list_by_location)

Classes and enums renamed:

* ServerFirewallRule -> FirewallRule
* DatabaseEditions -> DatabaseEdition
* ElasticPoolEditions -> ElasticPoolEdition
* ImportRequestParameters -> ImportRequest
* ExportRequestParameters -> ExportRequest
* ImportExportOperationResponse -> ImportExportResponse
* OperationMode -> ImportOperationMode
* TransparentDataEncryptionStates -> TransparentDataEncryptionStatus

Classes removed:

* Unused types: UpgradeHint, Schema, Table, Column

Operations renamed:

* servers.get_by_resource_group -> servers.get
* servers.create_or_update_firewall_rule -> firewall_rules.create_or_update, and similar for get, list, and delete
* databases.import -> databases.create_import_operation
* servers.import -> databases.import
* databases.pause_data_warehouse -> databases.pause
* databases.resume_data_warehouse -> databases.resume
* recommended_elastic_pools.list -> recommended_elastic_pools.list_by_server

Operations removed:

* Removed ImportExport operation results APIs since these are handled automatically by Azure async pattern.

0.3.3 (2017-03-14)
++++++++++++++++++

* Add database blob auditing and threat detection operations

0.3.2 (2017-03-08)
++++++++++++++++++

* Add import/export operations
* Expanded documentation of create modes

0.3.1 (2017-03-01)
++++++++++++++++++

* Added &#8216;filter&#8217; param to list databases

0.3.0 (2017-02-27)
++++++++++++++++++

**Breaking changes**

* Enums:

  * createMode renamed to CreateMode
  * Added ReadScale, SampleName, ServerState

* Added missing Database properties (failover_group_id, restore_point_in_time, read_scale, sample_name)
* Added missing ElasticPoolActivity properties (requested_*)
* Added missing ReplicationLink properties (is_termination_allowed, replication_mode)
* Added missing Server properties (external_administrator_*, state)
* Added operations APIs
* Removed unused Database.upgrade_hint property
* Removed unused RecommendedDatabaseProperties class
* Renamed incorrect RecommendedElasticPool.databases_property to databases
* Made firewall rule start/end ip address required
* Added missing kind property to many resources
* Many doc clarifications

0.2.0 (2016-12-12)
++++++++++++++++++

**Breaking changes**

* Parameters re-ordering (list_database_activity)
* Flatten create_or_update_firewall_rule from "parameters" to "start_ip_address" and "end_ip_address"

0.1.0 (2016-11-02)
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

%changelog
