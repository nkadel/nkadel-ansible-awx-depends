#
# spec file for package rh-python36-python-python3-openid
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name python3-openid

%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name python-%{pypi_name}}

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Common SRPM package
#Name:           %{?scl_prefix}python-%{pypi_name}
Name:           %{?scl_prefix}%{pypi_name}
Version:        3.1.0
Release:        0%{?dist}
Url:            http://github.com/necaris/python3-openid
Summary:        OpenID support for modern servers and consumers.
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:  %{?scl_prefix}python-defusedxml
%if %{with_dnf}
%endif # with_dnf

%description
This is a set of Python packages to support use of
the OpenID decentralized identity system in your application, update to Python
3.  Want to enable single sign-on for your web site?  Use the openid.consumer
package.  Want to run your own OpenID server? Check out openid.server.
Includes example code and support for a variety of storage back-ends.

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

%changelog
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 3.1.0-0
- Update .spec file with py2pack
- Manually add Requires for defusedxml
- Adjust "Name" to accomodate python3-openid package name
