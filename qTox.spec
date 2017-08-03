Name:	        qTox
Version:	1.11.0
Release:	1%{?dist}
Summary:	Feature-rich Tox client

License:	GPLv3
URL:		https://github.com/qTox/qTox/
Source0:	https://github.com/qTox/qTox/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(openal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:	qt5-linguist
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(vpx)
BuildRequires:  pkgconfig(libtoxcore)
Requires:	ffmpeg
Requires:	gtk2
Requires:       libXScrnSaver
Requires:	openal-soft
Requires:	openssl
Requires:	libsodium
Requires:	qrencode
Requires:	qt5-qtsvg
Requires:	qtsingleapplication-qt5
Requires:	qslcipher
Requires:	opus
Requires:	libvpx
Requires:	toxcore

%description
qTox is a powerful Tox client that follows the Tox design 
guidelines while running on all major platforms. 


%prep
%autosetup


%build
%cmake .
%make_build


%install
%make_install


%check
ctest -V %{?_smp_mflags}
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/qtox.desktop


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null ||:


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null ||:


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/qtox
%{_datadir}/appdata/qTox.appdata.xml
%{_datadir}/applications/qtox.desktop
%{_datadir}/icons/hicolor/*/apps/qtox.*


%changelog
* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.11.0-1
- First RPM release

