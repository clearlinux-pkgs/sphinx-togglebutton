#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinx-togglebutton
Version  : 0.2.3
Release  : 2
URL      : https://files.pythonhosted.org/packages/25/e7/cfe952ad8de462080eaebb41108994d5c822b4911fbb65ecb1ec79d25446/sphinx-togglebutton-0.2.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/25/e7/cfe952ad8de462080eaebb41108994d5c822b4911fbb65ecb1ec79d25446/sphinx-togglebutton-0.2.3.tar.gz
Summary  : Toggle page content and collapse admonitions in Sphinx.
Group    : Development/Tools
License  : MIT
Requires: sphinx-togglebutton-license = %{version}-%{release}
Requires: sphinx-togglebutton-python = %{version}-%{release}
Requires: sphinx-togglebutton-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docutils)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sphinx_book_theme)
BuildRequires : pypi(wheel)

%description
A small sphinx extension to make it possible to add a "toggle button" to

%package license
Summary: license components for the sphinx-togglebutton package.
Group: Default

%description license
license components for the sphinx-togglebutton package.


%package python
Summary: python components for the sphinx-togglebutton package.
Group: Default
Requires: sphinx-togglebutton-python3 = %{version}-%{release}

%description python
python components for the sphinx-togglebutton package.


%package python3
Summary: python3 components for the sphinx-togglebutton package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_togglebutton)
Requires: pypi(docutils)
Requires: pypi(setuptools)
Requires: pypi(sphinx)
Requires: pypi(wheel)

%description python3
python3 components for the sphinx-togglebutton package.


%prep
%setup -q -n sphinx-togglebutton-0.2.3
cd %{_builddir}/sphinx-togglebutton-0.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637344266
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinx-togglebutton
cp %{_builddir}/sphinx-togglebutton-0.2.3/LICENSE %{buildroot}/usr/share/package-licenses/sphinx-togglebutton/04f302f55e177936c00dce6b36ca9cf0c4e007ff
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinx-togglebutton/04f302f55e177936c00dce6b36ca9cf0c4e007ff

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
