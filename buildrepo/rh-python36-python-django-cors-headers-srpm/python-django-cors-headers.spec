#
# spec file for package rh-python36-python-django-cors-headers
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name django-cors-headers

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
Version:        2.4.0
Release:        0%{?dist}
Url:            https://github.com/ottoyiu/django-cors-headers
Summary:        django-cors-headers is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).
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
django-cors-headers
===================

A Django App that adds CORS (Cross-Origin Resource Sharing) headers to
responses.

Although JSON-P is useful, it is strictly limited to GET requests. CORS
builds on top of ``XmlHttpRequest`` to allow developers to make cross-domain
requests, similar to same-domain requests. Read more about it here:
http://www.html5rocks.com/en/tutorials/cors/

.. image:: https://travis-ci.org/ottoyiu/django-cors-headers.svg?branch=master
   :target: https://travis-ci.org/ottoyiu/django-cors-headers


Requirements
------------

Tested with all combinations of:

* Python: 2.7, 3.6
* Django: 1.8, 1.9, 1.10, 1.11, 2.0

Setup
-----

Install from **pip**:

.. code-block:: sh

    pip install django-cors-headers

and then add it to your installed apps:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'corsheaders',
        ...
    )

You will also need to add a middleware class to listen in on responses:

.. code-block:: python

    MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
        ...
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    ]

``CorsMiddleware`` should be placed as high as possible, especially before any
middleware that can generate responses such as Django's ``CommonMiddleware`` or
Whitenoise's ``WhiteNoiseMiddleware``. If it is not before, it will not be able
to add the CORS headers to these responses.

Also if you are using ``CORS_REPLACE_HTTPS_REFERER`` it should be placed before
Django's ``CsrfViewMiddleware`` (see more below).

Configuration
-------------

Configure the middleware's behaviour in your Django settings. You must add the
hosts that are allowed to do cross-site requests to
``CORS_ORIGIN_WHITELIST``, or set ``CORS_ORIGIN_ALLOW_ALL`` to ``True``
to allow all hosts.

``CORS_ORIGIN_ALLOW_ALL``
~~~~~~~~~~~~~~~~~~~~~~~~~
If ``True``, the whitelist will not be used and all origins will be accepted.
Defaults to ``False``.

``CORS_ORIGIN_WHITELIST``
~~~~~~~~~~~~~~~~~~~~~~~~~

A list of origin hostnames that are authorized to make cross-site HTTP
requests. The value ``'null'`` can also appear in this list, and will match the
``Origin: null`` header that is used in `"privacy-sensitive contexts"
<https://tools.ietf.org/html/rfc6454#section-6>`_, such as when the client is
running from a ``file://`` domain. Defaults to ``[]``.

Example:

.. code-block:: python

    CORS_ORIGIN_WHITELIST = (
        'google.com',
        'hostname.example.com',
        'localhost:8000',
        '127.0.0.1:9000'
    )


``CORS_ORIGIN_REGEX_WHITELIST``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A list of regexes that match origin regex list of origin hostnames that are
authorized to make cross-site HTTP requests. Defaults to ``[]``. Useful when
``CORS_ORIGIN_WHITELIST`` is impractical, such as when you have a large
number of subdomains.

Example:

.. code-block:: python

    CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?(\w+\.)?google\.com$', )

--------------

The following are optional settings, for which the defaults probably suffice.

``CORS_URLS_REGEX``
~~~~~~~~~~~~~~~~~~~

A regex which restricts the URL's for which the CORS headers will be sent.
Defaults to ``r'^.*$'``, i.e. match all URL's. Useful when you only need CORS
on a part of your site, e.g. an API at ``/api/``.

Example:

.. code-block:: python

    CORS_URLS_REGEX = r'^/api/.*$'

``CORS_ALLOW_METHODS``
~~~~~~~~~~~~~~~~~~~~~~

A list of HTTP verbs that are allowed for the actual request. Defaults to:

