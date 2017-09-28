%global altname ZeGrapher

Name:           zegrapher
Summary:        Free and opensource math graphing software
Version:        3.0.1
Release:        2%{?dist}
License:        GPLv3+

URL:            https://www.zegrapher.com/
Source0:        https://github.com/AdelKS/%{altname}/archive/v%{version}/%{altname}-%{version}.tar.gz

#https://github.com/AdelKS/ZeGrapher/pull/5
Patch0:         0001-add_appstream_file.patch
#https://github.com/AdelKS/ZeGrapher/pull/4
Patch1:         0002-add_install_method.patch
#https://github.com/AdelKS/ZeGrapher/pull/6
Patch2:         0003-fix_desktop_file.patch
#https://github.com/AdelKS/ZeGrapher/pull/7
Patch3:         0004-fix_permissions.patch

BuildRequires:  boost-devel
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib


%description
ZeGrapher is a plotting program for functions, sequences, parametric equations, 
and tabular data. It has been designed to be as easy to use as possible.

ZeGrapher supports importing and exporting of tabular data from and to CSV files
and polynomial (regression) fits, plotting of tangents (the point can be 
selected interactively). Calculation and plotting of derivatives and integrals 
is also possible.

Plots can be exported in various image formats and as PDF files.


%prep
%autosetup -p1 -n %{altname}-%{version}
sed -i 's|^QMAKE_LFLAGS_RELEASE = -s|QMAKE_LFLAGS_RELEASE =|' ZeGrapher.pro

# To remove when Patch1 is through:
cp icons/software.png icons/%{altname}.png

%build
mkdir build && pushd build
%qmake_qt5 ../ PREFIX=%{_prefix}
%make_build
popd


%install
pushd build
%make_install INSTALL_ROOT=%{buildroot}
popd

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{altname}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{altname}.appdata.xml

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
%doc README.md
%license LICENSE
%{_bindir}/%{altname}
%{_datadir}/appdata/%{altname}.appdata.xml
%{_datadir}/applications/%{altname}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{altname}.png
%dir %{_datadir}/%{altname}
%{_datadir}/%{altname}/locale


%changelog
* Tue Sep 26 2017 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.1-2
- Added patches to fix permissions, fix desktop file, add appdata and add install method

* Mon Sep 25 2017 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.1-1
- Initial package.


