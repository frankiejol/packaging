Name:           sparkleshare
Version:        2.0.0
Release:        1%{?dist}
Summary:        Easy file sharing based on git repositories

License:        GPLv3
URL:            http://www.sparkleshare.org/
Source0:        https://github.com/hbons/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         sparkleshare-2.0.0-fix_build.patch

BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(webkit2-sharp-4.0)
BuildRequires:  pkgconfig(gtk-sharp-3.0)
BuildRequires:  pkgconfig(notify-sharp-3.0)
BuildRequires:  pkgconfig(appindicator-sharp-0.1)
BuildRequires:  gvfs
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  gettext
Requires:       git >= 1.7.12
Requires:       yelp

ExclusiveArch:  %{mono_arches}


#https://fedoraproject.org/wiki/Packaging:Mono#Empty_debuginfo
%global debug_package %{nil}


%description
Easy file sharing based on git repositories. A special folder is setup and
directories/files placed within are placed in a git-based version control
system and synchronized elsewhere.


%prep
%autosetup -p1 -n SparkleShare-%{version}

%build
./autogen.sh
%configure
%make_build

%install
%make_install

chmod 0644 legal/*.txt News.txt

desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

mkdir -p %{buildroot}%{_datarootdir}/appdata/
install -m 644 \
    %{_builddir}/SparkleShare-%{version}/SparkleShare/Linux/org.sparkleshare.SparkleShare.appdata.xml \
    %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

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
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/SparkleShare.Autostart.desktop
%{_datadir}/applications/org.sparkleshare.SparkleShare.Invites.desktop
%{_datadir}/applications/org.sparkleshare.SparkleShare.desktop
%{_datadir}/icons/hicolor/symbolic/apps/org.sparkleshare.SparkleShare-symbolic.svg
%{_datadir}/icons/hicolor/*/apps/org.sparkleshare.SparkleShare.png
%{_datadir}/icons/ubuntu-mono-dark/status/24/*
%{_datadir}/icons/ubuntu-mono-light/status/24/*
%doc legal/Authors.txt legal/CODE_OF_CONDUCT.md News.txt README.md
%license legal/License_for_SparkleShare.txt


%changelog
* Sun Sep 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- mono rebuild for aarch64 support

* Mon Jun 06 2016 Nikos Roussos <comzeradd@fedoraproject.org> 1.2.0-6
- Fix mcs path

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 6 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> 1.2.0-4
- Another fix for mono4

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0-2
- Rebuild (mono4)

* Tue Sep 23 2014 Nikos Roussos <comzeradd@fedoraproject.org> 1.2.0-1
- Update to 1.2.0

* Thu Sep 19 2013 Nikos Roussos <comzeradd@fedoraproject.org> 1.1.0-3
- Add appdata file.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Nikos Roussos <comzeradd@fedoraproject.org> 1.1.0-1
- Update to 1.1.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Nikos Roussos <comzeradd@fedoraproject.org> 1.0.0-1
- Update to 1.0.9

* Mon Dec 03 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.9-1
- Update to 0.9.9

* Tue Nov 20 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.8-1
- Update to 0.9.8

* Wed Nov 07 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.6-1
- Update to 0.9.6

* Sat Oct 20 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.4-1
- Update to 0.9.4

* Sun Sep 30 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.3-1
- Update to 0.9.3

* Sun Sep 02 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.2-1
- Update to 0.9.2

* Tue Aug 28 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.1-1
- Update to 0.9.1

* Thu Jul 05 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.0-1
- Update to 0.9.0

* Wed Mar 21 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.4-2
- Patch to comment the misplaced update-desktop-database

* Mon Mar 19 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.4-1
- Update to 0.8.4

* Mon Mar 12 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.3-1
- Update to 0.8.3

* Fri Mar 02 2012 Dan Horák <dan[at]danny.cz> 0.8.0-4
- set ExclusiveArch

* Thu Mar 01 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.0-3
- added nautilus-python as dependency

* Tue Feb 14 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.0-2
- gettext added as buildrequirement, permissions error fixes

* Wed Feb 01 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.0-1
- Update to 0.8.0

* Wed Jun 29 2011 fedora@alexhudson.com - 0.2.4-1
- rebuilt for new upstrema 0.2.4

* Wed Jun 15 2011 Alex Hudson <fedora@alexhudson.com> - 0.2.2-1
- rebuilt for new upstream 0.2.2

* Wed Jun 08 2011 Alex Hudson <fedora@alexhudson.com> - 0.2.1-1
- rebuilt for new upstream 0.2.1

* Tue Jun 07 2011 Alex Hudson - 0.2.0-1
- initial release of 0.2!

* Sat May 21 2011 Alex Hudson <fedora@alexhudson.com> - 0.2.beta2rc2-3
- remove nautilus extension for now; causes segfaults in F15 :(

* Fri May 20 2011 Alex Hudson <fedora@alexhudson.com> - 0.2.beta2rc2-2
- rebuilt to address python errors in F15

* Fri Mar 25 2011 Alex Hudson - 0.2.beta2rc1-1
- Initial build of 0.2rc1

* Mon Nov 22 2010 Alex Hudson - 0.2.beta1-7
- rebuilt

* Sat Nov 20 2010 Alex Hudson - 0.2.beta1-3
- rebuilt

* Thu Sep 02 2010 Alex Hudson - 0.2.alpha2-5
- update from git; now includes end-user help

* Tue Aug 17 2010 Alex Hudson - 0.2.alpha2-4
- now includes man page and new icons

* Mon Aug 16 2010 Alex Hudson - 0.2.alpha2-3
- slightly cleaner wrt. rpmlint

* Sat Aug 07 2010 Alex Hudson - 0.2.alpha1-2
- various fixes from git post-alpha release

* Tue Aug 03 2010 Alex Hudson - 0.2.alpha1-1
- Initial release of the 0.2alpha series of SparkleShare
