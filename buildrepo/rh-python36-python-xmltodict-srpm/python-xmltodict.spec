#
# spec file for package rh-python36-python-xmltodict
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

%global pypi_name xmltodict

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
Version:        0.11.0
Release:        0%{?dist}
Url:            https://github.com/martinblech/xmltodict
Summary:        Makes working with XML feel like you are working with JSON
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
%if %{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python-%{pypi_name}}

%description
# xmltodict

`xmltodict` is a Python module that makes working with XML feel like you are working with [JSON](http://docs.python.org/library/json.html), as in this ["spec"](http://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html):

[![Build Status](https://secure.travis-ci.org/martinblech/xmltodict.svg)](http://travis-ci.org/martinblech/xmltodict)

```python
>>> print(json.dumps(xmltodict.parse("""
...  <mydocument has="an attribute">
...    <and>
...      <many>elements</many>
...      <many>more elements</many>
...    </and>
...    <plus a="complex">
...      element as well
...    </plus>
...  </mydocument>
...  """), indent=4))
{
    "mydocument": {
        "@has": "an attribute", 
        "and": {
            "many": [
                "elements", 
                "more elements"
            ]
        }, 
        "plus": {
            "@a": "complex", 
            "#text": "element as well"
        }
    }
}
```

## Namespace support

By default, `xmltodict` does no XML namespace processing (it just treats namespace declarations as regular node attributes), but passing `process_namespaces=True` will make it expand namespaces for you:

```python
>>> xml = """
... <root xmlns="http://defaultns.com/"
...       xmlns:a="http://a.com/"
...       xmlns:b="http://b.com/">
...   <x>1</x>
...   <a:y>2</a:y>
...   <b:z>3</b:z>
... </root>
... """
>>> xmltodict.parse(xml, process_namespaces=True) == {
...     'http://defaultns.com/:root': {
...         'http://defaultns.com/:x': '1',
...         'http://a.com/:y': '2',
...         'http://b.com/:z': '3',
...     }
... }
True
```

It also lets you collapse certain namespaces to shorthand prefixes, or skip them altogether:

```python
>>> namespaces = {
...     'http://defaultns.com/': None, # skip this namespace
...     'http://a.com/': 'ns_a', # collapse "http://a.com/" -> "ns_a"
... }
>>> xmltodict.parse(xml, process_namespaces=True, namespaces=namespaces) == {
...     'root': {
...         'x': '1',
...         'ns_a:y': '2',
...         'http://b.com/:z': '3',
...     },
... }
True
```

## Streaming mode

`xmltodict` is very fast ([Expat](http://docs.python.org/library/pyexpat.html)-based) and has a streaming mode with a small memory footprint, suitable for big XML dumps like [Discogs](http://discogs.com/data/) or [Wikipedia](http://dumps.wikimedia.org/):

```python
>>> def handle_artist(_, artist):
...     print(artist['name'])
...     return True
>>> 
>>> xmltodict.parse(GzipFile('discogs_artists.xml.gz'),
...     item_depth=2, item_callback=handle_artist)
A Perfect Circle
Fant&#244;mas
King Crimson
Chris Potter
...
```

It can also be used from the command line to pipe objects to a script like this:

```python
import sys, marshal
while True:
    _, article = marshal.load(sys.stdin)
    print(article['title'])
```

```sh
$ bunzip2 enwiki-pages-articles.xml.bz2 | xmltodict.py 2 | myscript.py
AccessibleComputing
Anarchism
AfghanistanHistory
AfghanistanGeography
AfghanistanPeople
AfghanistanCommunications
Autism
...
```

Or just cache the dicts so you don't have to parse that big XML file again. You do this only once:

```sh
$ bunzip2 enwiki-pages-articles.xml.bz2 | xmltodict.py 2 | gzip > enwiki.dicts.gz
```

And you reuse the dicts with every script that needs them:

```sh
$ gunzip enwiki.dicts.gz | script1.py
$ gunzip enwiki.dicts.gz | script2.py
...
```

## Roundtripping

You can also convert in the other direction, using the `unparse()` method:

```python
>>> mydict = {
...     'response': {
...             'status': 'good',
...             'last_updated': '2014-02-16T23:10:12Z',
...     }
... }
>>> print(unparse(mydict, pretty=True))
<?xml version="1.0" encoding="utf-8"?>
<response>
	<status>good</status>
	<last_updated>2014-02-16T23:10:12Z</last_updated>
</response>
```

Text values for nodes can be specified with the `cdata_key` key in the python dict, while node properties can be specified with the `attr_prefix` prefixed to the key name in the python dict. The default value for `attr_prefix` is `@` and the default value for `cdata_key` is `#text`.

```python
>>> import xmltodict
>>> 
>>> mydict = {
...     'text': {
...         '@color':'red',
...         '@stroke':'2',
...         '#text':'This is a test'
...     }
... }
>>> print(xmltodict.unparse(mydict, pretty=True))
<?xml version="1.0" encoding="utf-8"?>
<text stroke="2" color="red">This is a test</text>
```

## Ok, how do I get it?

### Using pypi

You just need to

```sh
$ pip install xmltodict
```

### RPM-based distro (Fedora, RHEL, &#8230;)

There is an [official Fedora package for xmltodict](https://apps.fedoraproject.org/packages/python-xmltodict).

```sh
$ sudo yum install python-xmltodict
```

### Arch Linux

There is an [official Arch Linux package for xmltodict](https://www.archlinux.org/packages/community/any/python-xmltodict/).

```sh
$ sudo pacman -S python-xmltodict
```

### Debian-based distro (Debian, Ubuntu, &#8230;)

There is an [official Debian package for xmltodict](https://tracker.debian.org/pkg/python-xmltodict).

```sh
$ sudo apt install python-xmltodict
```

### FreeBSD

There is an [official FreeBSD port for xmltodict](https://svnweb.freebsd.org/ports/head/devel/py-xmltodict/).

```sh
$ pkg install py36-xmltodict
```


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
