#
# Makefile - build wrapper for ansible and awx needed packages
#

#REPOBASE=http://localhost
REPOBASE=file://$(PWD)

REPOS+=dependsrepo/el/7

REPODIRS := $(patsubst %,%/x86_64/repodata,$(REPOS)) $(patsubst %,%/SRPMS/repodata,$(REPOS))

CFGS+=dependsrepo-7-x86_64.cfg
CFGS+=sclpy36-7-x86_64.cfg

# Link from /etc/mock
MOCKCFGS+=epel-7-x86_64.cfg

all:: $(CFGS)
all:: $(MOCKCFGS)
all:: $(REPODIRS)
all:: $(DEPENDSPKGS)

all build getsrc srpm:: /etc/rpm/macros.scl
getsrc:: /usr/bin/spectool

all:: *srpm

# Build and getsrc for locacl OS require scl-utils

build getsrc srpm install clean::
	@for name in *srpm; do \
	    (cd $$name && $(MAKE) $(MFLAGS) $@) || \
		echo Failed: $@ && echo; \
	done  

# Assemple dependencies from Requires: and BuildRequires: in .spec files
# The case of some modules, and number of "python-" in their names, is variable
rh-python36-Cython-srpm::	rh-python36-python-coverage-srpm
rh-python36-Cython-srpm::	rh-python36-python-jedi-srpm
rh-python36-python-Automat-srpm::	rh-python36-python-attrs-srpm
rh-python36-python-Automat-srpm::	rh-python36-python-m2r-srpm
rh-python36-python-Automat-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-Automat-srpm::	rh-python36-python-six-srpm
rh-python36-python-Django-srpm::	rh-python36-python-Pillow-srpm
rh-python36-python-Django-srpm::	rh-python36-python-PyYAML-srpm
rh-python36-python-Django-srpm::	rh-python36-python-argon2-cffi-srpm
rh-python36-python-Django-srpm::	rh-python36-python-bcrypt-srpm
rh-python36-python-Django-srpm::	rh-python36-python-geoip2-srpm
rh-python36-python-Django-srpm::	rh-python36-python-pylibmc-srpm
rh-python36-python-Django-srpm::	rh-python36-python-python-memcached-srpm
rh-python36-python-Django-srpm::	rh-python36-python-pytz-srpm
rh-python36-python-Django-srpm::	rh-python36-python-selenium-srpm
rh-python36-python-Django-srpm::	rh-python36-python-sqlparse-srpm
rh-python36-python-Django-srpm::	rh-python36-python-tblib-srpm
rh-python36-python-PyNaCl-srpm::	rh-python36-python-cffi-srpm
rh-python36-python-PyNaCl-srpm::	rh-python36-python-six-srpm
rh-python36-python-SecretStorage-srpm::	rh-python36-dbus-python-srpm
rh-python36-python-SecretStorage-srpm::	rh-python36-python-cryptography-srpm
rh-python36-python-Twisted-srpm::	rh-python36-python-incremental-srpm
rh-python36-python-amqp-srpm::	rh-python36-python-vine-srpm
rh-python36-python-ansible-runner-srpm::	rh-python36-python-PyYAML-srpm
rh-python36-python-ansible-runner-srpm::	rh-python36-python-pexpect-srpm
rh-python36-python-ansible-runner-srpm::	rh-python36-python-psutil-srpm
rh-python36-python-ansible-runner-srpm::	rh-python36-python-python-daemon-srpm
rh-python36-python-ansible-runner-srpm::	rh-python36-python-six-srpm
rh-python36-python-ansible-srpm::	rh-python36-python-PyYAML-srpm
rh-python36-python-ansible-srpm::	rh-python36-python-cryptography-srpm
rh-python36-python-ansible-srpm::	rh-python36-python-paramiko-srpm
rh-python36-python-apache-libcloud-srpm::	rh-python36-python-pytest-runner-srpm
rh-python36-python-argon2-cffi-srpm::	rh-python36-python-cffi-srpm
rh-python36-python-argon2-cffi-srpm::	rh-python36-python-six-srpm
rh-python36-python-asgi_amqp-srpm::	rh-python36-python-asgiref-srpm
rh-python36-python-asgi_amqp-srpm::	rh-python36-python-jsonpickle-srpm
rh-python36-python-asgi_amqp-srpm::	rh-python36-python-kombu-srpm
rh-python36-python-asgi_amqp-srpm::	rh-python36-python-msgpack-python-srpm
rh-python36-python-asgi_amqp-srpm::	rh-python36-python-six-srpm
rh-python36-python-azure-cli-nspkg-srpm::	rh-python36-python-azure-nspkg-srpm
rh-python36-python-azure-keyvault-srpm::	rh-python36-python-azure-common-srpm
rh-python36-python-azure-keyvault-srpm::	rh-python36-python-cryptography-srpm
rh-python36-python-azure-keyvault-srpm::	rh-python36-python-msrest-srpm
rh-python36-python-azure-keyvault-srpm::	rh-python36-python-msrestazure-srpm
rh-python36-python-azure-keyvault-srpm::	rh-python36-python-requests-srpm
rh-python36-python-azure-mgmt-batch-srpm::	rh-python36-python-azure-common-srpm
rh-python36-python-azure-mgmt-batch-srpm::	rh-python36-python-msrestazure-srpm
rh-python36-python-baron-srpm::	rh-python36-python-pandoc-srpm
rh-python36-python-baron-srpm::	rh-python36-python-ply-srpm
rh-python36-python-baron-srpm::	rh-python36-python-pypandoc-srpm
rh-python36-python-baron-srpm::	rh-python36-python-rply-srpm
rh-python36-python-bcrypt-srpm::	rh-python36-python-cffi-srpm
rh-python36-python-bcrypt-srpm::	rh-python36-python-six-srpm
rh-python36-python-boto3-srpm::	rh-python36-python-botocore-srpm
rh-python36-python-boto3-srpm::	rh-python36-python-jmespath-srpm
rh-python36-python-boto3-srpm::	rh-python36-python-mock-srpm
rh-python36-python-boto3-srpm::	rh-python36-python-s3transfer-srpm
rh-python36-python-botocore-srpm::	rh-python36-python-jmespath-srpm
rh-python36-python-botocore-srpm::	rh-python36-python-mock-srpm
rh-python36-python-botocore-srpm::	rh-python36-python-python-dateutil-srpm
rh-python36-python-botocore-srpm::	rh-python36-python-tox-srpm
rh-python36-python-celery-srpm::	rh-python36-python-billiard-srpm
rh-python36-python-celery-srpm::	rh-python36-python-kombu-srpm
rh-python36-python-celery-srpm::	rh-python36-python-pytz-srpm
rh-python36-python-cffi-srpm::	rh-python36-python-pycparser-srpm
rh-python36-python-channels-srpm::	rh-python36-python-Django-srpm
rh-python36-python-channels-srpm::	rh-python36-python-asgiref-srpm
rh-python36-python-channels-srpm::	rh-python36-python-daphne-srpm
rh-python36-python-cryptography-srpm::	rh-python36-python-asn1crypto-srpm
rh-python36-python-cryptography-srpm::	rh-python36-python-cffi-srpm
rh-python36-python-cryptography-srpm::	rh-python36-python-idna-srpm
rh-python36-python-cryptography-srpm::	rh-python36-python-pycparser-srpm
rh-python36-python-cryptography-srpm::	rh-python36-python-six-srpm
rh-python36-python-daemon-srpm::	rh-python36-python-lockfile-srpm
rh-python36-python-daphne-srpm::	rh-python36-python-Twisted-srpm
rh-python36-python-daphne-srpm::	rh-python36-python-asgiref-srpm
rh-python36-python-daphne-srpm::	rh-python36-python-autobahn-srpm
rh-python36-python-django-auth-ldap-srpm::	rh-python36-python-Django-srpm
rh-python36-python-django-auth-ldap-srpm::	rh-python36-python-python-ldap-srpm
rh-python36-python-django-crum-srpm::	rh-python36-python-Django-srpm
rh-python36-python-django-crum-srpm::	rh-python36-python-pytest-runner-srpm
rh-python36-python-django-extensions-srpm::	rh-python36-python-six-srpm
rh-python36-python-django-extensions-srpm::	rh-python36-python-typing-srpm
rh-python36-python-django-jsonbfield-srpm::	rh-python36-python-Django-srpm
rh-python36-python-django-jsonbfield-srpm::	rh-python36-python-psycopg2-srpm
rh-python36-python-django-oauth-toolkit-srpm::	rh-python36-python-Django-srpm
rh-python36-python-django-oauth-toolkit-srpm::	rh-python36-python-oauthlib-srpm
rh-python36-python-django-oauth-toolkit-srpm::	rh-python36-python-requests-srpm
rh-python36-python-django-polymorphic-srpm::	rh-python36-python-Django-srpm
rh-python36-python-django-qsstats-magic-srpm::	rh-python36-python-python-dateutil-srpm
rh-python36-python-django-radius-srpm::	rh-python36-python-future-srpm
rh-python36-python-django-radius-srpm::	rh-python36-python-pyrad-srpm
rh-python36-python-django-split-settings-srpm::	rh-python36-python-pytest-runner-srpm
rh-python36-python-django-taggit-srpm::	rh-python36-python-isort-srpm
rh-python36-python-djangorestframework-yaml-srpm::	rh-python36-python-PyYAML-srpm
rh-python36-python-geoip2-srpm::	rh-python36-python-maxminddb-srpm
rh-python36-python-geoip2-srpm::	rh-python36-python-requests-srpm
rh-python36-python-irc-srpm::	rh-python36-python-jaraco.collections-srpm
rh-python36-python-irc-srpm::	rh-python36-python-jaraco.functools-srpm
rh-python36-python-irc-srpm::	rh-python36-python-jaraco.itertools-srpm
rh-python36-python-irc-srpm::	rh-python36-python-jaraco.logging-srpm
rh-python36-python-irc-srpm::	rh-python36-python-jaraco.stream-srpm
rh-python36-python-irc-srpm::	rh-python36-python-jaraco.text-srpm
rh-python36-python-irc-srpm::	rh-python36-python-more-itertools-srpm
rh-python36-python-irc-srpm::	rh-python36-python-pytz-srpm
rh-python36-python-irc-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-irc-srpm::	rh-python36-python-six-srpm
rh-python36-python-irc-srpm::	rh-python36-python-tempora-srpm
rh-python36-python-isodate-srpm::	rh-python36-python-six-srpm
rh-python36-python-jaraco.classes-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.classes-srpm::	rh-python36-python-six-srpm
rh-python36-python-jaraco.collections-srpm::	rh-python36-python-jaraco.classes-srpm
rh-python36-python-jaraco.collections-srpm::	rh-python36-python-jaraco.text-srpm
rh-python36-python-jaraco.collections-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.collections-srpm::	rh-python36-python-six-srpm
rh-python36-python-jaraco.functools-srpm::	rh-python36-python-more-itertools-srpm
rh-python36-python-jaraco.functools-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.itertools-srpm::	rh-python36-python-inflect-srpm
rh-python36-python-jaraco.itertools-srpm::	rh-python36-python-more-itertools-srpm
rh-python36-python-jaraco.itertools-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.itertools-srpm::	rh-python36-python-six-srpm
rh-python36-python-jaraco.logging-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.logging-srpm::	rh-python36-python-six-srpm
rh-python36-python-jaraco.logging-srpm::	rh-python36-python-tempora-srpm
rh-python36-python-jaraco.packaging-srpm::	rh-python36-python-six-srpm
rh-python36-python-jaraco.stream-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.stream-srpm::	rh-python36-python-six-srpm
rh-python36-python-jaraco.text-srpm::	rh-python36-python-jaraco.collections-srpm
rh-python36-python-jaraco.text-srpm::	rh-python36-python-jaraco.functools-srpm
rh-python36-python-jaraco.text-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-jsonpatch-srpm::	rh-python36-python-jsonpointer-srpm
rh-python36-python-jsonschema-srpm::	rh-python36-python-vcversioner-srpm
rh-python36-python-keyring-srpm::	rh-python36-python-SecretStorage-srpm
rh-python36-python-keyring-srpm::	rh-python36-python-entrypoints-srpm
rh-python36-python-keyring-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-keystoneauth1-srpm::	rh-python36-python-iso8601-srpm
rh-python36-python-keystoneauth1-srpm::	rh-python36-python-pbr-srpm
rh-python36-python-keystoneauth1-srpm::	rh-python36-python-requests-srpm
rh-python36-python-keystoneauth1-srpm::	rh-python36-python-six-srpm
rh-python36-python-keystoneauth1-srpm::	rh-python36-python-stevedore-srpm
rh-python36-python-kombu-srpm::	rh-python36-python-amqp-srpm
rh-python36-python-lockfile-srpm::	rh-python36-python-pbr-srpm
rh-python36-python-lxml-srpm::	rh-python36-Cython-srpm
rh-python36-python-m2r-srpm::	rh-python36-python-mistune-srpm
rh-python36-python-more-itertools-srpm::	rh-python36-python-six-srpm
rh-python36-python-msest-srpm::	rh-python36-python-certifi-srpm
rh-python36-python-msest-srpm::	rh-python36-python-isodate-srpm
rh-python36-python-msest-srpm::	rh-python36-python-requests-oauthlib-srpm
rh-python36-python-msest-srpm::	rh-python36-python-requests-srpm
rh-python36-python-msrestazure-srpm::	rh-python36-python-adal-srpm
rh-python36-python-msrestazure-srpm::	rh-python36-python-keyring-srpm
rh-python36-python-msrestazure-srpm::	rh-python36-python-msrest-srpm
rh-python36-python-openstacksdk-srpm::	rh-python36-python-pbr-srpm
rh-python36-python-os-client-config-srpm::	rh-python36-python-PyYAML-srpm
rh-python36-python-os-client-config-srpm::	rh-python36-python-appdirs-srpm
rh-python36-python-os-client-config-srpm::	rh-python36-python-keystoneauth1-srpm
rh-python36-python-os-client-config-srpm::	rh-python36-python-pbr-srpm
rh-python36-python-os-client-config-srpm::	rh-python36-python-requestsexceptions-srpm
rh-python36-python-os-service-types-srpm::	rh-python36-python-pbr-srpm
rh-python36-python-ovirt-engine-sdk-python-srpm::	rh-python36-python-pycurl-srpm
rh-python36-python-ovirt-engine-sdk-python-srpm::	rh-python36-python-six-srpm
rh-python36-python-packaging-srpm::	rh-python36-python-pyparsing-srpm
rh-python36-python-packaging-srpm::	rh-python36-python-six-srpm
rh-python36-python-pandoc-srpm::	rh-python36-python-ply-srpm
rh-python36-python-paramiko-srpm::	rh-python36-python-PyNaCl-srpm
rh-python36-python-paramiko-srpm::	rh-python36-python-bcrypt-srpm
rh-python36-python-paramiko-srpm::	rh-python36-python-cryptography-srpm
rh-python36-python-paramiko-srpm::	rh-python36-python-pyasn1-srpm
rh-python36-python-pexpect-srpm::	rh-python36-python-ptyprocess-srpm
rh-python36-python-py-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-pyOpenSSL-srpm::	rh-python36-python-cryptography-srpm
rh-python36-python-pyOpenSSL-srpm::	rh-python36-python-six-srpm
rh-python36-python-pyasn1-modules-srpm::	rh-python36-python-pyasn1-srpm
rh-python36-python-pycurl-srpm::	rh-python36-python-bottle-srpm
rh-python36-python-pycurl-srpm::	rh-python36-python-nose-show-skipped-srpm
rh-python36-python-pycurl-srpm::	rh-python36-python-pyflakes-srpm
rh-python36-python-pygerduty-srpm::	rh-python36-python-six-srpm
rh-python36-python-pyrad-srpm::	rh-python36-python-netaddr-srpm
rh-python36-python-pyrad-srpm::	rh-python36-python-six-srpm
rh-python36-python-pytest-runner-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-pytest-srpm::	rh-python36-python-py-srpm
rh-python36-python-python-dateutil-srpm::	rh-python36-python-six-srpm
rh-python36-python-python-ldap-srpm::	rh-python36-python-pyasn1-srpm
rh-python36-python-python-ldap-srpm::	rh-python36-python-pyasn1-modules-srpm
rh-python36-python-python-memcached-srpm::	rh-python36-python-six-srpm
rh-python36-python-pyvmomi-srpm::	rh-python36-python-requests-srpm
rh-python36-python-pyvmomi-srpm::	rh-python36-python-six-srpm
rh-python36-python-pywinrm-srpm::	rh-python36-python-requests-srpm
rh-python36-python-pywinrm-srpm::	rh-python36-python-requests_ntlm-srpm
rh-python36-python-pywinrm-srpm::	rh-python36-python-six-srpm
rh-python36-python-pywinrm-srpm::	rh-python36-python-xmltodict-srpm
rh-python36-python-redbaron-srpm::	rh-python36-python-baron-srpm
rh-python36-python-requests-credssp-srpm::	rh-python36-python-ntlm-auth-srpm
rh-python36-python-requests-credssp-srpm::	rh-python36-python-pyOpenSSL-srpm
rh-python36-python-requests-credssp-srpm::	rh-python36-python-requests-srpm
rh-python36-python-requests-futures-srpm::	rh-python36-python-requests-srpm
rh-python36-python-requests-kerberos-srpm::	rh-python36-python-cryptography-srpm
rh-python36-python-requests-kerberos-srpm::	rh-python36-python-requests-srpm
rh-python36-python-requests-oauthlib-srpm::	rh-python36-python-oauthlib-srpm
rh-python36-python-requests-oauthlib-srpm::	rh-python36-python-requests-srpm
rh-python36-python-requests-srpm::	rh-python36-python-certifi-srpm
rh-python36-python-requests-srpm::	rh-python36-python-chardet-srpm
rh-python36-python-requests-srpm::	rh-python36-python-idna-srpm
rh-python36-python-requests-srpm::	rh-python36-python-urllib3-srpm
rh-python36-python-requests_ntlm-srpm::	rh-python36-python-cryptography-srpm
rh-python36-python-requests_ntlm-srpm::	rh-python36-python-ntlm-auth-srpm
rh-python36-python-requests_ntlm-srpm::	rh-python36-python-requests-srpm
rh-python36-python-requestsexceptions-srpm::	rh-python36-python-pbr-srpm
rh-python36-python-rply-srpm::	rh-python36-python-appdirs-srpm
rh-python36-python-rst.linker-srpm::	rh-python36-python-python-dateutil-srpm
rh-python36-python-rst.linker-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-rst.linker-srpm::	rh-python36-python-six-srpm
rh-python36-python-s3transfer-srpm::	rh-python36-python-botocore-srpm
rh-python36-python-selenium-srpm::	rh-python36-python-rdflib-srpm
rh-python36-python-service_identity-srpm::	rh-python36-python-attrs-srpm
rh-python36-python-service_identity-srpm::	rh-python36-python-pyOpenSSL-srpm
rh-python36-python-service_identity-srpm::	rh-python36-python-pyasn1-modules-srpm
rh-python36-python-service_identity-srpm::	rh-python36-python-pyasn1-srpm
rh-python36-python-shade-srpm::	rh-python36-python-openstacksdk-srpm
rh-python36-python-shade-srpm::	rh-python36-python-os-client-config-srpm
rh-python36-python-shade-srpm::	rh-python36-python-pbr-srpm
rh-python36-python-slackclient-srpm::	rh-python36-python-requests-srpm
rh-python36-python-slackclient-srpm::	rh-python36-python-six-srpm
rh-python36-python-slackclient-srpm::	rh-python36-python-websocket_client-srpm
rh-python36-python-social-auth-app-django-srpm::	rh-python36-python-six-srpm
rh-python36-python-social-auth-app-django-srpm::	rh-python36-python-social-auth-core-srpm
rh-python36-python-social-auth-core-srpm::	rh-python36-python-PyJWT-srpm
rh-python36-python-social-auth-core-srpm::	rh-python36-python-defusedxml-srpm
rh-python36-python-social-auth-core-srpm::	rh-python36-python-oauthlib-srpm
rh-python36-python-social-auth-core-srpm::	rh-python36-python-requests-oauthlib-srpm
rh-python36-python-social-auth-core-srpm::	rh-python36-python-requests-srpm
rh-python36-python-social-auth-core-srpm::	rh-python36-python-six-srpm
rh-python36-python-social-auth-core-srpm::	rh-python36-python3-openid-srpm
rh-python36-python-stevedore-srpm::	rh-python36-python-pbr-srpm
rh-python36-python-stevedore-srpm::	rh-python36-python-six-srpm
rh-python36-python-tacacs_plus-srpm::	rh-python36-python-pytest-runner-srpm
rh-python36-python-tacacs_plus-srpm::	rh-python36-python-six-srpm
rh-python36-python-tblib-srpm::	rh-python36-python-sphinx-py3doc-enhanced-theme-srpm
rh-python36-python-tempora-srpm::	rh-python36-python-jaraco.packaging-srpm
rh-python36-python-tempora-srpm::	rh-python36-python-pytz-srpm
rh-python36-python-tempora-srpm::	rh-python36-python-rst.linker-srpm
rh-python36-python-tempora-srpm::	rh-python36-python-setuptools_scm-srpm
rh-python36-python-tempora-srpm::	rh-python36-python-six-srpm
rh-python36-python-tox-srpm::	rh-python36-python-py-srpm
rh-python36-python-tox-srpm::	rh-python36-python-virtualenv-srpm
rh-python36-python-twilio-srpm::	rh-python36-python-PyJWT-srpm
rh-python36-python-twilio-srpm::	rh-python36-python-PySocks-srpm
rh-python36-python-twilio-srpm::	rh-python36-python-pytz-srpm
rh-python36-python-twilio-srpm::	rh-python36-python-six-srpm
rh-python36-python-txalo-srpm::	rh-python36-python-Twisted-srpm
rh-python36-python-txalo-srpm::	rh-python36-python-zope.interface-srpm
rh-python36-python-uwsgitop-srpm::	rh-python36-python-argparse-srpm
rh-python36-python-uwsgitop-srpm::	rh-python36-python-simplejson-srpm
rh-python36-python-xmlsec-srpm::	rh-python36-python-lxml-srpm
rh-python36-python-xmlsec-srpm::	rh-python36-python-pkgconfig-srpm
rh-python36-python3-openid-srpm::	rh-python36-python-defusedxml-srpm
rh-python36-python3-saml-srpm::	rh-python36-python-defusedxml-srpm
rh-python36-python3-saml-srpm::	rh-python36-python-isodate-srpm
rh-python36-python3-saml-srpm::	rh-python36-python-xmlsec-srpm

