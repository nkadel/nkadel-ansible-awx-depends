#
# spec file for package rh-python36-python-Pillow
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name Pillow

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
Version:        6.1.0
Release:        0%{?dist}
Url:            http://python-pillow.org
Summary:        Python Imaging Library (Fork)
License:        Historical Permission Notice and Disclaimer (HPND) (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  zlib-devel
BuildRequires:  libjpeg-turbo-devel

# List from fedora-23.sh
#sudo dnf install redhat-rpm-config
#sudo dnf install python-devel python3-devel python-virtualenv make gcc
#sudo dnf install libtiff-devel libjpeg-devel zlib-devel freetype-devel \
#    lcms2-devel libwebp-devel openjpeg2-devel tkinter python3-tkinter \
#    tcl-devel tk-devel harfbuzz-devel fribidi-devel libraqm-devel


%if %{with_dnf}
# Development, documentation & testing requirements.
Suggests:       %{?scl_prefix}python-alabaster
Suggests:       %{?scl_prefix}python-Babel
# python_version >= '3.6'
Suggests:       %{?scl_prefix}python-black

Suggests:       %{?scl_prefix}python-check-manifest
Suggests:       %{?scl_prefix}python-cov-core
Suggests:       %{?scl_prefix}python-coverage
Suggests:       %{?scl_prefix}python-coveralls
Suggests:       %{?scl_prefix}python-docopt
Suggests:       %{?scl_prefix}python-docutils
Suggests:       %{?scl_prefix}python-jarn.viewdoc
Suggests:       %{?scl_prefix}python-Jinja2
Suggests:       %{?scl_prefix}python-MarkupSafe
Suggests:       %{?scl_prefix}python-olefile
Suggests:       %{?scl_prefix}python-pycodestyle
Suggests:       %{?scl_prefix}python-pyflakes
Suggests:       %{?scl_prefix}python-Pygments
Suggests:       %{?scl_prefix}python-pyroma
Suggests:       %{?scl_prefix}python-pytest
Suggests:       %{?scl_prefix}python-pytest-cov
Suggests:       %{?scl_prefix}python-pytz
Suggests:       %{?scl_prefix}python-requests
Suggests:       %{?scl_prefix}python-six
Suggests:       %{?scl_prefix}python-snowballstemmer
Suggests:       %{?scl_prefix}python-Sphinx
Suggests:       %{?scl_prefix}python-sphinx-rtd-theme
%endif # with_dnf

%description
Pillow
======

Python Imaging Library (Fork)
-----------------------------

Pillow is the friendly PIL fork by `Alex Clark and Contributors <https://github.com/python-pillow/Pillow/graphs/contributors>`_. PIL is the Python Imaging Library by Fredrik Lundh and Contributors. As of 2019, Pillow development is `supported by Tidelift <https://tidelift.com/subscription/pkg/pypi-pillow>`_.


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
%{python3_sitearch}/*

%changelog
* Fri Jul 12 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 6.1.0=0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually add BuildRequires zlib-devel and libjpeg-turbo-devel
