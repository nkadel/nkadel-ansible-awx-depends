#
# spec file for package rh-python36-python-django-split-settings
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name django-split-settings

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
Version:        0.3.0
Release:        0%{?dist}
Url:            http://github.com/sobolevn/django-split-settings
Summary:        Organize Django settings into multiple files and directories. Easily override and modify settings. Use wildcards and optional settings files.
License:        BSD License (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-pytest-runner
%if %{with_dnf}
%endif # with_dnf

%description
.. image:: https://github.com/sobolevn/django-split-settings/blob/master/media/logo-black.png?raw=true
     :target: https://github.com/sobolevn/django-split-settings
     :align: center

----------

.. image:: https://travis-ci.org/sobolevn/django-split-settings.svg?branch=master
     :target: https://travis-ci.org/sobolevn/django-split-settings

.. image:: https://coveralls.io/repos/github/sobolevn/django-split-settings/badge.svg?branch=master
     :target: https://coveralls.io/github/sobolevn/django-split-settings?branch=master

.. image:: https://badge.fury.io/py/django-split-settings.svg
     :target: http://badge.fury.io/py/django-split-settings

.. image:: https://img.shields.io/pypi/pyversions/django-split-settings.svg
     :target: https://pypi.python.org/pypi/django-split-settings

.. image:: https://readthedocs.org/projects/django-split-settings/badge/?version=latest
      :target: http://django-split-settings.readthedocs.io/en/latest/?badge=latest

Organize Django settings into multiple files and directories. Easily
override and modify settings. Use wildcards in settings file paths
and mark settings files as optional.

Read this `medium`_ post for more information.

.. _medium: https://medium.com/wemake-services/managing-djangos-settings-e2b7f496120d

Requirements
------------

While this package will most likely work with the most versions of ``django``, we do not officially support any versions except the latest release and the current LTS version, which are ``1.11`` and ``2.0`` right now.

This package has no dependencies itself.


Installation
------------

Install by using ``pip``:

.. code:: bash

    pip install django-split-settings

We also recommend to try `pipenv <https://docs.pipenv.org/>`_ to handle dependencies.


Usage
-----

Replace your existing ``settings.py`` with a list of components that
make up your Django settings. Preferably create a settings package
that contains all the files.

Here's a minimal example:

.. code:: python

    from split_settings.tools import optional, include

    include(
        'components/base.py',
        'components/database.py',
        optional('local_settings.py')
    )

In the example, the files ``base.py`` and ``database.py`` are included
in that order from the subdirectory called ``components/``.
``local_settings.py`` in the same directory is included if it exists.

**Note:** The local context is passed on to each file, so each
following file can access and modify the settings declared in the
previous files.

We also made a in-depth `tutorial`_.

.. _tutorial: https://medium.com/wemake-services/managing-djangos-settings-e2b7f496120d


Tips and tricks
---------------

You can use wildcards in file paths:

.. code:: python

    include('components/my_app/*.py')

Note that files are included in the order that ``glob`` returns them,
probably in the same order as what ``ls -U`` would list them. The
files are NOT in alphabetical order.


Do you want to contribute?
--------------------------

Read the `contributing`_ file.

.. _contributing: https://github.com/sobolevn/django-split-settings/blob/master/CONTRIBUTING.rst


Version history
---------------

See `changelog`_ file.

.. _changelog: https://github.com/sobolevn/django-split-settings/blob/master/CHANGELOG.rst




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
