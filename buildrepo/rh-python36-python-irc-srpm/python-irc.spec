#
# spec file for package rh-python36-python-irc
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name irc

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
Version:        16.2
Release:        0%{?dist}
Url:            https://github.com/jaraco/irc
Summary:        IRC (Internet Relay Chat) protocol library for Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-setuptools_scm >= 1.15.0
Requires:       %{?scl_prefix}python-six
Requires:       %{?scl_prefix}python-jaraco.collections
Requires:       %{?scl_prefix}python-jaraco.text
Requires:       %{?scl_prefix}python-jaraco.itertools >= 1.8
Requires:       %{?scl_prefix}python-jaraco.logging
Requires:       %{?scl_prefix}python-jaraco.functools >= 1.5
Requires:       %{?scl_prefix}python-jaraco.stream
Requires:       %{?scl_prefix}python-pytz
Requires:       %{?scl_prefix}python-more_itertools
Requires:       %{?scl_prefix}python-tempora >= 1.6
%if %{with_dnf}
# Manually added for docs
Suggests:       %{?scl_prefix}python-sphinx
Suggests:       %{?scl_prefix}python-jaraco.packaging >= 3.2
Suggests:       %{?scl_prefix}python-rst.linker >= 1.9
# Manually added for testing
Suggests:       %{?scl_prefix}python-pytest >= 2.8
Suggests:       %{?scl_prefix}python-pytest-sugar
Suggests:       %{?scl_prefix}python-collective.checkdocs
Suggests:       %{?scl_prefix}python-backports.unittest_mock
Suggests:       %{?scl_prefix}python-pygments
%endif # with_dnf

%description
Full-featured Python IRC library for Python.

- `Project home <https://github.com/jaraco/irc>`_
- `Docs <https://python-irc.readthedocs.io/>`_
- `History <https://python-irc.readthedocs.io/en/latest/history.html>`_

Overview
========

This library provides a low-level implementation of the IRC protocol for
Python.  It provides an event-driven IRC client framework.  It has
a fairly thorough support for the basic IRC protocol, CTCP, and DCC
connections.

In order to understand how to make an IRC client, it is best to read up first
on the `IRC specifications
<http://web.archive.org/web/20160628193730/http://www.irchelp.org/irchelp/rfc/>`_.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
%{py_build}
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%{py_install}
%{?scl:EOF}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 16.2-0
- Update .spec from py2pack
- Manually add Requires and Suggests
