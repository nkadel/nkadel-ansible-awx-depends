#
# spec file for package rh-python36-python-requests-oauthlib
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name requests-oauthlib

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
Version:        1.2.0
Release:        0%{?dist}
Url:            https://github.com/requests/requests-oauthlib
Summary:        OAuthlib authentication support for Requests.
License:        ISC
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
# Manually added
Provides:       %{?scl_prefix}python-requests_oauthlib = %{version}-%{release}
Conflicts:      %{?scl_prefix}python-requests_oauthlib <= %{version}-%{release}
Obsoletes:      %{?scl_prefix}python-requests_oauthlib <= %{version}-%{release}

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Manually added
Requires:  %{?scl_prefix}python-requests >= 2.0.0
Requires:  %{?scl_prefix}python-oauthlib >= 3.0.0
%if %{with_dnf}
%endif # with_dnf

%description
Requests-OAuthlib |build-status| |coverage-status| |docs|
=========================================================

This project provides first-class OAuth library support for `Requests <http://python-requests.org>`_.

The OAuth 1 workflow
--------------------

OAuth 1 can seem overly complicated and it sure has its quirks. Luckily,
requests_oauthlib hides most of these and let you focus at the task at hand.

Accessing protected resources using requests_oauthlib is as simple as:

.. code-block:: pycon

    >>> from requests_oauthlib import OAuth1Session
    >>> twitter = OAuth1Session('client_key',
                                client_secret='client_secret',
                                resource_owner_key='resource_owner_key',
                                resource_owner_secret='resource_owner_secret')
    >>> url = 'https://api.twitter.com/1/account/settings.json'
    >>> r = twitter.get(url)

Before accessing resources you will need to obtain a few credentials from your
provider (e.g. Twitter) and authorization from the user for whom you wish to
retrieve resources for. You can read all about this in the full
`OAuth 1 workflow guide on RTD <https://requests-oauthlib.readthedocs.io/en/latest/oauth1_workflow.html>`_.

The OAuth 2 workflow
--------------------

OAuth 2 is generally simpler than OAuth 1 but comes in more flavours. The most
common being the Authorization Code Grant, also known as the WebApplication
flow.

Fetching a protected resource after obtaining an access token can be extremely
simple. However, before accessing resources you will need to obtain a few
credentials from your provider (e.g. Google) and authorization from the user
for whom you wish to retrieve resources for. You can read all about this in the
full `OAuth 2 workflow guide on RTD <https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html>`_.

Installation
-------------

To install requests and requests_oauthlib you can use pip:

.. code-block:: bash

    $ pip install requests requests_oauthlib

.. |build-status| image:: https://travis-ci.org/requests/requests-oauthlib.svg?branch=master
   :target: https://travis-ci.org/requests/requests-oauthlib
.. |coverage-status| image:: https://img.shields.io/coveralls/requests/requests-oauthlib.svg
   :target: https://coveralls.io/r/requests/requests-oauthlib
.. |docs| image:: https://readthedocs.org/projects/requests-oauthlib/badge/
   :alt: Documentation Status
   :scale: 100%
   :target: https://requests-oauthlib.readthedocs.io/


History
-------

UNRELEASED
++++++++++

nothing yet

v1.2.0 (14 January 2019)
++++++++++++++++++++++++

- This project now depends on OAuthlib 3.0.0 and above. It does **not** support
  versions of OAuthlib before 3.0.0.
- Updated oauth2 tests to use 'sess' for an OAuth2Session instance instead of `auth`
  because OAuth2Session objects and methods acceept an `auth` paramether which is
  typically an instance of `requests.auth.HTTPBasicAuth`
- `OAuth2Session.fetch_token` previously tried to guess how and where to provide
  "client" and "user" credentials incorrectly. This was incompatible with some
  OAuth servers and incompatible with breaking changes in oauthlib that seek to
  correctly provide the `client_id`. The older implementation also did not raise
  the correct exceptions when username and password are not present on Legacy
  clients.
- Avoid automatic netrc authentication for OAuth2Session.

v1.1.0 (9 January 2019)
+++++++++++++++++++++++

- Adjusted version specifier for ``oauthlib`` dependency: this project is
  not yet compatible with ``oauthlib`` 3.0.0.
- Dropped dependency on ``nose``.
- Minor changes to clean up the code and make it more readable/maintainable.

v1.0.0 (4 June 2018)
++++++++++++++++++++

- **Removed support for Python 2.6 and Python 3.3.**
  This project now supports Python 2.7, and Python 3.4 and above.
