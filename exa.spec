Name:		exa
Version:	0.7.0
Release:	1%{?dist}
Summary:	Replacement for ls written in Rust
		
License:	MIT
URL:		https://github.com/ogham/exa
Source0:	https://github.com/ogham/exa/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:		exa-0.7.0_Makefile_fix.patch

ExclusiveArch:  %{?rust_arches:%{rust_arches}}%{!?rust_arches:%{ix86} x86_64 aarch64 ppc64 ppc64le s390x %{arm}}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:	pkgconfig(libgit2)
BuildRequires:  pkgconfig(zlib)


%description
Replacement for ls written in Rust.


%prep
%autosetup -p1


%build
RUSTFLAGS+=-g cargo build --release %{?_smp_mflags}


%install
%make_install PREFIX=/usr
make install-bash-completions PREFIX=/ DESTDIR=%{buildroot}
make install-zsh-completions PREFIX=/usr DESTDIR=%{buildroot}
make install-fish-completions PREFIX=/usr DESTDIR=%{buildroot}


%files
%doc README.md
%license LICENCE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/bash_completion.d/exa
%{_datadir}/fish/vendor_completions.d/exa.fish
%{_datadir}/zsh/vendor-completions/_exa


%changelog
* Sat Aug 05 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.7.0-1
- Initial RPM package
