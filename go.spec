Name:          go
Version:       1.0.3
Release:       1%{?dist}
Summary:       Compiler for the Go language from Google
Group:         Development/Languages
License:       BSD
URL:           http://golang.org/
Source0:       %{name}%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: ed
BuildRequires: mercurial
BuildRequires: bison
%define _use_internal_dependency_generator 0
%define __find_requires %{nil}
%global debug_package %{nil}
%global __spec_install_post /usr/lib/rpm/check-rpaths   /usr/lib/rpm/check-buildroot  \
  /usr/lib/rpm/brp-compress

%ifarch %ix86
    %global GOARCH 386
%endif
%ifarch    x86_64
    %global GOARCH amd64
%endif

%description
Go is a systems programming language that aims to be both fast and convenient.

%prep
%setup -q -n go

%build
export GOSRC="$(pwd)"
export GOROOT="$(pwd)"
export GOROOT_FINAL=%{_libdir}/go
export GOOS=linux
export GOBIN="$GOROOT/bin"
export GOARCH="%{GOARCH}"
export MAKE=%{__make}
mkdir -p "$GOBIN"
cd src

LC_ALL=C PATH="$PATH:$GOBIN" ./make.bash

%install
rm -rf %{buildroot}

export GOROOT_FINAL=%{_libdir}/go
export GOROOT="%{buildroot}%{_libdir}/go"
export GOOS=linux
export GOBIN="$GOROOT/bin"
export GOARCH="%{GOARCH}"

mkdir -p $GOROOT/{misc,lib,src}
mkdir -p %{buildroot}%{_bindir}/

cp -ar pkg include lib bin $GOROOT
cp -ar src/pkg src/cmd $GOROOT/src
cp -ar misc/cgo $GOROOT/misc

ln -sf %{_libdir}/go/pkg/tool/linux_%{GOARCH}/cgo %{buildroot}%{_bindir}/cgo
ln -sf %{_libdir}/go/pkg/tool/linux_%{GOARCH}/ebnflint %{buildroot}%{_bindir}/ebnflint

ln -sf %{_libdir}/go/bin/go %{buildroot}%{_bindir}/go
ln -sf %{_libdir}/go/bin/godoc %{buildroot}%{_bindir}/godoc
ln -sf %{_libdir}/go/bin/gofmt %{buildroot}%{_bindir}/gofmt

%ifarch %ix86
for tool in 8a 8c 8g 8l; do
%else
for tool in 6a 6c 6g 6l; do
%endif
ln -sf %{_libdir}/go/pkg/tool/linux_%{GOARCH}/$tool %{buildroot}%{_bindir}/$tool
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/go
%ifarch %ix86
%{_bindir}/8*
%else
%{_bindir}/6*
%endif
%{_bindir}/ebnflint
%{_bindir}/go*
%{_bindir}/cgo

%changelog
* Wed Oct 3 2012 Sam Kottler <sam@kottlerdevelopment.com> - 2012102012
- Updated to 1.0.3
* Sat Aug 11 2012 Sam Kottler <sam@kottlerdevelopment.com> - 20120811
- Initial creation of the Go package
