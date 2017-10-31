Name:           rssguard
Version:        3.5.4
Release:        2%{?dist}
Summary:        Simple yet powerful feed reader

License:        GPLv3+
URL:            https://github.com/martinrotter/rssguard
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Qt5WebEngine is only available on those architectures
ExclusiveArch:  %{qt5_qtwebengine_arches}

BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5WebEngine)
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

%build
mkdir build && pushd build
%{qmake_qt5} ../rssguard.pro -r CONFIG+=debug LRELEASE_EXECUTABLE=lrelease-qt5 PREFIX=%{_prefix}
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
* Tue Oct 31 2017 Robert-André Mauchin <zebob.m@gmail.com> 3.5.4-2
- Added ExclusiveArch
* Tue Oct 31 2017 Robert-André Mauchin <zebob.m@gmail.com> 3.5.4-1
- First RPM release
