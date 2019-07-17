#
# spec file for package rh-python36-python-pkgconfig
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pkgconfig
%{?scl:%scl_package python-pkgconfig}
%{!?scl:%global pkg_name python-pkgconfig}

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Common SRPM package
Name:           %{?scl_prefix}python-pkgconfig
Version:        1.4.0
Release:        0%{?dist}
Url:            http://github.com/matze/pkgconfig
Summary:        Interface Python with pkg-config
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=pkgconfig; echo ${n:0:1})/pkgconfig/pkgconfig-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
pkgconfig
=========

.. image:: https://travis-ci.org/matze/pkgconfig.png?branch=master
    :target: https://travis-ci.org/matze/pkgconfig

``pkgconfig`` is a Python module to interface with the ``pkg-config``
command line tool and supports Python 2.6+.

It can be used to

-  find all pkg-config packages ::

       >>> packages = pkgconfig.list_all()

-  check if a package exists ::

       >>> pkgconfig.exists('glib-2.0')
       True

-  check if a package meets certain version requirements ::

       >>> pkgconfig.installed('glib-2.0', '< 2.26')
       False

-  query CFLAGS and LDFLAGS ::

       >>> pkgconfig.cflags('glib-2.0')
       '-I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include'

       >>> pkgconfig.libs('glib-2.0')
       '-lglib-2.0'

-  get all variables defined for a package::

        >>> pkgconfig.variables('glib-2.0')
        {u'exec_prefix': u'/usr'}

-  parse the output to build extensions with setup.py ::

       >>> d = pkgconfig.parse('glib-2.0 gtk+-2.0')
       >>> d['libraries']
       [u'gtk+-2.0', u'glib-2.0']

   The ``pkgconfig.parse`` function return a dictonary of list.
   The lists returned are an accurate representations of the equivalent
   ``pkg-config`` call, both in content and order.

If ``pkg-config`` is not on the path, raises ``EnvironmentError``.

The ``pkgconfig`` module is licensed under the MIT license.


Changelog
---------

Version 1.4.0
~~~~~~~~~~~~~

- Add boolean ``static`` keyword to output private libraries as well
- Raise original ``OSError`` as well

Version 1.3.1
~~~~~~~~~~~~~

- Fix compatibility problems with Python 2.6

Version 1.3.0
~~~~~~~~~~~~~

- Add variables() API to query defined variables
- Disable Python 3.2 and enable Python 3.5 and 3.6 tests
- Fix #16: handle spaces of values in .pc files correctly

Version 1.2.1 and 1.2.2
~~~~~~~~~~~~~~~~~~~~~~~

Bug fix releases released on December 1st and 2nd 2016.

- Include the ``data`` folder in the distribution in order to run tests
- Improve the tests


Version 1.2.0
~~~~~~~~~~~~~

Released on November 30th 2016.

- Potential break: switch from result set to list
- Expose --list-all query
- Added support for PKG_CONFIG environment variable


Version 1.1.0
~~~~~~~~~~~~~

Released on November 6th 2013.

- Multiple packages can now be parsed with a single call to ``.parse``.


Version 1.0.0
~~~~~~~~~~~~~

First release on September 8th 2013.




%prep
%setup -q -n pkgconfig-%{version}

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
