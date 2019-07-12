#
# spec file for package rh-python36-python-pylibmc
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name pylibmc

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
Version:        1.6.0
Release:        0%{?dist}
Url:            http://sendapatch.se/projects/pylibmc/
Summary:        Quick and small memcached client for Python
License:        3-clause BSD <http://www.opensource.org/licenses/bsd-license.php> (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  libmemcached-devel
BuildRequires:  zlib-devel
%if %{with_dnf}
%endif # with_dnf

%description
`pylibmc` is a Python client for `memcached <http://memcached.org/>`_ written in C.

See `the documentation at sendapatch.se/projects/pylibmc/`__ for more information.

__ http://sendapatch.se/projects/pylibmc/

.. image:: https://travis-ci.org/lericson/pylibmc.png?branch=master
   :target: https://travis-ci.org/lericson/pylibmc

New in version 1.6.0
====================

Though no major feature overhauls have taken place, this release is partially
incompatible with 1.5.0. This stems from the fact that python-memcached is now
using a flag that pylibmc has been using for some years. python-memcached uses
it for a different purpose, and an incompatible one. We deemed that it would be
better to support this interoperability. The change also means that Unicode
strings are now stored as UTF-8 rather than pickled, which may or may not
result in a slight performance improvement for this type of data.

We have also introduced a `pickle_protocol` behavior to enable seamless
interoperability between Python 2.x and 3.x. Also, this release introduces a
ManyLinux wheel, making installation a breeze on ManyLinux systems (which I
suppose is many linuxes.)

New in version 1.5.0
====================

This release fixes critical memory leaks in common code paths introduced in
1.4.2. Also fixes a critical bug in a corner of the zlib inflation code, where
prior memory errors would trigger a double free. Thank you to everybody
involved in the making of this release, and especially `Eau de Web`__, without
their contributions, this release and the bug fixes it contains wouldn't have
been so expedient.

__ http://www.eaudeweb.ro/

.. comment: 1.5.x should have been an extension to 1.4.x, therefore it's best
   to keep the 1.4.x release announcement below.

New in version 1.4.0
====================

Brace yourself, Python 3.x support has come!

Thanks to everybody involved in this project; this release involves less
authors but **a lot** more work per person. Thanks especially to Harvey Falcic
for the work he put in, without which there wouldn't be any Python 3.x support.
Also thanks to Sergey Pashinin for the initial stab at the problem.

Other than that, we had miscellaneous bug fixes, testing improvements, and
documentation updates.

Last but not least I would like to ask for your support in this project, either
by helping out with development, testing, documentation or anything at all; or
simply by donating some `magic internet money`__ to the project's Bitcoin
address `12dveKhqiJWCY8zXT4kaHdHELXPeGAUo9h`__.

__ http://static.adzerk.net/Advertisers/5af77cf0094d4303bb308b955dd05992.jpg
__ bitcoin:12dveKhqiJWCY8zXT4kaHdHELXPeGAUo9h

License
=======

Released under the BSD 3-clause license; see `LICENSE <LICENSE>`_ for details.

Maintainer
==========

- Website: `sendapatch.se/ <http://sendapatch.se/>`_
- Github: `github.com/lericson <http://github.com/lericson>`_
- IRC: ``lericson`` in ``#sendapatch`` on ``chat.freenode.net``
- E-mail: ``ludvig`` at ``sendapatch.se``

------

.. image:: http://www.smbc-comics.com/comics/20110908.gif
   :target: http://www.smbc-comics.com/index.php?db=comics&id=2362
   :align: center


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
* Fri Jul 12 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.6.0-0
- Initial setup
- Manually BuildRequires for libmemcached-devel and zlib-devel
