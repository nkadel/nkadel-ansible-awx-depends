#
# spec file for package rh-python36-python-knack
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name knack

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
Version:        0.3.3
Release:        0%{?dist}
Url:            https://github.com/microsoft/knack
Summary:        A Command-Line Interface framework
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
Knack
=====

.. image:: https://img.shields.io/pypi/v/knack.svg
    :target: https://pypi.python.org/pypi/knack

.. image:: https://img.shields.io/pypi/pyversions/knack.svg
    :target: https://pypi.python.org/pypi/knack

.. image:: https://travis-ci.org/Microsoft/knack.svg?branch=master
    :target: https://travis-ci.org/Microsoft/knack


------------


::

    _                     _    
   | | ___ __   __ _  ___| | __
   | |/ / '_ \ / _` |/ __| |/ /
   |   <| | | | (_| | (__|   < 
   |_|\_\_| |_|\__,_|\___|_|\_\


**A Command-Line Interface framework**


.. code-block:: bash

    pip install knack


------------

.. note:: The project is in `initial development phase <https://semver.org/#how-should-i-deal-with-revisions-in-the-0yz-initial-development-phase>`__ . We recommend pinning to at least a specific minor version when marking **knack** as a dependency in your project.

------------


Usage
=====


.. code-block:: python

    import sys
    from collections import OrderedDict
    from knack import CLI, CLICommandsLoader, ArgumentsContext

    def abc_list(myarg):
        import string
        return list(string.ascii_lowercase)

    class MyCommandsLoader(CLICommandsLoader):
        def load_command_table(self, args):
            with CommandGroup(__name__, self, 'abc', '__main__#{}') as g:
                g.command('list', 'abc_list')
            return OrderedDict(self.command_table)

        def load_arguments(self, command):
            with ArgumentsContext(self, 'abc list') as ac:
                ac.argument('myarg', type=int, default=100)
            super(MyCommandsLoader, self).load_arguments(command)

    mycli = CLI(cli_name='mycli', commands_loader_cls=MyCommandsLoader)
    exit_code = mycli.invoke(sys.argv[1:])
    sys.exit(exit_code)


More samples and snippets available at `examples <examples>`__.


Documentation
=============

Documentation is available at `docs <docs>`__.

Developer Setup
===============

In a virtual environment, install the `requirements.txt` file.

.. code-block:: bash

    pip install -r requirements.txt
    pip install -e .

Run Automation
==============

This project supports running automation using `tox <https://tox.readthedocs.io/en/latest/>`__.

.. code-block:: bash

    pip install tox
    tox


Real-world uses
===============

- `Azure CLI <https://github.com/Azure/azure-cli/>`__: The Azure CLI 2.0 is Azure's new command line experience for managing Azure resources.
- `VSTS CLI <https://github.com/Microsoft/vsts-cli>`__: A command-line interface for Visual Studio Team Services (VSTS) and Team Foundation Server (TFS). With the VSTS CLI, you can manage and work with resources including pull requests, work items, builds, and more.
- `Service Fabric CLI <https://github.com/Azure/service-fabric-cli>`__: A command-line interface for interacting with Azure Service Fabric clusters and their related entities.

Do you use knack in your CLI as well? Open a pull request to include it here. We would love to have it in our list.


Release History		
===============

See `GitHub Releases <https://github.com/Microsoft/knack/releases>`__.


Contribute Code
===============

This project has adopted the `Microsoft Open Source Code of Conduct <https://opensource.microsoft.com/codeofconduct/>`__.

For more information see the `Code of Conduct FAQ <https://opensource.microsoft.com/codeofconduct/faq/>`__ or contact `opencode@microsoft.com <mailto:opencode@microsoft.com>`__ with any additional questions or comments.

If you would like to become an active contributor to this project please
follow the instructions provided in `Contribution License Agreement <https://cla.microsoft.com/>`__


License
=======

Knack is licensed under `MIT <LICENSE>`__.





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