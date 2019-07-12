#
# spec file for package rh-python36-python-backports.ssl_match_hostname
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name backports.ssl_match_hostname

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
Version:        3.5.0.1
Release:        0%{?dist}
Url:            http://bitbucket.org/brandon/backports.ssl_match_hostname
Summary:        The ssl.match_hostname() function from Python 3.5
License:        Python-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
The ssl.match_hostname() function from Python 3.5
=================================================

The Secure Sockets Layer is only actually *secure*
if you check the hostname in the certificate returned
by the server to which you are connecting,
and verify that it matches to hostname
that you are trying to reach.

But the matching logic, defined in `RFC2818`_,
can be a bit tricky to implement on your own.
So the ``ssl`` package in the Standard Library of Python 3.2
and greater now includes a ``match_hostname()`` function
for performing this check instead of requiring every application
to implement the check separately.

This backport brings ``match_hostname()`` to users
of earlier versions of Python.
Simply make this distribution a dependency of your package,
and then use it like this::

    from backports.ssl_match_hostname import match_hostname, CertificateError
    [...]
    sslsock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_SSLv23,
                              cert_reqs=ssl.CERT_REQUIRED, ca_certs=...)
    try:
        match_hostname(sslsock.getpeercert(), hostname)
    except CertificateError, ce:
        ...

Brandon Craig Rhodes is merely the packager of this distribution;
the actual code inside comes from Python 3.5 with small changes for
portability.


Requirements
------------

* If you want to verify hosts match with certificates via ServerAltname
  IPAddress fields, you need to install the `ipaddress module`_.
  backports.ssl_match_hostname will continue to work without ipaddress but
  will only be able to handle ServerAltName DNSName fields, not IPAddress.
  System packagers (Linux distributions, et al) are encouraged to add
  this as a hard dependency in their packages.

* If you need to use this on Python versions earlier than 2.6 you will need to
  install the `ssl module`_.  From Python 2.6 upwards ``ssl`` is included in
  the Python Standard Library so you do not need to install it separately.

.. _`ipaddress module`:: https://pypi.python.org/pypi/ipaddress
.. _`ssl module`:: https://pypi.python.org/pypi/ssl

History
-------

* This function was introduced in python-3.2
* It was updated for python-3.4a1 for a CVE 
  (backports-ssl_match_hostname-3.4.0.1)
* It was updated from RFC2818 to RFC 6125 compliance in order to fix another
  security flaw for python-3.3.3 and python-3.4a5
  (backports-ssl_match_hostname-3.4.0.2)
* It was updated in python-3.5 to handle IPAddresses in ServerAltName fields
  (something that backports.ssl_match_hostname will do if you also install the
  ipaddress library from pypi).


.. _RFC2818: http://tools.ietf.org/html/rfc2818.html

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