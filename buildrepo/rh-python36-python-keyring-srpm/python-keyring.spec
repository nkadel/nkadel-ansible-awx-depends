#
# spec file for package rh-python36-python-keyring
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name keyring

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
Version:        15.1.0
Release:        0%{?dist}
Url:            https://github.com/jaraco/keyring
Summary:        Store and access your passwords safely.
License:        Python-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-setuptools_scm >= 1.15.0
# Manually added
Requires:       %{?scl_prefix}python-entrypoints
# Manually added for python < 3.5
#Requires:       %{?scl_prefix}python-secretstorage < 3
# Manually added for python >= 3.5
Requires:       %{?scl_prefix}python-secretstorage
# Manually added for Windows reference
#
#Conflicts:       %{?scl_prefix}python-pywin32-ctypes =0.1.0
#Conflicts:       %{?scl_prefix}python-pywin32-ctypes = 0.1.1
%if %{with_dnf}
# Manually added for docs
Suggests:       %{?scl_prefix}python-sphinx
Suggests:       %{?scl_prefix}python-jaraco.packaging >= 3.2
Suggests:       %{?scl_prefix}python-rst.linker >= 1.9

# Manually added for testing
Suggests:       %{?scl_prefix}python-pytest >= 3.5
Suggests:       %{?scl_prefix}python-pytest-sugar >= 0.9.1
Suggests:       %{?scl_prefix}python-collective.checkdocs
Suggests:       %{?scl_prefix}python-pytest-flake8

%endif # with_dnf

%description
---------------------------
What is Python keyring lib?
---------------------------

The Python keyring lib provides an easy way to access the system keyring service
from python. It can be used in any application that needs safe password storage.

The keyring library is licensed under both the `MIT license
<http://opensource.org/licenses/MIT>`_ and the PSF license.

These recommended keyring backends are supported by the Python keyring lib:

* macOS `Keychain
  <https://en.wikipedia.org/wiki/Keychain_%28software%29>`_
* Freedesktop `Secret Service
  <http://standards.freedesktop.org/secret-service/>`_ supports many DE including 
  GNOME (requires `secretstorage <https://pypi.python.org/pypi/secretstorage>`_)
* KDE4 & KDE5 `KWallet <https://en.wikipedia.org/wiki/KWallet>`_
  (requires `dbus <https://pypi.python.org/pypi/dbus-python>`_)
* `Windows Credential Locker
  <https://docs.microsoft.com/en-us/windows/uwp/security/credential-locker>`_

Other keyring implementations are available through `Third-Party Backends`_.

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
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 15.1.0-0
- Update .spec with py2pack
- Manually add Requires and BuildRequires for python-setuptools_scm > 1.15.0
- Manually add _bindir
