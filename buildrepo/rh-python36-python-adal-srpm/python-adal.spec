%{?scl:%scl_package python-adal}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}python-adal
Version:        0.5.0
Release:        0%{?dist}
Summary:        ADAL for Python

Group:          Development/Libraries
License:        MIT
Url:            https://pypi.python.org/pypi/adal/
Source0:        https://files.pythonhosted.org/packages/source/a/adal/adal-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python-devel

%description
The ADAL for Python library makes it easy for python application to authenticate to Azure Active Directory (AAD) in order to access AAD protected web resources.


%prep
%setup -n adal-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%{py_build}
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%{py_install}
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