- Added several examples to the documentation.
- Added plentymarkets compliance fix.
- Added a ``token`` property to OAuth1Session, to match the corresponding
  ``token`` property on OAuth2Session.

v0.8.0 (14 February 2017)
+++++++++++++++++++++++++

- Added Fitbit compliance fix.
- Fixed an issue where newlines in the response body for the access token
  request would cause errors when trying to extract the token.
- Fixed an issue introduced in v0.7.0 where users passing ``auth`` to several
  methods would encounter conflicts with the ``client_id`` and
  ``client_secret``-derived auth. The user-supplied ``auth`` argument is now
  used in preference to those options.

v0.7.0 (22 September 2016)
++++++++++++++++++++++++++

- Allowed ``OAuth2Session.request`` to take the ``client_id`` and
  ``client_secret`` parameters for the purposes of automatic token refresh,
  which may need them.

v0.6.2 (12 July 2016)
+++++++++++++++++++++

- Use ``client_id`` and ``client_secret`` for the Authorization header if
  provided.
- Allow explicit bypass of the Authorization header by setting ``auth=False``.
- Pass through the ``proxies`` kwarg when refreshing tokens.
- Miscellaneous cleanups.

v0.6.1 (19 February 2016)
+++++++++++++++++++++++++

- Fixed a bug when sending authorization in headers with no username and
  password present.
- Make sure we clear the session token before obtaining a new one.
- Some improvements to the Slack compliance fix.
- Avoid timing problems around token refresh.
- Allow passing arbitrary arguments to requests when calling
  ``fetch_request_token`` and ``fetch_access_token``.

v0.6.0 (14 December 2015)
+++++++++++++++++++++++++

- Add compliance fix for Slack.
- Add compliance fix for Mailchimp.
- ``TokenRequestDenied`` exceptions now carry the entire response, not just the
  status code.
- Pass through keyword arguments when refreshing tokens automatically.
- Send authorization in headers, not just body, to maximize compatibility.
- More getters/setters available for OAuth2 session client values.
- Allow sending custom headers when refreshing tokens, and set some defaults.


v0.5.0 (4 May 2015)
+++++++++++++++++++
- Fix ``TypeError`` being raised instead of ``TokenMissing`` error.
- Raise requests exceptions on 4XX and 5XX responses in the OAuth2 flow.
- Avoid ``AttributeError`` when initializing the ``OAuth2Session`` class
  without complete client information.

v0.4.2 (16 October 2014)
++++++++++++++++++++++++
- New ``authorized`` property on OAuth1Session and OAuth2Session, which allows
  you to easily determine if the session is already authorized with OAuth tokens
  or not.
- New ``TokenMissing`` and ``VerifierMissing`` exception classes for OAuth1Session:
  this will make it easier to catch and identify these exceptions.

v0.4.1 (6 June 2014)
++++++++++++++++++++
- New install target ``[rsa]`` for people using OAuth1 RSA-SHA1 signature
  method.
- Fixed bug in OAuth2 where supplied state param was not used in auth url.
- OAuth2 HTTPS checking can be disabled by setting environment variable
  ``OAUTHLIB_INSECURE_TRANSPORT``.
- OAuth1 now re-authorize upon redirects.
- OAuth1 token fetching now raise a detailed error message when the
  response body is incorrectly encoded or the request was denied.
- Added support for custom OAuth1 clients.
- OAuth2 compliance fix for Sina Weibo.
- Multiple fixes to facebook compliance fix.
- Compliance fixes now re-encode body properly as bytes in Python 3.
- Logging now properly done under ``requests_oauthlib`` namespace instead
  of piggybacking on oauthlib namespace.
- Logging introduced for OAuth1 auth and session.

v0.4.0 (29 September 2013)
++++++++++++++++++++++++++
- OAuth1Session methods only return unicode strings. #55.
- Renamed requests_oauthlib.core to requests_oauthlib.oauth1_auth for consistency. #79.
- Added Facebook compliance fix and access_token_response hook to OAuth2Session. #63.
- Added LinkedIn compliance fix.
- Added refresh_token_response compliance hook, invoked before parsing the refresh token.
- Correctly limit compliance hooks to running only once!
- Content type guessing should only be done when no content type is given
- OAuth1 now updates r.headers instead of replacing it with non case insensitive dict
- Remove last use of Response.content (in OAuth1Session). #44.
- State param can now be supplied in OAuth2Session.authorize_url


%prep
%setup -q -n %{pypi_name}-%{version}

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
* Sat Jul 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.2.0-0
- Update .spec file with py2pack
- Manually add Requires for python-oauthlib and python-requests
- Add Provides for python-requests_oauthlib for pypi.org mismatched names
