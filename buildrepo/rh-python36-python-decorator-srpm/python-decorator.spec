#
# spec file for package rh-python36-python-decorator
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name decorator

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
Version:        4.2.1
Release:        0%{?dist}
Url:            https://github.com/micheles/decorator
Summary:        Better living through Python with decorators
License:        new BSD License (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
Decorator module
=================

:Author: Michele Simionato
:E-mail: michele.simionato@gmail.com
:Requires: Python from 2.6 to 3.6
:Download page: http://pypi.python.org/pypi/decorator
:Installation: ``pip install decorator``
:License: BSD license

Installation
-------------

If you are lazy, just perform

 `$ pip install decorator`

which will install just the module on your system.

If you prefer to install the full distribution from source, including
the documentation, clone the `GitHub repo`_ or download the tarball_, unpack it and run

 `$ pip install .`

in the main directory, possibly as superuser.

.. _tarball: http://pypi.python.org/pypi/decorator
.. _GitHub repo: https://github.com/micheles/decorator

Testing
--------

If you have the source code installation you can run the tests with

 `$ python src/tests/test.py -v`

or (if you have setuptools installed)

 `$ python setup.py test`

Notice that you may run into trouble if in your system there
is an older version of the decorator module; in such a case remove the
old version. It is safe even to copy the module `decorator.py` over
an existing one, since we kept backward-compatibility for a long time.

Repository
---------------

The project is hosted on GitHub. You can look at the source here:

 https://github.com/micheles/decorator

Documentation
---------------

The documentation has been moved to http://decorator.readthedocs.io/en/latest/
You can download a PDF version of it from http://media.readthedocs.org/pdf/decorator/latest/decorator.pdf


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