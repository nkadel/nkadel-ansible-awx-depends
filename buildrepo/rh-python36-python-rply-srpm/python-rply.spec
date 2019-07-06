#
# spec file for package rh-python36-python-rply
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name rply

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
Version:        0.7.5
Release:        0%{?dist}
#Url:            
Summary:        A pure Python Lex/Yacc that works with RPython
# Manually set
License:        BSD 3-Clause License (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-appdirs
%if %{with_dnf}
%endif # with_dnf

%description
RPLY
====

.. image:: https://secure.travis-ci.org/alex/rply.png
    :target: https://travis-ci.org/alex/rply

Welcome to RPLY! A pure Python parser generator, that also works with RPython.
It is a more-or-less direct port of David Beazley's awesome PLY, with a new
public API, and RPython support.

You can find the documentation `online`_.

Basic API:

.. code:: python

    from rply import ParserGenerator, LexerGenerator
    from rply.token import BaseBox

    lg = LexerGenerator()
    # Add takes a rule name, and a regular expression that defines the rule.
    lg.add("PLUS", r"\+")
    lg.add("MINUS", r"-")
    lg.add("NUMBER", r"\d+")

    lg.ignore(r"\s+")

    # This is a list of the token names. precedence is an optional list of
    # tuples which specifies order of operation for avoiding ambiguity.
    # precedence must be one of "left", "right", "nonassoc".
    # cache_id is an optional string which specifies an ID to use for
    # caching. It should *always* be safe to use caching,
    # RPly will automatically detect when your grammar is
    # changed and refresh the cache for you.
    pg = ParserGenerator(["NUMBER", "PLUS", "MINUS"],
            precedence=[("left", ['PLUS', 'MINUS'])], cache_id="myparser")

    @pg.production("main : expr")
    def main(p):
        # p is a list, of each of the pieces on the right hand side of the
        # grammar rule
        return p[0]

    @pg.production("expr : expr PLUS expr")
    @pg.production("expr : expr MINUS expr")
    def expr_op(p):
        lhs = p[0].getint()
        rhs = p[2].getint()
        if p[1].gettokentype() == "PLUS":
            return BoxInt(lhs + rhs)
        elif p[1].gettokentype() == "MINUS":
            return BoxInt(lhs - rhs)
        else:
            raise AssertionError("This is impossible, abort the time machine!")

    @pg.production("expr : NUMBER")
    def expr_num(p):
        return BoxInt(int(p[0].getstr()))

    lexer = lg.build()
    parser = pg.build()

    class BoxInt(BaseBox):
        def __init__(self, value):
            self.value = value

        def getint(self):
            return self.value

Then you can do:

.. code:: python

    parser.parse(lexer.lex("1 + 3 - 2+12-32"))

You can also substitute your own lexer. A lexer is an object with a ``next()``
method that returns either the next token in sequence, or ``None`` if the token
stream has been exhausted.

Why do we have the boxes?
-------------------------

In RPython, like other statically typed languages, a variable must have a
specific type, we take advantage of polymorphism to keep values in a box so
that everything is statically typed. You can write whatever boxes you need for
your project.

If you don't intend to use your parser from RPython, and just want a cool pure
Python parser you can ignore all the box stuff and just return whatever you
like from each production method.

Error handling
--------------

By default, when a parsing error is encountered, an ``rply.ParsingError`` is
raised, it has a method ``getsourcepos()``, which returns an
``rply.token.SourcePosition`` object.

You may also provide an error handler, which, at the moment, must raise an
exception. It receives the ``Token`` object that the parser errored on.

.. code:: python

    pg = ParserGenerator(...)

    @pg.error
    def error_handler(token):
        raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

Python compatibility
--------------------

RPly is tested and known to work under Python 2.6, 2.7, 3.3+, and PyPy. It is
also valid RPython for PyPy checkouts from ``6c642ae7a0ea`` onwards.

Links
-----

* `Source code and issue tracker <https://github.com/alex/rply/>`_
* `PyPI releases <https://pypi.python.org/pypi/rply>`_
* `Talk at PyCon US 2013: So you want to write an interpreter? <http://pyvideo.org/video/1694/so-you-want-to-write-an-interpreter>`_

.. _`online`: https://rply.readthedocs.io/




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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.7.5-0
- Update .spec file with py2pack
- Manually set blank License and comment out blank Url
- Manually add Requires