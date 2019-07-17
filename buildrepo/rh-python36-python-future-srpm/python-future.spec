#
# spec file for package rh-python36-python-future
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name future

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
Version:        0.17.1
Release:        0%{?dist}
Url:            https://python-future.org
Summary:        Clean single-source support for Python 3 and 2
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
future: Easy, safe support for Python 2/3 compatibility
=======================================================

``future`` is the missing compatibility layer between Python 2 and Python
3. It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 2 and Python 3 with minimal overhead.

It is designed to be used as follows::

    from __future__ import (absolute_import, division,
                            print_function, unicode_literals)
    from builtins import (
             bytes, dict, int, list, object, range, str,
             ascii, chr, hex, input, next, oct, open,
             pow, round, super,
             filter, map, zip)

followed by predominantly standard, idiomatic Python 3 code that then runs
similarly on Python 2.6/2.7 and Python 3.3+.

The imports have no effect on Python 3. On Python 2, they shadow the
corresponding builtins, which normally have different semantics on Python 3
versus 2, to provide their Python 3 semantics.


Standard library reorganization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``future`` supports the standard library reorganization (PEP 3108) through the
following Py3 interfaces:

    >>> # Top-level packages with Py3 names provided on Py2:
    >>> import html.parser
    >>> import queue
    >>> import tkinter.dialog
    >>> import xmlrpc.client
    >>> # etc.

    >>> # Aliases provided for extensions to existing Py2 module names:
    >>> from future.standard_library import install_aliases
    >>> install_aliases()

    >>> from collections import Counter, OrderedDict   # backported to Py2.6
    >>> from collections import UserDict, UserList, UserString
    >>> import urllib.request
    >>> from itertools import filterfalse, zip_longest
    >>> from subprocess import getoutput, getstatusoutput


Automatic conversion
--------------------

An included script called `futurize
<http://python-future.org/automatic_conversion.html>`_ aids in converting
code (from either Python 2 or Python 3) to code compatible with both
platforms. It is similar to ``python-modernize`` but goes further in
providing Python 3 compatibility through the use of the backported types
and builtin functions in ``future``.


Documentation
-------------

See: http://python-future.org


Credits
-------

:Author:  Ed Schofield
:Sponsor: Python Charmers Pty Ltd, Australia, and Python Charmers Pte
          Ltd, Singapore. http://pythoncharmers.com
:Others:  See docs/credits.rst or http://python-future.org/credits.html


Licensing
---------
Copyright 2013-2018 Python Charmers Pty Ltd, Australia.
The software is distributed under an MIT licence. See LICENSE.txt.

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
%{_bindir}/*

%changelog
* Fri Jul 12 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.17.1-0
- Update .spec from py2pack
- Manually add Requires and Suggests
