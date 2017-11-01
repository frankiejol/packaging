Name:       libfilteraudio
Version:    0.0.1
Release:    2%{?dist}
Summary:    Lightweight audio filtering library made from webrtc code

License:    BSD
URL:        https://github.com/irungentoo/filter_audio/
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sndfile)


%description
Lightweight audio filtering library made from webrtc code.


%package devel
Summary:        Development files for libfilteraudio
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Development files for libfilteraudio, the lightweight audio 
filtering library made from webrtc code.


%prep
%autosetup -n filter_audio-%{version}


%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build


%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_lib}
find %{buildroot} -name '*.a' -delete


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc README
%{_libdir}/libfilteraudio.so.*


%files devel
%{_includedir}/filter_audio.h
%{_libdir}/libfilteraudio.so
%{_libdir}/pkgconfig/filteraudio.pc


%changelog
* Tue Oct 31 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.0.1-2
- Clean-up the SPEC

* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.0.1-1
- First RPM release

