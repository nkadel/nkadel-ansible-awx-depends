#
# spec file for package rh-python36-python-azure-mgmt-monitor
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name azure-mgmt-monitor

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
Version:        0.5.2
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Monitor Client Library for Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  unzip
%if %{with_dnf}
%endif # with_dnf

%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Monitor Client Library.

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

For code examples, see `Monitor
<https://docs.microsoft.com/python/api/overview/azure/monitoring>`__
on docs.microsoft.com.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

0.5.2 (2018-06-06)
++++++++++++++++++

**Features**

- Model ActionGroupResource has a new parameter voice_receivers
- Model ActionGroupResource has a new parameter azure_function_receivers
- Model ActionGroupResource has a new parameter logic_app_receivers
- Added operation group MetricAlertsOperations
- Added operation group ScheduledQueryRulesOperations
- Added operation group MetricAlertsStatusOperations

0.5.1 (2018-04-16)
++++++++++++++++++

**Bugfixes**

- Fix some invalid models in Python 3
- Compatibility of the sdist with wheel 0.31.0

0.5.0 (2017-03-19)
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

**Bugfixes**

- Fix invalid type of "top" in metrics.list operation

**Features**

- New operation group metric_baseline
- Add attribute action_group_resource itsm_receivers
- Add operation action_groups.update
- Add new parameter "metricnames" to metrics.list
- Add new parameter "metricnamespace" to metrics.list
- All operations group have now a "models" attribute

New ApiVersion version of metrics to 2018-01-01

0.4.0 (2017-10-25)
++++++++++++++++++

**Features**

- Merge into this package the "azure-monitor" package including following operations groups

  - event categories
  - activity log
  - tenant activity log
  - metrics definitions
  - metrics

- Adding new multi-dimensional metrics API

**Breaking changes**

- Some exceptions have moved from CloudError to ErrorResponseException
- "service_diagnostic_settings" renamed to "diagnostic_settings"

- Update API version of "metrics". Migrating from "azure-monitor" to "metrics" here needs to be rewritten.

**Bug fixes**

- Improving HTTP status code check for better exception

0.3.0 (2017-06-30)
++++++++++++++++++

**Features**

- Add action_groups operation group
- Add alert_rules.update method
- Add autoscale_settings.update method
- Add log_profiles.update method

**Breaking changes**

- activity_log_alerts.update has now flatten parameters "tags/enabled"

0.2.1 (2017-04-26)
++++++++++++++++++

* Removal of a REST endpoint not ready to release.

0.2.0 (2017-04-19)
++++++++++++++++++

* Add ActivityLogAlerts and DiagnosticSettings
* Minor improvements, might be breaking
* This wheel package is now built with the azure wheel extension

0.1.0 (2017-02-16)
++++++++++++++++++

* Initial Release




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

%changelog