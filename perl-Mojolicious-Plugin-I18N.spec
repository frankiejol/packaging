Name:           perl-Mojolicious-Plugin-I18N
Version:        1.6
Release:        1%{?dist}
Summary:        Internationalization Plugin for Mojolicious
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Mojolicious-Plugin-I18N/
Source0:        https://www.cpan.org/authors/id/S/SH/SHARIFULN/Mojolicious-Plugin-I18N-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(I18N::LangTags) >= 0.35
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mojolicious) >= 5
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Mojolicious::Plugin::I18N is internationalization plugin for Mojolicious It
works with Mojolicious 4.0+.

%prep
%autosetup -n Mojolicious-Plugin-I18N-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes script
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 04 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.6-1
- Specfile autogenerated by cpanspec 1.78.
