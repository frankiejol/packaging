Name:           orion
Version:        1.6.1
Release:        1%{?dist}
Summary:        Seek and watch streams on Twitch

License:        GPLv3+
URL:            https://github.com/alamminsalo/orion
Source0:        https://github.com/alamminsalo/orion/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml

Patch0:         orion-1.6.1-fix_prefix.patch
Patch1:         orion-1.6.1-fix_desktop.patch

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

#Depends on qt5-qt5webengine
ExclusiveArch: %{qt5_qtwebengine_arches}


%description
A desktop client for Twitch.tv. Features:

 - Login by twitch credentials
 - Desktop notifications
 - Integrated player
 - Chat support
 - Support for live streams and vods


%prep
%autosetup -p1 -n %{name}-%{version}


%build
mkdir build
cd build
%{qmake_qt5} ../ "CONFIG+=multimedia"
             
%make_build


%install
cd build
%make_install INSTALL_ROOT=%{buildroot}
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%post
/bin/touch --no-create %{_datadir}/icons &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons &>/dev/null || :


%files
%license COPYING LICENSE.txt
%doc README.md
%{_bindir}/orion
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.svg


%changelog
* Sun Sep 17 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.6.1-1
- Release 1.6.1
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
