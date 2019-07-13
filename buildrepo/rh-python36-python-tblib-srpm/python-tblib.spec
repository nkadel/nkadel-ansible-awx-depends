#
# spec file for package rh-python36-python-tblib
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name tblib

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
Version:        1.4.0
Release:        0%{?dist}
Url:            https://github.com/ionelmc/python-tblib
Summary:        Traceback serialization library.
License:        BSD 2-Clause License (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-sphinx >= 1.3
Requires:       %{?scl_prefix}python-sphinx-py3doc-enhanced-theme
%if %{with_dnf}
%endif # with_dnf

%description
========
Overview
========



Traceback serialization library.

* Free software: BSD license

It allows you to:

* `Pickle <https://docs.python.org/3/library/pickle.html>`_ tracebacks and raise exceptions
  with pickled tracebacks in different processes. This allows better error handling when running
  code over multiple processes (imagine multiprocessing, billiard, futures, celery etc).
* Create traceback objects from strings (the ``from_string`` method). *No pickling is used*.
* Serialize tracebacks to/from plain dicts (the ``from_dict`` and ``to_dict`` methods). *No pickling is used*.
* Raise the tracebacks created from the aforementioned sources.

**Again, note that using the pickle support is completely optional. You are solely responsible for
security problems should you decide to use the pickle support.**

Installation
============

::

    pip install tblib

Documentation
=============

.. contents::
   :local:

Pickling tracebacks
~~~~~~~~~~~~~~~~~~~

**Note**: The traceback objects that come out are stripped of some attributes (like variables). But you'll be able to raise exceptions with
those tracebacks or print them - that should cover 99% of the usecases.

::

    >>> from tblib import pickling_support
    >>> pickling_support.install()
    >>> import pickle, sys
    >>> def inner_0():
    ...     raise Exception('fail')
    ...
    >>> def inner_1():
    ...     inner_0()
    ...
    >>> def inner_2():
    ...     inner_1()
    ...
    >>> try:
    ...     inner_2()
    ... except:
    ...     s1 = pickle.dumps(sys.exc_info())
    ...
    >>> len(s1) > 1
    True
    >>> try:
    ...     inner_2()
    ... except:
    ...     s2 = pickle.dumps(sys.exc_info(), protocol=pickle.HIGHEST_PROTOCOL)
    ...
    >>> len(s2) > 1
    True

    >>> try:
    ...     import cPickle
    ... except ImportError:
    ...     import pickle as cPickle
    >>> try:
    ...     inner_2()
    ... except:
    ...     s3 = cPickle.dumps(sys.exc_info(), protocol=pickle.HIGHEST_PROTOCOL)
    ...
    >>> len(s3) > 1
    True

Unpickling
~~~~~~~~~~

::

    >>> pickle.loads(s1)
    (<...Exception'>, Exception('fail'...), <traceback object at ...>)

    >>> pickle.loads(s2)
    (<...Exception'>, Exception('fail'...), <traceback object at ...>)

    >>> pickle.loads(s3)
    (<...Exception'>, Exception('fail'...), <traceback object at ...>)

Raising
~~~~~~~

::

    >>> from six import reraise
    >>> reraise(*pickle.loads(s1))
    Traceback (most recent call last):
      ...
      File "<doctest README.rst[14]>", line 1, in <module>
        reraise(*pickle.loads(s2))
      File "<doctest README.rst[8]>", line 2, in <module>
        inner_2()
      File "<doctest README.rst[5]>", line 2, in inner_2
        inner_1()
      File "<doctest README.rst[4]>", line 2, in inner_1
        inner_0()
      File "<doctest README.rst[3]>", line 2, in inner_0
        raise Exception('fail')
    Exception: fail
    >>> reraise(*pickle.loads(s2))
    Traceback (most recent call last):
      ...
      File "<doctest README.rst[14]>", line 1, in <module>
        reraise(*pickle.loads(s2))
      File "<doctest README.rst[8]>", line 2, in <module>
        inner_2()
      File "<doctest README.rst[5]>", line 2, in inner_2
        inner_1()
      File "<doctest README.rst[4]>", line 2, in inner_1
        inner_0()
      File "<doctest README.rst[3]>", line 2, in inner_0
        raise Exception('fail')
    Exception: fail
    >>> reraise(*pickle.loads(s3))
    Traceback (most recent call last):
      ...
      File "<doctest README.rst[14]>", line 1, in <module>
        reraise(*pickle.loads(s2))
      File "<doctest README.rst[8]>", line 2, in <module>
        inner_2()
      File "<doctest README.rst[5]>", line 2, in inner_2
        inner_1()
      File "<doctest README.rst[4]>", line 2, in inner_1
        inner_0()
      File "<doctest README.rst[3]>", line 2, in inner_0
        raise Exception('fail')
    Exception: fail

What if we have a local stack, does it show correctly ?
-------------------------------------------------------

Yes it does::

    >>> exc_info = pickle.loads(s3)
    >>> def local_0():
    ...     reraise(*exc_info)
    ...
    >>> def local_1():
    ...     local_0()
    ...
    >>> def local_2():
    ...     local_1()
    ...
    >>> local_2()
    Traceback (most recent call last):
      File "...doctest.py", line ..., in __run
        compileflags, 1) in test.globs
      File "<doctest README.rst[24]>", line 1, in <module>
        local_2()
      File "<doctest README.rst[23]>", line 2, in local_2
        local_1()
      File "<doctest README.rst[22]>", line 2, in local_1
        local_0()
      File "<doctest README.rst[21]>", line 2, in local_0
        reraise(*exc_info)
      File "<doctest README.rst[11]>", line 2, in <module>
        inner_2()
      File "<doctest README.rst[5]>", line 2, in inner_2
        inner_1()
      File "<doctest README.rst[4]>", line 2, in inner_1
        inner_0()
      File "<doctest README.rst[3]>", line 2, in inner_0
        raise Exception('fail')
    Exception: fail

It also supports more contrived scenarios
-----------------------------------------

Like tracebacks with syntax errors::

    >>> from tblib import Traceback
    >>> from examples import bad_syntax
    >>> try:
    ...     bad_syntax()
    ... except:
    ...     et, ev, tb = sys.exc_info()
    ...     tb = Traceback(tb)
    ...
    >>> reraise(et, ev, tb.as_traceback())
    Traceback (most recent call last):
      ...
      File "<doctest README.rst[58]>", line 1, in <module>
        reraise(et, ev, tb.as_traceback())
      File "<doctest README.rst[57]>", line 2, in <module>
        bad_syntax()
      File "...tests...examples.py", line 18, in bad_syntax
        import badsyntax
      File "...tests...badsyntax.py", line 5
        is very bad
         ^
    SyntaxError: invalid syntax

Or other import failures::

    >>> from examples import bad_module
    >>> try:
    ...     bad_module()
    ... except:
    ...     et, ev, tb = sys.exc_info()
    ...     tb = Traceback(tb)
    ...
    >>> reraise(et, ev, tb.as_traceback())
    Traceback (most recent call last):
      ...
      File "<doctest README.rst[61]>", line 1, in <module>
        reraise(et, ev, tb.as_traceback())
      File "<doctest README.rst[60]>", line 2, in <module>
        bad_module()
      File "...tests...examples.py", line 23, in bad_module
        import badmodule
      File "...tests...badmodule.py", line 3, in <module>
        raise Exception("boom!")
    Exception: boom!

Or a traceback that's caused by exceeding the recursion limit (here we're
forcing the type and value to have consistency across platforms)::

    >>> def f(): f()
    >>> try:
    ...    f()
    ... except RuntimeError:
    ...    et, ev, tb = sys.exc_info()
    ...    tb = Traceback(tb)
    ...
    >>> reraise(RuntimeError, RuntimeError("maximum recursion depth exceeded"), tb.as_traceback())
    Traceback (most recent call last):
      ...
      File "<doctest README.rst[32]>", line 1, in f
        def f(): f()
      File "<doctest README.rst[32]>", line 1, in f
        def f(): f()
      File "<doctest README.rst[32]>", line 1, in f
        def f(): f()
      ...
    RuntimeError: maximum recursion depth exceeded

Reference
~~~~~~~~~

tblib.Traceback
---------------

It is used by the ``pickling_support``. You can use it too if you want more flexibility::

    >>> from tblib import Traceback
    >>> try:
    ...     inner_2()
    ... except:
    ...     et, ev, tb = sys.exc_info()
    ...     tb = Traceback(tb)
    ...
    >>> reraise(et, ev, tb.as_traceback())
    Traceback (most recent call last):
      ...
      File "<doctest README.rst[21]>", line 6, in <module>
        reraise(et, ev, tb.as_traceback())
      File "<doctest README.rst[21]>", line 2, in <module>
        inner_2()
      File "<doctest README.rst[5]>", line 2, in inner_2
        inner_1()
      File "<doctest README.rst[4]>", line 2, in inner_1
        inner_0()
      File "<doctest README.rst[3]>", line 2, in inner_0
        raise Exception('fail')
    Exception: fail

tblib.Traceback.to_dict
```````````````````````

You can use the ``to_dict`` method and the ``from_dict`` classmethod to
convert a Traceback into and from a dictionary serializable by the stdlib
json.JSONDecoder::

    >>> import json
    >>> from pprint import pprint
    >>> try:
    ...     inner_2()
    ... except:
    ...     et, ev, tb = sys.exc_info()
    ...     tb = Traceback(tb)
    ...     tb_dict = tb.to_dict()
    ...     pprint(tb_dict)
    {'tb_frame': {'f_code': {'co_filename': '<doctest README.rst[...]>',
                             'co_name': '<module>'},
                  'f_globals': {'__name__': '__main__'}},
     'tb_lineno': 2,
     'tb_next': {'tb_frame': {'f_code': {'co_filename': ...
                                         'co_name': 'inner_2'},
                              'f_globals': {'__name__': '__main__'}},
                 'tb_lineno': 2,
                 'tb_next': {'tb_frame': {'f_code': {'co_filename': ...
                                                     'co_name': 'inner_1'},
                                          'f_globals': {'__name__': '__main__'}},
                             'tb_lineno': 2,
                             'tb_next': {'tb_frame': {'f_code': {'co_filename': ...
                                                                 'co_name': 'inner_0'},
                                                      'f_globals': {'__name__': '__main__'}},
                                         'tb_lineno': 2,
                                         'tb_next': None}}}}

tblib.Traceback.from_dict
`````````````````````````

Building on the previous example::

    >>> tb_json = json.dumps(tb_dict)
    >>> tb = Traceback.from_dict(json.loads(tb_json))
    >>> reraise(et, ev, tb.as_traceback())
    Traceback (most recent call last):
      ...
      File "<doctest README.rst[21]>", line 6, in <module>
        reraise(et, ev, tb.as_traceback())
      File "<doctest README.rst[21]>", line 2, in <module>
        inner_2()
      File "<doctest README.rst[5]>", line 2, in inner_2
        inner_1()
      File "<doctest README.rst[4]>", line 2, in inner_1
        inner_0()
      File "<doctest README.rst[3]>", line 2, in inner_0
        raise Exception('fail')
    Exception: fail

tblib.Traceback.from_string
```````````````````````````

::

    >>> tb = Traceback.from_string("""
    ... File "skipped.py", line 123, in func_123
    ... Traceback (most recent call last):
    ...   File "tests/examples.py", line 2, in func_a
    ...     func_b()
    ...   File "tests/examples.py", line 6, in func_b
    ...     func_c()
    ...   File "tests/examples.py", line 10, in func_c
    ...     func_d()
    ...   File "tests/examples.py", line 14, in func_d
    ... Doesn't: matter
    ... """)
    >>> reraise(et, ev, tb.as_traceback())
    Traceback (most recent call last):
      ...
      File "<doctest README.rst[42]>", line 6, in <module>
        reraise(et, ev, tb.as_traceback())
      File "...examples.py", line 2, in func_a
        func_b()
      File "...examples.py", line 6, in func_b
        func_c()
      File "...examples.py", line 10, in func_c
        func_d()
      File "...examples.py", line 14, in func_d
        raise Exception("Guessing time !")
    Exception: fail


If you use the ``strict=False`` option then parsing is a bit more lax::

    >>> tb = Traceback.from_string("""
    ... File "bogus.py", line 123, in bogus
    ... Traceback (most recent call last):
    ...  File "tests/examples.py", line 2, in func_a
    ...   func_b()
    ...    File "tests/examples.py", line 6, in func_b
    ...     func_c()
    ...    File "tests/examples.py", line 10, in func_c
    ...   func_d()
    ...  File "tests/examples.py", line 14, in func_d
    ... Doesn't: matter
    ... """, strict=False)
    >>> reraise(et, ev, tb.as_traceback())
    Traceback (most recent call last):
      ...
      File "<doctest README.rst[42]>", line 6, in <module>
        reraise(et, ev, tb.as_traceback())
      File "bogus.py", line 123, in bogus
      File "...examples.py", line 2, in func_a
        func_b()
      File "...examples.py", line 6, in func_b
        func_c()
      File "...examples.py", line 10, in func_c
        func_d()
      File "...examples.py", line 14, in func_d
        raise Exception("Guessing time !")
    Exception: fail

tblib.decorators.return_error
-----------------------------

::

    >>> from tblib.decorators import return_error
    >>> inner_2r = return_error(inner_2)
    >>> e = inner_2r()
    >>> e
    <tblib.decorators.Error object at ...>
    >>> e.reraise()
    Traceback (most recent call last):
      ...
      File "<doctest README.rst[26]>", line 1, in <module>
        e.reraise()
      File "...tblib...decorators.py", line 19, in reraise
        reraise(self.exc_type, self.exc_value, self.traceback)
      File "...tblib...decorators.py", line 25, in return_exceptions_wrapper
        return func(*args, **kwargs)
      File "<doctest README.rst[5]>", line 2, in inner_2
        inner_1()
      File "<doctest README.rst[4]>", line 2, in inner_1
        inner_0()
      File "<doctest README.rst[3]>", line 2, in inner_0
        raise Exception('fail')
    Exception: fail

How's this useful? Imagine you're using multiprocessing like this::

    # Note that Python 3.4 and later will show the remote traceback (but as a string sadly) so we skip testing this.
    >>> import traceback
    >>> from multiprocessing import Pool
    >>> from examples import func_a
    >>> pool = Pool()  # doctest: +SKIP
    >>> try:  # doctest: +SKIP
    ...     for i in pool.map(func_a, range(5)):
    ...         print(i)
    ... except:
    ...     print(traceback.format_exc())
    ...
    Traceback (most recent call last):
      File "<doctest README.rst[...]>", line 2, in <module>
        for i in pool.map(func_a, range(5)):
      File "...multiprocessing...pool.py", line ..., in map
        ...
      File "...multiprocessing...pool.py", line ..., in get
        ...
    Exception: Guessing time !
    <BLANKLINE>
    >>> pool.terminate()  # doctest: +SKIP

Not very useful is it? Let's sort this out::

    >>> from tblib.decorators import apply_with_return_error, Error
    >>> from itertools import repeat
    >>> pool = Pool()
    >>> try:
    ...     for i in pool.map(apply_with_return_error, zip(repeat(func_a), range(5))):
    ...         if isinstance(i, Error):
    ...             i.reraise()
    ...         else:
    ...             print(i)
    ... except:
    ...     print(traceback.format_exc())
    ...
    Traceback (most recent call last):
      File "<doctest README.rst[...]>", line 4, in <module>
        i.reraise()
      File "...tblib...decorators.py", line ..., in reraise
        reraise(self.exc_type, self.exc_value, self.traceback)
      File "...tblib...decorators.py", line ..., in return_exceptions_wrapper
        return func(*args, **kwargs)
      File "...tblib...decorators.py", line ..., in apply_with_return_error
        return args[0](*args[1:])
      File "...examples.py", line 2, in func_a
        func_b()
      File "...examples.py", line 6, in func_b
        func_c()
      File "...examples.py", line 10, in func_c
        func_d()
      File "...examples.py", line 14, in func_d
        raise Exception("Guessing time !")
    Exception: Guessing time !
    <BLANKLINE>
    >>> pool.terminate()

Much better !

What if we have a local call stack ?
````````````````````````````````````

::

    >>> def local_0():
    ...     pool = Pool()
    ...     for i in pool.map(apply_with_return_error, zip(repeat(func_a), range(5))):
    ...         if isinstance(i, Error):
    ...             i.reraise()
    ...         else:
    ...             print(i)
    ...
    >>> def local_1():
    ...     local_0()
    ...
    >>> def local_2():
    ...     local_1()
    ...
    >>> try:
    ...     local_2()
    ... except:
    ...     print(traceback.format_exc())
    Traceback (most recent call last):
      File "<doctest README.rst[...]>", line 2, in <module>
        local_2()
      File "<doctest README.rst[...]>", line 2, in local_2
        local_1()
      File "<doctest README.rst[...]>", line 2, in local_1
        local_0()
      File "<doctest README.rst[...]>", line 5, in local_0
        i.reraise()
      File "...tblib...decorators.py", line 20, in reraise
        reraise(self.exc_type, self.exc_value, self.traceback)
      File "...tblib...decorators.py", line 27, in return_exceptions_wrapper
        return func(*args, **kwargs)
      File "...tblib...decorators.py", line 47, in apply_with_return_error
        return args[0](*args[1:])
      File "...tests...examples.py", line 2, in func_a
        func_b()
      File "...tests...examples.py", line 6, in func_b
        func_c()
      File "...tests...examples.py", line 10, in func_c
        func_d()
      File "...tests...examples.py", line 14, in func_d
        raise Exception("Guessing time !")
    Exception: Guessing time !
    <BLANKLINE>

Other weird stuff
`````````````````

Clearing traceback works (Python 3.4 and up)::

    >>> tb = Traceback.from_string("""
    ... File "skipped.py", line 123, in func_123
    ... Traceback (most recent call last):
    ...   File "tests/examples.py", line 2, in func_a
    ...     func_b()
    ...   File "tests/examples.py", line 6, in func_b
    ...     func_c()
    ...   File "tests/examples.py", line 10, in func_c
    ...     func_d()
    ...   File "tests/examples.py", line 14, in func_d
    ... Doesn't: matter
    ... """)
    >>> import traceback, sys
    >>> if sys.version_info > (3, 4):
    ...     traceback.clear_frames(tb)

Credits
=======

* `mitsuhiko/jinja2 <https://github.com/mitsuhiko/jinja2>`_ for figuring a way to create traceback objects.


Changelog
=========

1.4.0 (2019-05-02)
~~~~~~~~~~~~~~~~~~

* Remove support for end of life Python 3.3.
* Fixed tests for Python 3.7. Contributed by Elliott Sales de Andrade in
  `#36 <https://github.com/ionelmc/python-tblib/issues/36>`_.
* Fixed compatibility issue with Twised (``twisted.python.failure.Failure`` expected a ``co_code`` attribute).

1.3.2 (2017-04-09)
~~~~~~~~~~~~~~~~~~

* Add support for PyPy3.5-5.7.1-beta. Previously ``AttributeError:
  'Frame' object has no attribute 'clear'``  could be raised. See PyPy
  issue `#2532 <https://bitbucket.org/pypy/pypy/issues/2532/pypy3-attributeerror-frame-object-has-no>`_.

1.3.1 (2017-03-27)
~~~~~~~~~~~~~~~~~~

* Fixed handling for tracebacks due to exceeding the recursion limit.
  Fixes `#15 <https://github.com/ionelmc/python-tblib/issues/15>`_.

1.3.0 (2016-03-08)
~~~~~~~~~~~~~~~~~~

* Added ``Traceback.from_string``.

1.2.0 (2015-12-18)
~~~~~~~~~~~~~~~~~~

* Fixed handling for tracebacks from generators and other internal improvements
  and optimizations. Contributed by DRayX in `#10 <https://github.com/ionelmc/python-tblib/issues/10>`_
  and `#11 <https://github.com/ionelmc/python-tblib/pull/11>`_.

1.1.0 (2015-07-27)
~~~~~~~~~~~~~~~~~~

* Added support for Python 2.6. Contributed by Arcadiy Ivanov in
  `#8 <https://github.com/ionelmc/python-tblib/pull/8>`_.

1.0.0 (2015-03-30)
~~~~~~~~~~~~~~~~~~

* Added ``to_dict`` method and ``from_dict`` classmethod on Tracebacks.
  Contributed by beckjake in `#5 <https://github.com/ionelmc/python-tblib/pull/5>`_.




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
