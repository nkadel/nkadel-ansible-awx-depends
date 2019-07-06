#
# spec file for package rh-python36-python-txaio
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name txaio

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
Version:        2.9.0
Release:        0%{?dist}
Url:            https://github.com/crossbario/txaio
Summary:        Compatibility API between asyncio/Twisted/Trollius
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires:       %{?scl_prefix}python-zope.interface >= 3.6
Requires:       %{?scl_prefix}python-twisted >= 12.1.0
%if %{with_dnf}
# Manually added
Suggests:       %{?scl_prefix}python-pytest >= 2.6.4
Suggests:       %{?scl_prefix}python-pytest-cov >= 1.8.1
Suggests:       %{?scl_prefix}python-pep8 >= 1.6.2
Suggests:       %{?scl_prefix}python-sphinx >= 1.2.3
Suggests:       %{?scl_prefix}python-pyenchant >= 1.6.6
Suggests:       %{?scl_prefix}python-sphinxcontrib-spelling >= 2.1.2
Suggests:       %{?scl_prefix}python-sphinx_rtd_theme >= 0.1.9
Suggests:       %{?scl_prefix}python-tox >= 2.1.1
Suggests:       %{?scl_prefix}python-mock = 1.3.0
Suggests:       %{?scl_prefix}python-twine >= 1.6.5
%endif # with_dnf
%{?python_provide:%python_provide python-%{pypi_name}}

%description
**txaio** is a helper library for writing code that runs unmodified on
both `Twisted <https://twistedmatrix.com/>`_ and `asyncio <https://docs.python.org/3/library/asyncio.html>`_ / `Trollius <http://trollius.readthedocs.org/en/latest/index.html>`_.

This is like `six <http://pythonhosted.org/six/>`_, but for wrapping
over differences between Twisted and asyncio so one can write code
that runs unmodified on both (aka *source code compatibility*). In
other words: your *users* can choose if they want asyncio **or** Twisted
as a dependency.

Note that, with this approach, user code **runs under the native event
loop of either Twisted or asyncio**. This is different from attaching
either event loop to the other using some event loop adapter.

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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.9.0-0
- Update .spec file from py2pack
- Add Requires python-zope.interface and python-twisted manually
- Add Suggests manually
