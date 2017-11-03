Name:       utox
Version:    0.16.1
Release:    2%{?dist}
Summary:    The lightweight Tox client

License:    MIT or GPLv3+
URL:        https://github.com/uTox/uTox/
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(filteraudio)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libtoxcore)
Requires:       hicolor-icon-theme


%description
%summary


%prep
%autosetup -n uTox-%{version}


%build
mkdir build
pushd build
%cmake .. -DENABLE_ASAN=OFF
%make_build
popd


%install
pushd build
%make_install
popd
install -Dp -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
rm -rf %{buildroot}/%{_datadir}/icons/hicolor/14x14


%check
ctest -V %{?_smp_mflags}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
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
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Oct 31 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.16.1-2
- Clean-up the SPEC

* Thu Oct 12 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.16.1-1
- New upstream release 0.16.1

* Fri Aug 18 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.15.0-2
- Added appdata.xml
- Fixed Requires dependencies

* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.15.0-1
- First RPM release
