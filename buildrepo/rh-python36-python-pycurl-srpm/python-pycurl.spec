#
# spec file for package rh-python36-python-pycurl
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pycurl

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
Version:        7.43.0.1
Release:        0%{?dist}
Url:            http://pycurl.io/
Summary:        PycURL -- A Python Interface To The cURL library
License:        LGPL/MIT (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added for curl-config
BuildRequires:  libcurl-devel
# Manually added
Requires:       %{?scl_prefix}python-bottle
# nose 1.3.1 is broken on python 3:
# https://github.com/nose-devs/nose/issues/780
Requires:       %{?scl_prefix}python-nose>=1.3.2
# flaky 2.2.0 is not installable on python 3.1.5,
# install it manually
Requires:       %{?scl_prefix}python-pyflakes
Requires:       %{?scl_prefix}python-nose-show-skipped

%if %{with_dnf}
bottle
# nose 1.3.1 is broken on python 3:
# https://github.com/nose-devs/nose/issues/780
nose>=1.3.2
flaky
pyflakes
nose-show-skipped
# for python 2.6
#unittest2
#sphinx
%endif # with_dnf

%description
PycURL -- A Python Interface To The cURL library
================================================

PycURL is a Python interface to `libcurl`_, the multiprotocol file
transfer library. Similarly to the urllib_ Python module,
PycURL can be used to fetch objects identified by a URL from a Python program.
Beyond simple fetches however PycURL exposes most of the functionality of
libcurl, including:

- Speed - libcurl is very fast and PycURL, being a thin wrapper above
  libcurl, is very fast as well. PycURL `was benchmarked`_ to be several
  times faster than requests_.
- Features including multiple protocol support, SSL, authentication and
  proxy options. PycURL supports most of libcurl's callbacks.
- Multi_ and share_ interfaces.
- Sockets used for network operations, permitting integration of PycURL
  into the application's I/O loop (e.g., using Tornado_).

.. _was benchmarked: http://stackoverflow.com/questions/15461995/python-requests-vs-pycurl-performance
.. _requests: http://python-requests.org/
.. _Multi: https://curl.haxx.se/libcurl/c/libcurl-multi.html
.. _share: https://curl.haxx.se/libcurl/c/libcurl-share.html
.. _Tornado: http://www.tornadoweb.org/


Requirements
------------

- Python 2.6, 2.7 or 3.1 through 3.6.
- libcurl 7.19.0 or better.


Installation
------------

Download source and binary distributions from `PyPI`_ or `Bintray`_.
Binary wheels are now available for 32 and 64 bit Windows versions.

Please see `the installation documentation`_ for installation instructions.

.. _PyPI: https://pypi.python.org/pypi/pycurl
.. _Bintray: https://dl.bintray.com/pycurl/pycurl/
.. _the installation documentation: http://pycurl.io/docs/latest/install.html


Documentation
-------------

Documentation for the most recent PycURL release is available on
`PycURL website <http://pycurl.io/docs/latest/>`_.


Support
-------

For support questions please use `curl-and-python mailing list`_.
`Mailing list archives`_ are available for your perusal as well.

Although not an official support venue, `Stack Overflow`_ has been
popular with some PycURL users.

Bugs can be reported `via GitHub`_. Please use GitHub only for bug
reports and direct questions to our mailing list instead.

.. _curl-and-python mailing list: http://cool.haxx.se/mailman/listinfo/curl-and-python
.. _Stack Overflow: http://stackoverflow.com/questions/tagged/pycurl
.. _Mailing list archives: https://curl.haxx.se/mail/list.cgi?list=curl-and-python
.. _via GitHub: https://github.com/pycurl/pycurl/issues


License
-------

PycURL is dual licensed under the LGPL and an MIT/X derivative license
based on the libcurl license. The complete text of the licenses is available
in COPYING-LGPL_ and COPYING-MIT_ files in the source distribution.

.. _libcurl: https://curl.haxx.se/libcurl/
.. _urllib: http://docs.python.org/library/urllib.html
.. _COPYING-LGPL: https://raw.githubusercontent.com/pycurl/pycurl/master/COPYING-LGPL
.. _COPYING-MIT: https://raw.githubusercontent.com/pycurl/pycurl/master/COPYING-MIT

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

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 7.43.0.1=0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Add BuldRequires for libcurl-devel

