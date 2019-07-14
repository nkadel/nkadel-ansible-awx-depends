#
# Makefile - build wrapper for Samba 4 on RHEL 6
#
#	git clone RHEL 6 SRPM building tools from
#	https://github.com/nkadel/[package] into designated
##	SAMBAPKGS below
#
#	Set up local 


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

getsrc:: /usr/bin/spectool
# Build and getsrc for locacl OS require scl-utils
all build getsrc srpm:: /etc/rpm/macros.scl

all build getsrc srpm install clean::
	@for name in *srpm; do \
	     (cd $$name && $(MAKE) $(MFLAGS) $@); \
	done  

# Dependencies of libraries on other libraries for compilation
*srpm::
	(cd $@ && $(MAKE) $(MFLAGS) install install)

# python-lxml requires Cython
rh-python36-python-lxml-srpm::                   rh-python36-Cython-srpm

rh-python36-python-xmlsec-srpm::                 rh-python36-python-lxml-srpm
rh-python36-python-defusedxml-srpm::             rh-python36-python-lxml-srpm
rh-python36-python-ncclient-srpm::               rh-python36-python-lxml-srpm

rh-python36-python-keystoneauth1-srpm::          rh-python36-pbr-srpm
rh-python36-python-lockfile-srpm::               rh-python36-pbr-srpm
rh-python36-python-openstacksdk-srpm::           rh-python36-pbr-srpm
rh-python36-python-os-service-types::            rh-python36-pbr-srpm
rh-python36-python-requestsexceptions-srpm::     rh-python36-pbr-srpm
rh-python36-python-stevedore-srpm::              rh-python36-pbr-srpm

rh-python36-python-daemon::                      rh-python36-python-lockfile-srpm

rh-python36-python-jsonschema-srpm::             rh-python36-python-vcversioner-srpm

rh-python36-python-cryptography-srpm::           rh-python36-python-pycparser-srpm
rh-python36-python-cryptography-srpm::           rh-python36-python-cffi-srpm
rh-python36-python-bcrypt-srpm::                 rh-python36-python-cffi-srpm
rh-python36-python-arg2-cffi-srpm::              rh-python36-python-cffi-srpm
rh-python36-python-PyNaCl-srpm::                 rh-python36-python-cffi-srpm

# Lots and lots of dependencies, consider using built-in release
rh-python36-python-ansible-srpm::                rh-python36-python-cryptography-srpm

rh-python36-python-boto3-srpm::                  rh-python36-python-botocore
rh-python36-python-boto3-srpm::                  rh-python36-python-s3transfer-srpm
rh-python36-python-boto3-srpm::                  rh-python36-python-mock
rh-python36-python-boto3-srpm::                  rh-python36-python-jmespath

rh-python36-python-rply-srpm::                   rh-python36-python-appdirs-srpm

rh-python36-python-pypandoc-srpmn::              rh-python36-python-pandoc-srpmn

rh-python36-python-baron-srpm::                  rh-python36-python-rply-srpm
rh-python36-python-baron-srpm::                  rh-python36-python-ply-srpm
rh-python36-python-baron-srpm::                  rh-python36-python-pandoc-srpmn
rh-python36-python-baron-srpm::                  rh-python36-python-pypandoc-srpmn

rh-python36-python-Twisted-srpm::                rh-python36-python-incremental-srpm

rh-python36-python-django-taggit-srpm::          rh-python36-python-isort-srpm

# setuptools_scm is not explicitly in "requires" lists because even to read
# the lists, you need this installed first
rh-python36-python-irc-srpm::                    rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.classes-srpm::         rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.collections-srpm::     rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.functools-srpm::       rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.itertools-srpm::       rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.logging-srpm::         rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.stream-srpm::          rh-python36-python-setuptools_scm-srpm
rh-python36-python-jaraco.text-srpm::            rh-python36-python-setuptools_scm-srpm
rh-python36-python-keyring-srpm::                rh-python36-python-setuptools_scm-srpm
rh-python36-python-py-srpm::                     rh-python36-python-setuptools_scm-srpm
rh-python36-python-pytest-runner-srpm::          rh-python36-python-setuptools_scm-srpm
rh-python36-python-rst.linker-srpm::             rh-python36-python-setuptools_scm-srpm
rh-python36-python-tempora-srpm::                rh-python36-python-setuptools_scm-srpm
rh-python36-python-tox-srpm::                    rh-python36-python-setuptools_scm-srpm

rh-python36-python-django-crum-srpm::            rh-python36-python-pytest-runner-srpm
rh-python36-python-django-split-settings-srpm::  rh-python36-python-pytest-runner-srpm
rh-python36-pythontacacs_plus-srpm::             rh-python36-python-pytest-runner-srpm
rh-python36-pyton-apache-libcloud-srpm::         rh-python36-python-pytest-runner-srpm


# Actually build in directories
$(SAMBAPKGS):: FORCE
	(cd $@ && $(MAKE) $(MLAGS) install)

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
	@echo 'metadata_expire=3' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo '"""' >> $@
	@uniq -u $@ > $@.out
	@mv $@.out $@

# Enable rh-python36 SCL builds, do not include local packages
sclpy36-7-x86_64.cfg: /etc/mock/epel-7-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i 's/epel-7-x86_64/sclpy36-7-x86_64/g' $@
	@sed -i "s/= 'install @buildsys-build'/= 'install @buildsys-build rh-python36-build'/g" $@
	@sed -i 's/^includepkgs=/#includepkgs=/g' $@
	@mv $@.out $@

$(MOCKCFGS)::
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
	    $(MAKE) -C $$name clean; \
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

FORCE::

