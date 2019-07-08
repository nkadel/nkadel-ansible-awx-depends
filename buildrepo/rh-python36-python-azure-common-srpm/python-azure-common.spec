#
# spec file for package rh-python36-python-azure-common
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name azure-common

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
Version:        1.1.11
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Client Library for Python (Common)
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
# [autorest]
Suggests: %{?scl_prefix}python-msrestazure < 2.0.0
Suggests: %{?scl_prefix}python-msrestazure >= 0.4.0
%endif # with_dnf

%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure common code.

This package provides shared code by the Azure packages.

If you are looking to install the Azure client libraries, see the
`azure <https://pypi.python.org/pypi/azure>`__ bundle package.


.. :changelog:

Release History
===============

1.1.11 (2018-05-08)
+++++++++++++++++++

**Features**

- Add support for "resource" in "get_azure_cli_credentials"

1.1.10 (2018-04-30)
+++++++++++++++++++

**Bugfixes**

- Fix MultiApiClientMixin.__init__ to be a real mixin

1.1.9 (2018-04-03)
++++++++++++++++++

**Features**

- Add "azure.profiles" namespace #2247

**Bugfixes**

- get_client_from_cli_profile now supports Datalake #2318

1.1.8 (2017-07-28)
++++++++++++++++++

**Bugfix**

- Fix get_client_from_auth_file and get_client_from_json_dict on Python 2.7

Thank you to @jayden-at-arista for the contribution.

1.1.7 (2017-07-19)
++++++++++++++++++

- Adds azure.common.client_factory.get_client_from_auth_file
- Adds azure.common.client_factory.get_client_from_json_dict

1.1.6 (2017-05-16)
++++++++++++++++++

- Adds azure.common.client_factory.get_client_from_cli_profile

1.1.5 (2017-04-11)
++++++++++++++++++

- "extra_requires" autorest is deprecated and should not be used anymore
- This wheel package is now built with the azure wheel extension

1.1.4 (2016-05-25)
++++++++++++++++++

- Support for msrest/msrestazure 0.4.x series
- Drop support for msrest/msrestazure 0.3.x series

1.1.3 (2016-04-26)
++++++++++++++++++

- Support for msrest/msrestazure 0.3.x series
- Drop support for msrest/msrestazure 0.2.x series

1.1.2 (2016-03-28)
++++++++++++++++++

- Support for msrest/msrestazure 0.2.x series
- Drop support for msrest/msrestazure 0.1.x series

1.1.1 (2016-03-07)
++++++++++++++++++

- Move msrestazure depency as "extra_requires"

1.1.0 (2016-03-04)
++++++++++++++++++

- Support for msrest/msrestazure 0.1.x series
- Adds alias from msrestazure.azure_active_directory.* to azure.common.credentials

1.0.0 (2015-08-31)
++++++++++++++++++

Initial release, extracted from azure==0.11.1




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
