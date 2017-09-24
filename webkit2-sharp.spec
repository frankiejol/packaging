%global commit		a59fd76dd730432c76b12ee6347ea66567107ab9
%global commitdate	20170219
%global shortcommit	%(c=%{commit}; echo ${c:0:7})

Name:		webkit2-sharp
Version:	0
Release:	0.2%{?commitdate:.%{commitdate}git%{shortcommit}}%{?dist}
Summary:	C# bindings for WebKit 2 with GTK+ 3

License:	MIT
URL:		https://github.com/hbons/%{name}
%{?shortcommit:
Source0:	%url/archive/%{commit}/%{name}-%{shortcommit}.tar.gz}
%{!?shortcommit:
Source0:	%url/archive/%{commit}/%{name}-%{version}.tar.gz}

Patch0:		%{name}-a59fd76-fix_libdir.patch

Requires:		webkitgtk4
BuildRequires:	pkgconfig(webkit2gtk-4.0)
BuildRequires:	pkgconfig(mono)
BuildRequires:	pkgconfig(gtk-sharp-3.0)
BuildRequires:	pkgconfig(gapi-3.0)
BuildRequires:	pkgconfig(monodoc)
BuildRequires:	libxslt
BuildRequires:	dos2unix
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	gettext

ExclusiveArch:	%mono_arches

#https://fedoraproject.org/wiki/Packaging:Mono#Empty_debuginfo
%global debug_package %{nil}


%description
C# bindings for WebKit 2 with GTK+ 3


%package devel
Summary:	Development files for WebKit2-sharp
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig


%description devel
Development files for WebKit2-sharp


%prep
%{?shortcommit:
%autosetup -n %{name}-%{commit}}
%{!?shortcommit:
%autosetup -n %{name}-%{version}}

%build
./autogen.sh
%configure
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING README.md
%{_prefix}/lib/mono/
%{_datadir}/gapi-3.0/webkit2-sharp-api.xml
%{_libdir}/libwebkit2sharpglue-2.10.9.so

%files devel
%{_libdir}/pkgconfig/webkit2-sharp-4.0.pc
%{_libdir}/libwebkit2sharpglue-2.10.9.a
%{_prefix}/lib/monodoc/sources/webkit2-sharp*

%changelog
* Sun Sep 24 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 0-0.2.20170219gita59fd76
- Improve spec file

* Sun Sep 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170219gita59fd76
- Initial package
