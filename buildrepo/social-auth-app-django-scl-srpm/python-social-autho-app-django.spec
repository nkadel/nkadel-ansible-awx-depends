#
# spec file for package rh-python36-python-social-auth-app-django
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name social-auth-app-django

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
Version:        2.1.0
Release:        0%{?dist}
Url:            https://github.com/python-social-auth/social-app-django
Summary:        Python Social Authentication, Django integration.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-social-auth-core >= 1.2.0
Requires:       %{?scl_prefix}python-six
%if %{with_dnf}
Suggests:	%{?scl_prefix}python-tox = 2.7.0
Suggests:	%{?scl_prefix}python-codecov = 2.0.7
Suggests:	%{?scl_prefix}python-mock = 2.0.0
%endif # with_dnf

%description
This is the [Django](https://www.djangoproject.com/) component of the
[python-social-auth ecosystem](https://github.com/python-social-auth/social-core),
it implements the needed functionality to integrate
[social-auth-core](https://github.com/python-social-auth/social-core)
in a Django based project.

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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.1.0-0
- Update spec file with py2pack
- Manually add requirements, and dev requirements s "Suggests"

