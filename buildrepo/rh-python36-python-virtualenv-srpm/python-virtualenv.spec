#
# spec file for package rh-python36-python-virtualenv
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name virtualenv

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
Version:        16.6.1
Release:        0%{?dist}
Url:            https://virtualenv.pypa.io/
Summary:        Virtual Python Environment builder
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
virtualenv
==========

A tool for creating isolated 'virtual' python environments.

.. image:: https://img.shields.io/pypi/v/virtualenv.svg
  :target: https://pypi.org/project/virtualenv
  :alt: Latest version on PyPi
.. image:: https://img.shields.io/pypi/pyversions/virtualenv.svg
  :target: https://pypi.org/project/virtualenv/
  :alt: Supported Python versions
.. image:: https://dev.azure.com/pypa/virtualenv/_apis/build/status/pypa.virtualenv?branchName=master
  :target: https://dev.azure.com/pypa/virtualenv/_build/latest?definitionId=11&branchName=master
  :alt: Azure Pipelines build status
.. image:: https://readthedocs.org/projects/virtualenv/badge/?version=latest&style=flat-square
  :target: https://virtualenv.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation status
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
  :target: https://github.com/ambv/black
  :alt: Code style: black

* `Installation <https://virtualenv.pypa.io/en/latest/installation.html>`_
* `Documentation <https://virtualenv.pypa.io/>`_
* `Changelog <https://virtualenv.pypa.io/en/latest/changes.html>`_
* `Issues <https://github.com/pypa/virtualenv/issues>`_
* `PyPI <https://pypi.org/project/virtualenv/>`_
* `Github <https://github.com/pypa/virtualenv>`_
* `User mailing list <http://groups.google.com/group/python-virtualenv>`_
* `Dev mailing list <http://groups.google.com/group/pypa-dev>`_
* User IRC: `#pypa on Freenode <https://webchat.freenode.net/?channels=%23pypa>`_
* Dev IRC: `#pypa-dev on Freenode <https://webchat.freenode.net/?channels=%23pypa-dev>`_


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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 16.6.1-0
- Update .spec from py2pack
- Manually add Requires and Suggests