.. code-block:: python

    CORS_ALLOW_METHODS = (
        'DELETE',
        'GET',
        'OPTIONS',
        'PATCH',
        'POST',
        'PUT',
    )

The default can be imported as ``corsheaders.defaults.default_methods`` so you
can just extend it with your custom methods. This allows you to keep up to date
with any future changes. For example:

.. code-block:: python

    from corsheaders.defaults import default_methods

    CORS_ALLOW_METHODS = default_methods + (
        'POKE',
    )

``CORS_ALLOW_HEADERS``
~~~~~~~~~~~~~~~~~~~~~~

The list of non-standard HTTP headers that can be used when making the actual
request. Defaults to:

.. code-block:: python

    CORS_ALLOW_HEADERS = (
        'accept',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
    )

The default can be imported as ``corsheaders.defaults.default_headers`` so you
can extend it with your custom headers. This allows you to keep up to date with
any future changes. For example:

.. code-block:: python

    from corsheaders.defaults import default_headers

    CORS_ALLOW_HEADERS = default_headers + (
        'my-custom-header',
    )

``CORS_EXPOSE_HEADERS``
~~~~~~~~~~~~~~~~~~~~~~~

The list of HTTP headers that are to be exposed to the browser. Defaults to
``[]``.


``CORS_PREFLIGHT_MAX_AGE``
~~~~~~~~~~~~~~~~~~~~~~~~~~

The number of seconds a client/browser can cache the preflight response. If
this is 0 (or any falsey value), no max age header will be sent. Defaults to
``86400`` (one day).


**Note:** A preflight request is an extra request that is made when making a
"not-so-simple" request (e.g. ``Content-Type`` is not
``application/x-www-form-urlencoded``) to determine what requests the server
actually accepts. Read more about it in the `HTML 5 Rocks CORS tutorial
<https://www.html5rocks.com/en/tutorials/cors/>`_.

``CORS_ALLOW_CREDENTIALS``
~~~~~~~~~~~~~~~~~~~~~~~~~~

If ``True``, cookies will be allowed to be included in cross-site HTTP
requests. Defaults to ``False``.

``CORS_MODEL``
~~~~~~~~~~~~~~

If set, this should be the path to a model to look up allowed origins, in the
form ``app.modelname``. Defaults to ``None``.

The model should inherit from ``corsheaders.models.AbstractCorsModel`` and specify
the allowed origin in the ``CharField`` called ``cors``.

CSRF Integration
----------------

Most sites will need to take advantage of the `Cross-Site Request Forgery
protection <https://docs.djangoproject.com/en/dev/ref/csrf/>`_ that Django
offers. CORS and CSRF are separate, and Django has no way of using your CORS
configuration to exempt sites from the ``Referer`` checking that it does on
secure requests. The way to do that is with its `CSRF_TRUSTED_ORIGINS setting
<https://docs.djangoproject.com/en/dev/ref/settings/#csrf-trusted-origins>`_.
For example:

.. code-block:: python

    CORS_ORIGIN_WHITELIST = (
        'read.only.com',
        'change.allowed.com',
    )

    CSRF_TRUSTED_ORIGINS = (
        'change.allowed.com',
    )

``CORS_REPLACE_HTTPS_REFERER``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``CSRF_TRUSTED_ORIGINS`` was introduced in Django 1.9, so users of earlier
versions will need an alternate solution. If ``CORS_REPLACE_HTTPS_REFERER`` is
``True``, ``CorsMiddleware`` will change the ``Referer`` header to something
that will pass Django's CSRF checks whenever the CORS checks pass. Defaults to
``False``.

Note that unlike ``CSRF_TRUSTED_ORIGINS``, this setting does not allow you to
distinguish between domains that are trusted to *read* resources by CORS and
domains that are trusted to *change* resources by avoiding CSRF protection.

With this feature enabled you should also add
``corsheaders.middleware.CorsPostCsrfMiddleware`` after
``django.middleware.csrf.CsrfViewMiddleware`` in your ``MIDDLEWARE_CLASSES`` to
undo the ``Referer`` replacement:

