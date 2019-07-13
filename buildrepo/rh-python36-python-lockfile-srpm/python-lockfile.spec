#
# spec file for package rh-python36-python-lockfile
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name lockfile

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
Version:        0.12.2
Release:        0%{?dist}
Url:            http://launchpad.net/pylockfile
Summary:        Platform-independent file locking module
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-pbr >= 1.0
%if %{with_dnf}
Suggests:       %{?scl_prefix}python-nose
Suggests:       %{?scl_prefix}python-sphinx >= 1.1.2
Conflicts:      %{?scl_prefix}python-sphinx = 1.2.0
Conflicts:      %{?scl_prefix}python-sphinx = 1.3b1
Conflicts:      %{?scl_prefix}python-sphinx = 1.3
%endif # with_dnf

%description
Note: This package is **deprecated**. It is highly preferred that instead of
using this code base that instead `fasteners`_ or `oslo.concurrency`_ is
used instead. For any questions or comments or further help needed
please email `openstack-dev`_ and prefix your email subject
with ``[oslo][pylockfile]`` (for a faster response).

.. _fasteners: https://pypi.python.org/pypi/fasteners
.. _oslo.concurrency: http://docs.openstack.org/developer/oslo.concurrency/
.. _openstack-dev: http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-dev

The lockfile package exports a LockFile class which provides a simple API for
locking files.  Unlike the Windows msvcrt.locking function, the fcntl.lockf
and flock functions, and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms.
The lock mechanism relies on the atomic nature of the link (on Unix) and
mkdir (on Windows) system calls.  An implementation based on SQLite is also
provided, more as a demonstration of the possibilities it provides than as
production-quality code.

Note: In version 0.9 the API changed in two significant ways:

 * It changed from a module defining several classes to a package containing
   several modules, each defining a single class.

 * Where classes had been named SomethingFileLock before the last two words
   have been reversed, so that class is now SomethingLockFile.

The previous module-level definitions of LinkFileLock, MkdirFileLock and
SQLiteFileLock will be retained until the 1.0 release.

To install:

    python setup.py install

* Documentation: http://docs.openstack.org/developer/pylockfile
* Source: http://git.openstack.org/cgit/openstack/pylockfile
* Bugs: http://bugs.launchpad.net/pylockfile

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
