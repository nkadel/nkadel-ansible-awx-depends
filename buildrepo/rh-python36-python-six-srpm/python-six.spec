%{?scl:%scl_package python-six}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}python-six
Version:        1.12.0
Release:        0%{?dist}
Summary:        Python 2 and 3 compatibility utilities

Group:          Development/Languages
License:        MIT
URL:            https://pypi.python.org/pypi/six/
Source0:        https://files.pythonhosted.org/packages/source/s/six/six-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python-devel
# RHSCL-1.1: pytest and tkinter are not in scl -- disable tests
# For use by selftests:
#BuildRequires:  pytest
#BuildRequires:  tkinter

%description
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

This is the Python 3 build of the module.

%prep
%setup -q -n six-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
%{py_build}
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%{py_install}
%{?scl:EOF}

# disable tests: rhscl doesn't contain pytest and tkinter
#%%check
#py.test -rfsxX test_six.py
#%if 0%{?with_python3}
#pushd %{py3dir}
#py.test-%{python3_version} -rfsxX test_six.py
#popd
#%endif

%files
%doc LICENSE README.rst documentation/index.rst
%{python3_sitelib}/six.py
%{python3_sitelib}/six-*.egg-info/
%{python3_sitelib}/__pycache__/*


%changelog
* Mon Sep 25 2017 Charalampos Stratakis <cstratak@redhat.com> - 1.11.0-1
- Update to 1.11.0
Resolves: rhbz#1494494

* Sat Feb 13 2016 Robert Kuska <rkuska@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Tue Jan 20 2015 Matej Stuchlik <mstuchli@redhat.com> - 1.8.0-1
- Update to 1.8.0

* Tue Nov 19 2013 Tomas Tomecek <ttomecek@redhat.com> - 1.3.0-4
- bump release to be greater than build in RHEL-7

* Wed Nov 13 2013 Tomas Tomecek <ttomecek@redhat.com> - 1.3.0-2
- RHSCL-1.1 build

* Thu Mar 21 2013 David Malcolm <dmalcolm@redhat.com> - 1.3.0-1
- 1.3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 David Malcolm <dmalcolm@redhat.com> - 1.2.0-1
- 1.2.0 (rhbz#852658)
- add %%check section

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.0-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Ralph Bean <rbean@redhat.com> - 1.1.0-2
- Conditionalized python3-six, allowing an el6 build.

* Tue Feb  7 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.0-1
- 1.1.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 24 2011 David Malcolm <dmalcolm@redhat.com> - 1.0.0-1
- initial packaging


