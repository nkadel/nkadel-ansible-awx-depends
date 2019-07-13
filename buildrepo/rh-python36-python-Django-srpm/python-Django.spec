#
# spec file for package rh-python36-python-Django
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name Django

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
Version:        1.11.16
Release:        0%{?dist}
Url:            https://www.djangoproject.com/
Summary:        A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-argon2-cffi >= 16.1.0
Requires:       %{?scl_prefix}python-bcrypt
Requires:       %{?scl_prefix}python-docutils
Requires:       %{?scl_prefix}python-geoip2
Requires:       %{?scl_prefix}python-jinja2 >= 2.9.2
Requires:       %{?scl_prefix}python-numpy
Requires:       %{?scl_prefix}python-Pillow
Requires:       %{?scl_prefix}python-PyYAML
# pylibmc/libmemcached can't be built on Windows.
Requires:       %{?scl_prefix}python-pylibmc
Requires:       %{?scl_prefix}python-python-memcached >= 1.59
Requires:       %{?scl_prefix}python-pytz
Requires:       %{?scl_prefix}python-selenium
Requires:       %{?scl_prefix}python-sqlparse
Requires:       %{?scl_prefix}python-tblib
# For python2
#Requires:       %{?scl_prefix}python-enum34
#Requires:       %{?scl_prefix}python-mock
%if %{with_dnf}
# Manually added from oracle.txt
#Suggests:       %{?scl_prefix}python-cx_oracle  < 7
# Manually added from postgres.txt
Suggests:         %{?scl_prefix}python-psycopg2-binary >= 2.5.4
# Manually added from mysql.txt
Suggests:         %{?scl_prefix}python-mysqlclient >= 1.3.7
# Manually added for argon2
Suggests:         %{?scl_prefix}python-argon2-cffi >= 16.1.0
# Manually added for bcrypt
Suggests:         %{?scl_prefix}python-bcrypt
%endif # with_dnf
# Manually added for case switched packages
Provides:         %{?scl_prefix}python-django = %{version}-%{release}
Obsoletes:        %{?scl_prefix}python-django <= %{version}-%{release}
Conflicts:        %{?scl_prefix}python-django <= %{version}-%{release}

%description
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design. Thanks for checking it out.

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
%{_bindir}/*

%changelog
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.11.16-0
- Update .spec file with py2pack
- Manually add Requires
- Manually add _bindir/*
- Manually add Provides for mixed case python-django packages

