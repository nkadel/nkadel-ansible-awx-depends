#
# spec file for package rh-python36-python-pytest
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pytest

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
Version:        2.9.2
Release:        0%{?dist}
Url:            http://pytest.org
Summary:        pytest: simple powerful testing with Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:  %{?scl_prefix}python-py >= 1.4.29
#[:python_version=="2.6" or python_version=="3.0" or python_version=="3.1"]
#Requires:  %{?scl_prefix}python-argparse
#[:sys_platform=="win32"]
#colorama
%if %{with_dnf}
%endif # with_dnf

%description
The ``pytest`` framework makes it easy to write small tests, yet
scales to support complex functional testing for applications and libraries.    

An example of a simple test:

.. code-block:: python

    # content of test_sample.py
    def func(x):
        return x + 1

    def test_answer():
        assert func(3) == 5


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
