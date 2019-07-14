#
# spec file for package rh-python36-python-netifaces
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name netifaces

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
Version:        0.10.6
Release:        0%{?dist}
Url:            https://bitbucket.org/al45tair/netifaces
Summary:        Portable network interface information.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
netifaces 0.10.6
================

.. image:: https://drone.io/bitbucket.org/al45tair/netifaces/status.png
   :target: https://drone.io/bitbucket.org/al45tair/netifaces/latest
   :alt: Build Status

1. What is this?
----------------

It has been annoying me for some time that there is no easy way to get the
address(es) of the machine network interfaces from Python.  There is
a good reason for this difficulty, which is that it is virtually impossible
to do so in a portable manner.  However, it seems to me that there should
be a package you can easy_install that will take care of working out the
details of doing so on the machine you are using, then you can get on with
writing Python code without concerning yourself with the nitty gritty of
system-dependent low-level networking APIs.

This package attempts to solve that problem.


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
%{python3_sitearch}/*

%changelog
