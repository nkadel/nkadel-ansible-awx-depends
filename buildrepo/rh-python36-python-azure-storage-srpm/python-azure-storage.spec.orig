#
# spec file for package rh-python36-python-azure-storage
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name azure-storage

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
Version:        0.35.1
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-storage-python
Summary:        Microsoft Azure Storage Client Library for Python
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
Microsoft Azure Storage SDK for Python
======================================

This project provides a client library in Python that makes it easy to
consume Microsoft Azure Storage services. For documentation please see
the Microsoft Azure `Python Developer Center`_ and our `API Reference`_ Page.

    If you are looking for the Service Bus or Azure Management
    libraries, please visit
    https://github.com/Azure/azure-sdk-for-python.


Compatibility
=============

**IMPORTANT**: If you have an earlier version of the azure package
(version < 1.0), you should uninstall it before installing this package.

You can check the version using pip:

.. code:: shell

    pip freeze

If you see azure==0.11.0 (or any version below 1.0), uninstall it first then install it again:

.. code:: shell

    pip uninstall azure
    pip install azure

If you are upgrading from a version older than 0.30.0, see the upgrade doc, the 
usage samples in the samples directory, and the ChangeLog and BreakingChanges.

Features
========

-  Blob

   -  Create/Read/Update/Delete Containers
   -  Create/Read/Update/Delete Blobs
   -  Advanced Blob Operations

-  Queue

   -  Create/Delete Queues
   -  Insert/Peek Queue Messages
   -  Advanced Queue Operations

-  Table

   -  Create/Read/Update/Delete Tables
   -  Create/Read/Update/Delete Entities
   -  Batch operations
   -  Advanced Table Operations

-  Files

   -  Create/Update/Delete Shares
   -  Create/Update/Delete Directories
   -  Create/Read/Update/Delete Files
   -  Advanced File Operations

Getting Started
===============

Download
--------

Option 1: Via PyPi
~~~~~~~~~~~~~~~~~~

To install via the Python Package Index (PyPI), type:
::

    pip install azure-storage

Option 2: Source Via Git
~~~~~~~~~~~~~~~~~~~~~~~~

To get the source code of the SDK via git just type:

::

    git clone git://github.com/Azure/azure-storage-python.git
    cd ./azure-storage-python
    python setup.py install

Option 3: Source Zip
~~~~~~~~~~~~~~~~~~~~

Download a zip of the code via GitHub or PyPi. Then, type:

::

    cd ./azure-storage-python
    python setup.py install

Minimum Requirements
--------------------

-  Python 2.7, 3.3, 3.4, or 3.5.
-  See setup.py for dependencies

Usage
-----

To use this SDK to call Microsoft Azure storage services, you need to
first `create an account`_.

Code Sample
-----------

See the samples directory for blob, queue, table, and file usage samples.

Need Help?
==========

Be sure to check out the Microsoft Azure `Developer Forums on MSDN`_ or
the `Developer Forums on Stack Overflow`_ if you have trouble with the
provided code.

Contribute Code or Provide Feedback
===================================

If you would like to become an active contributor to this project, please
follow the instructions provided in `Azure Projects Contribution
Guidelines`_. You can find more details for contributing in the `CONTRIBUTING.md doc`_.

If you encounter any bugs with the library, please file an issue in the
`Issues`_ section of the project.

Learn More
==========

-  `Python Developer Center`_
-  `Azure Storage Service`_
-  `Azure Storage Team Blog`_
-  `API Reference`_

.. _Python Developer Center: http://azure.microsoft.com/en-us/develop/python/
.. _API Reference: https://azure-storage.readthedocs.io/en/latest/
.. _here: https://github.com/Azure/azure-storage-python/archive/master.zip
.. _create an account: https://account.windowsazure.com/signup
.. _Developer Forums on MSDN: http://social.msdn.microsoft.com/Forums/windowsazure/en-US/home?forum=windowsazuredata
.. _Developer Forums on Stack Overflow: http://stackoverflow.com/questions/tagged/azure+windows-azure-storage
.. _Azure Projects Contribution Guidelines: http://azure.github.io/guidelines.html
.. _Issues: https://github.com/Azure/azure-storage-python/issues
.. _Azure Storage Service: http://azure.microsoft.com/en-us/documentation/services/storage/
.. _Azure Storage Team Blog: http://blogs.msdn.com/b/windowsazurestorage/
.. _CONTRIBUTING.md doc: CONTRIBUTING.md

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