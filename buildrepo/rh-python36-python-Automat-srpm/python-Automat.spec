#
# spec file for package rh-python36-python-Automat
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name Automat

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
Version:        0.6.0
Release:        0%{?dist}
Url:            https://github.com/glyph/Automat
Summary:        Self-service finite-state machines for the programmer on the go.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-setuptools_scm
BuildRequires:  %{?scl_prefix}python-m2r
Requires:       %{?scl_prefix}python-attrs
Requires:       %{?scl_prefix}python-m2r
Requires:       %{?scl_prefix}python-six
%if %{with_dnf}
#[visualize]
Suggests:       %{?scl_prefix}python-graphviz > 0.5.1
Suggests:       %{?scl_prefix}python-Twisted >= 16.1.1
%endif # with_dnf

%description
Automat
=======


.. image:: https://travis-ci.org/glyph/automat.svg?branch=master
   :target: https://travis-ci.org/glyph/automat
   :alt: Build Status


.. image:: https://coveralls.io/repos/glyph/automat/badge.png
   :target: https://coveralls.io/r/glyph/automat
   :alt: Coverage Status


Self-service finite-state machines for the programmer on the go.
----------------------------------------------------------------

Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).

Why use state machines?
^^^^^^^^^^^^^^^^^^^^^^^

Sometimes you have to create an object whose behavior varies with its state,
but still wishes to present a consistent interface to its callers.

For example, let us say you are writing the software for a coffee machine.  It
has a lid that can be opened or closed, a chamber for water, a chamber for
coffee beans, and a button for "brew".

There are a number of possible states for the coffee machine.  It might or
might not have water.  It might or might not have beans.  The lid might be open
or closed.  The "brew" button should only actually attempt to brew coffee in
one of these configurations, and the "open lid" button should only work if the
coffee is not, in fact, brewing.

With diligence and attention to detail, you can implement this correctly using
a collection of attributes on an object; ``has_water``\ , ``has_beans``\ ,
``is_lid_open`` and so on.  However, you have to keep all these attributes
consistent.  As the coffee maker becomes more complex - perhaps you add an
additional chamber for flavorings so you can make hazelnut coffee, for
example - you have to keep adding more and more checks and more and more
reasoning about which combinations of states are allowed.

Rather than adding tedious 'if' checks to every single method to make sure that
each of these flags are exactly what you expect, you can use a state machine to
ensure that if your code runs at all, it will be run with all the required
values initialized, because they have to be called in the order you declare
them.

You can read about state machines and their advantages for Python programmers
in considerably more detail
`in this excellent series of articles from ClusterHQ <https://clusterhq.com/blog/what-is-a-state-machine/>`_.

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
%{_bindir}/*

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.6.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests and _bindir
- Manually add BuildRequires for python-m2r

