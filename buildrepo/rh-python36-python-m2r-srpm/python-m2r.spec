#
# spec file for package rh-python36-python-m2r
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name m2r

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
Version:        0.2.1
Release:        0%{?dist}
Url:            https://github.com/miyakogi/m2r
Summary:        Markdown and reStructuredText in a single file.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-mistune
Requires:       %{?scl_prefix}python-docutils
%if %{with_dnf}
%endif # with_dnf

%description

M2R
===


.. image:: https://img.shields.io/pypi/v/m2r.svg
   :target: https://pypi.python.org/pypi/m2r
   :alt: PyPI


.. image:: https://img.shields.io/pypi/pyversions/m2r.svg
   :target: https://pypi.python.org/pypi/m2r
   :alt: PyPI version


.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg
   :target: https://miyakogi.github.io/m2r
   :alt: Documentation


.. image:: https://travis-ci.org/miyakogi/m2r.svg?branch=master
   :target: https://travis-ci.org/miyakogi/m2r
   :alt: Build Status


.. image:: https://codecov.io/gh/miyakogi/m2r/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/miyakogi/m2r
   :alt: codecov


----

M2R converts a markdown file including reStructuredText (rst) markups to a valid
rst format.

Why another converter?
----------------------

I wanted to write sphinx document in markdown, since it's widely used now and
easy to write code blocks and lists. However, converters using pandoc or
recommonmark do not support many rst markups and sphinx extensions. For
example, rst's reference link like ``see `ref`_`` (this is very convenient in
long document in which same link appears multiple times) will be converted to
a code block in HTML like ``see <code>ref</code>_``\ , which is not expected.

Features
--------


* Basic markdown and some extensions (see below)

  * inline/block-level raw html
  * fenced-code block
  * tables
  * footnotes (\ ``[^1]``\ )

* Inline- and Block-level rst markups

  * single- and multi-line directives (\ ``.. directive::``\ )
  * inline-roles (\ ``:code:`print(1)` ...``\ )
  * ref-link (\ ``see `ref`_``\ )
  * footnotes (\ ``[#fn]_``\ )
  * math extension inspired by `recommonmark <https://recommonmark.readthedocs.io/en/latest/index.html>`_

* Sphinx extension

  * add markdown support for sphinx
  * ``mdinclude`` directive to include markdown from md or rst files
  * option to parse relative links into ref and doc directives (\ ``m2r_parse_relative_links``\ )

* Pure python implementation

  * pandoc is not required

Installation
------------

Python 2.7 or Python 3.4+ is required.

.. code-block::

   pip install m2r

Or,

.. code-block::

   python3 -m pip install m2r

Usage
-----

Command Line
^^^^^^^^^^^^

``m2r`` command converts markdown file to rst format.

.. code-block::

   m2r your_document.md [your_document2.md ...]

Then you will find ``your_document.rst`` in the same directory.

Programmatic Use
^^^^^^^^^^^^^^^^

Import ``m2r.convert`` function and call it with markdown text.
Then it will return converted text.

.. code-block:: python

   from m2r import convert
   rst = convert('# Title\n\nSentence.')
   print(rst)
   # Title
   # =====
   #
   # Sentence.

Or, use ``parse_from_file`` function to load markdown file and obtain converted
text.

.. code-block:: python

   from m2r import parse_from_file
   output = parse_from_file('markdown_file.md')

This is an example of setup.py to write README in markdown, and publish it to
PyPI as rst format.

.. code-block:: python

   readme_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
   try:
       from m2r import parse_from_file
       readme = parse_from_file(readme_file)
   except ImportError:
       # m2r may not be installed in user environment
       with open(readme_file) as f:
           readme = f.read()
   setup(
       ...,
       long_description=readme,
       ...,
   )

Sphinx Integration
^^^^^^^^^^^^^^^^^^

In your conf.py, add the following lines.

.. code-block:: python

   extensions = [
       ...,
       'm2r',
   ]

   # source_suffix = '.rst'
   source_suffix = ['.rst', '.md']

Write index.md and run ``make html``.

When ``m2r`` extension is enabled on sphinx and ``.md`` file is loaded, m2r
converts to rst and pass to sphinx, not making new ``.rst`` file.

mdinclude directive
~~~~~~~~~~~~~~~~~~~

Like ``.. include:: file`` directive, ``.. mdinclude:: file`` directive inserts
markdown file at the line.

Note: do not use ``.. include:: file`` directive to include markdown file even if
in the markdown file, please use ``.. mdinclude:: file`` instead.

Restrictions
------------


* In the rst's directives, markdown is not available. Please write in rst.
* Column alignment of tables is not supported. (rst does not support this feature)
* Heading with overline-and-underline is not supported.

  * Heading with underline is OK

* Rst heading marks are currently hard-coded and unchangeable.

  * H1: ``=``\ , H2: ``-``\ , H3: ``^``\ , H4: ``~``\ , H5: ``"``\ , H6: ``#``

If you find any bug or unexpected behaviour, please report it to
`Issues <https://github.com/miyakogi/m2r/issues>`_.

Example
-------

See `example document <https://miyakogi.github.io/m2r/example.html>`_ and `its
source code <https://github.com/miyakogi/m2r/blob/master/docs/example.md>`_.

I'm using m2r for writing user guide of `WDOM <https://github.com/miyakogi/wdom>`_.
So you can see it as another example. Its `HTML is
here <http://wdom-py.readthedocs.io/en/latest/guide/index.html>`_\ , and `its
source code is here <https://github.com/miyakogi/wdom/tree/dev/docs/guide>`_.

Demo editor
^^^^^^^^^^^

Demo editor of m2r is available.
If you are interested in m2r, please try it.

`https://github.com/miyakogi/m2rdemo <https://github.com/miyakogi/m2rdemo>`_

Acknowledgement
---------------

m2r is written as an extension of
`mistune <http://mistune.readthedocs.io/en/latest/>`_\ , which is highly extensible
pure-python markdown parser.
Without the mistune, I couldn't write this. Thank you!

Licence
-------

`MIT <https://github.com/miyakogi/m2r/blob/master/LICENSE>`_


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
