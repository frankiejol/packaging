Name:           qdirstat
Version:        1.4
Release:        3%{?dist}
Summary:        Qt-based directory statistics

License:        GPLv2
URL:            https://github.com/shundhammer/qdirstat
Source0:        https://github.com/shundhammer/qdirstat/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml

BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       qt5-qtbase
Requires:       hicolor-icon-theme


%description
QDirStat is a graphical application to show where your disk space has gone
and to help you to clean it up.

This is a Qt-only port of the old Qt3/KDE3-based KDirStat, now based on the
 latest Qt 5. It does not need any KDE libs or infrastructure. It runs on
 every X11-based desktop on Linux, BSD and other Unix-like systems.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%{qmake_qt5}
%make_build


%install
%make_install INSTALL_ROOT=$RPM_BUILD_ROOT
install -Dp -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/qdirstat.desktop
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
%{_docdir}/%{name}/
%{_bindir}/qdirstat
%{_bindir}/qdirstat-cache-writer
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Tue Jul 25 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.4-3
- Fix for Fedora Review
* Thu Jul 20 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.4-2
- Update to Fedora Packaging Guidelines specification
* Sat Jun 24 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.4-1
- Update to version 1.4
* Tue Mar 07 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.3-1
- Update to version 1.3
* Fri Jan 06 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.2-1
- Update to version 1.2
* Sat Dec 03 2016 Robert-André Mauchin <zebob.m@gmail.com> 1.1-1
- First RPM release
