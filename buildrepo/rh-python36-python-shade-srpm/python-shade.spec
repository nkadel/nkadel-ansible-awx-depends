#
# spec file for package rh-python36-python-shade
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name shade

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
Version:        1.27.0
Release:        0%{?dist}
Url:            http://docs.openstack.org/shade/latest
Summary:        Simple client library for interacting with OpenStack clouds
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Conflicts:      %{?scl_prefix}python-pbr = 2.1.0
BuildRequires:  %{?scl_prefix}python-pbr >= 2.0.0
Requires:       %{?scl_prefix}python-pbr >= 2.0.0
Requires:       %{?scl_prefix}python-os-client-config >= 1.28.0
Requires:       %{?scl_prefix}python-openstacksdk >= 0.9.19
%if %{with_dnf}
# The order of packages is significant, because pip processes them in the order
# of appearance. Changing the order has an impact on the overall integration
# process, which may cause wedges in the gate later.
Suggests:       %{?scl_prefix}python-hacking < 0.12
Suggests:       %{?scl_prefix}python-hacking >=0.11.0
Conflicts:      %{?scl_prefix}python-coverage = 4.4
Suggests:       %{?scl_prefix}python-coverage >= 4.0
Suggests:       %{?scl_prefix}python-fixtures >= 3.0.0
Suggests:       %{?scl_prefix}python-mock >= 2.0.0
Suggests:       %{?scl_prefix}python-python-subunit >= 1.0.0
Suggests:       %{?scl_prefix}python-openstackdocstheme >= 1.18.1
Suggests:       %{?scl_prefix}python-oslotest >= 3.2.0
Suggests:       %{?scl_prefix}python-requests-mock >= 1.1.0
Conflicts:      %{?scl_prefix}python-sphinx = 1.6.6
Suggests:       %{?scl_prefix}python-sphinx >= 1.6.2
Suggests:       %{?scl_prefix}python-stestr >= 1.0.0
Suggests:       %{?scl_prefix}python-testscenarios >= 0.4
Suggests:       %{?scl_prefix}python-testtools >= 2.2.0
Suggests:       %{?scl_prefix}python-reno >= 2.5.0
%endif # with_dnf

%description
Introduction
============

shade is a simple client library for interacting with OpenStack clouds. The
key word here is *simple*. Clouds can do many many many things - but there are
probably only about 10 of them that most people care about with any
regularity. If you want to do complicated things, you should probably use
the lower level client libraries - or even the REST API directly. However,
if what you want is to be able to write an application that talks to clouds
no matter what crazy choices the deployer has made in an attempt to be
more hipster than their self-entitled narcissist peers, then shade is for you.

shade started its life as some code inside of ansible. ansible has a bunch
of different OpenStack related modules, and there was a ton of duplicated
code. Eventually, between refactoring that duplication into an internal
library, and adding logic and features that the OpenStack Infra team had
developed to run client applications at scale, it turned out that we'd written
nine-tenths of what we'd need to have a standalone library.

.. _example:

Example
=======

Sometimes an example is nice.

#. Create a ``clouds.yml`` file::

     clouds:
      mordred:
        region_name: RegionOne
        auth:
          username: 'mordred'
          password: XXXXXXX
          project_name: 'shade'
          auth_url: 'https://montytaylor-sjc.openstack.blueboxgrid.com:5001/v2.0'

   Please note: *os-client-config* will look for a file called ``clouds.yaml``
   in the following locations:

   * Current Directory
   * ``~/.config/openstack``
   * ``/etc/openstack``

   More information at https://pypi.python.org/pypi/os-client-config


#. Create a server with *shade*, configured with the ``clouds.yml`` file::

    import shade

    # Initialize and turn on debug logging
    shade.simple_logging(debug=True)

    # Initialize cloud
    # Cloud configs are read with os-client-config
    cloud = shade.openstack_cloud(cloud='mordred')

    # Upload an image to the cloud
    image = cloud.create_image(
        'ubuntu-trusty', filename='ubuntu-trusty.qcow2', wait=True)

    # Find a flavor with at least 512M of RAM
    flavor = cloud.get_flavor_by_ram(512)

    # Boot a server, wait for it to boot, and then do whatever is needed
    # to get a public ip for it.
    cloud.create_server(
        'my-server', image=image, flavor=flavor, wait=True, auto_ip=True)


Links
=====

* `Issue Tracker <https://storyboard.openstack.org/#!/project/760>`_
* `Code Review <https://review.openstack.org/#/q/status:open+project:openstack-infra/shade,n,z>`_
* `Documentation <https://docs.openstack.org/shade/latest/>`_
* `PyPI <https://pypi.python.org/pypi/shade/>`_
* `Mailing list <http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-infra>`_





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
%{_bindir}/*

%changelog
* Sun Jul 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.27.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
- Manually add _bindir
