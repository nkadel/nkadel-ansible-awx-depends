#
# spec file for package rh-python36-python-django_polymorphic
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# The django-polymorphicmodule is listed as djangl_polymorphic on pypi.org
#%global pypi_name django_polymorphic
%global pypi_name django-polymorphic

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
Version:        2.0.2
Release:        0%{?dist}
Url:            https://github.com/django-polymorphic/django-polymorphic
Summary:        Seamless polymorphic inheritance for Django models
License:        BSD License (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:  %{?scl_prefix}python-Django >= 1.11
%if %{with_dnf}
%endif # with_dnf

%description
.. image::  https://travis-ci.org/django-polymorphic/django-polymorphic.svg?branch=master
    :target: http://travis-ci.org/django-polymorphic/django-polymorphic
.. image:: https://img.shields.io/pypi/v/django-polymorphic.svg
    :target: https://pypi.python.org/pypi/django-polymorphic/
.. image:: https://img.shields.io/codecov/c/github/django-polymorphic/django-polymorphic/master.svg
    :target: https://codecov.io/github/django-polymorphic/django-polymorphic?branch=master

Polymorphic Models for Django
=============================

Django-polymorphic simplifies using inherited models in Django projects.
When a query is made at the base model, the inherited model classes are returned.

When we store models that inherit from a ``Project`` model...

.. code-block:: python

    >>> Project.objects.create(topic="Department Party")
    >>> ArtProject.objects.create(topic="Painting with Tim", artist="T. Turner")
    >>> ResearchProject.objects.create(topic="Swallow Aerodynamics", supervisor="Dr. Winter")

...and want to retrieve all our projects, the subclassed models are returned!

.. code-block:: python

    >>> Project.objects.all()
    [ <Project:         id 1, topic "Department Party">,
      <ArtProject:      id 2, topic "Painting with Tim", artist "T. Turner">,
      <ResearchProject: id 3, topic "Swallow Aerodynamics", supervisor "Dr. Winter"> ]

Using vanilla Django, we get the base class objects, which is rarely what we wanted:

.. code-block:: python

    >>> Project.objects.all()
    [ <Project: id 1, topic "Department Party">,
      <Project: id 2, topic "Painting with Tim">,
      <Project: id 3, topic "Swallow Aerodynamics"> ]

This also works when the polymorphic model is accessed via
ForeignKeys, ManyToManyFields or OneToOneFields.

Features
--------

* Full admin integration.
* ORM integration:

  * support for ForeignKey, ManyToManyField, OneToOneField descriptors.
  * Filtering/ordering of inherited models (``ArtProject___artist``).
  * Filtering model types: ``instance_of(...)`` and ``not_instance_of(...)``
  * Combining querysets of different models (``qs3 = qs1 | qs2``)
  * Support for custom user-defined managers.
* Uses the minumum amount of queries needed to fetch the inherited models.
* Disabling polymorphic behavior when needed.

While *django-polymorphic* makes subclassed models easy to use in Django,
we still encourage to use them with caution. Each subclassed model will require
Django to perform an ``INNER JOIN`` to fetch the model fields from the database.
While taking this in mind, there are valid reasons for using subclassed models.
That's what this library is designed for!

The current release of *django-polymorphic* supports Django 1.11, 2.0 and Python 2.7 and 3.4+ is supported.
For older Django versions, install *django-polymorphic==1.3*.

For more information, see the `documentation at Read the Docs <https://django-polymorphic.readthedocs.io/>`_.

Installation
------------

Install using ``pip``\ ...

.. code:: bash

    $ pip install django-polymorphic

License
=======

Django-polymorphic uses the same license as Django (BSD-like).




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
%{python3_sitelib}/*

%changelog
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.0.2-0
- Update .spec from py2pack
- Reset global_name to django-polymorphic from django_polymorphic, pypi.org mixes the names
- Add Requires for Django
