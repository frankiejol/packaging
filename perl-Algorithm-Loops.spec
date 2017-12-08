Name:           perl-Algorithm-Loops
Version:        1.032
Release:        1%{?dist}
Summary:        Perl module for looping constructs
License:        Unlicense
URL:            http://search.cpan.org/dist/Algorithm-Loops/
Source0:        https://www.cpan.org/authors/id/T/TY/TYEMQ/Algorithm-Loops-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(Exporter)
Requires:       perl(strict)
Requires:       perl(vars)
Requires:       perl(warnings)

%description
Looping constructs: NestedLoops, MapCar*, Filter, and NextPermute*

%prep
%autosetup -n Algorithm-Loops-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.txt
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 06 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.032-1
- Specfile autogenerated by cpanspec 1.78.