#
# spec file for package rh-python36-python-twilio
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name twilio

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
Version:        6.10.4
Release:        0%{?dist}
Url:            https://github.com/twilio/twilio-python/
Summary:        Twilio API client and TwiML generator
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-six
Requires:       %{?scl_prefix}python-pytz
Requires:       %{?scl_prefix}python-PyJWT >= 1.4.2
# python <  3.8
Requires:       %{?scl_prefix}python-requests >= 2.0.0
# python >=  3.8
Requires:       %{?scl_prefix}python-requests >= 3.0.0
Requires:       %{?scl_prefix}python-pysocks
%if %{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python-%{pypi_name}}

%description
Python Twilio Helper Library
    ----------------------------

    DESCRIPTION
    The Twilio REST SDK simplifies the process of making calls using the Twilio REST API.
    The Twilio REST API lets to you initiate outgoing calls, list previous calls,
    and much more.  See https://www.github.com/twilio/twilio-python for more information.

     LICENSE The Twilio Python Helper Library is distributed under the MIT
    License

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
