#
# spec file for package rh-python36-python-python-logstash
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name python-logstash

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
Version:        0.4.6
Release:        0%{?dist}
Url:            https://github.com/vklochan/python-logstash
Summary:        Python logging handler for Logstash.
License:        UNKNOWN (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf

%description
python-logstash
===============

Python logging handler for Logstash.
http://logstash.net/

Changelog
=========
0.4.6
  - Updated field names to match java counterparts supported by logstash crew
0.4.5
  - Allow passing exchange's routing key to AMQP handler
0.4.4
  - Fixed urllib import python3 compatibility.
  - Added long type to easy_types.
0.4.3
  - Added AMQP handler.
0.4.2
  - Updated README
  - Added ``tags`` parameter to handler
0.4.1
  - Added TCP handler.
0.3.1
  - Added support for Python 3
0.2.2
  - Split Handler into Handler and Formatter classes
0.2.1
  - Added support for the new JSON schema in Logstash 1.2.x. See details in
    http://tobrunet.ch/2013/09/logstash-1-2-0-upgrade-notes-included/ and
    https://logstash.jira.com/browse/LOGSTASH-675

    - Added ``version`` parameter. Available values: 1 (Logstash 1.2.x version format), 0 - default (previous version).


Installation
============

Using pip::

  pip install python-logstash

Usage
=====

``LogstashHandler`` is a custom logging handler which sends Logstash messages using UDP.

For example::

  import logging
  import logstash
  import sys

  host = 'localhost'

  test_logger = logging.getLogger('python-logstash-logger')
  test_logger.setLevel(logging.INFO)
  test_logger.addHandler(logstash.LogstashHandler(host, 5959, version=1))
  # test_logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))

  test_logger.error('python-logstash: test logstash error message.')
  test_logger.info('python-logstash: test logstash info message.')
  test_logger.warning('python-logstash: test logstash warning message.')

  # add extra field to logstash message
  extra = {
      'test_string': 'python version: ' + repr(sys.version_info),
      'test_boolean': True,
      'test_dict': {'a': 1, 'b': 'c'},
      'test_float': 1.23,
      'test_integer': 123,
      'test_list': [1, 2, '3'],
  }
  test_logger.info('python-logstash: test extra fields', extra=extra)

When using ``extra`` field make sure you don't use reserved names. From `Python documentation <https://docs.python.org/2/library/logging.html>`_.
     | "The keys in the dictionary passed in extra should not clash with the keys used by the logging system. (See the `Formatter <https://docs.python.org/2/library/logging.html#logging.Formatter>`_ documentation for more information on which keys are used by the logging system.)"

To use the AMQPLogstashHandler you will need to install pika first.

   pip install pika

For example::

  import logging
  import logstash

  test_logger = logging.getLogger('python-logstash-logger')
  test_logger.setLevel(logging.INFO)
  test_logger.addHandler(logstash.AMQPLogstashHandler(host='localhost', version=1))

  test_logger.info('python-logstash: test logstash info message.')
  try:
      1/0
  except:
      test_logger.exception('python-logstash-logger: Exception with stack trace!')



Using with Django
=================

Modify your ``settings.py`` to integrate ``python-logstash`` with Django's logging::

  LOGGING = {
    ...
    'handlers': {
        'logstash': {
            'level': 'DEBUG',
            'class': 'logstash.LogstashHandler',
            'host': 'localhost',
            'port': 5959, # Default value: 5959
            'version': 1, # Version of logstash event schema. Default value: 0 (for backward compatibility of the library)
            'message_type': 'logstash',  # 'type' field in logstash message. Default value: 'logstash'.
            'fqdn': False, # Fully qualified domain name. Default value: false.
            'tags': ['tag1', 'tag2'], # list of tags. Default: None.
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['logstash'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    ...
  }

Note
====

Example Logstash Configuration (``logstash.conf``) for Receiving Events from python-logstash is::

  input {
    tcp {
      port => 5000
      codec => json
    }
  }
  output {
    stdout {
      codec => rubydebug
    }
  }

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