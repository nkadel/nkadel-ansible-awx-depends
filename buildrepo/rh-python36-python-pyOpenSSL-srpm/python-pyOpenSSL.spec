#
# spec file for package rh-python36-python-pyOpenSSL
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pyOpenSSL

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
Version:        19.0.0
Release:        0%{?dist}
Url:            https://pyopenssl.org/
Summary:        Python wrapper module around the OpenSSL library
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-cryptography >= 2.3
Requires:       %{?scl_prefix}python-six >= 1.5.2

%if %{with_dnf}
#[docs]
Suggests:       %{?scl_prefix}python-sphinx
Suggests:       %{?scl_prefix}python-sphinx_rtd_theme
#[test]
Suggests:       %{?scl_prefix}python-flaky
Suggests:       %{?scl_prefix}python-pretend
Suggests:       %{?scl_prefix}python-pytest >= 3.0.1
%endif # with_dnf

%description
========================================================
pyOpenSSL -- A Python wrapper around the OpenSSL library
========================================================

.. image:: https://readthedocs.org/projects/pyopenssl/badge/?version=stable
   :target: https://pyopenssl.org/en/stable/
   :alt: Stable Docs

.. image:: https://travis-ci.org/pyca/pyopenssl.svg?branch=master
   :target: https://travis-ci.org/pyca/pyopenssl
   :alt: Build status

.. image:: https://codecov.io/github/pyca/pyopenssl/branch/master/graph/badge.svg
   :target: https://codecov.io/github/pyca/pyopenssl
   :alt: Test coverage

**Note:** The Python Cryptographic Authority **strongly suggests** the use of `pyca/cryptography`_
where possible. If you are using pyOpenSSL for anything other than making a TLS connection 
**you should move to cryptography and drop your pyOpenSSL dependency**.

High-level wrapper around a subset of the OpenSSL library. Includes

* ``SSL.Connection`` objects, wrapping the methods of Python's portable sockets
* Callbacks written in Python
* Extensive error-handling mechanism, mirroring OpenSSL's error codes

... and much more.

You can find more information in the documentation_.
Development takes place on GitHub_.


Discussion
==========

If you run into bugs, you can file them in our `issue tracker`_.

We maintain a cryptography-dev_ mailing list for both user and development discussions.

You can also join ``#cryptography-dev`` on Freenode to ask questions or get involved.


.. _documentation: https://pyopenssl.org/
.. _`issue tracker`: https://github.com/pyca/pyopenssl/issues
.. _cryptography-dev: https://mail.python.org/mailman/listinfo/cryptography-dev
.. _GitHub: https://github.com/pyca/pyopenssl
.. _`pyca/cryptography`: https://github.com/pyca/cryptography


Release Information
===================

19.0.0 (2019-01-21)
-------------------


Backward-incompatible changes:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``X509Store.add_cert`` no longer raises an error if you add a duplicate cert.
  `#787 <https://github.com/pyca/pyopenssl/pull/787>`_


Deprecations:
^^^^^^^^^^^^^

*none*


Changes:
^^^^^^^^

- pyOpenSSL now works with OpenSSL 1.1.1.
  `#805 <https://github.com/pyca/pyopenssl/pull/805>`_
- pyOpenSSL now handles NUL bytes in ``X509Name.get_components()``
  `#804 <https://github.com/pyca/pyopenssl/pull/804>`_


`Full changelog <https://pyopenssl.org/en/stable/changelog.html>`_.





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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 19.0.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
