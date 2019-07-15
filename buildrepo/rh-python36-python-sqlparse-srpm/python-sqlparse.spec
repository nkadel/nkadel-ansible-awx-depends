#
# spec file for package rh-python36-python-sqlparse
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name sqlparse

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
Version:        0.3.0
Release:        0%{?dist}
Url:            https://github.com/andialbrecht/sqlparse
Summary:        Non-validating SQL parser
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

``sqlparse`` is a non-validating SQL parser module.
It provides support for parsing, splitting and formatting SQL statements.

Visit the `project page <https://github.com/andialbrecht/sqlparse>`_ for
additional information and documentation.

**Example Usage**


Splitting SQL statements::

   >>> import sqlparse
   >>> sqlparse.split('select * from foo; select * from bar;')
   [u'select * from foo; ', u'select * from bar;']


Formatting statements::

   >>> sql = 'select * from foo where id in (select id from bar);'
   >>> print sqlparse.format(sql, reindent=True, keyword_case='upper')
   SELECT *
   FROM foo
   WHERE id IN
     (SELECT id
      FROM bar);


Parsing::

   >>> sql = 'select * from someschema.mytable where id = 1'
   >>> res = sqlparse.parse(sql)
   >>> res
   (<Statement 'select...' at 0x9ad08ec>,)
   >>> stmt = res[0]
   >>> str(stmt)  # converting it back to unicode
   'select * from someschema.mytable where id = 1'
   >>> # This is how the internal representation looks like:
   >>> stmt.tokens
   (<DML 'select' at 0x9b63c34>,
    <Whitespace ' ' at 0x9b63e8c>,
    <Operator '*' at 0x9b63e64>,
    <Whitespace ' ' at 0x9b63c5c>,
    <Keyword 'from' at 0x9b63c84>,
    <Whitespace ' ' at 0x9b63cd4>,
    <Identifier 'somes...' at 0x9b5c62c>,
    <Whitespace ' ' at 0x9b63f04>,
    <Where 'where ...' at 0x9b5caac>)





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
%{_bindir}/*

%changelog
* Sat Jul 13 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.3.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Add _bindir to files
