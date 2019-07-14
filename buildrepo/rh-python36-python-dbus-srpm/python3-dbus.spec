Summary: D-Bus Python 3 Bindings 
Name:    python3-dbus
Version: 1.2.4
Release: 3%{?dist}

License: MIT
URL:     http://www.freedesktop.org/wiki/Software/DBusBindings/
Source0: http://dbus.freedesktop.org/releases/dbus-python/dbus-python-%{version}.tar.gz
Source1: http://dbus.freedesktop.org/releases/dbus-python/dbus-python-%{version}.tar.gz.asc

# borrow centos7 patch to use sitearch properly
Patch0: 0001-Move-python-modules-to-architecture-specific-directo.patch

BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
#BuildRequires: python-docutils
BuildRequires: python%{python3_pkgversion}-devel
# for %%check
BuildRequires: dbus-x11 pygobject3
# autoreconf and friends
BuildRequires: autoconf-archive automake libtool

%description
%{summary}.

%package -n python%{python3_pkgversion}-dbus
Summary: D-Bus bindings for python %{python3_version}
%description -n python%{python3_pkgversion}-dbus
%{summary}.


%prep
%setup -q -n dbus-python-%{version}
%patch0 -p1 -b .sitearch
# Remove obsolete macros such as AC_PROG_LIBTOOL
autoupdate
# For new arches (aarch64/ppc64le), and patch0
autoreconf -vif


%build
%global _configure ../configure
mkdir python%{python3_pkgversion}-build; pushd python%{python3_pkgversion}-build
%configure PYTHON=%{__python3}
make %{?_smp_mflags}
popd


%install
make install DESTDIR=%{buildroot} -C python%{python3_pkgversion}-build

# unpackaged files
rm -r  %{buildroot}%{_includedir}
rm -r  %{buildroot}%{_libdir}/pkgconfig
rm %{buildroot}%{python3_sitearch}/*.la
rm -r %{buildroot}%{_datadir}/doc/dbus-python/


%check
make check -k -C python%{python3_pkgversion}-build


%files -n python%{python3_pkgversion}-dbus
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
