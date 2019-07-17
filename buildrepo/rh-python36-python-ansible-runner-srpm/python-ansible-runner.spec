#
# spec file for package rh-python36-python-ansible-runner
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name ansible-runner

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
Version:        1.3.4
Release:        0%{?dist}
Url:            https://github.com/ansible/ansible-runner
Summary:        A tool and python library to interface with Ansible
License:        Apache (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-PyYAML
Requires:       %{?scl_prefix}python-pexpect >= 4.5
Requires:       %{?scl_prefix}python-psutil
Requires:       %{?scl_prefix}python-python-daemon
Requires:       %{?scl_prefix}python-six
%if %{with_dnf}
%endif # with_dnf

%description
Ansible Runner is a tool and python library that helps when
interfacing with Ansible directly or as part of another system whether
that be through a container image interface, as a standalone tool, or
as a Python module that can be imported. The goal is to provide a
stable and consistent interface abstraction to Ansible.

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
%{_bindir}/*

%changelog
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.3.4-0
- Generate .spec file with py2pack
- Add _bindir
