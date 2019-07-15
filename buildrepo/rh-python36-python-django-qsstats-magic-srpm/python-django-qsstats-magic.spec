#
# spec file for package rh-python36-python-django-qsstats-magic
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name django-qsstats-magic

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
Version:        0.7.2
Release:        0%{?dist}
Url:            http://bitbucket.org/kmike/django-qsstats-magic/
Summary:        A django microframework that eases the generation of aggregate data for querysets.
License:        UNKNOWN (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires:       %{?scl_prefix}python-dateutil >= 1.4.1
Requires:       %{?scl_prefix}python-dateutil < 2.0
%if %{with_dnf}
%endif # with_dnf

%description
====================================================
django-qsstats-magic: QuerySet statistics for Django
====================================================

The goal of django-qsstats is to be a microframework to make
repetitive tasks such as generating aggregate statistics of querysets
over time easier.  It is probably overkill for the task at hand, but yay
microframeworks!

django-qsstats-magic is a refactoring of django-qsstats app with slightly
changed API, simplified internals and faster time_series implementation.

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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.7.2-0
- Update .spec from py2pack
- Manually add Requires and Suggests
