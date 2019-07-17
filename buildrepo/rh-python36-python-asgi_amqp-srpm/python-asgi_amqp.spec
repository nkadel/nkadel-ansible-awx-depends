#
# spec file for package rh-python36-python-asgi-amqp
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name asgi-amqp
%global src_name asgi_amqp

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
Version:        1.1.3
Release:        0%{?dist}
Url:            http://github.com/ansible/asgi_amqp/
Summary:        AMQP-backed ASGI channel layer implementation
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{src_name}; echo ${n:0:1})/%{src_name}/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-six
Requires:       %{?scl_prefix}python-kombu >= 3.0.35
Requires:       %{?scl_prefix}python-msgpack-python >= 0.4.7
#Requires:       %{?scl_prefix}python-asgiref = 1.1.2
Requires:       %{?scl_prefix}python-asgiref >= 1.1.2
Requires:       %{?scl_prefix}python-jsonpickle >= 0.9.3

%if %{with_dnf}
%endif # with_dnf

%description
asgi_amqp
==========

An ASGI channel layer that uses AMQP as its backing store with group support.

Settings
--------

The `asgi_amqp` channel layer looks for settings in `ASGI_AMQP` and
has the following configuration options. URL and connection settings
are configured through `CHANNEL_LAYER` same as any channel layer.

**MODEL**
Set a custom `ChannelGroup` model to use. See more about this in the ChannelGroup
Model section of this README.

Usage::

    ASGI_AMQP = {'MODEL': 'awx.main.models.channels.ChannelGroup'}

**INIT_FUNC**
A function that you want run when the channel layer is first instantiated.

Usage::

    ASGI_AMQP = {'INIT_FUNC': 'awx.prepare_env'}


ChannelGroup Model
------------------

This channel layer requires a database model called `ChannelGroup`. You
can use the model and migation provided by adding `asgi_amqp` to your
installed apps or you can point the `ASGI_AMQP.MODEL` setting to a
model you have already defined.

Installed Apps::

    INSTALLED_APPS = [
        ...
        'asgi_amqp',
        ...
    ]

Settings::

    ASGI_AMQP = {
        'MODEL': 'awx.main.models.channels.ChannelGroup',
    }




%prep
%setup -q -n %{src_name}-%{version}

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

%changelog
* Sun Jul 7 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.1.3-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Update asgiref to >= 1.1.2, instead of = 1.1.2
