%bcond_without check

Name:       exa
Version:    0.7.0
Release:    2%{?dist}
Summary:    Replacement for ls written in Rust
        
License:    MIT
URL:        https://github.com/ogham/exa
Source0:    https://github.com/ogham/exa/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:     exa-0.7.0-fix_metadata.patch
Patch1:     exa-0.7.0-Makefile_fix.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  cmake
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  (crate(ansi_term) >= 0.9.0 with crate(ansi_term) < 0.10.0)
BuildRequires:  (crate(datetime) >= 0.4.3 with crate(datetime) < 0.5.0)
BuildRequires:  (crate(env_logger) >= 0.4 with crate(env_logger) < 0.5)
BuildRequires:  (crate(getopts) >= 0.2.14 with crate(getopts) < 0.3.0)
BuildRequires:  (crate(git2) >= 0.6.0 with crate(git2) < 0.7.0)
BuildRequires:  (crate(glob) >= 0.2 with crate(glob) < 0.3)
BuildRequires:  (crate(lazy_static) >= 0.2 with crate(lazy_static) < 0.3)
BuildRequires:  (crate(libc) >= 0.2.9 with crate(libc) < 0.3.0)
BuildRequires:  (crate(locale) >= 0.2.1 with crate(locale) < 0.3.0) 
BuildRequires:  (crate(log) >= 0.3 with crate(log) < 0.4) 
BuildRequires:  (crate(natord) >= 1.0.7 with crate(natord) < 1.1.0) 
BuildRequires:  (crate(num_cpus) >= 1.6.0 with crate(num_cpus) < 1.7.0) 
BuildRequires:  (crate(number_prefix) >= 0.2.3 with crate(number_prefix) < 0.3.0) 
BuildRequires:  (crate(scoped_threadpool) >= 0.1.0 with crate(scoped_threadpool) < 0.2.0) 
BuildRequires:  (crate(term_grid) >= 0.1.6 with crate(term_grid) < 0.2.0) 
BuildRequires:  (crate(term_size) >= 0.3.0 with crate(term_size) < 0.4.0) 
BuildRequires:  (crate(unicode-width) >= 0.1.4 with crate(unicode-width) < 0.2.0) 
BuildRequires:  (crate(users) >= 0.5.2 with crate(users) < 0.6.0) 
BuildRequires:  (crate(tz) >= 0.2.1 with crate(tz) < 0.3.0) 


%description
Replacement for ls written in Rust.


%prep
%autosetup -p1
rm Cargo.lock
%cargo_prep


%build
RUSTFLAGS+=-g %cargo_build


%install
%cargo_install
make install-man
make install-bash-completions PREFIX=/ DESTDIR=%{buildroot}
make install-zsh-completions PREFIX=/usr DESTDIR=%{buildroot}
make install-fish-completions PREFIX=/usr DESTDIR=%{buildroot}


%if %{with check}
%check
%cargo_test
%endif


%files
%doc README.md
%license LICENCE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/bash_completion.d/exa
%{_datadir}/fish/vendor_completions.d/exa.fish
%{_datadir}/zsh/vendor-completions/_exa


%changelog
* Sat Sep 02 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.7.0-2
- Update to Rust Packaging Guidelines
* Sat Aug 05 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.7.0-1
- Initial RPM package