# Dependencies of libraries on other libraries for compilation
.PHONY: srpm
srpm:: *srpm
.PHONY: *srpm
*-srpm::
	@(cd $@ && $(MAKE) $(MFLAGS) install) || \
		echo Failed: install $@ && echo

# Actually build in directories
repos: $(REPOS) $(REPODIRS)
$(REPOS):
	install -d -m 755 $@

.PHONY: $(REPODIRS)
$(REPODIRS):: /usr/bin/createrepo
$(REPODIRS):: $(REPOS)
	@install -d -m 755 `dirname $@`
	/usr/bin/createrepo -q `dirname $@`


.PHONY: cfg
cfg:: cfgs

.PHONY: cfgs
cfgs: $(CFGS) $(MOCKCFGS)

# Keep metadata very short for local repo
dependsrepo-7-x86_64.cfg: /etc/mock/epel-7-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i 's/epel-7-x86_64/dependsrepo-7-x86_64/g' $@
	@sed -i "s/= 'install @buildsys-build'/= 'install @buildsys-build rh-python36-build'/g" $@
	@sed -i 's/^includepkgs=/#includepkgs=/g' $@
	@echo '"""' >> $@
	@echo >> $@
	@echo '[repo]' >> $@
	@echo 'name=repo' >> $@
	@echo 'enabled=1' >> $@
	@echo 'baseurl=$(REPOBASE)/dependsrepo/el/7/x86_64/' >> $@
	@echo 'failovermethod=priority' >> $@
	@echo 'skip_if_unavailable=False' >> $@
	@echo 'metadata_expire=1' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo '"""' >> $@
	@uniq -u $@ > $@.out && mv $@.out $@

