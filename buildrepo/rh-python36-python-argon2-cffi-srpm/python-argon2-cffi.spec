#
# spec file for package rh-python36-python-argon2-cffi
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name argon2-cffi
# Manually added
%global srcname argon2_cffi


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
Version:        19.1.0
Release:        0%{?dist}
Url:            https://argon2-cffi.readthedocs.io/
Summary:        The secure Argon2 password hashing algorithm.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{srcname}; echo ${n:0:1})/%{srcname}/%{srcname}-%{version}.tar.gz
# Manually added
Provides: %{?scl_prefix}python-arg2_cffi = %{version}-%{release}
Obsoletes: %{?scl_prefix}python-arg2_cffi <= %{version}-%{release}
Conflicts: %{?scl_prefix}python-arg2_cffi <= %{version}-%{release}

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-cffi >= 1.0.0
Requires:       %{?scl_prefix}python-cffi >= 1.0.0
Requires:       %{?scl_prefix}python-six

%if %{with_dnf}
#[dev]
Suggests:       %{?scl_prefix}python-coverage
Suggests:       %{?scl_prefix}python-hypothesis
Suggests:       %{?scl_prefix}python-pytest
Suggests:       %{?scl_prefix}python-sphinx
Suggests:       %{?scl_prefix}python-wheel
Suggests:       %{?scl_prefix}python-pre-commit
#[docs]
Suggests:       %{?scl_prefix}python-sphinx
#[tests]
Suggests:       %{?scl_prefix}python-coverage
Suggests:       %{?scl_prefix}python-hypothesis
Suggests:       %{?scl_prefix}python-pytest
%endif # with_dnf

%description
=====================================
CFFI-based Argon2 Bindings for Python
=====================================

`Argon2 <https://github.com/p-h-c/phc-winner-argon2>`_ won the `Password Hashing Competition <https://password-hashing.net/>`_ and ``argon2_cffi`` is the simplest way to use it in Python and PyPy:

%prep
%setup -q -n %{srcname}-%{version}

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
* Fri Jul 12 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 19.1.0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually add srcname, since tarball does not match pypi.org publied module name
