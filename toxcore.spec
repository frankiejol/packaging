Name:           toxcore 
Version:        0.1.9
Release:        1%{?dist}
Summary:        Peer to peer instant messenger

License:        GPLv3
URL:            https://github.com/TokTok/c-toxcore
Source0:        https://github.com/TokTok/c-toxcore/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)
Requires:       libsodium
Requires:       opus
Requires:       libvpx


%description
Tox is a peer to peer (serverless) instant messenger aimed at making 
security and privacy easy to obtain for regular users. It uses NaCl 
for its encryption and authentication.

%package devel
Summary:        Development files for Toxcore 
Requires:       %{name}%{?_isa} = %{version}-%{release}, pkgconfig


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
%make_install INSTALL_ROOT=$RPM_BUILD_ROOT
find %{buildroot} -regex ".*\.la$" | xargs rm -f --


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license COPYING
%doc README.md CHANGELOG.md
%{_libdir}/libtoxav.so*
%{_libdir}/libtoxcore.so*
%{_libdir}/libtoxdns.so*
%{_libdir}/libtoxencryptsave.so*


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
* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.1.9-1
- First RPM release
