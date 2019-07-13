#
# spec file for package rh-python36-python-boto3
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name boto3

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
Version:        1.6.2
Release:        0%{?dist}
Url:            https://github.com/boto/boto3
Summary:        The AWS SDK for Python
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-nose  1.3.3
Requires:       %{?scl_prefix}python-mock = 1.3.0
Requires:       %{?scl_prefix}python-wheel = 0.24.0
# For python 2.6
#Requires:       %{?scl_prefix}python-unittest2 = 0.5.1

Requires:       %{?scl_prefix}python-botocore < 1.10.0
Requires:       %{?scl_prefix}python-botocore >= 1.9.2
Requires:       %{?scl_prefix}python-jmespath < 1.0.0
Requires:       %{?scl_prefix}python-jmespath >= 0.7.1
Requires:       %{?scl_prefix}python-s3transfer < 0.2.0
Requires:       %{?scl_prefix}python-s3transfer >= 0.1.10
%if %{with_dnf}
%endif # with_dnf

%description
===============================
Boto 3 - The AWS SDK for Python
===============================

|Build Status| |Docs| |Version| |Gitter|

Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2. You can find the latest, most
up to date, documentation at `Read the Docs`_, including a list of
services that are supported. To see only those features which have been
released, check out the `stable docs`_.


.. _boto: https://docs.pythonboto.org/
.. _`stable docs`: https://boto3.readthedocs.io/en/stable/
.. _`Read the Docs`: https://boto3.readthedocs.io/en/latest/
.. |Build Status| image:: http://img.shields.io/travis/boto/boto3/develop.svg?style=flat
    :target: https://travis-ci.org/boto/boto3
    :alt: Build Status
.. |Gitter| image:: https://badges.gitter.im/boto/boto3.svg
   :target: https://gitter.im/boto/boto3
   :alt: Gitter
.. |Docs| image:: https://readthedocs.org/projects/boto3/badge/?version=latest&style=flat
    :target: https://boto3.readthedocs.io/en/latest/
    :alt: Read the docs
.. |Downloads| image:: http://img.shields.io/pypi/dm/boto3.svg?style=flat
    :target: https://pypi.python.org/pypi/boto3/
    :alt: Downloads
.. |Version| image:: http://img.shields.io/pypi/v/boto3.svg?style=flat
    :target: https://pypi.python.org/pypi/boto3/
    :alt: Version
.. |License| image:: http://img.shields.io/pypi/l/boto3.svg?style=flat
    :target: https://github.com/boto/boto3/blob/develop/LICENSE
    :alt: License

Quick Start
-----------
First, install the library and set a default region:

.. code-block:: sh

    $ pip install boto3

Next, set up credentials (in e.g. ``~/.aws/credentials``):

.. code-block:: ini

    [default]
    aws_access_key_id = YOUR_KEY
    aws_secret_access_key = YOUR_SECRET

Then, set up a default region (in e.g. ``~/.aws/config``):

.. code-block:: ini

    [default]
    region=us-east-1

Then, from a Python interpreter:

.. code-block:: python

    >>> import boto3
    >>> s3 = boto3.resource('s3')
    >>> for bucket in s3.buckets.all():
            print(bucket.name)

Development
-----------

Getting Started
~~~~~~~~~~~~~~~
Assuming that you have Python and ``virtualenv`` installed, set up your
environment and install the required dependencies like this instead of
the ``pip install boto3`` defined above:

.. code-block:: sh

    $ git clone https://github.com/boto/boto3.git
    $ cd boto3
    $ virtualenv venv
    ...
    $ . venv/bin/activate
    $ pip install -r requirements.txt
    $ pip install -e .

Running Tests
~~~~~~~~~~~~~
You can run tests in all supported Python versions using ``tox``. By default,
it will run all of the unit and functional tests, but you can also specify your own
``nosetests`` options. Note that this requires that you have all supported
versions of Python installed, otherwise you must pass ``-e`` or run the
``nosetests`` command directly:

.. code-block:: sh

    $ tox
    $ tox -- unit/test_session.py
    $ tox -e py26,py33 -- integration/

You can also run individual tests with your default Python version:

.. code-block:: sh

    $ nosetests tests/unit

Generating Documentation
~~~~~~~~~~~~~~~~~~~~~~~~
Sphinx is used for documentation. You can generate HTML locally with the
following:

.. code-block:: sh

    $ pip install -r requirements-docs.txt
    $ cd docs
    $ make html


Getting Help
------------

We use GitHub issues for tracking bugs and feature requests and have limited
bandwidth to address them. Please use these community resources for getting
help:

* Ask a question on `Stack Overflow <https://stackoverflow.com/>`__ and tag it with `boto3 <https://stackoverflow.com/questions/tagged/boto3>`__
* Come join the AWS Python community chat on `gitter <https://gitter.im/boto/boto3>`__
* Open a support ticket with `AWS Support <https://console.aws.amazon.com/support/home#/>`__
* If it turns out that you may have found a bug, please `open an issue <https://github.com/boto/boto3/issues/new>`__

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