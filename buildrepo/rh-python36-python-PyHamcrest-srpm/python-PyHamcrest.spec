#
# spec file for package rh-python36-python-PyHamcrest
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name PyHamcrest

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
Version:        1.9.0
Release:        0%{?dist}
Url:            https://github.com/hamcrest/PyHamcrest
Summary:        Hamcrest framework for matcher objects
License:        New BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-six
Requires:  %{?scl_prefix}python-six
%if %{with_dnf}
%endif # with_dnf

%description
PyHamcrest
==========

| |docs| |travis| |coveralls| |landscape| |scrutinizer| |codeclimate|
| |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/pyhamcrest/badge/?style=flat
    :target: https://pyhamcrest.readthedocs.org/
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/hamcrest/PyHamcrest/master.png?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/hamcrest/PyHamcrest

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/hamcrest/PyHamcrest?branch=master
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/hamcrest/PyHamcrest

.. |coveralls| image:: http://img.shields.io/coveralls/hamcrest/PyHamcrest/master.png?style=flat
    :alt: Coverage Status
    :target: https://coveralls.io/r/hamcrest/PyHamcrest

.. |landscape| image:: https://landscape.io/github/hamcrest/PyHamcrest/master/landscape.svg?style=flat
    :target: https://landscape.io/github/hamcrest/PyHamcrest/master
    :alt: Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/hamcrest/PyHamcrest/badges/gpa.svg
   :target: https://codeclimate.com/github/hamcrest/PyHamcrest
   :alt: Code Climate

.. |version| image:: http://img.shields.io/pypi/v/PyHamcrest.png?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/PyHamcrest

.. |downloads| image:: http://img.shields.io/pypi/dm/PyHamcrest.png?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/PyHamcrest

.. |wheel| image:: https://pypip.in/wheel/PyHamcrest/badge.png?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/PyHamcrest

.. |supported-versions| image:: https://pypip.in/py_versions/PyHamcrest/badge.png?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/PyHamcrest

.. |supported-implementations| image:: https://pypip.in/implementation/PyHamcrest/badge.png?style=flat
    :alt: Supported imlementations
    :target: https://pypi.python.org/pypi/PyHamcrest

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/hamcrest/PyHamcrest/master.png?style=flat
    :alt: Scrtinizer Status
    :target: https://scrutinizer-ci.com/g/hamcrest/PyHamcrest/


Introduction
============

PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations where
matchers are invaluable, such as UI validation, or data filtering, but it is in
the area of writing flexible tests that matchers are most commonly used. This
tutorial shows you how to use PyHamcrest for unit testing.

When writing tests it is sometimes difficult to get the balance right between
overspecifying the test (and making it brittle to changes), and not specifying
enough (making the test less valuable since it continues to pass even when the
thing being tested is broken). Having a tool that allows you to pick out
precisely the aspect under test and describe the values it should have, to a
controlled level of precision, helps greatly in writing tests that are "just
right." Such tests fail when the behavior of the aspect under test deviates
from the expected behavior, yet continue to pass when minor, unrelated changes
to the behaviour are made.

Installation
============

Hamcrest can be installed using the usual Python packaging tools. It depends on
distribute, but as long as you have a network connection when you install, the
installation process will take care of that for you.

My first PyHamcrest test
========================

We'll start by writing a very simple PyUnit test, but instead of using PyUnit's
``assertEqual`` method, we'll use PyHamcrest's ``assert_that`` construct and
the standard set of matchers:

.. code:: python

 from hamcrest import *
 import unittest

 class BiscuitTest(unittest.TestCase):
     def testEquals(self):
         theBiscuit = Biscuit('Ginger')
         myBiscuit = Biscuit('Ginger')
         assert_that(theBiscuit, equal_to(myBiscuit))

 if __name__ == '__main__':
     unittest.main()

The ``assert_that`` function is a stylized sentence for making a test
assertion. In this example, the subject of the assertion is the object
``theBiscuit``, which is the first method parameter. The second method
parameter is a matcher for ``Biscuit`` objects, here a matcher that checks one
object is equal to another using the Python ``==`` operator. The test passes
since the ``Biscuit`` class defines an ``__eq__`` method.

If you have more than one assertion in your test you can include an identifier
for the tested value in the assertion:

.. code:: python

 assert_that(theBiscuit.getChocolateChipCount(), equal_to(10), 'chocolate chips')
 assert_that(theBiscuit.getHazelnutCount(), equal_to(3), 'hazelnuts')

As a convenience, assert_that can also be used to verify a boolean condition:

.. code:: python

 assert_that(theBiscuit.isCooked(), 'cooked')

This is equivalent to the ``assert_`` method of unittest.TestCase, but because
it's a standalone function, it offers greater flexibility in test writing.


Predefined matchers
===================

PyHamcrest comes with a library of useful matchers:

* Object

  * ``equal_to`` - match equal object
  * ``has_length`` - match ``len()``
  * ``has_property`` - match value of property with given name
  * ``has_properties`` - match an object that has all of the given properties.
  * ``has_string`` - match ``str()``
  * ``instance_of`` - match object type
  * ``none``, ``not_none`` - match ``None``, or not ``None``
  * ``same_instance`` - match same object
  * ``calling, raises`` - wrap a method call and assert that it raises an exception

* Number

  * ``close_to`` - match number close to a given value
  * ``greater_than``, ``greater_than_or_equal_to``, ``less_than``,
    ``less_than_or_equal_to`` - match numeric ordering

