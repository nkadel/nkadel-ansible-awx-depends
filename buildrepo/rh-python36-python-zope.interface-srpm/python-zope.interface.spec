%{?scl:%scl_package python-zope.interface}
%{!?scl:%global pkg_name %{name}}
%global py_pkgname zope.interface

Name:           %{?scl_prefix}python-%{py_pkgname}
Version:        4.4.3
Release:        0%{?dist}
Summary:        Zope 3 Interfaces for Python

Group:          Development/Libraries
License:        ZPL 2.1
Url:            https://pypi.python.org/pypi/%{py_pkgname}
Vendor:         Zope Foundation and Contributors <zope-dev@zope.org>

Source0:        https://pypi.io/packages/source/z/%{py_pkgname}/%{py_pkgname}-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}python-devel
Provides:	%{?scl_prefix}python-zope-interface = %{version}-%{release}
Obsoletes:	%{?scl_prefix}python-zope-interface < %{version}-%{release}

%description
Interfaces are a mechanism for labeling objects as conforming to a given API \
or contract. \
This is a separate distribution of the zope.interface package used in Zope 3.

%prep
%setup -n %{py_pkgname}-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
env CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%{__python3} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}

%files -f INSTALLED_FILES
%defattr(-,root,root)
