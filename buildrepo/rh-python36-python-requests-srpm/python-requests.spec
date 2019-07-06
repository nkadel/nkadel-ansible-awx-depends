#
# spec file for package rh-python36-python-requests
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name requests

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
Version:        2.20.0
Release:        0%{?dist}
Url:            http://python-requests.org
Summary:        Python HTTP for Humans.
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-certifi >= 2017.4.17
Requires:       %{?scl_prefix}python-chardet < 3.1.0
Requires:       %{?scl_prefix}python-chardet >= 3.0.2
Requires:       %{?scl_prefix}python-idna < 2.8
Requires:       %{?scl_prefix}python-idna >= 2.5
Requires:       %{?scl_prefix}python-urllib3 < 1.25
Requires:       %{?scl_prefix}python-urllib3 >= 1.21.1

%if %{with_dnf}
# Manualy added for security
Suggests:       %{?scl_prefix}python-pyOpenSSL >= 0.14
Suggests:       %{?scl_prefix}python-cryptography >= 1.3.4
Suggests:       %{?scl_prefix}python-idna >= 2.0.0
# Manualy added for socks
Conflicts:      %{?scl_prefix}python-PySocks = 1.5.7
Suggests:       %{?scl_prefix}python-PySocks >= 1.5.6
# Only or Windoes
#Suggests:       %{?scl_prefix}python-win_inet_pton
%endif # with_dnf

%description
Requests: HTTP for Humans&#8482;
==========================

Requests is the only *Non-GMO* HTTP library for Python, safe for human
consumption.

![image](https://farm5.staticflickr.com/4317/35198386374_1939af3de6_k_d.jpg)

Requests allows you to send *organic, grass-fed* HTTP/1.1 requests,
without the need for manual labor. There is no need to manually add query
strings to your URLs, or to form-encode your POST data. Keep-alive and
HTTP connection pooling are 100% automatic, thanks to
[urllib3](https://github.com/shazow/urllib3).

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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com>
- Update .spec file with py2pack
- Manually set Requires and Suggests
- Manually reduce description
