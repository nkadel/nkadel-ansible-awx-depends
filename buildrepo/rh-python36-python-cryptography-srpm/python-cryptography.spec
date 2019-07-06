#
# spec file for package rh-python36-python-cryptography
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name cryptography

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
Version:        2.1.4
Release:        0%{?dist}
Url:            https://github.com/pyca/cryptography
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers.
License:        BSD or Apache License, Version 2.0 (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-idna >= 2.1
Requires:       %{?scl_prefix}python-asn1crypto >= 0.21.0
Requires:       %{?scl_prefix}python-six >= 1.4.1
# Manually added for PyPy
Requires:       %{?scl_prefix}python-cffi >= 1.7
# Manually added to supply cffi
Requires:       %{?scl_prefix}python-pycparser
# Manually added For python < 3
#Requires:       %{?scl_prefix}python-enum34
#Requires:       %{?scl_prefix}python-ipaddress

%if %{with_dnf}
# Manually added for docstest
Suggests:       %{?scl_prefix}python-doc8
Suggests:       %{?scl_prefix}python-pyenchant >= 1.6.11
Suggests:       %{?scl_prefix}python-readme_renderer >= 16.0
Suggests:       %{?scl_prefix}python-sphinx
Suggests:       %{?scl_prefix}python-sphinx_rtd_theme
Suggests:       %{?scl_prefix}python-sphinxcontrib-spelling
# Manually added for pep8test
Suggests:       %{?scl_prefix}python-flake8
Suggests:       %{?scl_prefix}python-flake8-import-order
Suggests:       %{?scl_prefix}python-pep8-naming
# Manually added for test
Conflicts:      %{?scl_prefix}python-pytest = 3.3.0
Suggests:       %{?scl_prefix}python-pytest >= 3.2.1
Suggests:       %{?scl_prefix}python-pretend
Suggests:       %{?scl_prefix}python-iso8601
Suggests:       %{?scl_prefix}python-pytz
Suggests:       %{?scl_prefix}python-hypothesis >= 1.11.4
%endif # with_dnf

%description
pyca/cryptography
=================
``cryptography`` is a package which provides cryptographic recipes and
primitives to Python developers.  Our goal is for it to be your "cryptographic
standard library". It supports Python 2.6-2.7, Python 3.4+, and PyPy 5.3+.

``cryptography`` includes both high level recipes and low level interfaces to
common cryptographic algorithms such as symmetric ciphers, message digests, and
key derivation functions. For example, to encrypt something with
the ``cryptography`` high level symmetric encryption recipe:

.. code-block:: pycon

    >>> from cryptography.fernet import Fernet
    >>> # Put this somewhere safe!
    >>> key = Fernet.generate_key()
    >>> f = Fernet(key)
    >>> token = f.encrypt(b"A really secret message. Not for prying eyes.")
    >>> token
    '...'
    >>> f.decrypt(token)
    'A really secret message. Not for prying eyes.'

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
