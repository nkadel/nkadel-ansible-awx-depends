%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}
%define _unpackaged_files_terminate_build 0

%define name azure-mgmt-rdbms
%define version 1.2.0
%define unmangled_version 1.2.0
%define unmangled_version 1.2.0
%define release 2

Summary: Microsoft Azure RDBMS Management Client Library for Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}azure-mgmt-rdbms
Version: %{version}
Release: %{release}
Source0: azure-mgmt-rdbms-%{unmangled_version}.zip
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/azure-mgmt-rdbms-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Microsoft Corporation <azpysdkhelp@microsoft.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/Azure/azure-sdk-for-python


%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure RDBMS Management Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.4, 3.5 and 3.6.

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

For code examples, see `PostgreSQL
<https://docs.microsoft.com/python/api/overview/azure/postgresql>`__
on docs.microsoft.com.

For code examples, see `MySQL
<https://docs.microsoft.com/python/api/overview/azure/mysql>`__
on docs.microsoft.com.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

1.2.0 (2018-05-30)
++++++++++++++++++

**Features**

- Added operation group VirtualNetworkRulesOperations
- Added operation group ServerSecurityAlertPoliciesOperations (PostgreSQL only)
- Client class can be used as a context manager to keep the underlying HTTP session open for performance

1.1.1 (2018-04-17)
++++++++++++++++++

**Bugfixes**

- Fix some invalid models in Python 3
- Compatibility of the sdist with wheel 0.31.0

1.1.0 (2018-03-29)
++++++++++++++++++

**Features**

- Add  Geo-Restore ability for MySQL and PostgreSQL

1.0.0 (2018-03-19)
++++++++++++++++++

**General Breaking changes**

This version uses a next-generation code generator that *might* introduce breaking changes.

- Model signatures now use only keyword-argument syntax. All positional arguments must be re-written as keyword-arguments.
  To keep auto-completion in most cases, models are now generated for Python 2 and Python 3. Python 3 uses the "*" syntax for keyword-only arguments.
- Enum types now use the "str" mixin (class AzureEnum(str, Enum)) to improve the behavior when unrecognized enum values are encountered.
  While this is not a breaking change, the distinctions are important, and are documented here:
  https://docs.python.org/3/library/enum.html#others
  At a glance:

  - "is" should not be used at all.
  - "format" will return the string value, where "%s" string formatting will return `NameOfEnum.stringvalue`. Format syntax should be prefered.

- New Long Running Operation:

  - Return type changes from `msrestazure.azure_operation.AzureOperationPoller` to `msrest.polling.LROPoller`. External API is the same.
  - Return type is now **always** a `msrest.polling.LROPoller`, regardless of the optional parameters used.
  - The behavior has changed when using `raw=True`. Instead of returning the initial call result as `ClientRawResponse`,
    without polling, now this returns an LROPoller. After polling, the final resource will be returned as a `ClientRawResponse`.
  - New `polling` parameter. The default behavior is `Polling=True` which will poll using ARM algorithm. When `Polling=False`,
    the response of the initial call will be returned without polling.
  - `polling` parameter accepts instances of subclasses of `msrest.polling.PollingMethod`.
  - `add_done_callback` will no longer raise if called after polling is finished, but will instead execute the callback right away.

**RDBMS breaking changes**

- Some properties moved from object "PerformanceTierProperties" to "PerformanceTierServiceLevelObjectives "(One level down).

Api Version is now 2017-12-01

0.3.1 (2018-02-28)
++++++++++++++++++

* Remove GeoRestore option that is not available yet.

0.3.0 (2018-02-26)
++++++++++++++++++

* New pricing model release

0.2.0rc1 (2017-10-16)
+++++++++++++++++++++

* VNET Rules API spec for Postgres and MySQL

0.1.0 (2017-05-08)
++++++++++++++++++

* Initial Release



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n azure-mgmt-rdbms-%{unmangled_version} -n azure-mgmt-rdbms-%{unmangled_version}
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
cat INSTALLED_FILES | \
	grep -v "%{python3_sitelib}/azure/__pycache__" | \
	grep -v "%{python3_sitelib}/azure/__init__.py" | \
	grep -v "%{python3_sitelib}/azure/mgmt/__pycache__" | \
	grep -v "%{python3_sitelib}/azure/mgmt/__init__.py" > INSTALLED_FILES_WITHOUT_COMMON_PYCACHE


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES_WITHOUT_COMMON_PYCACHE
%defattr(-,root,root)
%exclude %{python3_sitelib}/azure/__pycache__
%exclude %{python3_sitelib}/azure/__init__.py
%exclude %{python3_sitelib}/azure/mgmt/__pycache__
%exclude %{python3_sitelib}/azure/mgmt/__init__.py
