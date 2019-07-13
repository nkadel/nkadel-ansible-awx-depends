#
# spec file for package rh-python36-python-geoip2
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name geoip2

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
Version:        2.9.0
Release:        0%{?dist}
Url:            http://www.maxmind.com/
Summary:        MaxMind GeoIP2 API
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:       %{?scl_prefix}python-requests >= 2.9
Requires:       %{?scl_prefix}python-maxminddb >= 1.4.0

#[:python_version=="2.7"]
#Requires:       %{?scl_prefix}python-ipaddress
%if %{with_dnf}
%endif # with_dnf

%description
=========================
MaxMind GeoIP2 Python API
=========================

Description
-----------

This package provides an API for the GeoIP2 `web services
<http://dev.maxmind.com/geoip/geoip2/web-services>`_ and `databases
<http://dev.maxmind.com/geoip/geoip2/downloadable>`_. The API also works with
MaxMind's free `GeoLite2 databases
<http://dev.maxmind.com/geoip/geoip2/geolite2/>`_.

Installation
------------

To install the ``geoip2`` module, type:

.. code-block:: bash

    $ pip install geoip2

If you are not able to use pip, you may also use easy_install from the
source directory:

.. code-block:: bash

    $ easy_install .

Database Reader Extension
^^^^^^^^^^^^^^^^^^^^^^^^^

If you wish to use the C extension for the database reader, you must first
install the `libmaxminddb C API <https://github.com/maxmind/libmaxminddb>`_.
Please `see the instructions distributed with it
<https://github.com/maxmind/libmaxminddb/blob/master/README.md>`_.

IP Geolocation Usage
--------------------

IP geolocation is inherently imprecise. Locations are often near the center of
the population. Any location provided by a GeoIP2 database or web service
should not be used to identify a particular address or household.

Usage
-----

To use this API, you first create either a web service object with your
MaxMind ``account_id`` and ``license_key`` or a database reader object with the
path to your database file. After doing this, you may call the method
corresponding to request type (e.g., ``city`` or ``country``), passing it the
IP address you want to look up.

If the request succeeds, the method call will return a model class for the
end point you called. This model in turn contains multiple record classes,
each of which represents part of the data returned by the web service.

If the request fails, the client class throws an exception.

Web Service Example
-------------------

.. code-block:: pycon

    >>> import geoip2.webservice
    >>>
    >>> # This creates a Client object that can be reused across requests.
    >>> # Replace "42" with your account ID and "license_key" with your license
    >>> # key.
    >>> client = geoip2.webservice.Client(42, 'license_key')
    >>>
    >>> # Replace "insights" with the method corresponding to the web service
    >>> # that you are using, e.g., "country", "city".
    >>> response = client.insights('128.101.101.101')
    >>>
    >>> response.country.iso_code
    'US'
    >>> response.country.name
    'United States'
    >>> response.country.names['zh-CN']
    u'&#32654;&#22269;'
    >>>
    >>> response.subdivisions.most_specific.name
    'Minnesota'
    >>> response.subdivisions.most_specific.iso_code
    'MN'
    >>>
    >>> response.city.name
    'Minneapolis'
    >>>
    >>> response.postal.code
    '55455'
    >>>
    >>> response.location.latitude
    44.9733
    >>> response.location.longitude
    -93.2323

Web Service Client Exceptions
-----------------------------

For details on the possible errors returned by the web service itself, see
http://dev.maxmind.com/geoip/geoip2/web-services for the GeoIP2 Precision web
service docs.

If the web service returns an explicit error document, this is thrown as a
``AddressNotFoundError``, ``AuthenticationError``, ``InvalidRequestError``, or
``OutOfQueriesError`` as appropriate. These all subclass ``GeoIP2Error``.

If some other sort of error occurs, this is thrown as an ``HTTPError``. This
is thrown when some sort of unanticipated error occurs, such as the web
service returning a 500 or an invalid error document. If the web service
returns any status code besides 200, 4xx, or 5xx, this also becomes an
``HTTPError``.

Finally, if the web service returns a 200 but the body is invalid, the client
throws a ``GeoIP2Error``.

Database Example
-------------------

City Database
^^^^^^^^^^^^^

