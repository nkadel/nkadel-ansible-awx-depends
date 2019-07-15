#
# spec file for package rh-python36-python-coverage
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name coverage

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
Version:        4.5.3
Release:        0%{?dist}
Url:            https://github.com/nedbat/coveragepy
Summary:        Code coverage measurement for Python
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
.. Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
.. For details: https://bitbucket.org/ned/coveragepy/src/default/NOTICE.txt

===========
Coverage.py
===========

Code coverage testing for Python.

|  |license| |versions| |status| |docs|
|  |ci-status| |win-ci-status| |codecov|
|  |kit| |format| |repos|
|  |tidelift| |saythanks|

.. downloads badge seems to be broken... |downloads|

Coverage.py measures code coverage, typically during test execution. It uses
the code analysis tools and tracing hooks provided in the Python standard
library to determine which lines are executable, and which have been executed.

.. |tideliftlogo| image:: https://nedbatchelder.com/pix/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png
   :width: 75
   :alt: Tidelift

.. list-table::
   :widths: 10 100

   * - |tideliftlogo|
     - Professional support for coverage.py is available as part of the `Tidelift
       Subscription`_.  Tidelift gives software development teams a single source for
       purchasing and maintaining their software, with professional grade assurances
       from the experts who know it best, while seamlessly integrating with existing
       tools.

.. _Tidelift Subscription: https://tidelift.com/subscription/pkg/pypi-coverage?utm_source=pypi-coverage&utm_medium=referral&utm_campaign=readme

Coverage.py runs on many versions of Python:

* CPython 2.6, 2.7 and 3.3 through alpha 3.8.
* PyPy2 6.0 and PyPy3 6.0.
* Jython 2.7.1, though not for reporting.
* IronPython 2.7.7, though not for reporting.

Documentation is on `Read the Docs`_.  Code repository and issue tracker are on
`GitHub`_.

.. _Read the Docs: https://coverage.readthedocs.io/
.. _GitHub: https://github.com/nedbat/coveragepy


**New in 4.5:** Configurator plug-ins.

New in 4.4: Suppressable warnings, continuous coverage measurement.

New in 4.3: HTML ``--skip-covered``, sys.excepthook support, tox.ini
support.

New in 4.2: better support for multiprocessing and combining data.

New in 4.1: much-improved branch coverage.

New in 4.0: ``--concurrency``, plugins for non-Python files, setup.cfg
support, --skip-covered, HTML filtering, and more than 50 issues closed.


Getting Started
---------------

See the `Quick Start section`_ of the docs.

.. _Quick Start section: https://coverage.readthedocs.io/#quick-start


Contributing
------------

See the `Contributing section`_ of the docs.

.. _Contributing section: https://coverage.readthedocs.io/en/latest/contributing.html


License
-------

Licensed under the `Apache 2.0 License`_.  For details, see `NOTICE.txt`_.

.. _Apache 2.0 License: http://www.apache.org/licenses/LICENSE-2.0
.. _NOTICE.txt: https://bitbucket.org/ned/coveragepy/src/default/NOTICE.txt


.. |ci-status| image:: https://travis-ci.org/nedbat/coveragepy.svg?branch=master
    :target: https://travis-ci.org/nedbat/coveragepy
    :alt: Build status
.. |win-ci-status| image:: https://ci.appveyor.com/api/projects/status/kmeqpdje7h9r6vsf/branch/master?svg=true
    :target: https://ci.appveyor.com/project/nedbat/coveragepy
    :alt: Windows build status
.. |docs| image:: https://readthedocs.org/projects/coverage/badge/?version=latest&style=flat
    :target: https://coverage.readthedocs.io/
    :alt: Documentation
.. |reqs| image:: https://requires.io/github/nedbat/coveragepy/requirements.svg?branch=master
    :target: https://requires.io/github/nedbat/coveragepy/requirements/?branch=master
    :alt: Requirements status
.. |kit| image:: https://badge.fury.io/py/coverage.svg
    :target: https://pypi.python.org/pypi/coverage
    :alt: PyPI status
.. |format| image:: https://img.shields.io/pypi/format/coverage.svg
    :target: https://pypi.python.org/pypi/coverage
    :alt: Kit format
.. |downloads| image:: https://img.shields.io/pypi/dw/coverage.svg
    :target: https://pypi.python.org/pypi/coverage
    :alt: Weekly PyPI downloads
.. |versions| image:: https://img.shields.io/pypi/pyversions/coverage.svg
    :target: https://pypi.python.org/pypi/coverage
    :alt: Python versions supported
.. |status| image:: https://img.shields.io/pypi/status/coverage.svg
    :target: https://pypi.python.org/pypi/coverage
    :alt: Package stability
.. |license| image:: https://img.shields.io/pypi/l/coverage.svg
    :target: https://pypi.python.org/pypi/coverage
    :alt: License
.. |codecov| image:: http://codecov.io/github/nedbat/coveragepy/coverage.svg?branch=master&precision=2
    :target: http://codecov.io/github/nedbat/coveragepy?branch=master
    :alt: Coverage!
.. |repos| image:: https://repology.org/badge/tiny-repos/python:coverage.svg
    :target: https://repology.org/metapackage/python:coverage/versions
    :alt: Packaging status
.. |saythanks| image:: https://img.shields.io/badge/saythanks.io-%E2%98%BC-1EAEDB.svg
    :target: https://saythanks.io/to/nedbat
    :alt: Say thanks :)
.. |tidelift| image:: https://tidelift.com/badges/github/nedbat/coveragepy
    :target: https://tidelift.com/subscription/pkg/pypi-coverage?utm_source=pypi-coverage&utm_medium=referral&utm_campaign=readme
    :alt: Tidelift




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
%{python3_sitearch}/*
%{_bindir}/*

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.10-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually add _bindir
