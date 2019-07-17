#
# spec file for package rh-python36-python-argparse
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name argparse

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
Version:        1.4.0
Release:        0%{?dist}
Url:            https://github.com/ThomasWaldmann/argparse/
Summary:        Python command-line parsing library
License:        Python-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
The argparse module makes it easy to write user friendly command line
interfaces.

The program defines what arguments it requires, and argparse will figure out
how to parse those out of sys.argv. The argparse module also automatically
generates help and usage messages and issues errors when users give the
program invalid arguments.

As of Python >= 2.7 and >= 3.2, the argparse module is maintained within the
Python standard library. For users who still need to support Python < 2.7 or
< 3.2, it is also provided as a separate package, which tries to stay
compatible with the module in the standard library, but also supports older
Python versions.

Also, we can fix bugs here for users who are stuck on some non-current python
version, like e.g. 3.2.3 (which has bugs that were fixed in a later 3.2.x
release).

argparse is licensed under the Python license, for details see LICENSE.txt.


Compatibility
-------------

argparse should work on Python >= 2.3, it was tested on:

* 2.3, 2.4, 2.5, 2.6 and 2.7
* 3.1, 3.2, 3.3, 3.4


Installation
------------

Try one of these:

    python setup.py install

    easy_install argparse

    pip install argparse

    putting argparse.py in some directory listed in sys.path should also work


Bugs
----

If you find a bug in argparse (pypi), please try to reproduce it with latest
python 2.7 and 3.4 (and use argparse from stdlib).

If it happens there also, please file a bug in the python.org issue tracker.
If it does not happen there, file a bug in the argparse package issue tracker.

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