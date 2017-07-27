Name:           orion
Version:        1.5.1
Release:        2%{?dist}
Summary:        QML/C++-written desktop client for Twitch.tv

License:        GPLv3
URL:            https://github.com/alamminsalo/orion
Source0:        https://github.com/alamminsalo/orion/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5Multimedia)
Requires:       qt5-qtbase
Requires:       qt5-qtquickcontrols2
Requires:       qt5-qtsvg
Requires:       qt5-qtwebengine
Requires:       qt5-qtmultimedia


%description
A desktop client for Twitch.tv


%prep
%autosetup -p1 -n %{name}-%{version}


%build
mkdir build
cd build
%{qmake_qt5} ../ "CMAKE_CXX_FLAGS+=-g" "CONFIG+=multimedia"
%make_build


%install
install -p -D -m 755 build/orion $RPM_BUILD_ROOT%{_bindir}/orion
install -p -D -m 644 distfiles/orion.svg $RPM_BUILD_ROOT%{_datadir}/icons/orion.svg

desktop-file-install                                    \
--remove-category="Games"                               \
--add-category="Game"                                   \
--delete-original                                       \
--set-icon=orion                                        \
--dir=$RPM_BUILD_ROOT%{_datadir}/applications/          \
distfiles/Orion.desktop


%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
update-desktop-database &> /dev/null || :


%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
update-desktop-database &> /dev/null || :


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%license COPYING LICENSE.txt
%doc README.md
%{_bindir}/orion
%{_datadir}/icons/orion.svg
%{_datadir}/applications/Orion.desktop


%changelog
* Thu Jul 20 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.5.1-2
- Update to Fedora Packaging Guidelines specification
* Sun Jul 09 2017  Robert-André Mauchin <zebob.m@gmail.com> 1.5.1-1
- Release 1.5.1
* Sun Apr 30 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.5.1.rc-1
- Pre-release 1.5.1.rc
* Thu Feb 2 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.4.0-1
- Release 1.4.0
* Sun Oct 16 2016 Robert-André Mauchin <zebob.m@gmail.com> 1.3.5-1
- Release 1.3.5
* Mon Oct 10 2016 Robert-André Mauchin <zebob.m@gmail.com> 1.3.2-1
- Release 1.3.2
* Thu Sep 22 2016 Robert-André Mauchin <zebob.m@gmail.com> 1.3.1-1
- First RPM release
