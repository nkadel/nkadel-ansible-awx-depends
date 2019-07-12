#
# spec file for package rh-python36-python-requests_ntlm
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name requests_ntlm

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
Version:        1.1.0
Release:        0%{?dist}
Url:            https://github.com/requests/requests-ntlm
Summary:        This package allows for HTTP NTLM authentication using the requests library.
License:        ISC
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:  %{?scl_prefix}python-requests >= 2.0.0
Requires:  %{?scl_prefix}python-ntlm-auth >= 1.0.2
Requires:  %{?scl_prefix}python-cryptography >= 1.3
%if %{with_dnf}
%endif # with_dnf

%description
This package allows for HTTP NTLM authentication using the requests library.

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.1-0
- Update .spec from py2pack
- Manually add Requires and Suggests