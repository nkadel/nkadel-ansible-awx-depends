#
# spec file for package rh-python36-python-dogpile.cache
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name dogpile.cache

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
Version:        0.6.5
Release:        0%{?dist}
Url:            http://bitbucket.org/zzzeek/dogpile.cache
Summary:        A caching front-end based on the Dogpile lock.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
dogpile
=======

Dogpile consists of two subsystems, one building on top of the other.

``dogpile`` provides the concept of a "dogpile lock", a control structure
which allows a single thread of execution to be selected as the "creator" of
some resource, while allowing other threads of execution to refer to the previous
version of this resource as the creation proceeds; if there is no previous
version, then those threads block until the object is available.

``dogpile.cache`` is a caching API which provides a generic interface to
caching backends of any variety, and additionally provides API hooks which
integrate these cache backends with the locking mechanism of ``dogpile``.

Overall, dogpile.cache is intended as a replacement to the `Beaker
<http://beaker.groovie.org>`_ caching system, the internals of which are
written by the same author.   All the ideas of Beaker which "work" are re-
implemented in dogpile.cache in a more efficient and succinct manner, and all
the cruft (Beaker's internals were first written in 2005) relegated to the
trash heap.

Documentation
-------------

See dogpile.cache's full documentation at
`dogpile.cache documentation <http://dogpilecache.readthedocs.org>`_.  The
sections below provide a brief synopsis of the ``dogpile`` packages.

Features
--------

* A succinct API which encourages up-front configuration of pre-defined
  "regions", each one defining a set of caching characteristics including
  storage backend, configuration options, and default expiration time.
* A standard get/set/delete API as well as a function decorator API is
  provided.
* The mechanics of key generation are fully customizable.   The function
  decorator API features a pluggable "key generator" to customize how
  cache keys are made to correspond to function calls, and an optional
  "key mangler" feature provides for pluggable mangling of keys
  (such as encoding, SHA-1 hashing) as desired for each region.
* The dogpile lock, first developed as the core engine behind the Beaker
  caching system, here vastly simplified, improved, and better tested.
  Some key performance
  issues that were intrinsic to Beaker's architecture, particularly that
  values would frequently be "double-fetched" from the cache, have been fixed.
* Backends implement their own version of a "distributed" lock, where the
  "distribution" matches the backend's storage system.  For example, the
  memcached backends allow all clients to coordinate creation of values
  using memcached itself.   The dbm file backend uses a lockfile
  alongside the dbm file.  New backends, such as a Redis-based backend,
  can provide their own locking mechanism appropriate to the storage
  engine.
* Writing new backends or hacking on the existing backends is intended to be
  routine - all that's needed are basic get/set/delete methods. A distributed
  lock tailored towards the backend is an optional addition, else dogpile uses
  a regular thread mutex. New backends can be registered with dogpile.cache
  directly or made available via setuptools entry points.
* Included backends feature three memcached backends (python-memcached, pylibmc,
  bmemcached), a Redis backend, a backend based on Python's
  anydbm, and a plain dictionary backend.
* Space for third party plugins, including one which provides the
  dogpile.cache engine to Mako templates.

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