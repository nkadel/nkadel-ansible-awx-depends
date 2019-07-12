#
# spec file for package rh-python36-python-billiard
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name billiard

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
Version:        3.5.0.4
Release:        0%{?dist}
Url:            http://github.com/celery/billiard
Summary:        Python multiprocessing fork with improvements and bugfixes
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
%if %{with_dnf}
# M<anually added for pkgutils
Suggests:       %{?scl_prefix}python-wheel >= 0.29.0
Suggests:       %{?scl_prefix}python-flake8 >= 2.5.4
Suggests:       %{?scl_prefix}python-flakeplus >= 1.1
Suggests:       %{?scl_prefix}python-tox >= 2.3.1
# Manually added for test
Suggests:       %{?scl_prefix}python-case >= 1.3.1
Suggests:       %{?scl_prefix}python-pytest >= 3.0
# Manuallyed added for test-c1
Suggests:       %{?scl_prefix}python-pytest-cov
%endif # with_dnf

%description
========
billiard
========
:version: 3.5.0.4

`billiard` is a fork of the Python 2.7 `multiprocessing <http://docs.python.org/library/multiprocessing.html>`_
package. The multiprocessing package itself is a renamed and updated version of
R Oudkerk `pyprocessing <https://pypi.org/project/processing/>`_ package.
This standalone variant draws its fixes/improvements from python-trunk and provides
additional bug fixes and improvements.

- This package would not be possible if not for the contributions of not only
  the current maintainers but all of the contributors to the original pyprocessing
  package listed `here <http://pyprocessing.berlios.de/doc/THANKS.html>`_

- Also it is a fork of the multiprocessing backport package by Christian Heims.

- It includes the no-execv patch contributed by R. Oudkerk.

- And the Pool improvements previously located in `Celery`_.

- Billiard is used in and is a dependency for `Celery`_ and is maintained by the
  Celery team.

.. _`Celery`: http://celeryproject.org

Bug reporting
-------------

Please report bugs related to multiprocessing at the
`Python bug tracker <http://bugs.python.org/>`_. Issues related to billiard
should be reported at http://github.com/celery/billiard/issues.

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
