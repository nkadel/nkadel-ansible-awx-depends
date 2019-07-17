%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name humanfriendly
%define version 4.8
%define unmangled_version 4.8
%define unmangled_version 4.8
%define release 1

Summary: Human friendly output for text interfaces using Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}humanfriendly
Version: %{version}
Release: %{release}
Source0: humanfriendly-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/humanfriendly-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Peter Odding <peter@peterodding.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://humanfriendly.readthedocs.io


%description
humanfriendly: Human friendly input/output in Python
====================================================

.. image:: https://travis-ci.org/xolox/python-humanfriendly.svg?branch=master
   :target: https://travis-ci.org/xolox/python-humanfriendly

.. image:: https://coveralls.io/repos/xolox/python-humanfriendly/badge.png?branch=master
   :target: https://coveralls.io/r/xolox/python-humanfriendly?branch=master

The functions and classes in the `humanfriendly` package can be used to make
text interfaces more user friendly. Some example features:

- Parsing and formatting numbers, file sizes, pathnames and timespans in
  simple, human friendly formats.

- Easy to use timers for long running operations, with human friendly
  formatting of the resulting timespans.

- Prompting the user to select a choice from a list of options by typing the
  option's number or a unique substring of the option.

- Terminal interaction including text styling (ANSI escape sequences), user
  friendly rendering of usage messages and querying the terminal for its
  size.

The `humanfriendly` package is currently tested on Python 2.6, 2.7, 3.4, 3.5,
3.6 and PyPy (2.7) on Linux and Mac OS X. While the intention is to support
Windows as well, you may encounter some rough edges.

.. contents::
   :local:

Getting started
---------------

It's very simple to start using the `humanfriendly` package::

   >>> import humanfriendly
   >>> user_input = raw_input("Enter a readable file size: ")
   Enter a readable file size: 16G
   >>> num_bytes = humanfriendly.parse_size(user_input)
   >>> print num_bytes
   16000000000
   >>> print "You entered:", humanfriendly.format_size(num_bytes)
   You entered: 16 GB
   >>> print "You entered:", humanfriendly.format_size(num_bytes, binary=True)
   You entered: 14.9 GiB

Command line
------------

.. A DRY solution to avoid duplication of the `humanfriendly --help' text:
..
.. [[[cog
.. from humanfriendly.usage import inject_usage
.. inject_usage('humanfriendly.cli')
.. ]]]

**Usage:** `humanfriendly [OPTIONS]`

Human friendly input/output (text formatting) on the command
line based on the Python package with the same name.

**Supported options:**

.. csv-table::
   :header: Option, Description
   :widths: 30, 70


   "``-c``, ``--run-command``","Execute an external command (given as the positional arguments) and render
   a spinner and timer while the command is running. The exit status of the
   command is propagated."
   ``--format-table``,"Read tabular data from standard input (each line is a row and each
   whitespace separated field is a column), format the data as a table and
   print the resulting table to standard output. See also the ``--delimiter``
   option."
   "``-d``, ``--delimiter=VALUE``","Change the delimiter used by ``--format-table`` to ``VALUE`` (a string). By default
   all whitespace is treated as a delimiter."
   "``-l``, ``--format-length=LENGTH``","Convert a length count (given as the integer or float ``LENGTH``) into a human
   readable string and print that string to standard output."
   "``-n``, ``--format-number=VALUE``","Format a number (given as the integer or floating point number ``VALUE``) with
   thousands separators and two decimal places (if needed) and print the
   formatted number to standard output."
   "``-s``, ``--format-size=BYTES``","Convert a byte count (given as the integer ``BYTES``) into a human readable
   string and print that string to standard output."
   "``-b``, ``--binary``","Change the output of ``-s``, ``--format-size`` to use binary multiples of bytes
   (base-2) instead of the default decimal multiples of bytes (base-10)."
   "``-t``, ``--format-timespan=SECONDS``","Convert a number of seconds (given as the floating point number ``SECONDS``)
   into a human readable timespan and print that string to standard output."
   ``--parse-length=VALUE``,"Parse a human readable length (given as the string ``VALUE``) and print the
   number of metres to standard output."
   ``--parse-size=VALUE``,"Parse a human readable data size (given as the string ``VALUE``) and print the
   number of bytes to standard output."
   ``--demo``,"Demonstrate changing the style and color of the terminal font using ANSI
   escape sequences."
   "``-h``, ``--help``",Show this message and exit.

.. [[[end]]]

A note about size units
-----------------------

When I originally published the `humanfriendly` package I went with binary
multiples of bytes (powers of two). It was pointed out several times that this
was a poor choice (see issue `#4`_ and pull requests `#8`_ and `#9`_) and thus
the new default became decimal multiples of bytes (powers of ten):

+------+---------------+---------------+
| Unit | Binary value  | Decimal value |
+------+---------------+---------------+
| KB   |          1024 |          1000 +
+------+---------------+---------------+
| MB   |       1048576 |       1000000 |
+------+---------------+---------------+
| GB   |    1073741824 |    1000000000 |
+------+---------------+---------------+
| TB   | 1099511627776 | 1000000000000 |
+------+---------------+---------------+
| etc  |               |               |
+------+---------------+---------------+

The option to use binary multiples of bytes remains by passing the keyword
argument `binary=True` to the `format_size()`_ and `parse_size()`_ functions.

Contact
-------

The latest version of `humanfriendly` is available on PyPI_ and GitHub_. The
documentation is hosted on `Read the Docs`_. For bug reports please create an
issue on GitHub_. If you have questions, suggestions, etc. feel free to send me
an e-mail at `peter@peterodding.com`_.

License
-------

This software is licensed under the `MIT license`_.

© 2018 Peter Odding.

.. External references:
.. _#4: https://github.com/xolox/python-humanfriendly/issues/4
.. _#8: https://github.com/xolox/python-humanfriendly/pull/8
.. _#9: https://github.com/xolox/python-humanfriendly/pull/9
.. _format_size(): https://humanfriendly.readthedocs.io/en/latest/#humanfriendly.format_size
.. _GitHub: https://github.com/xolox/python-humanfriendly
.. _MIT license: http://en.wikipedia.org/wiki/MIT_License
.. _parse_size(): https://humanfriendly.readthedocs.io/en/latest/#humanfriendly.parse_size
.. _peter@peterodding.com: peter@peterodding.com
.. _PyPI: https://pypi.python.org/pypi/humanfriendly
.. _Read the Docs: https://humanfriendly.readthedocs.io



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n humanfriendly-%{unmangled_version} -n humanfriendly-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
