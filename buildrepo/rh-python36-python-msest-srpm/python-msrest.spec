#
# spec file for package rh-python36-python-msrest
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name msrest

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
Version:        0.4.29
Release:        0%{?dist}
Url:            https://github.com/Azure/msrest-for-python
Summary:        AutoRest swagger generator Python client runtime.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
#Requires:       %{?scl_prefix}python-requests = 2.14
Requires:       %{?scl_prefix}python-requests >= 2.14
Requires:       %{?scl_prefix}python-requests_oauthlib >= 0.5.0
Requires:       %{?scl_prefix}python-isodate >= 0.6.0
Requires:       %{?scl_prefix}python-certifi >= 2017.4.17
# Manually added for python < 3.4
#Requires:       %{?scl_prefix}python-enum34 >= 1.0.4
%if %{with_dnf}
%endif # with_dnf

%description
AutoRest: Python Client Runtime
===============================

**Features**

- msrest is now able to keep the "requests.Session" alive for performance. To activate this behavior:

  - Use the final Client as a context manager (requires generation with Autorest.Python 3.0.50 at least)
  - Use `client.config.keep_alive = True` and `client.close()` (requires generation with Autorest.Python 3.0.50 at least)
  - Use `client.config.keep_alive = True` and client._client.close() (not recommended, but available in old releases of SDK)

- All Authentication classes now define `signed_session` and `refresh_session` with an optional `session` parameter.
  To take benefits of the session improvement, a subclass of Authentication *MUST* add this optional parameter
  and use it if it is not `None`:

     def signed_session(self, session=None):
         session = session or requests.Session()

         # As usual from here.

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.4.29-0
- Update .spec with py2pack
- Add manual Requires
- Tune Requires for python-requests to >= 2.14
