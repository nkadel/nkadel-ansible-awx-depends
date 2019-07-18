#
# spec file for package rh-python36-python-jaraco.text
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name jaraco.text

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
Version:        1.10
Release:        0%{?dist}
Url:            https://github.com/jaraco/jaraco.text
Summary:        jaraco.text
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-setuptools_scm >= 1.15.0
Requires:       %{?scl_prefix}python-jaraco.functools
Requires:       %{?scl_prefix}python-jaraco.collections
%if %{with_dnf}
# Manually added for docs
Suggests:       %{?scl_prefix}python-sphinx
Suggests:       %{?scl_prefix}python-jaraco.packaging >= 3.2
Suggests:       %{?scl_prefix}python-rst.linker >= 1.9
# Manually added for testing
Suggests:       %{?scl_prefix}python-pytest >= 2.8
Suggests:       %{?scl_prefix}python-pytest-sugar >= 0.9.1
Suggests:       %{?scl_prefix}python-collective.checkdocs
Suggests:       %{?scl_prefix}python-pytest-flake8
%endif # with_dnf

%description
.. image:: https://img.shields.io/pypi/v/jaraco.text.svg
   :target: https://pypi.org/project/jaraco.text

.. image:: https://img.shields.io/pypi/pyversions/jaraco.text.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.text/master.svg
   :target: https://travis-ci.org/jaraco/jaraco.text

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/skeleton/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/skeleton/branch/master

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest




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
%exclude %{python3_sitelib}/jaraco/__init__.py
%exclude %{python3_sitelib}/jaraco/__pycache__

%changelog
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.10-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually exclude cross-duplicated files
