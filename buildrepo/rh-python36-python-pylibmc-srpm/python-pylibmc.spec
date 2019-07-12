#
# spec file for package rh-python36-python-pylibmc
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pylibmc

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
Version:        1.6.0
Release:        0%{?dist}
Url:            http://sendapatch.se/projects/pylibmc/
Summary:        Quick and small memcached client for Python
License:        3-clause BSD <http://www.opensource.org/licenses/bsd-license.php> (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  libmemcached-devel
BuildRequires:  zlib-devel
%if %{with_dnf}
%endif # with_dnf

%description
`pylibmc` is a Python client for `memcached <http://memcached.org/>`_ written in C.

See `the documentation at sendapatch.se/projects/pylibmc/`__ for more information.

__ http://sendapatch.se/projects/pylibmc/

.. image:: https://travis-ci.org/lericson/pylibmc.png?branch=master
   :target: https://travis-ci.org/lericson/pylibmc

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
* Fri Jul 12 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.6.0-0
- Initial setup
- Manually BuildRequires for libmemcached-devel and zlib-devel
