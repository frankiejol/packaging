Name:       qTox
Version:    1.12.1
Release:    1%{?dist}
Summary:    Feature-rich Tox client

License:    GPLv3
URL:        https://github.com/qTox/qTox/
Source0:    https://github.com/qTox/qTox/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:     qTox-1.11.0-remove_project_group.patch
Patch1:     qTox-1.12.1-disable_Werror.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  qtsingleapplication
BuildRequires:  pkgconfig(libtoxcore)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  pkgconfig(filteraudio)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  qt5-linguist
Requires:       hicolor-icon-theme


%description
qTox is a powerful Tox client that follows the Tox design 
guidelines while running on all major platforms. 


%prep
%autosetup -p1


%build
mkdir build
pushd build
%cmake "CMAKE_CXX_FLAGS+=-Wno-error" ..
%make_build
popd


%install
pushd build
%make_install
popd


%check
ctest -V %{?_smp_mflags}
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/qtox.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


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
* Thu Oct 12 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.12.1-1
- New upstream release 1.12.1

* Fri Aug 18 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.11.0-2
- Fix typo

* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.11.0-1
- First RPM release

