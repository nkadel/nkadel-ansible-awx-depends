#
# spec file for package rh-python36-python-websocket_client
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name websocket_client
%{?scl:%scl_package python-websocket_client}
%{!?scl:%global pkg_name python-websocket_client}

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Common SRPM package
Name:           %{?scl_prefix}python-websocket_client
Version:        0.47.0
Release:        0%{?dist}
Url:            https://github.com/websocket-client/websocket-client.git
Summary:        WebSocket client for python. hybi13 is supported.
License:        LGPL (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=websocket_client; echo ${n:0:1})/websocket_client/websocket_client-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added for old package name
Provides:       %{?scl_prefix}python-websocket-client = %{version}-%{release}
Conflicts:      %{?scl_prefix}python-websocket-client <= %{version}-%{release}
Obsoletes:      %{?scl_prefix}python-websocket-client <= %{version}-%{release}
%if %{with_dnf}
%endif # with_dnf

%description
=================
websocket-client
=================

websocket-client module  is WebSocket client for python. This provide the low level APIs for WebSocket. All APIs are the synchronous functions.

websocket-client supports only hybi-13.

%prep
%setup -q -n websocket_client-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
%{__python3} setup.py build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# Manually rename script to wsdump
%{__mv} $RPM_BUILD_ROOT%{_bindir}/wsdump.py  $RPM_BUILD_ROOT%{_bindir}/wsdump
%{?scl:EOF}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/wsdump

%changelog
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.47.0-0
- Update .spec file with py2pack
- Add Providec, Obsolete, and Conflicts for distinct python-websocket-client package
- Rename wsdump.py to wsdump
- Add _bindir

