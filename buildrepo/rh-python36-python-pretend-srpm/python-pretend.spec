#
# spec file for package rh-python36-python-pretend
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pretend

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
Version:        1.0.8
Release:        0%{?dist}
Url:            https://github.com/alex/pretend
Summary:        A library for stubbing in Python
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
pretend
=======

.. image:: https://secure.travis-ci.org/alex/pretend.png
    :target: https://travis-ci.org/alex/pretend

Pretend is a library to make stubbing with Python easier.

What is stubbing?
-----------------

Stubbing is a technique for writing tests. You may hear the term mixed up with
mocks, fakes, or doubles. Basically a stub is an object that returns pre-canned
responses, rather than doing any computation.

Martin Fowler does a good job explaining the terms in his `Mocks Aren't Stubs`_
article.

.. _`Mocks Aren't Stubs`: http://martinfowler.com/articles/mocksArentStubs.html

How do I install ``pretend``?
-----------------------------

It's easy with ``pip``!

.. code:: bash

    $ pip install pretend

How do I use ``pretend``?
-------------------------

It's easy, the ``stub`` function makes it easy to create a stub:

.. code:: pycon

    >>> from pretend import stub
    >>> x = stub(country_code="US")
    >>> some_function(x)

Here ``x`` will be an object with a single attribute ``country_code`` which has
the value ``"US"``. Unlike mocks, ``x`` will not respond to any other attribute
or methods, nor does it have any methods for making assertions about what you
accessed.

If you want to add a method to the stub, simple provide a function to it:

.. code:: pycon

    >>> from pretend import stub
    >>> x = stub(country_code=lambda: "US")
    >>> x.country_code()
    'US'

It's important to note that functions on stubs *do not* take a ``self``
argument, this is because stubs should be returning pre-canned values, not
doing computations.

Exceptions with ``pretend``
---------------------------

Sometimes a method you want to stub doesn't return a value, but instead raises
an exception. To make this easy, ``pretend`` provides a helper function,
``raiser``, it can be used like so:

.. code:: pycon

    >>> from pretend import stub, raiser
    >>> x = stub(func=raiser(ValueError))
    >>> x.func()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "pretend.py", line 74, in inner
        raise exc
    ValueError

Why is stubbing better?
-----------------------

Ideally stubbing tests how your system responds to a particular input, rather
than which API is used. Stubbing still requires you to write tests that check
the results of a computation, rather than looking for side effects. This
doesn't always work though, so you do sometimes still need mocking (e.g.
sometimes you really want to check for a side effect.)

How do I get my stub into place?
--------------------------------

If you come from other mocking libraries you're probably used to a ``patch``
method to put a mock in place. ``pretend`` doesn't include anything like this,
a) we believe it's better, where possible, to pass stubs as arguments rather
than monkey patch them into place, b) we believe that when you do need to
monkey patch something into place you should use something provided by your
testing tool. ``py.test`` includes `such a tool`_.

.. _`such a tool`: http://pytest.org/latest/monkeypatch.html

What if I really need to record the calls?
------------------------------------------

If you really really need to, ``pretend`` includes a ``call_recorder`` utility:

.. code:: pycon

    >>> from pretend import call_recorder, call
    >>> f = call_recorder(lambda a: a + 2)
    >>> f(3)
    5
    >>> assert f.calls == [call(3)]

Who wrote this?
---------------

``pretend`` is by Alex Gaynor, who was just tired of not having a good stubbing
tool for Python. The name is from Idan Gazit.

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