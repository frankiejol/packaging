Name:           cmrt
Version:        1.0.6
Release:        3%{?dist}
Summary:        C for Media Runtime
License:        MIT
URL:            https://github.com/01org/cmrt
Source0:        https://github.com/01org/cmrt/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch0:         cmrt-1.0.6_replace_obsolete_AC_PROG_LIBTOOL.patch

#This library depends on specific intel instructions like sse, avx…
ExclusiveArch:  %{ix86} x86_64 ia64

BuildRequires:  libtool
BuildRequires:  pkgconfig(libdrm) >= 2.4.23
BuildRequires:  pkgconfig(libva) >= 0.34


%description
Media GPU kernel manager for Intel G45 & HD Graphics family


%package devel
Summary:        Development files for the C for Media Runtime
Requires:       %{name}%{?_isa} = %{version}-%{release}, pkgconfig


%description devel
Media GPU kernel manager for Intel G45 & HD Graphics family, 
development files.


%prep
%autosetup -p1 n %{name}-%{version}


%build
autoreconf -vif
%configure
%make_build


%install
%make_install 
find %{buildroot} -regex ".*\.la$" | xargs rm -f --


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license AUTHORS COPYING
%doc NEWS README
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_libdir}/lib%{name}.so.*


%files devel
%license AUTHORS COPYING
%{_includedir}/cm_rt.h
%{_includedir}/cm_rt_linux.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/libcmrt.pc


%changelog
* Tue Jul 25 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.0.6-3
- Added patch to replace the obsolete AC_PROG_LIBTOOL
* Wed Jul 19 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.0.6-2
- Update to Fedora Packaging Guidelines specification
* Wed Jul 19 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.0.6-1
- First RPM release