.. code-block:: pycon

    >>> import geoip2.database
    >>>
    >>> # This creates a Reader object. You should use the same object
    >>> # across multiple requests as creation of it is expensive.
    >>> reader = geoip2.database.Reader('/path/to/GeoLite2-City.mmdb')
    >>>
    >>> # Replace "city" with the method corresponding to the database
    >>> # that you are using, e.g., "country".
    >>> response = reader.city('128.101.101.101')
    >>>
    >>> response.country.iso_code
    'US'
    >>> response.country.name
    'United States'
    >>> response.country.names['zh-CN']
    u'&#32654;&#22269;'
    >>>
    >>> response.subdivisions.most_specific.name
    'Minnesota'
    >>> response.subdivisions.most_specific.iso_code
    'MN'
    >>>
    >>> response.city.name
    'Minneapolis'
    >>>
    >>> response.postal.code
    '55455'
    >>>
    >>> response.location.latitude
    44.9733
    >>> response.location.longitude
    -93.2323
    >>> reader.close()

Anonymous IP Database
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: pycon

    >>> import geoip2.database
    >>>
    >>> # This creates a Reader object. You should use the same object
    >>> # across multiple requests as creation of it is expensive.
    >>> reader = geoip2.database.Reader('/path/to/GeoIP2-Anonymous-IP.mmdb')
    >>>
    >>> response = reader.anonymous_ip('85.25.43.84')
    >>>
    >>> response.is_anonymous
    True
    >>> response.is_anonymous_vpn
    False
    >>> response.is_hosting_provider
    False
    >>> response.is_public_proxy
    False
    >>> response.is_tor_exit_node
    True
    >>> response.ip_address
    '128.101.101.101'
    >>> reader.close()

ASN Database
^^^^^^^^^^^^

.. code-block:: pycon

    >>> import geoip2.database
    >>>
    >>> # This creates a Reader object. You should use the same object
    >>> # across multiple requests as creation of it is expensive.
    >>> with geoip2.database.Reader('/path/to/GeoLite2-ASN.mmdb') as reader:
    >>>     response = reader.asn('1.128.0.0')
    >>>     response.autonomous_system_number
    1221
    >>>     response.autonomous_system_organization
    'Telstra Pty Ltd'

Connection-Type Database
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: pycon

    >>> import geoip2.database
    >>>
    >>> # This creates a Reader object. You should use the same object
    >>> # across multiple requests as creation of it is expensive.
    >>> reader = geoip2.database.Reader('/path/to/GeoIP2-Connection-Type.mmdb')
    >>>
    >>> response = reader.connection_type('128.101.101.101')
    >>>
    >>> response.connection_type
    'Corporate'
    >>> response.ip_address
    '128.101.101.101'
    >>> reader.close()


Domain Database
^^^^^^^^^^^^^^^

.. code-block:: pycon

    >>> import geoip2.database
    >>>
    >>> # This creates a Reader object. You should use the same object
    >>> # across multiple requests as creation of it is expensive.
    >>> reader = geoip2.database.Reader('/path/to/GeoIP2-Domain.mmdb')
    >>>
    >>> response = reader.domain('128.101.101.101')
    >>>
    >>> response.domain
    'umn.edu'
    >>> response.ip_address
    '128.101.101.101'
    >>> reader.close()

Enterprise Database
^^^^^^^^^^^^^^^^^^^

.. code-block:: pycon

    >>> import geoip2.database
    >>>
    >>> # This creates a Reader object. You should use the same object
    >>> # across multiple requests as creation of it is expensive.
    >>> with geoip2.database.Reader('/path/to/GeoIP2-Enterprise.mmdb') as reader:
    >>>
    >>>     # Use the .enterprise method to do a lookup in the Enterprise database
    >>>     response = reader.enterprise('128.101.101.101')
    >>>
    >>>     response.country.confidence
    99
    >>>     response.country.iso_code
    'US'
    >>>     response.country.name
    'United States'
    >>>     response.country.names['zh-CN']
    u'&#32654;&#22269;'
    >>>
    >>>     response.subdivisions.most_specific.name
    'Minnesota'
    >>>     response.subdivisions.most_specific.iso_code
    'MN'
    >>>     response.subdivisions.most_specific.confidence
    77
    >>>
    >>>     response.city.name
    'Minneapolis'
    >>>     response.country.confidence
    11
    >>>
    >>>     response.postal.code
    '55455'
    >>>
    >>>     response.location.accuracy_radius
    50
    >>>     response.location.latitude
    44.9733
    >>>     response.location.longitude
    -93.2323

