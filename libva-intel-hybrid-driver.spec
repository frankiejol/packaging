Name:           libva-intel-hybrid-driver
Version:        1.0.2
Release:        3%{?dist}
Summary:        VA driver for Intel G45 & HD Graphics family

License:        MIT
URL:            https://github.com/01org/intel-hybrid-driver
Source0:        https://github.com/01org/intel-hybrid-driver/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         libva-intel-hybrid-driver-1.0.2_replace_obsolete_AC_PROG_LIBTOOL.patch

#obviously only for intel platform
ExclusiveArch:  %{ix86} x86_64 ia64

BuildRequires:  libtool
BuildRequires:  pkgconfig(libdrm) >= 2.4.45
BuildRequires:  pkgconfig(libva) >= 0.38
BuildRequires:  pkgconfig(libcmrt) >= 0.10.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-server)


%description
libva-intel-hybrid-driver is the VA-API implementation for Intel G45 chipsets
and Intel HD Graphics for Intel Core processor family.


%prep
%autosetup -p1 -n intel-hybrid-driver-%{version}


%build
autoreconf -vif
%configure
%make_build


%install
%make_install 
find %{buildroot} -name "*.la" -delete


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license AUTHORS COPYING
%doc NEWS README
%{_libdir}/dri/hybrid_drv_video.so


%changelog
* Tue Jul 25 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.0.2-3
- Added patch to replace the obsolete AC_PROG_LIBTOOL
* Thu Jul 20 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.0.2-2
- Update to Fedora Packaging Guidelines specification
* Wed Jul 19 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.0.2-1
- First RPM release
