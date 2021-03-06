Name:           prename
Version:        1.9
Release:        4%{?dist}
Summary:        Perl script to rename multiple files
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/rename/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PE/PEDERST/rename-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/pstray/rename/master/LICENSE

# This patch renames the executable from rename to prename
Patch0:         %{name}-1.9-namechange.patch
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)


%description
Prename renames the file names supplied according to the rule specified as
the first argument. The argument is a Perl expression which is expected
to modify the $_ string for at least some of the file names specified.


%prep
%autosetup -p1 -n rename-%{version}
cp %{SOURCE1} .

%build
%__perl Makefile.PL PREFIX=%{_prefix} NO_PACKLIST=1
%make_build


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*


%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Aug 18 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.9-4
- Added LICENSE from upstream

* Tue Jul 25 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.9-3
- Fix for Fedora Review

* Thu Jul 20 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.9-2
- Update to Fedora Packaging Guidelines specification

* Mon Oct 17 2016 Robert-André Mauchin <zebob.m@gmail.com> 1.9-1
- Initial release
