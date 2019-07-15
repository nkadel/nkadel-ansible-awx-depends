#
# spec file for package rh-python36-python-pyflakes
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pyflakes

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
Version:        2.1.1
Release:        0%{?dist}
Url:            https://github.com/PyCQA/pyflakes
Summary:        passive checker of Python programs
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
========
Pyflakes
========

A simple program which checks Python source files for errors.

Pyflakes analyzes programs and detects various errors.  It works by
parsing the source file, not importing it, so it is safe to use on
modules with side effects.  It's also much faster.

It is `available on PyPI <https://pypi.org/project/pyflakes/>`_
and it supports all active versions of Python: 2.7 and 3.4 to 3.7.



Installation
------------

It can be installed with::

  $ pip install --upgrade pyflakes


Useful tips:

* Be sure to install it for a version of Python which is compatible
  with your codebase: for Python 2, ``pip2 install pyflakes`` and for
  Python3, ``pip3 install pyflakes``.

* You can also invoke Pyflakes with ``python3 -m pyflakes .`` or
  ``python2 -m pyflakes .`` if you have it installed for both versions.

* If you require more options and more flexibility, you could give a
  look to Flake8_ too.


Design Principles
-----------------
Pyflakes makes a simple promise: it will never complain about style,
and it will try very, very hard to never emit false positives.

Pyflakes is also faster than Pylint_
or Pychecker_. This is
largely because Pyflakes only examines the syntax tree of each file
individually. As a consequence, Pyflakes is more limited in the
types of things it can check.

If you like Pyflakes but also want stylistic checks, you want
flake8_, which combines
Pyflakes with style checks against
`PEP 8`_ and adds
per-project configuration ability.


Mailing-list
------------

Share your feedback and ideas: `subscribe to the mailing-list
<https://mail.python.org/mailman/listinfo/code-quality>`_

Contributing
------------

Issues are tracked on `GitHub <https://github.com/PyCQA/pyflakes/issues>`_.

Patches may be submitted via a `GitHub pull request`_ or via the mailing list
if you prefer. If you are comfortable doing so, please `rebase your changes`_
so they may be applied to master with a fast-forward merge, and each commit is
a coherent unit of work with a well-written log message.  If you are not
comfortable with this rebase workflow, the project maintainers will be happy to
rebase your commits for you.

All changes should include tests and pass flake8_.

.. image:: https://api.travis-ci.org/PyCQA/pyflakes.svg?branch=master
   :target: https://travis-ci.org/PyCQA/pyflakes
   :alt: Build status

.. _Pylint: http://www.pylint.org/
.. _flake8: https://pypi.org/project/flake8/
.. _`PEP 8`: http://legacy.python.org/dev/peps/pep-0008/
.. _Pychecker: http://pychecker.sourceforge.net/
.. _`rebase your changes`: https://git-scm.com/book/en/v2/Git-Branching-Rebasing
.. _`GitHub pull request`: https://github.com/PyCQA/pyflakes/pulls

Changelog
---------

Please see `NEWS.rst <NEWS.rst>`_.




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