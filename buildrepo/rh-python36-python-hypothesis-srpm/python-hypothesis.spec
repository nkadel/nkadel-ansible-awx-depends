#
# spec file for package rh-python36-python-hypothesis
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name hypothesis

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
Version:        3.12.0
Release:        0%{?dist}
Url:            https://github.com/HypothesisWorks/hypothesis-python
Summary:        A library for property based testing
License:        MPL v2 (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
# [:python_version == '2.7']
#enum34
#
#[:python_version == '3.3']
#enum34
#
#[all]
#Faker>=0.7.0,<=0.7.1
#Faker>=0.7.0,<=0.7.1
#django>=1.8,<2
#numpy>=1.9.0
#pytest>=2.8.0
#pytz
#pytz
#pytz
#
#[datetime]
#pytz
#
#[django]
#pytz
#django>=1.8,<2
#
#[fakefactory]
#Faker>=0.7.0,<=0.7.1
#
#[faker]
#Faker>=0.7.0,<=0.7.1
#
#[numpy]
#numpy>=1.9.0
#
#[pytest]
#pytest>=2.8.0
#
#[pytz]
#pytz
%endif # with_dnf

%description
==========
Hypothesis
==========

Hypothesis is an advanced testing library for Python. It lets you write tests which
are parametrized by a source of examples, and then generates simple and comprehensible
examples that make your tests fail. This lets you find more bugs in your code with less
work.

e.g.

.. code-block:: python

  @given(st.lists(
    st.floats(allow_nan=False, allow_infinity=False), min_size=1))
  def test_mean(xs):
      assert min(xs) <= mean(xs) <= max(xs)

.. code-block::

  Falsifying example: test_mean(
    xs=[1.7976321109618856e+308, 6.102390043022755e+303]
  )

Hypothesis is extremely practical and advances the state of the art of
unit testing by some way. It's easy to use, stable, and powerful. If
you're not using Hypothesis to test your project then you're missing out.

------------------------
Quick Start/Installation
------------------------
If you just want to get started:

.. code-block::

  pip install hypothesis


-----------------
Links of interest
-----------------

The main Hypothesis site is at `hypothesis.works <http://hypothesis.works>`_, and contains a lot
of good introductory and explanatory material.

Extensive documentation and examples of usage are `available at readthedocs <https://hypothesis.readthedocs.io/en/master/>`_.

If you want to talk to people about using Hypothesis, `we have both an IRC channel
and a mailing list <https://hypothesis.readthedocs.io/en/latest/community.html>`_.

If you want to receive occasional updates about Hypothesis, including useful tips and tricks, there's a
`TinyLetter mailing list to sign up for them <http://tinyletter.com/DRMacIver/>`_.

If you want to contribute to Hypothesis, `instructions are here <https://github.com/HypothesisWorks/hypothesis-python/blob/master/CONTRIBUTING.rst>`_.

If you want to hear from people who are already using Hypothesis, some of them `have written
about it <https://hypothesis.readthedocs.io/en/latest/endorsements.html>`_.

If you want to create a downstream package of Hypothesis, please read `these guidelines for packagers <https://hypothesis.readthedocs.io/en/latest/packaging.html>`_.

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