ISP Database
^^^^^^^^^^^^

.. code-block:: pycon

    >>> import geoip2.database
    >>>
    >>> # This creates a Reader object. You should use the same object
    >>> # across multiple requests as creation of it is expensive.
    >>> reader = geoip2.database.Reader('/path/to/GeoIP2-ISP.mmdb')
    >>>
    >>> response = reader.isp('1.128.0.0')
    >>>
    >>> response.autonomous_system_number
    1221
    >>> response.autonomous_system_organization
    'Telstra Pty Ltd'
    >>> response.isp
    'Telstra Internet'
    >>> response.organization
    'Telstra Internet'
    >>> response.ip_address
    '128.101.101.101'
    >>> reader.close()

Database Reader Exceptions
--------------------------

If the database file does not exist or is not readable, the constructor will
raise a ``FileNotFoundError`` on Python 3 or an ``IOError`` on Python 2.
If the IP address passed to a method is invalid, a ``ValueError`` will be
raised. If the file is invalid or there is a bug in the reader, a
``maxminddb.InvalidDatabaseError`` will be raised with a description of the
problem. If an IP address is not in the database, a ``AddressNotFoundError``
will be raised.

Values to use for Database or Dictionary Keys
---------------------------------------------

**We strongly discourage you from using a value from any ``names`` property as
a key in a database or dictionaries.**

These names may change between releases. Instead we recommend using one of the
following:

* ``geoip2.records.City`` - ``city.geoname_id``
* ``geoip2.records.Continent`` - ``continent.code`` or ``continent.geoname_id``
* ``geoip2.records.Country`` and ``geoip2.records.RepresentedCountry`` - ``country.iso_code`` or ``country.geoname_id``
* ``geoip2.records.subdivision`` - ``subdivision.iso_code`` or ``subdivision.geoname_id``

What data is returned?
----------------------

While many of the models contain the same basic records, the attributes which
can be populated vary between web service end points or databases. In
addition, while a model may offer a particular piece of data, MaxMind does not
always have every piece of data for any given IP address.

Because of these factors, it is possible for any request to return a record
where some or all of the attributes are unpopulated.

The only piece of data which is always returned is the ``ip_address``
attribute in the ``geoip2.records.Traits`` record.

Integration with GeoNames
-------------------------

`GeoNames <http://www.geonames.org/>`_ offers web services and downloadable
databases with data on geographical features around the world, including
populated places. They offer both free and paid premium data. Each feature is
uniquely identified by a ``geoname_id``, which is an integer.

Many of the records returned by the GeoIP web services and databases include a
``geoname_id`` field. This is the ID of a geographical feature (city, region,
country, etc.) in the GeoNames database.

Some of the data that MaxMind provides is also sourced from GeoNames. We
source things like place names, ISO codes, and other similar data from the
GeoNames premium data set.

Reporting Data Problems
-----------------------

If the problem you find is that an IP address is incorrectly mapped, please
`submit your correction to MaxMind <http://www.maxmind.com/en/correction>`_.

If you find some other sort of mistake, like an incorrect spelling, please
check the `GeoNames site <http://www.geonames.org/>`_ first. Once you've
searched for a place and found it on the GeoNames map view, there are a
number of links you can use to correct data ("move", "edit", "alternate
names", etc.). Once the correction is part of the GeoNames data set, it
will be automatically incorporated into future MaxMind releases.

If you are a paying MaxMind customer and you're not sure where to submit a
correction, please `contact MaxMind support
<http://www.maxmind.com/en/support>`_ for help.

Requirements
------------

This code requires Python 2.7+ or 3.3+. Older versions are not supported.
This library has been tested with CPython and PyPy.

The Requests HTTP library is also required. See
<http://python-requests.org> for details.

Versioning
----------

The GeoIP2 Python API uses `Semantic Versioning <http://semver.org/>`_.

Support
-------

Please report all issues with this code using the `GitHub issue tracker
<https://github.com/maxmind/GeoIP2-python/issues>`_

If you are having an issue with a MaxMind service that is not specific to the
client API, please contact `MaxMind support
<http://www.maxmind.com/en/support>`_ for assistance.


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
* Sat Jul 13 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.9.0-0
- Update .spec from py2pack
- Manually add Requires and Suggests
