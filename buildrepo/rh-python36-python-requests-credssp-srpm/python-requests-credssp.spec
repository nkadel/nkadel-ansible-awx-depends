#
# spec file for package rh-python36-python-requests-credssp
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name requests-credssp

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
Version:        0.1.0
Release:        0%{?dist}
Url:            https://github.com/jborean93/requests-credssp
Summary:        HTTPS CredSSP authentication with the requests library.
License:        ISC
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
# Manually added
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires:       %{?scl_prefix}python-ntlm-auth
Requires:       %{?scl_prefix}python-pyOpenSSL >= 16.0.0
Requires:       %{?scl_prefix}python-requests >= 2.0.0
#[:python_version < "2.7"]
#Requires:       %{?scl_prefix}python-ordereddict
%if %{with_dnf}
%endif # with_dnf

%description
requests-credssp
================

|Build Status| |Appveyor Build status| |Coverage Status|

About this library
------------------

This package allows for HTTPS CredSSP authentication using the requests
library. CredSSP is a Microsoft authentication that allows your
credentials to be delegated to a server giving you double hop
authentication.

Features
--------

Currently only CredSSP is supported through NTLM with later plans on
adding support for Kerberos. CredSSP allows you to connect and delegate
your credentials to a computer that has CredSSP enabled.

Installation
------------

requests-credssp supports Python 2.6, 2.7 and 3.3+

Before installing the following packages need to be installed on the
system

.. code:: bash

    # for Debian/Ubuntu/etc:
    sudo apt-get install gcc python-dev libssl-dev

    # for RHEL/CentOS/etc:
    sudo yum install gcc python-devel openssl-devel

To install, use pip:

.. code:: bash

    pip install requests-credssp

To install from source, download the source code, then run:

.. code:: bash

    python setup.py install

Requirements
------------

-  ntlm-auth
-  ordereddict (Python 2.6 Only)
-  pyOpenSSL>=16.0.0
-  requests>=2.0.0

Usage
-----

With NTLM Auth
^^^^^^^^^^^^^^

Currently this is the only way to use CredSSP, there are plans in the
future to add Kerberos auth support as well.

.. code:: python

    import requests
    from requests_credssp import HttpCredSSPAuth

    credssp_auth = HttpCredSSPAuth('domain\\user', 'password', auth_mechanism='ntlm')
    r = requests.get("https://server:5986/wsman", auth=credssp_auth)
    ...

Disable TLSv1.2
^^^^^^^^^^^^^^^

There is an option to disable TLSv1.2 connections and revert back to
TLSv1. Windows 7 and Server 2008 did not support TLSv1.2 by default and
require a patch be installed and registry keys modified to allow TLSv1.2
support.

.. code:: python

    import requests
    from requests_credssp import HttpCredSSPAuth

    credssp_auth = HttpCredSSPAuth('domain\\user', 'password', auth_mechanism='ntlm', disable_tlsv1_2=True)
    r = requests.get("https://server:5986/wsman", auth=credssp_auth)
    ...

Message Encryption
^^^^^^^^^^^^^^^^^^

You can use this library to encrypt and decrypt messages sent to and
from the server. Message encryption is done over the TLS channel that
was negotiated in the authentication stage. The below is an example of
encrypting and decrypting messages, note this is only a basic example
and not a working script.

.. code:: python

    import requests
    from requests_credssp import HttpCredSSPAuth

    # build the auth request and sent an empty message to authenticate
    session = requests.Session()
    session.auth = HttpCredSSPAuth('domain\\user', 'password')

    request = requests.Request('POST', 'https://server:5986/wsman', data=None)
    prepared_request = self.session.prepare_request(request)
    response = session.send(prepared_request)

    # encrypt the message using the wrap command
    message = b'hi server'
    encrypted_message = session.auth.wrap(message)

    # send the encrypted message and get the encrypted response
    request = requests.Request('POST', 'https://server:5986/wsman', data=encrypted_message)
    prepared_request = self.session.prepare_request(request)
    response = session.send(prepared_request)

    # decrypt the encrypted response from the server
    encrypted_response = response.content
    decrypted_response = session.auth.unwrap(encrypted_response)

Logging
-------

This library uses the standard Python logging facilities. Log messages
are logged to the ``requests_credssp`` and ``requests_credssp.credssp``
named loggers.

If you are receiving any errors or wish to debug the CredSSP process you
should enable DEBUG level logs. These logs show fine grain information
such as the protocol and cipher negotiated in the TLS handshake as well
as any non confidential data such as the 1st 2 NTLM messages sent and
received in the auth process.

Backlog
-------

-  Add support for Kerberos authentication
-  Once above is added, auto detect which version to use, preference
   Kerberos over NTLM
-  Replace dependency of pyOpenSSL if possible with inbuilt functions in
   Python
-  Add support for different credential types like smart card and
   redirected credentials

.. |Build Status| image:: https://travis-ci.org/jborean93/requests-credssp.svg?branch=master
   :target: https://travis-ci.org/jborean93/requests-credssp
.. |Appveyor Build status| image:: https://ci.appveyor.com/api/projects/status/6osajucq8sf8aeed/branch/master?svg=true
   :target: https://ci.appveyor.com/project/jborean93/requests-credssp/branch/master
.. |Coverage Status| image:: https://coveralls.io/repos/github/jborean93/requests-credssp/badge.svg?branch=master
   :target: https://coveralls.io/github/jborean93/requests-credssp?branch=master




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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.1.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
