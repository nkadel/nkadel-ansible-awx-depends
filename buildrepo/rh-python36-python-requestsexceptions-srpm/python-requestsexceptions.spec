#
# spec file for package rh-python36-python-requestsexceptions
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name requestsexceptions

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
Version:        1.4.0
Release:        0%{?dist}
Url:            http://www.openstack.org/
Summary:        Import exceptions from potentially bundled packages in requests.
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-pbr
%if %{with_dnf}
# Manually added
Conflicts:      %{?scl_prefix}python-hacking !=0.13.0
Conflicts:      %{?scl_prefix}python-hacking < 0.14
Conflicts:      %{?scl_prefix}python-hacking >= 0.12.0
%endif # with_dnf

%description
requestsexceptions
==================

The python requests library bundles the urllib3 library, however, some
software distributions modify requests to remove the bundled library.
This makes some operations, such as supressing the "insecure platform
warning" messages that urllib emits difficult.  This is a simple
library to find the correct path to exceptions in the requests library
regardless of whether they are bundled.





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
* Sat Jul 13 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.4.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
