#
# spec file for package rh-python36-python-azure-mgmt-network
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name azure-mgmt-network

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
Version:        1.7.1
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Network Management Client Library for Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  unzip
#Requires:       %{?scl_prefix}python-msrestazure ~= 0.4.11
#Requires:       %{?scl_prefix}python-azure-common ~= 1.1
Requires:       %{?scl_prefix}python-msrestazure >= 0.4.11
Requires:       %{?scl_prefix}python-azure-common >= 1.1
%if %{with_dnf}
%endif # with_dnf

%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Network Management Client Library.

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

For code examples, see `Compute and Network Resource Management 
<https://azure-sdk-for-python.readthedocs.org/en/latest/resourcemanagementcomputenetwork.html>`__
on readthedocs.org.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

1.7.1 (2017-12-20)
++++++++++++++++++

**Bugfixes**

Fix `SecurityRule` constructor parameters order to respect the one used until 1.5.0.
This indeed introduces a breaking change for users of 1.6.0 and 1.7.0, but this constructor signature change was
not expected, and following semantic versionning all 1.x versions should follow the same signature.

This fixes third party library, like Ansible, that expects (for excellent reasons) this SDK to follow strictly semantic versionning
with regards to breaking changes and have their dependency system asking for `>=1.0;<2.0`

1.7.0 (2017-12-14)
++++++++++++++++++

**Features**

- Add iptag. IpTag is way to restrict the range of IPaddresses to be allocated.
- Default API version is now 2017-11-01

**Bug fixes**

- Added valid ASN range in ExpressRouteCircuitPeering (#1672)

1.6.0 (2017-11-28)
++++++++++++++++++

**Bug fixes**

- Accept space in location for "usage" (i.e. "west us").
- sourceAddressPrefix, sourceAddressPrefixes and sourceApplicationSecurityGroups 
  are mutually exclusive and one only is needed, meaning none of them is required 
  by itself. Thus, sourceAddressPrefix is not required anymore.
- destinationAddressPrefix, destinationAddressPrefixes and destinationApplicationSecurityGroups 
  are mutually exclusive and one only is needed, meaning none of them is required 
  by itself. Thus, destinationAddressPrefix is not required anymore.
- Client now accept unicode string as a valid subscription_id parameter
- Restore missing azure.mgmt.network.__version__

**Features**

- Client now accept a "profile" parameter to define API version per operation group.
- Add update_tags to most of the resources
- Add operations group to list all available rest API operations
- NetworkInterfaces_ListVirtualMachineScaleSetIpConfigurations
- NetworkInterfaces_GetVirtualMachineScaleSetIpConfiguration

1.5.0 (2017-09-26)
++++++++++++++++++

**Features**

- Availability Zones
- Add network_watchers.get_azure_reachability_report
- Add network_watchers.list_available_providers
- Add virtual_network_gateways.supported_vpn_devices
- Add virtual_network_gateways.vpn_device_configuration_script

1.5.0rc1 (2017-09-18)
+++++++++++++++++++++

**Features**

- Add ApiVersion 2017-09-01 (new default)
- Add application_security_groups (ASG) operations group
- Add ASG to network_interface operations
- Add ASG to IP operations
- Add source/destination ASGs to network security rules
- Add DDOS protection and VM protection to vnet operations

**Bug fix**

- check_dns_name_availability now correctly defines "domain_name_label" as required and not optional

1.4.0 (2017-08-23)
++++++++++++++++++

**Features**

- Add ApiVersion 2017-08-01 (new default)
- Added in both 2017-08-01 and 2017-06-01:

  - virtual_network_gateways.list_connections method
  - default_security_rules operations group
  - inbound_nat_rules operations group
  - load_balancer_backend_address_pools operations group
  - load_balancer_frontend_ip_configurations operations group
  - load_balancer_load_balancing_rules operations group
  - load_balancer_network_interfaces operations group
  - load_balancer_probes operations group
  - network_interface_ip_configurations operations group
  - network_interface_load_balancers operations group
  - EffectiveNetworkSecurityGroup.tag_map attribute
  - EffectiveNetworkSecurityRule.source_port_ranges attribute
  - EffectiveNetworkSecurityRule.destination_port_ranges attribute
  - EffectiveNetworkSecurityRule.source_address_prefixes attribute
  - EffectiveNetworkSecurityRule.destination_address_prefixes attribute
  - SecurityRule.source_port_ranges attribute
  - SecurityRule.destination_port_ranges attribute
  - SecurityRule.source_address_prefixes attribute
  - SecurityRule.destination_address_prefixes attribute

- Added in 2017-08-01 only

  - PublicIPAddress.sku
  - LoadBalancer.sku

**Changes on preview**

  - "available_private_access_services" is renamed "available_endpoint_services"
  - "radius_secret" parsing fix (was unable to work in 1.3.0)


1.3.0 (2017-07-10)
++++++++++++++++++

**Preview features**

- Adding "available_private_access_services" operation group (preview)
- Adding "radius_secret" in Virtual Network Gateway (preview)

**Bug Fixes**

- VMSS Network ApiVersion fix in 2017-06-01 (point to 2017-03-30)

1.2.0 (2017-07-03)
++++++++++++++++++

**Features**

Adding the following features to both 2017-03-01 and 2017-06-01:

- express route ipv6
- VMSS Network (get, list, etc.)
- VMSS Public IP (get, list, etc.)

1.1.0 (2017-06-27)
++++++++++++++++++

**Features**

- Add list_usage in virtual networks (2017-03-01)

- Add ApiVersion 2017-06-01 (new default)

This new ApiVersion is for new Application Gateway features:

  - ApplicationGateway Ssl Policy custom cipher suites support [new properties added to Sslpolicy Property of ApplciationGatewayPropertiesFormat]
  - Get AvailableSslOptions api [new resource ApplicationGatewayAvailableSslOptions and child resource ApplicationGatewayPredefinedPolicy]
  - Redirection support [new child resource ApplicationGatewayRedirectConfiguration for Application Gateway,
    new properties in UrlPathMap, PathRules and RequestRoutingRule]
  - Azure Websites feature support [new properties in ApplicationGatewayBackendHttpSettingsPropertiesFormat,
    ApplicationGatewayProbePropertiesFormat, schema for property ApplicationGatewayProbeHealthResponseMatch]

1.0.0 (2017-05-15)
++++++++++++++++++

- Tag 1.0.0rc3 as stable (same content)

1.0.0rc3 (2017-05-03)
+++++++++++++++++++++

**Features**

- Added check connectivity api to network watcher

1.0.0rc2 (2017-04-18)
+++++++++++++++++++++

**Features**

- Add ApiVersion 2016-12-01 and 2017-03-01
- 2017-03-01 is now default ApiVersion

**Bugfixes**

- Restore access to NetworkWatcher and PacketCapture from 2016-09-01

1.0.0rc1 (2017-04-11)
+++++++++++++++++++++

**Features**

To help customers with sovereign clouds (not general Azure),
this version has official multi ApiVersion support for 2015-06-15 and 2016-09-01

0.30.1 (2017-03-27)
+++++++++++++++++++

* Add NetworkWatcher
* Add PacketCapture
* Add new methods to Virtualk Network Gateway

  * get_bgp_peer_status
  * get_learned_routes
  * get_advertised_routes

0.30.0 (2016-11-01)
+++++++++++++++++++

* Initial preview release. Based on API version 2016-09-01.


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

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.7.1-0
- Update .spec from py2pack
- Manually add Requires and Suggests

