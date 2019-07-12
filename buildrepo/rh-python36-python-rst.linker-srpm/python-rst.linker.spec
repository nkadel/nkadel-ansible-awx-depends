#
# spec file for package rh-python36-python-rst.linker
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name rst.linker

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
Url:            https://github.com/jaraco/rst.linker
Summary:        rst.linker
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
Requires:       %{?scl_prefix}python-python-dateutil
%if %{with_dnf}
# [docs]
Suggests:       %{?scl_prefix}python-sphinx
Suggests:       %{?scl_prefix}python-jaraco.packaging >= 3.2
Suggests:       %{?scl_prefix}python-rst.linker >= 1.9

# [testing]
Suggests:       %{?scl_prefix}python-pytest >= 3.5
Suggests:       %{?scl_prefix}python-pytest-sugar >= 0.9.1
Suggests:       %{?scl_prefix}python-collective.checkdocs
Suggests:       %{?scl_prefix}python-pytest-flake8
Suggests:       %{?scl_prefix}python-path.py
%endif # with_dnf

%description
.. image:: https://img.shields.io/pypi/v/rst.linker.svg
   :target: https://pypi.org/project/rst.linker

.. image:: https://img.shields.io/pypi/pyversions/rst.linker.svg

.. image:: https://img.shields.io/travis/jaraco/rst.linker/master.svg
   :target: https://travis-ci.org/jaraco/rst.linker

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/rst-linker/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/rst-linker/branch/master

.. .. image:: https://readthedocs.org/projects/rstlinker/badge/?version=latest
..    :target: https://rstlinker.readthedocs.io/en/latest/?badge=latest


``rst.linker`` provides a routine for adding links and performing
other custom replacements to reStructuredText files as a Sphinx
extension.

Usage
=====

In your sphinx ``conf`` file, include ``rst.linker`` as an extension
and then add a ``link_files`` configuration section describing
the substitutions to make. For an example, see `rst.linker's own
conf.py
<https://github.com/jaraco/rst.linker/blob/master/docs/conf.py>`_
or read the source to learn more about the the linkers provided.




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
* Fri Jul 12 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.10-0
- Initialize with py2pack
- Manually add Requires for python-six and python-python-dateutil
- Manually add Suggests for docs and testing
- Manually add BuildRequires for setuptools_scm
