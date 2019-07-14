#
# spec file for package rh-python36-python-pyrad
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pyrad

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
Version:        2.1
Release:        0%{?dist}
Url:            https://github.com/wichert/pyrad
Summary:        RADIUS tools
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-six
Requires:       %{?scl_prefix}python-netaddr
%if %{with_dnf}
%endif # with_dnf

%description
.. image:: https://travis-ci.org/wichert/pyrad.svg?branch=master
    :target: https://travis-ci.org/wichert/pyrad
.. image:: https://img.shields.io/pypi/v/pyrad.svg
    :target: https://pypi.python.org/pypi/pyrad
.. image:: https://img.shields.io/pypi/dm/pyrad.svg
    :target: https://pypi.python.org/pypi/pyrad

Introduction
============

pyrad is an implementation of a RADIUS client/server as described in RFC2865.
It takes care of all the details like building RADIUS packets, sending
them and decoding responses.

Here is an example of doing a authentication request::

    from __future__ import print_function
    from pyrad.client import Client
    from pyrad.dictionary import Dictionary
    import pyrad.packet

    srv = Client(server="localhost", secret=b"Kah3choteereethiejeimaeziecumi",
                 dict=Dictionary("dictionary"))

    # create request
    req = srv.CreateAuthPacket(code=pyrad.packet.AccessRequest,
                               User_Name="wichert", NAS_Identifier="localhost")
    req["User-Password"] = req.PwCrypt("password")

    # send request
    reply = srv.SendPacket(req)

    if reply.code == pyrad.packet.AccessAccept:
        print("access accepted")
    else:
        print("access denied")

    print("Attributes returned by server:")
    for i in reply.keys():
        print("%s: %s" % (i, reply[i]))



Requirements & Installation
===========================

pyrad requires Python 2.6 or later, or Python 3.2 or later

Installing is simple; pyrad uses the standard distutils system for installing
Python modules::

  python setup.py install


Author, Copyright, Availability
===============================

pyrad was written by Wichert Akkerman <wichert@wiggy.net> and is licensed
under a BSD license.

Copyright and license information can be found in the LICENSE.txt file.

The current version and documentation can be found on pypi:
http://pypi.python.org/pypi/pyrad

Bugs and wishes can be submitted in the pyrad issue tracker on github:
https://github.com/wichert/pyrad/issues




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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.1-0
- Update .spec from py2pack
- Manually add Requires and Suggests
