#
# spec file for package rh-python36-python-python-daemon
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name python-daemon

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
Version:        2.2.3
Release:        0%{?dist}
Url:            https://pagure.io/python-daemon/
Summary:        Library to implement a well-behaved Unix daemon process.
License:        Apache-2 (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-docutils
#BuildRequires:  %{?scl_prefix}python-lockfile >= 0.10
Requires:       %{?scl_prefix}python-lockfile >= 0.10
%if %{with_dnf}
%endif # with_dnf

%description
This library implements the well-behaved daemon specification of
:pep:`3143`, &#8220;Standard daemon process library&#8221;.

A well-behaved Unix daemon process is tricky to get right, but the
required steps are much the same for every daemon program. A
`DaemonContext` instance holds the behaviour and configured
process environment for the program; use the instance as a context
manager to enter a daemon state.

Simple example of usage::

    import daemon

    from spam import do_main_program

    with daemon.DaemonContext():
        do_main_program()

Customisation of the steps to become a daemon is available by
setting options on the `DaemonContext` instance; see the
documentation for that class for each option.



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