.. code-block:: python

    MIDDLEWARE_CLASSES = [
        ...
        'corsheaders.middleware.CorsMiddleware',
        ...
        'django.middleware.csrf.CsrfViewMiddleware',
        'corsheaders.middleware.CorsPostCsrfMiddleware',
        ...
    ]

Signals
-------

If you have a use case that requires more than just the above configuration,
you can attach code to check if a given request should be allowed. For example,
this can be used to read the list of origins you allow from a model. Attach any
number of handlers to the ``check_request_enabled``
`Django signal <https://docs.djangoproject.com/en/1.10/ref/signals/>`_, which
provides the ``request`` argument (use ``**kwargs`` in your handler to protect
against any future arguments being added). If any handler attached to the
signal returns a truthy value, the request will be allowed.

For example you might define a handler like this:

.. code-block:: python

    # myapp/handlers.py
    from corsheaders.signals import check_request_enabled

    from .models import MySite

    def cors_allow_mysites(sender, request, **kwargs):
        return MySite.objects.filter(host=request.host).exists()

    check_request_enabled.connect(cors_allow_mysites)

Then connect it at app ready time using a `Django AppConfig
<https://docs.djangoproject.com/en/1.10/ref/applications/>`_:

.. code-block:: python

    # myapp/__init__.py

    default_app_config = 'myapp.apps.MyAppConfig'

.. code-block:: python

    # myapp/apps.py

    from django.apps import AppConfig

    class MyAppConfig(AppConfig):
        name = 'myapp'

        def ready(self):
            # Makes sure all signal handlers are connected
            from . import handlers  # noqa


A common use case for the signal is to allow *all* origins to access a subset
of URL's, whilst allowing a normal set of origins to access *all* URL's. This
isn't possible using just the normal configuration, but it can be achieved with
a signal handler.

First set ``CORS_ORIGIN_WHITELIST`` to the list of trusted origins that are
allowed to access every URL, and then add a handler to
``check_request_enabled`` to allow CORS regardless of the origin for the
unrestricted URL's. For example:

.. code-block:: python

    # myapp/handlers.py
    from corsheaders.signals import check_request_enabled

    def cors_allow_api_to_everyone(sender, request, **kwargs):
        return request.path.startswith('/api/')

    check_request_enabled.connect(cors_allow_api_to_everyone)

Credits
-------

``django-cors-headers`` was created by Otto Yiu (`@ottoyiu
<https://github.com/ottoyiu>`_) and has been worked on by `25+ contributors
<https://github.com/ottoyiu/django-cors-headers/graphs/contributors>`_.
Thanks to every contributor, and if you want to get involved please don't
hesitate to make a pull request.


History
=======

Pending
-------

.. Insert new release notes below this line

2.4.0 (2018-07-18)
------------------

* Always add 'Origin' to the 'Vary' header for responses to enabled URL's,
  to prevent caching of responses intended for one origin being served for
  another.

2.3.0 (2018-06-27)
------------------

* Match ``CORS_URLS_REGEX`` to ``request.path_info`` instead of
  ``request.path``, so the patterns can work without knowing the site's path
  prefix at configuration time.

2.2.1 (2018-06-27)
------------------

* Add ``Content-Length`` header to CORS preflight requests. This fixes issues
  with some HTTP proxies and servers, e.g. AWS Elastic Beanstalk.

2.2.0 (2018-02-28)
------------------

* Django 2.0 compatibility. Again there were no changes to the actual library
  code, so previous versions probably work.
* Ensured that ``request._cors_enabled`` is always a ``bool()`` - previously it
  could be set to a regex match object.

2.1.0 (2017-05-28)
------------------

* Django 1.11 compatibility. There were no changes to the actual library code,
  so previous versions probably work, though they weren't properly tested on
  1.11.

2.0.2 (2017-02-06)
------------------

* Fix when the check for ``CORS_MODEL`` is done to allow it to properly add
  the headers and respond to ``OPTIONS`` requests.

2.0.1 (2017-01-29)
------------------

