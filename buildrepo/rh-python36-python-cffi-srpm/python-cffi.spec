#
# spec file for package rh-python36-python-cffi
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name cffi

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
Version:        1.12.3
Release:        0%{?dist}
Url:            http://cffi.readthedocs.org
Summary:        Foreign Function Interface for Python calling C code.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Manually add epoch to force use of local version
Epoch: 3

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  libffi-devel
Requires:       %{?scl_prefix}python-pycparser
%if %{with_dnf}
%endif # with_dnf

%description

CFFI
====

Foreign Function Interface for Python calling C code.
Please see the `Documentation <http://cffi.readthedocs.org/>`_.

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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.11.5-0
- Update .spec with py2pack
- Add Requires for libffi-devel
- Add Epoch to displace upstream cffi

