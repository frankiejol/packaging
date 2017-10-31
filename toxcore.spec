Name:           toxcore 
Version:        0.1.10
Release:        2%{?dist}
Summary:        Peer to peer instant messenger

License:        GPLv3+
URL:            https://github.com/TokTok/c-toxcore
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         toxcore-0.1.10-fix_obsolete_m4s.patch

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)


%description
Tox is a peer to peer (serverless) instant messenger aimed at making 
security and privacy easy to obtain for regular users. It uses NaCl 
for its encryption and authentication.


%package devel
Summary:        Development files for Toxcore 
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Tox is a peer to peer (serverless) instant messenger aimed at making
security and privacy easy to obtain for regular users. It uses NaCl
for its encryption and authentication.

This package contains Toxcore development files.


%prep
%autosetup -p1 -n c-%{name}-%{version}


%build
autoreconf -vif
%configure --disable-static
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}
find %{buildroot} -name '*.la' -delete


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%license COPYING
%doc README.md CHANGELOG.md
%{_libdir}/libtoxav.so.*
%{_libdir}/libtoxcore.so.*
%{_libdir}/libtoxdns.so.*
%{_libdir}/libtoxencryptsave.so.*


%files devel
%license COPYING
%{_includedir}/tox/*
%{_libdir}/libtoxav.so
%{_libdir}/libtoxcore.so
%{_libdir}/libtoxdns.so
%{_libdir}/libtoxencryptsave.so
%{_libdir}/pkgconfig/libtoxav.pc
%{_libdir}/pkgconfig/libtoxcore.pc


%changelog
* Tue Oct 31 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.1.10-2
- Clean-up the SPEC

* Thu Oct 12 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.1.10-1
- New upstream release 0.1.10

* Fri Aug 18 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.1.9-2
- Fix Requires dependencies

* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.1.9-1
- First RPM release
