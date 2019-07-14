#
# spec file for package rh-python36-python3-dbus
#    Heavily modified on top of EPEL python3-dbes
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name dbus-python

%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name python-%{pypi_name}}

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Change EPEL name to py2pack compliant name
#Name:    python3-dbus
#Name:    %{?scl_prefix}python-%{pypi_name}
Name:    %{?scl_prefix}%{pypi_name}
Summary: D-Bus Python 3 Bindings 
Version: 1.2.4
#Release: 3%{?dist}
Release: 0%{?dist}

License: MIT
URL:     http://www.freedesktop.org/wiki/Software/DBusBindings/
Source0: http://dbus.freedesktop.org/releases/dbus-python/dbus-python-%{version}.tar.gz
Source1: http://dbus.freedesktop.org/releases/dbus-python/dbus-python-%{version}.tar.gz.asc

# borrow centos7 patch to use sitearch properly
Patch0: 0001-Move-python-modules-to-architecture-specific-directo.patch

BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
# Switch to scl compatible dependencies
BuildRequires: %{?scl_prefix}python-docutils
BuildRequires: %{?scl_prefix}python-devel
BuildRequires: %{?scl_prefix}python-setuptools
# for %%check
BuildRequires: dbus-x11
BuildRequires: pygobject3
# autoreconf and friends
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: libtool

%description
%{summary}.

#%package -n %{?scl_prefix}python%{python3_pkgversion}-dbus
#Summary: D-Bus bindings for python %{python3_version}
#%description -n python%{python3_pkgversion}-dbus
#%{summary}.

%prep
%setup -q -n dbus-python-%{version}
%patch0 -p1 -b .sitearch
# Remove obsolete macros such as AC_PROG_LIBTOOL
autoupdate
# For new arches (aarch64/ppc64le), and patch0
autoreconf -vif


%build
%global _configure ../configure
%{?scl:scl enable %{scl} - << \EOF}
mkdir python%{python3_pkgversion}-build
pushd python%{python3_pkgversion}-build
%configure PYTHON=%{__python3}
make %{?_smp_mflags}
popd
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
make install DESTDIR=%{buildroot} -C python%{python3_pkgversion}-build
%{?scl:EOF}

# unpackaged files
rm -r  %{buildroot}%{_includedir}
rm -r  %{buildroot}%{_libdir}/pkgconfig
rm %{buildroot}%{python3_sitearch}/*.la
rm -r %{buildroot}%{_datadir}/doc/dbus-python/


%check
make check -k -C python%{python3_pkgversion}-build || :

%files
%license COPYING
%{python3_sitearch}/*.so
%{python3_sitearch}/dbus/


%changelog
* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com>
- Rebuilt to change main python from 3.4 to 3.6

* Mon Nov 7 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.4-2
- Run autoupdate to remove obsolete macros such as AC_PROG_LIBTOOL

* Wed Apr 6 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.4-1
- Initial EPEL package
