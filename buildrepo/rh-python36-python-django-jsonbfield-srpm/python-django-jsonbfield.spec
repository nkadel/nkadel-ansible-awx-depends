#
# spec file for package rh-python36-python-django-jsonbfield
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name django-jsonbfield

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
Version:        0.1.0
Release:        0%{?dist}
Url:            https://github.com/totalgood/django-jsonbfield/
Summary:        Django JSONField that utilized PostGRESQL jsonb field type
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-psycopg2 >= 2.5.4
Requires:       %{?scl_prefix}python-Django >= 1.8
%if %{with_dnf}
%endif # with_dnf

%description
**Note:** This is basically a standalone version of the JSONB support in the Postgres contrib package of the Django master branch, targeted for the Django 1.9 release. 

JSONField
---------

.. class:: JSONField(**options)

    A field for storing JSON encoded data. In Python the data is represented in
    its Python native format: dictionaries, lists, strings, numbers, booleans
    and ``None``.

.. note::

    PostgreSQL has two native JSON based data types: ``json`` and ``jsonb``.
    The main difference between them is how they are stored and how they can be
    queried. The PostgreSQL ``json`` field is stored as the original string
    representation of the JSON and must be decoded on the fly when queried
    based on keys. The ``jsonb`` field is stored based on the actual structure
    of the JSON which allows indexing. The trade-off is a small additional cost
    on writing to the ``jsonb`` field. ``JSONField`` uses ``jsonb``.

    **This field is only supported on PostgreSQL versions at least 9.4**.

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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.1.0-0
- Rename from "python-jsonbfield" to "python-django-jsonbfield
- Update .spec from py2pack
- Manually add Requires and Suggests
