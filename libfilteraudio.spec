%ifarch x86_64
%global libdir lib64
%else
%global libdir lib
%endif

Name:	        libfilteraudio
Version:	0.0.1
Release:	1%{?dist}
Summary:	Lightweight audio filtering library made from webrtc code

License:	BSD
URL:		https://github.com/irungentoo/filter_audio/
Source0:	https://github.com/irungentoo/filter_audio/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sndfile)
Requires:	portaudio
Requires:	libsndfile

%description
Lightweight audio filtering library made from webrtc code.


%package devel
Summary:        Development files for libfilteraudio
Requires:       %{name}%{?_isa} = %{version}-%{release}, pkgconfig


%description devel
Development files for libfilteraudio, the lightweight audio 
filtering library made from webrtc code.


%prep
%autosetup -n filter_audio-%{version}


%build
export CFLAGS=-g
%make_build


%install
%make_install PREFIX=/usr LIBDIR=%{libdir}
find %{buildroot} -regex ".*\.a$" | xargs rm -f --


%files
%doc README
%{_libdir}/libfilteraudio.so*


%files devel
%{_includedir}/filter_audio.h
%{_libdir}/libfilteraudio.so
%{_libdir}/pkgconfig/filteraudio.pc


%changelog
* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.0.1-1
- First RPM release