* Text

  * ``contains_string`` - match part of a string
  * ``ends_with`` - match the end of a string
  * ``equal_to_ignoring_case`` - match the complete string but ignore case
  * ``equal_to_ignoring_whitespace`` - match the complete string but ignore extra whitespace
  * ``matches_regexp`` - match a regular expression in a string
  * ``starts_with`` - match the beginning of a string
  * ``string_contains_in_order`` - match parts of a string, in relative order

* Logical

  * ``all_of`` - ``and`` together all matchers
  * ``any_of`` - ``or`` together all matchers
  * ``anything`` - match anything, useful in composite matchers when you don't care about a particular value
  * ``is_not`` - negate the matcher

* Sequence

  * ``contains`` - exactly match the entire sequence
  * ``contains_inanyorder`` - match the entire sequence, but in any order
  * ``has_item`` - match if given item appears in the sequence
  * ``has_items`` - match if all given items appear in the sequence, in any order
  * ``is_in`` - match if item appears in the given sequence
  * ``only_contains`` - match if sequence's items appear in given list
  * ``empty`` - match if the sequence is empty

* Dictionary

  * ``has_entries`` - match dictionary with list of key-value pairs
  * ``has_entry`` - match dictionary containing a key-value pair
  * ``has_key`` - match dictionary with a key
  * ``has_value`` - match dictionary with a value

* Decorator

  * ``calling`` - wrap a callable in a deffered object, for subsequent matching on calling behaviour
  * ``raises`` - Ensure that a deferred callable raises as expected
  * ``described_as`` - give the matcher a custom failure description
  * ``is_`` - decorator to improve readability - see `Syntactic sugar` below

The arguments for many of these matchers accept not just a matching value, but
another matcher, so matchers can be composed for greater flexibility. For
example, ``only_contains(less_than(5))`` will match any sequence where every
item is less than 5.


Syntactic sugar
===============

PyHamcrest strives to make your tests as readable as possible. For example, the
``is_`` matcher is a wrapper that doesn't add any extra behavior to the
underlying matcher. The following assertions are all equivalent:

.. code:: python

 assert_that(theBiscuit, equal_to(myBiscuit))
 assert_that(theBiscuit, is_(equal_to(myBiscuit)))
 assert_that(theBiscuit, is_(myBiscuit))

The last form is allowed since ``is_(value)`` wraps most non-matcher arguments
with ``equal_to``. But if the argument is a type, it is wrapped with
``instance_of``, so the following are also equivalent:

.. code:: python

 assert_that(theBiscuit, instance_of(Biscuit))
 assert_that(theBiscuit, is_(instance_of(Biscuit)))
 assert_that(theBiscuit, is_(Biscuit))

*Note that PyHamcrest's ``is_`` matcher is unrelated to Python's ``is``
operator. The matcher for object identity is ``same_instance``.*


Writing custom matchers
=======================

PyHamcrest comes bundled with lots of useful matchers, but you'll probably find
that you need to create your own from time to time to fit your testing needs.
This commonly occurs when you find a fragment of code that tests the same set
of properties over and over again (and in different tests), and you want to
bundle the fragment into a single assertion. By writing your own matcher you'll
eliminate code duplication and make your tests more readable!

Let's write our own matcher for testing if a calendar date falls on a Saturday.
This is the test we want to write:

.. code:: python

 def testDateIsOnASaturday(self):
     d = datetime.date(2008, 04, 26)
     assert_that(d, is_(on_a_saturday()))

And here's the implementation:

.. code:: python

 from hamcrest.core.base_matcher import BaseMatcher
 from hamcrest.core.helpers.hasmethod import hasmethod

 class IsGivenDayOfWeek(BaseMatcher):

     def __init__(self, day):
         self.day = day  # Monday is 0, Sunday is 6

     def _matches(self, item):
         if not hasmethod(item, 'weekday'):
             return False
         return item.weekday() == self.day

     def describe_to(self, description):
         day_as_string = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                          'Friday', 'Saturday', 'Sunday']
         description.append_text('calendar date falling on ')    \
                    .append_text(day_as_string[self.day])

 def on_a_saturday():
     return IsGivenDayOfWeek(5)

For our Matcher implementation we implement the ``_matches`` method - which
calls the ``weekday`` method after confirming that the argument (which may not
be a date) has such a method - and the ``describe_to`` method - which is used
to produce a failure message when a test fails. Here's an example of how the
failure message looks:

.. code:: python

 assert_that(datetime.date(2008, 04, 06), is_(on_a_saturday()))

fails with the message::

    AssertionError:
    Expected: is calendar date falling on Saturday
         got: <2008-04-06>

Let's say this matcher is saved in a module named ``isgivendayofweek``. We
could use it in our test by importing the factory function ``on_a_saturday``:

.. code:: python

 from hamcrest import *
 import unittest
 from isgivendayofweek import on_a_saturday

 class DateTest(unittest.TestCase):
     def testDateIsOnASaturday(self):
         d = datetime.date(2008, 04, 26)
         assert_that(d, is_(on_a_saturday()))

 if __name__ == '__main__':
     unittest.main()

Even though the ``on_a_saturday`` function creates a new matcher each time it
is called, you should not assume this is the only usage pattern for your
matcher. Therefore you should make sure your matcher is stateless, so a single
instance can be reused between matches.


More resources
==============

* Documentation_
* Package_
* Sources_
* Hamcrest_

.. _Documentation: http://readthedocs.org/docs/pyhamcrest/en/V1.8.2/
.. _Package: http://pypi.python.org/pypi/PyHamcrest
.. _Sources: https://github.com/hamcrest/PyHamcrest
.. _Hamcrest: http://hamcrest.org

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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.9.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
