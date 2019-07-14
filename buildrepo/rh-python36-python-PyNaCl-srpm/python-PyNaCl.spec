#
# spec file for package rh-python36-python-PyNaCl
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name PyNaCl

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
Version:        1.2.1
Release:        0%{?dist}
Url:            https://github.com/pyca/pynacl/
Summary:        Python binding to the Networking and Cryptography (NaCl) library
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-cffi >= 1.4.1
BuildRequires:  %{?scl_prefix}python-six
%if %{with_dnf}
#[docs]
Suggests:       %{?scl_prefix}python-sphinx >= 1.6.5
Suggests:       %{?scl_prefix}python-sphinx_rtd_theme
#[tests]
Suggests:       %{?scl_prefix}python-pytest >= 3.2.1
Conflicts:      %{?scl_prefix}python-pytest = 3.3.0
Suggests:       %{?scl_prefix}python-hypothesis >= 3.27.0
%endif # with_dnf

%description
===============================================
PyNaCl: Python binding to the libsodium library
===============================================

.. image:: https://img.shields.io/pypi/v/pynacl.svg
    :target: https://pypi.python.org/pypi/PyNaCl/
    :alt: Latest Version

.. image:: https://travis-ci.org/pyca/pynacl.svg?branch=master
    :target: https://travis-ci.org/pyca/pynacl

.. image:: https://codecov.io/github/pyca/pynacl/coverage.svg?branch=master
    :target: https://codecov.io/github/pyca/pynacl?branch=master

PyNaCl is a Python binding to `libsodium`_, which is a fork of the
`Networking and Cryptography library`_. These libraries have a stated goal of
improving usability, security and speed. It supports Python 2.7 and 3.4+ as
well as PyPy 2.6+.

.. _libsodium: https://github.com/jedisct1/libsodium
.. _Networking and Cryptography library: https://nacl.cr.yp.to/

Features
--------

* Digital signatures
* Secret-key encryption
* Public-key encryption
* Hashing and message authentication
* Password based key derivation and password hashing

Installation
============

Binary wheel install
--------------------

PyNaCl ships as a binary wheel on OS X, Windows and Linux ``manylinux1`` [#many]_ ,
so all dependencies are included. Make sure you have an up-to-date pip
and run:

.. code-block:: console

    $ pip install pynacl

Linux source build
------------------

PyNaCl relies on `libsodium`_, a portable C library. A copy is bundled
with PyNaCl so to install you can run:

.. code-block:: console

    $ pip install pynacl

If you'd prefer to use the version of ``libsodium`` provided by your
distribution, you can disable the bundled copy during install by running:

.. code-block:: console

    $ SODIUM_INSTALL=system pip install pynacl

.. warning:: Usage of the legacy ``easy_install`` command provided by setuptools
   is generally discouraged, and is completely unsupported in PyNaCl's case.

.. _libsodium: https://github.com/jedisct1/libsodium

.. [#many] `manylinux1 wheels <https://www.python.org/dev/peps/pep-0513/>`_
    are built on a baseline linux environment based on Centos 5.11
    and should work on most x86 and x86_64 glibc based linux environments.

Changelog
=========

1.2.1 - 2017-12-04
------------------

* Update hypothesis minumum allowed version.
* Infrastructure: add proper configuration for readthedocs builder
  runtime environment.

1.2.0 - 2017-11-01
------------------

* Update ``libsodium`` to 1.0.15.
* Infrastructure: add jenkins support for automatic build of
  ``manylinux1`` binary wheels
* Added support for ``SealedBox`` construction.
* Added support for ``argon2i`` and ``argon2id`` password hashing constructs
  and restructured high-level password hashing implementation to expose
  the same interface for all hashers.
* Added support for 128 bit ``siphashx24`` variant of ``siphash24``.
* Added support for ``from_seed`` APIs for X25519 keypair generation.
* Dropped support for Python 3.3.

1.1.2 - 2017-03-31
------------------

* reorder link time library search path when using bundled
  libsodium

1.1.1 - 2017-03-15
------------------

* Fixed a circular import bug in ``nacl.utils``.

1.1.0 - 2017-03-14
------------------

* Dropped support for Python 2.6.
* Added ``shared_key()`` method on ``Box``.
* You can now pass ``None`` to ``nonce`` when encrypting with ``Box`` or
  ``SecretBox`` and it will automatically generate a random nonce.
* Added support for ``siphash24``.
* Added support for ``blake2b``.
* Added support for ``scrypt``.
* Update ``libsodium`` to 1.0.11.
* Default to the bundled ``libsodium`` when compiling.
* All raised exceptions are defined mixing-in
  ``nacl.exceptions.CryptoError``

1.0.1 - 2016-01-24
------------------

* Fix an issue with absolute paths that prevented the creation of wheels.

1.0 - 2016-01-23
----------------

* PyNaCl has been ported to use the new APIs available in cffi 1.0+.
  Due to this change we no longer support PyPy releases older than 2.6.
* Python 3.2 support has been dropped.
* Functions to convert between Ed25519 and Curve25519 keys have been added.

0.3.0 - 2015-03-04
------------------

* The low-level API (`nacl.c.*`) has been changed to match the
  upstream NaCl C/C++ conventions (as well as those of other NaCl bindings).
  The order of arguments and return values has changed significantly. To
  avoid silent failures, `nacl.c` has been removed, and replaced with
  `nacl.bindings` (with the new argument ordering). If you have code which
  calls these functions (e.g. `nacl.c.crypto_box_keypair()`), you must review
  the new docstrings and update your code/imports to match the new
  conventions.

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
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.2.1-0
- Update .spec from py2pack
- Manually add Requires and Suggests
