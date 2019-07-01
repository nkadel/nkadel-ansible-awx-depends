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

# Link from /etc/mock
MOCKCFGS+=epel-7-x86_64.cfg

all:: $(CFGS)
all:: $(MOCKCFGS)
all:: $(REPODIRS)
all:: $(DEPENDSPKGS)

all install clean getsrc:: FORCE
	@for name in *srpm; do \
	     (cd $$name && $(MAKE) $(MFLAGS) $@); \
	done  

# Build for locacl OS
build:: FORCE
	@for name in *srpm; do \
	     (cd $$name && $(MAKE) $(MFLAGS) $@); \
	done

# Git submodule checkout operation
# For more recent versions of git, use "git checkout --recurse-submodules"
*-srpm::
	@[ -d $@/.git ] || \
	     git submodule update --init $@

# Dependencies of libraries on other libraries for compilation

compat-gnutls34-3.x-srpm:: compat-nettle32-3.x-srpm

libtevent-0.9.x-srpm:: libtalloc-2.1.x-srpm

libldb-1.5.x-srpm:: libtalloc-2.1.x-srpm
libldb-1.5.x-srpm:: libtdb-1.3.x-srpm
libldb-1.5.x-srpm:: libtevent-0.9.x-srpm

# Needed for with_mitkrb5
samba-4.10.x-srpm:: compat-gnutls34-3.x-srpm

# Samba rellies on all the othe components
samba-4.10.x-srpm:: libtalloc-2.1.x-srpm
samba-4.10.x-srpm:: libldb-1.5.x-srpm
samba-4.10.x-srpm:: libtevent-0.9.x-srpm
samba-4.10.x-srpm:: libtdb-1.3.x-srpm

# Actually build in directories
$(SAMBAPKGS):: FORCE
	(cd $@ && $(MAKE) $(MLAGS) install)

repos: $(REPOS) $(REPODIRS)
$(REPOS):
	install -d -m 755 $@

.PHONY: $(REPODIRS)
$(REPODIRS): $(REPOS)
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

