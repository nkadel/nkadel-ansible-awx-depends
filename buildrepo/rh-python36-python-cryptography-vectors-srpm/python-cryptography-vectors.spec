#
# spec file for package rh-python36-python-cryptography-vectors
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Warning: tarball uses cryptography_vectors name, but pypi.org calls it cryptography-vectors
%global pypi_name cryptography-vectors
%global src_name cryptography_vectors

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
Version:        2.3
Release:        0%{?dist}
Url:            https://github.com/pyca/cryptography
Summary:        Test vectors for the cryptography package.
License:        BSD or Apache License, Version 2.0 (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{src_name}; echo ${n:0:1})/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description


%prep
%setup -q -n %{src_name}-%{version}

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.3-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Add src_name because RPMs and pypi.org cal this cryptography-vectors,
  but tarball is cryptography_vectors
