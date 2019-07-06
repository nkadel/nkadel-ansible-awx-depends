#
# spec file for package rh-python36-python-xmlsec
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name xmlsec
%{?scl:%scl_package python-xmlsec}
%{!?scl:%global pkg_name python-xmlsec}

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Common SRPM package
Name:           %{?scl_prefix}python-xmlsec
Version:        1.3.3
Release:        0%{?dist}
Url:            https://github.com/mehcode/python-xmlsec
Summary:        Python bindings for the XML Security Library
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=xmlsec; echo ${n:0:1})/xmlsec/xmlsec-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Added manually
BuildRequires:  %{?scl_prefix}python-pkgconfig
BuildRequires:  xmlsec1-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  %{?scl_prefix}python-lxml >= 3.0
%if %{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python-xmlsec}

%description


%prep
%setup -q -n xmlsec-%{version}

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
* Fri Jul 5 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.3.3-0
- Rebuild .spec file with py2pack
- Add BuldRequires for li xmlsec1-devel, libtool-ltdl-devel, python-lxml, and reset BuildArch
