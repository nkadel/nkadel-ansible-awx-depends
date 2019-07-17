#
# spec file for package rh-python36-python-sphinx_py3doc_enhanced_theme
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Resolve mismatched pypi anme and source tarball
#%global pypi_name sphinx_py3doc_enhanced_theme
%global pypi_name sphinx-py3doc-enhanced-theme

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
Version:        2.4.0
Release:        0%{?dist}
Url:            https://github.com/ionelmc/sphinx-py3doc-enhanced-theme
Summary:        A theme based on the theme of https://docs.python.org/3/ with some responsive enhancements.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Provides:       %{?scl_prefix}python-sphinx_py3doc_enhanced_theme = %{version}-%{release}
Obsoletes:      %{?scl_prefix}python-sphinx_py3doc_enhanced_theme <= %{version}-%{release}
Conflicts:      %{?scl_prefix}python-sphinx_py3doc_enhanced_theme <= %{version}-%{release}

%if %{with_dnf}
%endif # with_dnf

%description
==============================================
Enhanced Sphinx theme (based on Python 3 docs)
==============================================

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
    * - demo
      - `default <http://ionelmc.github.io/sphinx-py3doc-enhanced-theme/default/>`_,
        `bare <http://ionelmc.github.io/sphinx-py3doc-enhanced-theme/bare/>`_
    * - package
      - |version| |downloads|

.. |docs| image:: https://readthedocs.org/projects/sphinx-py3doc-enhanced-theme/badge/?style=flat
    :target: https://readthedocs.org/projects/sphinx-py3doc-enhanced-theme
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/ionelmc/sphinx-py3doc-enhanced-theme/master.svg?style=flat&label=Travis
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/sphinx-py3doc-enhanced-theme

.. |version| image:: http://img.shields.io/pypi/v/sphinx-py3doc-enhanced-theme.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/sphinx-py3doc-enhanced-theme

.. |downloads| image:: http://img.shields.io/pypi/dm/sphinx-py3doc-enhanced-theme.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/sphinx-py3doc-enhanced-theme

A theme based on the theme of https://docs.python.org/3/ with some responsive enhancements.

* Free software: BSD license

Installation
============

::

    pip install sphinx_py3doc_enhanced_theme

Add this in your documentation's ``conf.py``:

.. sourcecode:: python

    import sphinx_py3doc_enhanced_theme
    html_theme = "sphinx_py3doc_enhanced_theme"
    html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]

Customization
=============

No extra styling
----------------

This theme has some extra styling like different fonts, text shadows for headings, slightly different styling for inline code and code blocks.

To get the original styling Python 3 docs have add this in you ``conf.py``:

.. sourcecode:: python

    html_theme_options = {
        'githuburl': 'https://github.com/ionelmc/sphinx-py3doc-enhanced-theme/',
        'bodyfont': '"Lucida Grande",Arial,sans-serif',
        'headfont': '"Lucida Grande",Arial,sans-serif',
        'codefont': 'monospace,sans-serif',
        'linkcolor': '#0072AA',
        'visitedlinkcolor': '#6363bb',
        'extrastyling': False,
    }
    pygments_style = 'friendly'

Custom favicon
--------------

To have a custom favicon create a ``theme`` directory near your ``conf.py`` and add this ``theme.conf`` in it:

.. sourcecode:: ini

    [theme]
    inherit = sphinx_py3doc_enhanced_theme

Then create a ``favicon.png`` in the ``static`` directory.

And then edit your ``conf.py`` to have something like this:

.. sourcecode:: python

    import sphinx_py3doc_enhanced_theme
    html_theme = "theme"
    html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path(), "."]

The final file structure should be like this::

    docs
    &#9500;&#9472;&#9472; conf.py
    &#9492;&#9472;&#9472; theme
        &#9500;&#9472;&#9472; static
        &#9474;&#160;&#160; &#9492;&#9472;&#9472; favicon.png
        &#9492;&#9472;&#9472; theme.conf

A bit of extra css
------------------

.. sourcecode:: python

    html_theme_options = {
        'appendcss': 'div.body code.descclassname { display: none }',
    }

Examples
========

* http://python-aspectlib.readthedocs.org/en/latest/
* http://python-manhole.readthedocs.org/en/latest/

Changelog
=========

2.4.0 (2016-12-17)
------------------

* Added option to use Google Web Fonts. Contributed by Marius P Isken in 
  `#11 <https://github.com/ionelmc/sphinx-py3doc-enhanced-theme/pull/11>`_.

2.3.2 (2015-12-24)
------------------

* Fixed regression in sidebar size when there was no page content. Sidebar has its own height again.

2.3.1 (2015-12-18)
------------------

* Fixed sidebar contents not moving while scrolling at all.

2.3.0 (2015-12-18)
------------------

* Removed use of ``!important`` from various places. Contributed by Matthias Geier in
  `#10 <https://github.com/ionelmc/sphinx-py3doc-enhanced-theme/pull/10>`_.

2.2.4 (2015-10-23)
------------------

* Removed awkward bottom padding of paragraphs in table cells.
* Fix highlight of "p" anchors (that have id and got :target).

2.2.3 (2015-09-13)
------------------

* Fixed display of argument descriptions when there are multiple paragraphs. First paragraph shouldn't be on a second line.

2.2.2 (2015-09-12)
------------------

* Fixed issues with highlighting a section (via anchor location hash). Previously code blocks would get ugly bar on the left.

2.2.1 (2015-08-21)
------------------

* Fixed positioning of navigation sidebar when displayed in narrow mode (at the bottom). Previously it overlapped the
  footer.

2.2.0 (2015-08-19)
------------------

* Added the ``appendcss`` theme options for quick customization.
* Added the ``path`` setuptools entrypoint so ``html_theme_path`` doesn't need to be set anymore in ``conf.py``.

2.1.1 (2015-07-11)
------------------

* Remove background from reference links when ``extrastyling`` is off.

2.1.0 (2015-07-11)
------------------

* Added new theme option ``extrastyling`` which can be used to get the
  original Python 3 docs styling (green code blocks, gray inline code
  blocks, no text shadows etc)
* The ``py.png`` favicon is renamed to ``favicon.png``.
* Added some examples for customizing the styling or using a custom favicon.

2.0.2 (2015-07-08)
------------------

* Make inline code blocks bold.

2.0.1 (2015-03-25)
------------------

* Fix inclusion of default.css (now classic.css).

2.0.0 (2015-03-23)
------------------

* Use HTML5 doctype and force IE into Edge mode.
* Add a embedded flag that removes JS (for building CHM docs).
* Inherit correct theme (default renamed in Sphinx 1.3).

1.2.0 (2015-02-24)
------------------

* Fat-fingered another version. Should had been 1.0.1 ... damn.

1.1.0 (2015-02-24)
------------------

* Match some markup changes in latest Sphinx.

1.0.0 (2015-02-13)
------------------

* Fix depth argument for toctree (contributed by Georg Brandl).

0.1.0 (2014-05-31)
------------------

* First release on PyPI.

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
* Sat Jul 13 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.4.0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Add Provides for sphinx_py3doc_enhanced_theme, pypi module name