# Enable rh-python36 SCL builds, do not include local packages
sclpy36-7-x86_64.cfg: /etc/mock/epel-7-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i 's/epel-7-x86_64/sclpy36-7-x86_64/g' $@
	@sed -i "s/= 'install @buildsys-build'/= 'install @buildsys-build rh-python36-build'/g" $@
	@sed -i 's/^includepkgs=/#includepkgs=/g' $@

$(MOCKCFGS):: /etc/mock/$@
	ln -sf /etc/mock/$@ $@

repo: dependsrepo.repo
dependsrepo.repo:: Makefile dependsrepo.repo.in
	if [ -s /etc/fedora-release ]; then \
		cat $@.in | \
			sed "s|@REPOBASEDIR@/|$(PWD)/|g" | \
			sed "s|/@RELEASEDIR@/|/fedora/|g" > $@; \
	elif [ -s /etc/redhat-release ]; then \
		cat $@.in | \
			sed "s|@REPOBASEDIR@/|$(PWD)/|g" | \
			sed "s|/@RELEASEDIR@/|/el/|g" > $@; \
	else \
		echo Error: unknown release, check /etc/*-release; \
		exit 1; \
	fi

dependsrepo.repo::
	@cmp -s $@ /etc/yum.repos.d/$@ || \
	    diff -u $@ /etc/yum.repos.d/$@

clean::
	find . -name \*~ -exec rm -f {} \;
	rm -f *.cfg
	rm -f *.out
	@for name in $(SAMBAPKGS); do \
	    (cd $$name; $(MAKE) $(MFLAGS) clean); \
	done

distclean: clean
	rm -rf $(REPOS)
	rm -rf repo
	@for name in $(SAMBAPKGS); do \
	    (cd $$name; git clean); \
	done

maintainer-clean: distclean
	rm -rf $(SAMBAPKGS)
	@for name in $(SAMBAPKGS); do \
	    (cd $$name; git clean -x -d -f); \
	done
