#
# spec file for package rh-python36-python-py
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name py

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
Version:        1.8.0
Release:        0%{?dist}
Url:            http://py.readthedocs.io/
Summary:        library with cross-python path, ini-parsing, io, code, log facilities
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-setuptools_scm
%if %{with_dnf}
%endif # with_dnf

%description
.. image:: https://img.shields.io/pypi/v/py.svg
    :target: https://pypi.org/project/py

.. image:: https://img.shields.io/conda/vn/conda-forge/py.svg
    :target: https://anaconda.org/conda-forge/py

.. image:: https://img.shields.io/pypi/pyversions/pytest.svg
  :target: https://pypi.org/project/py

.. image:: https://img.shields.io/travis/pytest-dev/py.svg
   :target: https://travis-ci.org/pytest-dev/py

.. image:: https://ci.appveyor.com/api/projects/status/10keglan6uqwj5al/branch/master?svg=true
   :target: https://ci.appveyor.com/project/pytestbot/py


**NOTE**: this library is in **maintenance mode** and should not be used in new code.

The py lib is a Python development support library featuring
the following tools and modules:

* ``py.path``:  uniform local and svn path objects  -> please use pathlib/pathlib2 instead
* ``py.apipkg``:  explicit API control and lazy-importing -> please use the standalone package instead
* ``py.iniconfig``:  easy parsing of .ini files -> please use the standalone package instead
* ``py.code``: dynamic code generation and introspection (deprecated, moved to ``pytest`` as a implementation detail).

**NOTE**: prior to the 1.4 release this distribution used to
contain py.test which is now its own package, see http://pytest.org

For questions and more information please visit http://py.readthedocs.org

Bugs and issues: https://github.com/pytest-dev/py

Authors: Holger Krekel and others, 2004-2017




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
