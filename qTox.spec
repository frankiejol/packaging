Name:       qTox
Version:    1.11.0
Release:    2%{?dist}
Summary:    Feature-rich Tox client

License:    GPLv3
URL:        https://github.com/qTox/qTox/
Source0:    https://github.com/qTox/qTox/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch0:     qTox-1.11.0-remove_project_group.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(libtoxcore)


%description
qTox is a powerful Tox client that follows the Tox design 
guidelines while running on all major platforms. 


%prep
%autosetup -p1


%build
%cmake .
%make_build


%install
%make_install


%check
ctest -V %{?_smp_mflags}
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/qtox.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml


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
* Fri Aug 18 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.11.0-2
- Fix typo

* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.11.0-1
- First RPM release

