#
# spec file for package rh-python36-python-jaraco.packaging
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name jaraco.packaging

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
Version:        6.1
Release:        0%{?dist}
Url:            https://github.com/jaraco/jaraco.packaging
Summary:        tools to supplement packaging Python releases
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Mahually added
Requires:       %{?scl_prefix}python-six >= 1.4
Requires:       %{?scl_prefix}python-setuptools
%if %{with_dnf}
#[docs]
Suggests:       %{?scl_prefix}python-sphinx
Suggests:       %{?scl_prefix}python-jaraco.packaging >= 3.2
Suggests:       %{?scl_prefix}python-rst.linker >= 1.9
##[testing]
Conflicts:      %{?scl_prefix}python-pytest = 3.7.3
Suggests:       %{?scl_prefix}python-pytest >= 3.5
Suggests:       %{?scl_prefix}python-pytest-checkdocs
Suggests:       %{?scl_prefix}python-pytest-flake8
%endif # with_dnf

%description
Tools for packaging.

dependency_tree
===============

A distutils command for reporting the dependency tree as resolved
by setuptools. Use after installing a package.

show
====

A distutils command for reporting the attributes of a distribution,
such as the version or author name. Here are some examples against
this package::

    $ python -q setup.py show
    jaraco.packaging 2.8.2.dev1+nfaae9fb96b36.d20151127
    $ python -q setup.py show --attributes version
    2.8.2.dev1+nfaae9fb96b36.d20151127
    $ python -q setup.py show --attributes author,author_email
    "Jason R. Coombs" jaraco@jaraco.com
    $ python setup.py -q show --attributes classifiers
    "['Development Status :: 5 - Production/Stable', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3']"
    $ python setup.py -q show --attributes "description url"
    "tools to supplement packaging Python releases" https://bitbucket.org/jaraco/jaraco.packaging

Note that passing -q suppresses the "running show" message.

Attributes may be specified as comma-separated or space-separated keys.
Results are printed using ``subprocess.list2cmdline`` so may be parsed using
``shlex.split``. By default, 'name' and 'version' are printed.

sphinx
======

This package provides a Sphinx extension that will inject into the config
the following values from the project's package metadata (as presented by
distutils):

 - project (from name)
 - author
 - copyright (same as author)
 - version
 - release (same as version)
 - package_url (from url)

To enable, include 'jaraco.packaging' in your requirements and add
'jaraco.packaging.sphinx' to your list of extensions in your config file::

    extensions=['jaraco.packaging.sphinx']

make-tree
=========

A utility for taking output from ``pipdeptree --json`` and producing a tree
rooted at a given package.

Usage::

    pipdeptree --json | python -m jaraco.packaging.make-tree mypkg




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
