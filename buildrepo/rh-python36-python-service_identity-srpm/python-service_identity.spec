#
# spec file for package rh-python36-python-service_identity
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name service_identity

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
Version:        17.0.0
Release:        0%{?dist}
Url:            https://service-identity.readthedocs.io/
Summary:        Service identity verification for pyOpenSSL.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-attrs
Requires:       %{?scl_prefix}python-pyasn1
Requires:       %{?scl_prefix}python-pyasn1-modules
Requires:       %{?scl_prefix}python-pyopenssl >= 0.12
%if %{with_dnf}
#[idna]
Suggests:       %{?scl_prefix}python-idna
# Manually added for docs
Suggests:       %{?scl_prefix}python-sphinx
%endif # with_dnf

%description
=============================
Service Identity Verification
=============================

.. image:: https://readthedocs.org/projects/service-identity/badge/?version=stable
   :target: https://service-identity.readthedocs.io/en/stable/?badge=stable
   :alt: Documentation Status

.. image:: https://travis-ci.org/pyca/service_identity.svg?branch=master
   :target: https://travis-ci.org/pyca/service_identity
   :alt: CI status

.. image:: https://codecov.io/github/pyca/service_identity/branch/master/graph/badge.svg
   :target: https://codecov.io/github/pyca/service_identity
   :alt: Test Coverage

.. image:: https://www.irccloud.com/invite-svg?channel=%23cryptography-dev&amp;hostname=irc.freenode.net&amp;port=6697&amp;ssl=1
    :target: https://www.irccloud.com/invite?channel=%23cryptography-dev&amp;hostname=irc.freenode.net&amp;port=6697&amp;ssl=1

.. begin

Use this package if:

- you use pyOpenSSL_ and don&#8217;t want to be MITM_\ ed or
- if you want to verify that a `PyCA cryptography`_ certificate is valid for a certain hostname.

``service_identity`` aspires to give you all the tools you need for verifying whether a certificate is valid for the intended purposes.

In the simplest case, this means *host name verification*.
However, ``service_identity`` implements `RFC 6125`_ fully and plans to add other relevant RFCs too.

``service_identity``\ &#8217;s documentation lives at `Read the Docs <https://service-identity.readthedocs.io/>`_, the code on `GitHub <https://github.com/pyca/service_identity>`_.


.. _Twisted: https://twistedmatrix.com/
.. _pyOpenSSL: https://pypi.python.org/pypi/pyOpenSSL/
.. _MITM: https://en.wikipedia.org/wiki/Man-in-the-middle_attack
.. _RFC 6125: http://www.rfc-editor.org/info/rfc6125
.. _PyCA cryptography: https://cryptography.io/


Release Information
===================

17.0.0 (2017-05-23)
-------------------

Deprecations:
^^^^^^^^^^^^^

- Since Chrome 58 and Firefox 48 both don't accept certificates that contain only a Common Name, its usage is hereby deprecated in ``service_identity`` too.
  We have been raising a warning since 16.0.0 and the support will be removed in mid-2018 for good.


Changes:
^^^^^^^^

- When ``service_identity.SubjectAltNameWarning`` is raised, the Common Name of the certificate is now included in the warning message.
  `#17 <https://github.com/pyca/service_identity/pull/17>`_
- Added ``cryptography.x509`` backend for verifying certificates.
  `#18 <https://github.com/pyca/service_identity/pull/18>`_
- Wildcards (``*``) are now only allowed if they are the leftmost label in a certificate.
  This is common practice by all major browsers.
  `#19 <https://github.com/pyca/service_identity/pull/19>`_

`Full changelog <https://service-identity.readthedocs.io/en/stable/changelog.html>`_.

Authors
=======

``service_identity`` is written and maintained by `Hynek Schlawack <https://hynek.me/>`_.

The development is kindly supported by `Variomedia AG <https://www.variomedia.de/>`_.

Other contributors can be found in `GitHub's overview <https://github.com/pyca/service_identity/graphs/contributors>`_.




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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.10-0
- Update .spec from py2pack
- Manually add Requires and Suggests
