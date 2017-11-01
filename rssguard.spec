Name:           rssguard
Version:        3.5.4
Release:        3%{?dist}
Summary:        Simple yet powerful feed reader

# GPLv3+: main program
# BSD: src/dynamic-shortcuts, src/miscellaneous/simplecrypt,
#      src/network-web/googlesuggest
# AGPLv3: src/network-web/oauth2service
License:        GPLv3+ and BSD and AGPLv3
URL:            https://github.com/martinrotter/rssguard
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         rssguard-3.5.4-unbundle_qtsinglecoreapplication.patch

# Qt5WebEngine is only available on those architectures
ExclusiveArch:  %{qt5_qtwebengine_arches}

BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  qtsingleapplication-qt5-devel
BuildRequires:  qt5-linguist
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils


%description
RSS Guard is simple, light and easy-to-use RSS/ATOM feed aggregator developed 
using Qt framework which supports online feed synchronization.


%prep
%autosetup -p1 -n %{name}-%{version}

find src -type f | xargs chmod 0644
chmod 0644 resources/desktop/com.github.rssguard.appdata.xml
sed -i 's/\r$//' README.md
rm -rf src/qtsingleapplication

%build
mkdir build && pushd build
%{qmake_qt5} ../rssguard.pro -r LRELEASE_EXECUTABLE=lrelease-qt5 PREFIX=%{_prefix}
%make_build
popd


%install
pushd build
%make_install INSTALL_ROOT=%{buildroot}
popd


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.github.rssguard.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/com.github.rssguard.appdata.xml


%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/com.github.rssguard.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/metainfo/com.github.rssguard.appdata.xml


%changelog
* Wed Nov 01 2017 Robert-André Mauchin <zebob.m@gmail.com> 3.5.4-3
- Unbundle qtsinglecoreapplication
- Correct licensing

* Tue Oct 31 2017 Robert-André Mauchin <zebob.m@gmail.com> 3.5.4-2
- Added ExclusiveArch

* Tue Oct 31 2017 Robert-André Mauchin <zebob.m@gmail.com> 3.5.4-1
- First RPM release
