Summary:    Wallpaper changer that automatically downloads wallpapers
Name:       variety
Version:    0.6.4
Release:    2%{?dist}
License:    GPLv3
Url:        https://launchpad.net/variety
Source0:    https://launchpad.net/variety/trunk/0.6.4/+download/variety_0.6.4-0-589-201704290523.tar.gz
# https://bugs.launchpad.net/variety/+bug/1705199
Source1:    %{name}-README
Source2:    %{name}.appdata.xml
BuildArch:  noarch

BuildRequires:  python2-devel 
BuildRequires:  python-setuptools 
BuildRequires:  python-distutils-extra
BuildRequires:  python-appindicator
BuildRequires:  python-beautifulsoup4 
BuildRequires:  python-configobj 
BuildRequires:  python-lxml
BuildRequires:  python2-gexiv2
BuildRequires:  python-pycurl
BuildRequires:  python2-requests
BuildRequires:  python-pillow-devel
BuildRequires:  python-imaging-devel
BuildRequires:  pyexiv2 
BuildRequires:  intltool 
BuildRequires:  yelp-devel
BuildRequires:  dbus-python
BuildRequires:  pkgconfig(pycairo)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
%if 0%{?fedora} <= 26
BuildRequires:  webkitgtk-devel
%endif
Requires:       python-lxml
Requires:       python-pillow
Requires:       pycairo
Requires:       dbus-python
Requires:       python-appindicator
Requires:       python-beautifulsoup4 
Requires:       python-configobj
Requires:       python2-gexiv2
Requires:       python-pycurl
Requires:       python2-requests
Requires:       pyexiv2
Requires:       imagemagick
Requires:       hicolor-icon-theme


%description
Variety changes the desktop wallpaper on a regular basis, 
using user-specified or automatically downloaded images.

Variety sits conveniently as an indicator in the panel 
and can be easily paused and resumed. The mouse wheel 
can be used to scroll wallpapers back and forth until 
you find the perfect one for your current mood.

Apart from displaying images from local folders, several 
different online sources can be used to fetch wallpapers 
according to user-specified criteria.

Variety can also automatically apply various fancy 
filters to the displayed images - charcoal painting, 
oil painting, heavy blurring, etc. - so that your 
desktop is always fresh and unique. 



%prep
%autosetup -n %{name}-%{version}
cp -p %{SOURCE1} ./README

# remove debian part
rm -rf debian

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --root=%{buildroot}

install -Dp -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

chmod a+x %{buildroot}%{_datadir}/%{name}/scripts/install_ssl_deps.sh

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    

%files -f %{name}.lang
%doc README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{python2_sitelib}/jumble/
%{python2_sitelib}/%{name}-*-py*.egg-info
%{python2_sitelib}/%{name}/
%{python2_sitelib}/%{name}_lib/
%{_datadir}/help/C/%{name}/
%{_datadir}/icons/hicolor/22x22/apps/%{name}-indicator-dark.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}-indicator.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Sat Jun 24 2017 Robert-André Mauchin zebob.m@gmail.com> - 0.6.4-2
- Fix dependency issue reported.

* Sat Jun 24 2017 Robert-André Mauchin zebob.m@gmail.com> - 0.6.4-1
- Updated to 0.6.4

* Fri Jan 20 2017 Robert-André Mauchin zebob.m@gmail.com> - 0.6.3-2
- Fix webkitgtk requirement

* Fri Jan 20 2017 Robert-André Mauchin zebob.m@gmail.com> - 0.6.3-1
- Updated to 0.6.3

* Mon Apr 18 2016 David Vásquez <davidjeremias82@gmail.com> 0.6.0-1
- Updated 0.6.0

* Mon Oct 05 2015 David Vásquez <davidjeremias82@gmail.com> - 0.5.3-1
- Updated to 0.5.5

* Wed Apr 22 2015 David Vásquez <davidjeremias82@gmail.com> - 0.5.3-1
- Updated to 0.5.3

* Thu Jan 08 2015 David Vásquez <davidjeremias82@gmail.com> - 0.5.0-1
- Updated to 0.5.0

* Sat Jul 19 2014 David Vásquez <davidjeremias82@gmail.com> - 0.4.20-1
- Updated to 0.4.20

* Thu Jul 10 2014 David Vásquez <davidjeremias82@gmail.com> - 0.4.18-1
- Updated to 0.4.18

* Thu Dec 19 2013 David Vásquez <davidjeremias82@gmail.com> - 0.4.17-3
- Added some requires

* Thu Nov 7 2013 David Vásquez <davidjeremias82@gmail.com> - 0.4.17-1
- Updated to 0.4.17

* Thu Jun 13 2013 David Vásquez <davidjeremias82@gmail.com> - 0.4.15-1
- Initial build rpm
