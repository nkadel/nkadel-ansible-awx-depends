#
# spec file for package rh-python36-python-vcversioner
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global modname vcversioner

%{?scl:%scl_package python-%{modname}}
%{!?scl:%global pkg_name python-%{modname}}

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Common SRPM package
Name:           %{?scl_prefix}python-%{modname}
Version:        2.16.0.0
Release:        0%{?dist}
Url:            https://github.com/habnabit/vcversioner
Summary:        Use version control tags to discover version numbers
License:        ISC
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{modname}; echo ${n:0:1})/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python-%{modname}}

%description
===========
vcversioner
===========

`Elevator pitch`_: you can write a ``setup.py`` with no version information
specified, and vcversioner will find a recent, properly-formatted VCS tag and
extract a version from it.

It is much more convenient to be able to use your version control system
tagging mechanism to derive a version number than to have to duplicate that
information all over the place. I eventually ended up copy-pasting the same
code into a couple different ``setup.py`` files just to avoid duplicating
version information. But, copy-pasting is dumb and unit testing ``setup.py``
files is hard. This code got factored out into vcversioner.

%prep
%setup -q -n %{modname}-%{version}

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
