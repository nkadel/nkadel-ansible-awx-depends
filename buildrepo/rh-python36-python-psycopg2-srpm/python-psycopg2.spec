#
# spec file for package rh-python36-python-psycopg2
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name psycopg2

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
Version:        2.7.3.2
Release:        0%{?dist}
Url:            http://initd.org/psycopg/
Summary:        psycopg2 - Python-PostgreSQL Database Adapter
License:        LGPL with exceptions or ZPL (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added for postgresql support
Buildrequires:  postgresql-devel
%if %{with_dnf}
# Packages only needed to build the docs
Suggests:       %{?scl_prefix}python-Pygments >= 1.5
Suggests:       %{?scl_prefix}python-Sphinx >= 1.2
Suggests:       %{?scl_prefix}python-Sphinx <= 1.3
%endif # with_dnf

%description
Psycopg is the most popular PostgreSQL database adapter for the Python
programming language.  Its main features are the complete implementation of
the Python DB API 2.0 specification and the thread safety (several threads can
share the same connection).  It was designed for heavily multi-threaded
applications that create and destroy lots of cursors and make a large number
of concurrent "INSERT"s or "UPDATE"s.

Psycopg 2 is mostly implemented in C as a libpq wrapper, resulting in being
both efficient and secure.  It features client-side and server-side cursors,
asynchronous communication and notifications, "COPY TO/COPY FROM" support.
Many Python types are supported out-of-the-box and adapted to matching
PostgreSQL data types; adaptation can be extended and customized thanks to a
flexible objects adaptation system.

Psycopg 2 is both Unicode and Python 3 friendly.


Documentation
-------------

Documentation is included in the ``doc`` directory and is `available online`__.

.. __: http://initd.org/psycopg/docs/


Installation
------------

If your ``pip`` version supports wheel_ packages it should be possible to
install a binary version of Psycopg including all the dependencies from PyPI_.
Just run::

    $ pip install -U pip      # make sure your pip is up-to-date
    $ pip install psycopg2

If you want to build Psycopg from source you will need some prerequisites (a C
compiler, development packages): please check the install_ and the faq_
documents in the ``doc`` dir for the details.

.. _wheel: http://pythonwheels.com/
.. _PyPI: https://pypi.python.org/pypi/psycopg2
.. _install: http://initd.org/psycopg/docs/install.html#install-from-source
.. _faq: http://initd.org/psycopg/docs/faq.html#faq-compile

For any other resource (source code repository, bug tracker, mailing list)
please check the `project homepage`__.

.. __: http://initd.org/psycopg/


:Linux/OSX: |travis|
:Windows: |appveyor|

.. |travis| image:: https://travis-ci.org/psycopg/psycopg2.svg?branch=master
    :target: https://travis-ci.org/psycopg/psycopg2
    :alt: Linux and OSX build status

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/psycopg/psycopg2?branch=master&svg=true
    :target: https://ci.appveyor.com/project/psycopg/psycopg2/branch/master
    :alt: Windows build status




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
%{python3_sitearch}/*

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.7.3.2-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Add postgresql-devel Buildrequires for pg-config and include files
