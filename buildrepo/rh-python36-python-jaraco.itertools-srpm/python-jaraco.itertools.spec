#
# spec file for package rh-python36-python-jaraco.itertools
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name jaraco.itertools

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
Version:        2.1.1
Release:        0%{?dist}
Url:            https://github.com/jaraco/jaraco.itertools
Summary:        jaraco.itertools
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-setuptools_scm >= 1.15.0
Requires:       %{?scl_prefix}python-six
Requires:       %{?scl_prefix}python-more_itertools >= 2.6
Requires:       %{?scl_prefix}python-inflect
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
.. image:: https://img.shields.io/pypi/v/jaraco.itertools.svg
   :target: https://pypi.org/project/jaraco.itertools

.. image:: https://img.shields.io/pypi/pyversions/jaraco.itertools.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.itertools/master.svg
   :target: https://travis-ci.org/jaraco/jaraco.itertools

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/jaraco.itertools/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/jaraco.itertools/branch/master

.. image:: https://readthedocs.org/projects/jaracoitertools/badge/?version=latest
   :target: https://jaracoitertools.readthedocs.io/en/latest/?badge=latest




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
