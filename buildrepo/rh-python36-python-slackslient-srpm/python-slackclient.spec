#
# spec file for package rh-python36-python-slackclient
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name slackclient

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
Version:        1.1.2
Release:        0%{?dist}
Url:            https://github.com/slackapi/python-slackclient
Summary:        Slack API clients for Web API and RTM API
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Added manually
Requires:       %{?scl_prefix}python-websocket-client >= 0.36
Requires:       %{?scl_prefix}python-websocket-client < 1.0a0
Requires:       %{?scl_prefix}python-websocket-requests >= 2.11
Requires:       %{?scl_prefix}python-websocket-requests < 3.0a0
Requires:       %{?scl_prefix}python-six >= 1.10
Requires:       %{?scl_prefix}python-six < 2.0a0
%if %{with_dnf}
%endif # with_dnf

%description
python-slackclient
===================

A client for Slack, which supports the Slack Web API and Real Time Messaging (RTM) API.

Whether you are building a custom app for your team, or integrating a third party
service into your Slack workflows, Slack Developer Kit for Python allows you to leverage the flexibility
of Python to get your project up and running as quickly as possible.

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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.1.2-0
- Update .spec file with py2pack
- Activate Requires manually

