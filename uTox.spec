Name:       uTox
Version:    0.15.0
Release:    2%{?dist}
Summary:    The lightweight Tox client

License:    GPLv3
URL:        https://github.com/uTox/uTox/
Source0:    https://github.com/uTox/uTox/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:    %{name}.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libasan
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(filteraudio)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libtoxcore)

%description
%summary


%prep
%autosetup


%build
%cmake .
%make_build


%install
%make_install
install -Dp -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml


%check
ctest -V %{?_smp_mflags}
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/utox.desktop
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
%{_bindir}/utox
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/utox.desktop
%{_datadir}/icons/hicolor/*/apps/utox*
%{_mandir}/man1/utox.1*


%changelog
* Fri Aug 18 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.15.0-2
- Added appdata.xml
- Fixed Requires dependencies

* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.15.0-1
- First RPM release