* Add support for specifying 'null' in ``CORS_ORIGIN_WHITELIST``.

2.0.0 (2017-01-07)
------------------

* Remove previously undocumented ``CorsModel`` as it was causing migration
  issues. For backwards compatibility, any users previously using ``CorsModel``
  should create a model in their own app that inherits from the new
  ``AbstractCorsModel``, and to keep using the same data, set the model's
  ``db_table`` to 'corsheaders_corsmodel'. Users not using ``CorsModel``
  will find they have an unused table that they can drop.
* Make sure that ``Access-Control-Allow-Credentials`` is in the response if the
  client asks for it.

1.3.1 (2016-11-09)
------------------

* Fix a bug with the single check if CORS enabled added in 1.3.0: on Django
  < 1.10 shortcut responses could be generated by middleware above
  ``CorsMiddleware``, before it processed the request, failing with an
  ``AttributeError`` for ``request._cors_enabled``. Also clarified the docs
  that ``CorsMiddleware`` should be kept as high as possible in your middleware
  stack, above any middleware that can generate such responses.

1.3.0 (2016-11-06)
------------------

* Add checks to validate the types of the settings.
* Add the 'Do Not Track' header ``'DNT'`` to the default for
  ``CORS_ALLOW_HEADERS``.
* Add 'Origin' to the 'Vary' header of outgoing requests when not allowing all
  origins, as per the CORS spec. Note this changes the way HTTP caching works
  with your CORS-enabled responses.
* Check whether CORS should be enabled on a request only once. This has had a
  minor change on the conditions where any custom signals will be called -
  signals will now always be called *before* ``HTTP_REFERER`` gets replaced,
  whereas before they could be called before and after. Also this attaches the
  attribute ``_cors_enabled`` to ``request`` - please take care that other
  code you're running does not remove it.

1.2.2 (2016-10-05)
------------------

* Add ``CorsModel.__str__`` for human-readable text
* Add a signal that allows you to add code for more intricate control over when
  CORS headers are added.

1.2.1 (2016-09-30)
------------------

* Made settings dynamically respond to changes, and which allows you to import
  the defaults for headers and methods in order to extend them.

1.2.0 (2016-09-28)
------------------

* Drop Python 2.6 support.
* Drop Django 1.3-1.7 support, as they are no longer supported.
* Confirmed Django 1.9 support (no changes outside of tests were necessary).
* Added Django 1.10 support.
* Package as a universal wheel.

1.1.0 (2014-12-15)
------------------

* django-cors-header now supports Django 1.8 with its new application loading
  system! Thanks @jpadilla for making this possible and sorry for the delay in
  making a release.

1.0.0 (2014-12-13)
------------------

django-cors-headers is all grown-up :) Since it's been used in production for
many many deployments, I think it's time we mark this as a stable release.

* Switching this middleware versioning over to semantic versioning
* #46 add user-agent and accept-encoding default headers
* #45 pep-8 this big boy up

0.13 (2014-08-14)
-----------------

* Add support for Python 3
* Updated tests
* Improved docuemntation
* Small bugfixes

0.12 (2013-09-24)
-----------------

* Added an option to selectively enable CORS only for specific URLs

0.11 (2013-09-24)

* Added the ability to specify a regex for whitelisting many origin hostnames
  at once

0.10 (2013-09-05)
-----------------

* Introduced port distinction for origin checking
* Use ``urlparse`` for Python 3 support
* Added testcases to project

0.06 (2013-02-18)
-----------------

* Add support for exposed response headers

0.05 (2013-01-26)
-----------------

* Fixed middleware to ensure correct response for CORS preflight requests

0.04 (2013-01-25)
-----------------

* Add ``Access-Control-Allow-Credentials`` control to simple requests

0.03 (2013-01-22)
-----------------

* Bugfix to repair mismatched default variable names

0.02 (2013-01-19)
-----------------

* Refactor/pull defaults into separate file

0.01 (2013-01-19)
-----------------

* Initial release


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