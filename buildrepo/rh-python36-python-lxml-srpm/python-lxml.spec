#
# spec file for package rh-python36-python-lxml
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name lxml
%{?scl:%scl_package python-lxml}
%{!?scl:%global pkg_name python-lxml}

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Common SRPM package
Name:           %{?scl_prefix}python-lxml
Version:        4.1.1
Release:        0%{?dist}
Url:            http://lxml.de/
Summary:        Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=lxml; echo ${n:0:1})/lxml/lxml-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Added for C copilation
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
# Cython should really be named python-Cython
BuildRequires:  %{?scl_prefix}Cython >= 0.26.1
%if %{with_dnf}
%endif # with_dnf

%description
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.  It
provides safe and convenient access to these libraries using the ElementTree
API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

To contact the project, go to the `project home page
<http://lxml.de/>`_ or see our bug tracker at
https://launchpad.net/lxml

In case you want to use the current in-development version of lxml,
you can get it from the github repository at
https://github.com/lxml/lxml .  Note that this requires Cython to
build the sources, see the build instructions on the project home
page.  To the same end, running ``easy_install lxml==dev`` will
install lxml from
https://github.com/lxml/lxml/tarball/master#egg=lxml-dev if you have
an appropriate version of Cython installed.


After an official release of a new stable series, bug fixes may become
available at
https://github.com/lxml/lxml/tree/lxml-4.1 .
Running ``easy_install lxml==4.1bugfix`` will install
the unreleased branch state from
https://github.com/lxml/lxml/tarball/lxml-4.1#egg=lxml-4.1bugfix
as soon as a maintenance branch has been established.  Note that this
requires Cython to be installed at an appropriate version for the build.

4.1.1 (2017-11-04)
==================

* Rebuild with Cython 0.27.3 to improve support for Py3.7.

%prep
%setup -q -n lxml-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
export CFLAGS="${CFLAGS} `xslt-config --cflags`"
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
%{python3_sitearch}/*

%changelog
* Fri Jul 5 2019  Nico Kadel-Garcia <nkadel@gmail.com> - 4.1.1-0
- Build .spec with py2pack
- ADd Buildrequires for libxslt-devel and libxml2-devel
- Add "xslt-config --cflags" to CFLAGS
