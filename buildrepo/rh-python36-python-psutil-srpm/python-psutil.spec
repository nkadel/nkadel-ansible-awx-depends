#
# spec file for package rh-python36-python-psutil
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name psutil

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
Version:        5.4.3
Release:        0%{?dist}
Url:            https://github.com/giampaolo/psutil
Summary:        Cross-platform lib for process and system monitoring in Python.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
# Manually added for enum - not suitable for python3
#Suggests:  %{?scl_prefix}python-enum34
%endif # with_dnf

%description
psutil (process and system utilities) is a cross-platform library for
retrieving information on **running processes** and **system utilization**
(CPU, memory, disks, network, sensors) in Python.
It is useful mainly for **system monitoring**, **profiling and limiting process
resources** and **management of running processes**.
It implements many functionalities offered by UNIX command line tools such as:
ps, top, lsof, netstat, ifconfig, who, df, kill, free, nice, ionice, iostat,
iotop, uptime, pidof, tty, taskset, pmap.
psutil currently supports the following platforms:

- **Linux**
- **Windows**
- **OSX**,
- **FreeBSD, OpenBSD**, **NetBSD**
- **Sun Solaris**
- **AIX**

...both **32-bit** and **64-bit** architectures, with Python
versions from **2.6 to 3.6**.
`PyPy <http://pypy.org/>`__ is also known to work.

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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 5.4.3-0
- Update .spec file with py2pack
- Add disabled requires for enum34
