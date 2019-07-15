#
# spec file for package rh-python36-python-ansible
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name ansible

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
Version:        2.7.6
Release:        0%{?dist}
Url:            https://ansible.com/
Summary:        Radically simple IT automation
License:        GPL-3.0+
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
BuildRequires:  %{?scl_prefix}python-PyYAML
BuildRequires:  %{?scl_prefix}python-cryptography
BuildRequires:  %{?scl_prefix}python-jinja2
BuildRequires:  %{?scl_prefix}python-paramiko
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
Suggests:       %{?scl_prefix}-packaging
Suggests:       %{?scl_prefix}-requests
Suggests:       %{?scl_prefix}-azure-cli-core == 2.0.35
Suggests:       %{?scl_prefix}-azure-cli-nspkg == 3.0.2
Suggests:       %{?scl_prefix}-azure-common == 1.1.11
Suggests:       %{?scl_prefix}-azure-mgmt-batch == 4.1.0
Suggests:       %{?scl_prefix}-azure-mgmt-compute == 2.1.0
Suggests:       %{?scl_prefix}-azure-mgmt-containerinstance == 0.4.0
Suggests:       %{?scl_prefix}-azure-mgmt-containerregistry == 2.0.0
Suggests:       %{?scl_prefix}-azure-mgmt-containerservice == 3.0.1
Suggests:       %{?scl_prefix}-azure-mgmt-dns == 1.2.0
Suggests:       %{?scl_prefix}-azure-mgmt-keyvault == 0.40.0
Suggests:       %{?scl_prefix}-azure-mgmt-marketplaceordering == 0.1.0
Suggests:       %{?scl_prefix}-azure-mgmt-monitor == 0.5.2
Suggests:       %{?scl_prefix}-azure-mgmt-network == 1.7.1
Suggests:       %{?scl_prefix}-azure-mgmt-nspkg == 2.0.0
Suggests:       %{?scl_prefix}-azure-mgmt-rdbms == 1.2.0
Suggests:       %{?scl_prefix}-azure-mgmt-resource == 1.2.2
Suggests:       %{?scl_prefix}-azure-mgmt-sql == 0.7.1
Suggests:       %{?scl_prefix}-azure-mgmt-storage == 1.5.0
Suggests:       %{?scl_prefix}-azure-mgmt-trafficmanager == 0.50.0
Suggests:       %{?scl_prefix}-azure-mgmt-web == 0.32.0
Suggests:       %{?scl_prefix}-azure-nspkg == 2.0.0
Suggests:       %{?scl_prefix}-azure-storage == 0.35.1
Suggests:       %{?scl_prefix}-msrest == 0.4.29
Suggests:       %{?scl_prefix}-msrestazure == 0.4.31
Suggests:       %{?scl_prefix}-azure-keyvault == 1.0.0a1
Suggests:       %{?scl_prefix}-azure-graphrbac == 0.40.0
%endif # with_dnf

%description
|PyPI version| |Docs badge| |Chat badge| |Build Status|

*******
Ansible
*******

Ansible is a radically simple IT automation system. It handles
configuration-management, application deployment, cloud provisioning,
ad-hoc task-execution, and multinode orchestration -- including
trivializing things like zero-downtime rolling updates with load
balancers.

Read the documentation and more at https://ansible.com/

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
%doc README.rst changelogs changelogs/CHANGELOG-v2.7.rst changelogs/CHANGELOG.rst
%{_bindir}/ansible
%{_bindir}/ansible-config
%{_bindir}/ansible-connection
%{_bindir}/ansible-console
%{_bindir}/ansible-doc
%{_bindir}/ansible-galaxy
%{_bindir}/ansible-inventory
%{_bindir}/ansible-playbook
%{_bindir}/ansible-pull
%{_bindir}/ansible-vault
%{_bindir}/ansible
%{_bindir}/ansible-config
%{_bindir}/ansible-connection
%{_bindir}/ansible-console
%{_bindir}/ansible-doc
%{_bindir}/ansible-galaxy
%{_bindir}/ansible-inventory
%{_bindir}/ansible-playbook
%{_bindir}/ansible-pull
%{_bindir}/ansible-vault
%{python3_sitelib}/*

%changelog
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.7.6-0
- Updte .spec file with py2pack
