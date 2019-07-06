#
# spec file for package rh-python36-python-appdirs
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name appdirs
%{?scl:%scl_package python-appdirs}
%{!?scl:%global pkg_name python-appdirs}

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Common SRPM package
Name:           %{?scl_prefix}python-appdirs
Version:        1.4.2
Release:        0%{?dist}
Url:            http://github.com/ActiveState/appdirs
Summary:        A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir".
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=appdirs; echo ${n:0:1})/appdirs/appdirs-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
# Manually added for check
Suggests:       %{?scl_prefix}python-unittest2
%endif # with_dnf
%{?python_provide:%python_provide python-appdirs}

%description
the problem
===========

What directory should your app use for storing user data? 

``appdirs`` to the rescue
=========================

This kind of thing is what the ``appdirs`` module is for. ``appdirs`` will
help you choose an appropriate:

- user data dir (``user_data_dir``)
- user config dir (``user_config_dir``)
- user cache dir (``user_cache_dir``)
- site data dir (``site_data_dir``)
- site config dir (``site_config_dir``)
- user log dir (``user_log_dir``)

and also:

- is a single module so other Python packages can include their own private copy
- is slightly opinionated on the directory names used. Look for "OPINION" in
  documentation and code for when an opinion is being applied.

%prep
%setup -q -n appdirs-%{version}

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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.4.20-0
- Update .spec file with py2pack
# Add Suggests for python-unittest2 for unit testing
