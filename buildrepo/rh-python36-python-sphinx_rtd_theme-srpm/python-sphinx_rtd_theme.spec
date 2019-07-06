#
# spec file for package rh-python36-python-sphinx-rtd-theme
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name sphinx_rtd_theme

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
Version:        0.4.2
Release:        0%{?dist}
Url:            https://github.com/rtfd/sphinx_rtd_theme/
Summary:        Read the Docs theme for Sphinx
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
BuildRequires:  %{?scl_prefix}python-sphinx
# Manually added for renaming requirements
Provides:       %{?scl_prefix}python-sphinx-rtd-theme = %{version}-%{release}
Obsoletes:      %{?scl_prefix}python-sphinx-rtd-theme <= %{version}-%{release}
Conflicts:      %{?scl_prefix}python-sphinx-rtd-theme <= %{version}-%{release}
%if %{with_dnf}
%endif # with_df

%description
The ``sphinx_rtd_theme`` is a sphinx_ theme designed to look modern and be mobile-friendly.
This theme is primarily focused to be used on readthedocs.org_ but can work with your
own sphinx projects. To read more and see a working demo_ head over to readthedocs.org_.

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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> = 0.4.2-0
- Upgrade .spec file with py2pack
- Explicitly list conflicts with sphinx-rtd-theme packages

