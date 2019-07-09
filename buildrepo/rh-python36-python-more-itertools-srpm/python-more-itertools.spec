#
# spec file for package rh-python36-python-more-itertools
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name more-itertools

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
Version:        4.1.0
Release:        0%{?dist}
Url:            https://github.com/erikrose/more-itertools
Summary:        More routines for operating on iterables, beyond itertools
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires: %{?scl_prefix}python-six < 2.0.0
Requires: %{?scl_prefix}python-six >= 1.0.0
%if %{with_dnf}
%endif # with_dnf
# Manually added for mixed case pypi.org names
Provides:           %{?scl_prefix}python-more_itertools = %{version}-%{release}
Obsoletes:          %{?scl_prefix}python-more_itertools <= %{version}-%{release}
Conflicts:          %{?scl_prefix}python-more_itertools <= %{version}-%{release}

%description
==============
More Itertools
==============


The Python ``itertools`` library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In ``more-itertools``
we collect additional building blocks, recipes, and routines for working with
Python iterables.

Getting started
===============

To get started, install the library with `pip <https://pip.pypa.io/en/stable/>`_:

.. code-block:: shell

    pip install more-itertools

The recipes from the `itertools docs <https://docs.python.org/3/library/itertools.html#itertools-recipes>`_
are included in the top-level package:

.. code-block:: python

    >>> from more_itertools import flatten
    >>> iterable = [(0, 1), (2, 3)]
    >>> list(flatten(iterable))
    [0, 1, 2, 3]

Several new recipes are available as well:

.. code-block:: python

    >>> from more_itertools import chunked
    >>> iterable = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    >>> list(chunked(iterable, 3))
    [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    >>> from more_itertools import spy
    >>> iterable = (x * x for x in range(1, 6))
    >>> head, iterable = spy(iterable, n=3)
    >>> list(head)
    [1, 4, 9]
    >>> list(iterable)
    [1, 4, 9, 16, 25]



For the full listing of functions, see the `API documentation <https://more-itertools.readthedocs.io/en/latest/api.html>`_.

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 4.1.0-0
- Update .spec with py2pack
- Add Requires manually
- Add Provides for python-more_internals
