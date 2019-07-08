#
# spec file for package rh-python36-python-django-pglocks
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name django-pglocks

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
Version:        1.0.2
Release:        0%{?dist}
Url:            https://github.com/Xof/django-pglocks
Summary:        django_pglocks provides useful context managers for advisory locks for PostgreSQL.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
==============
django-pglocks
==============

django-pglocks provides a useful context manager to manage PostgreSQL advisory locks. It requires Django (tested with 1.5), PostgreSQL, and (probably) psycopg2.

Advisory Locks
==============

Advisory locks are application-level locks that are acquired and released purely by the client of the database; PostgreSQL never acquires them on its own. They are very useful as a way of signalling to other sessions that a higher-level resource than a single row is in use, without having to lock an entire table or some other structure.

It's entirely up to the application to correctly acquire the right lock.

Advisory locks are either session locks or transaction locks. A session lock is held until the database session disconnects (or is reset); a transaction lock is held until the transaction terminates.

Currently, the context manager only creates session locks, as the behavior of a lock persisting after the context body has been exited is surprising, and there's no way of releasing a transaction-scope advisory lock except to exit the transaction.

Installing
==========

Just use pip::

    pip install django-pglocks
    
Transactions
============

This assumes you are controlling transactions within the view; do not use this
if you controlling transactions through the Django transation middleware.

Usage
=====

Usage example::

    from django_pglocks import advisory_lock

    lock_id = 'some lock'

    with advisory_lock(lock_id) as acquired:
        # code that should be inside of the lock.

The context manager attempts to take the lock, and then executes the code inside the context with the lock acquired. The lock is released when the context exits, either normally or via exception.

The parameters are:

* ``lock_id`` -- The ID of the lock to acquire. It can be a string, long, or a tuple of two ints. If it's a string, the hash of the string is used as the lock ID (PostgreSQL advisory lock IDs are 64 bit values).

* ``shared`` (default False) -- If True, a shared lock is taken. Any number of sessions can hold a shared lock; if another session attempts to take an exclusive lock, it will wait until all shared locks are released; if a session is holding a shared lock, it will block attempts to take a shared lock. If False (the default), an exclusive lock is taken.

* ``wait`` (default True) -- If True (the default), the context manager will wait until the lock has been acquired before executing the content; in that case, it always returns True (unless a deadlock occurs, in which case an exception is thrown). If False, the context manager will return immediately even if it cannot take the lock, in which case it returns false. Note that the context body is *always* executed; the only way to tell in the ``wait=False`` case whether or not the lock was acquired is to check the returned value.

* ``using`` (default None) -- The database alias on which to attempt to acquire the lock. If None, the default connection is used.

Contributing
============

To run the test suite, you must create a user and a database::

    $ createuser -s -P django_pglocks
    Enter password for new role: django_pglocks
    Enter it again: django_pglocks
    $ createdb django_pglocks -O django_pglocks

You can then run the tests with::

    $ DJANGO_SETTINGS_MODULE=django_pglocks.test_settings PYTHONPATH=. django-admin.py test

License
=======

It's released under the `MIT License <http://opensource.org/licenses/mit-license.php>`_.

Change History 1.0.2
====================

Fixed bug where lock would not be released when acquired with wait=False.
Many thanks to Aymeric Augustin for finding this!

Change History 1.0.1
====================

Removed transaction-level locks, as their behavior was somewhat surprising (having the lock persist after the context manager exited was unexpected behavior).

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