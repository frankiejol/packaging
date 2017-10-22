# Generated by rust2rpm
%bcond_with check

%global crate exa

Name:           %{crate}
Version:        0.8.0
Release:        2%{?dist}
Summary:        A modern replacement for ls

License:        MIT
URL:            https://crates.io/crates/exa
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

Patch0:         exa-0.8.0-directory_fix.patch
Patch1:         exa-0.8.0-fix_metadata.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(ansi_term) >= 0.10.0 with crate(ansi_term) < 0.11.0)
BuildRequires:  (crate(datetime) >= 0.4.5 with crate(datetime) < 0.5.0)
BuildRequires:  (crate(env_logger) >= 0.4.0 with crate(env_logger) < 0.5.0)
BuildRequires:  (crate(getopts) >= 0.2.14 with crate(getopts) < 0.3.0)
BuildRequires:  (crate(git2) >= 0.6.4 with crate(git2) < 0.7.0)
BuildRequires:  (crate(glob) >= 0.2.0 with crate(glob) < 0.3.0)
BuildRequires:  (crate(lazy_static) >= 0.2.0 with crate(lazy_static) < 0.3.0)
BuildRequires:  (crate(libc) >= 0.2.9 with crate(libc) < 0.3.0)
BuildRequires:  (crate(locale) >= 0.2.1 with crate(locale) < 0.3.0)
BuildRequires:  (crate(log) >= 0.3.0 with crate(log) < 0.4.0)
BuildRequires:  (crate(natord) >= 1.0.7 with crate(natord) < 2.0.0)
BuildRequires:  (crate(num_cpus) >= 1.3.0 with crate(num_cpus) < 2.0.0)
BuildRequires:  (crate(number_prefix) >= 0.2.3 with crate(number_prefix) < 0.3.0)
BuildRequires:  (crate(scoped_threadpool) >= 0.1.0 with crate(scoped_threadpool) < 0.2.0)
BuildRequires:  (crate(term_grid) >= 0.1.6 with crate(term_grid) < 0.2.0)
BuildRequires:  (crate(term_size) >= 0.3.0 with crate(term_size) < 0.4.0)
BuildRequires:  (crate(unicode-width) >= 0.1.4 with crate(unicode-width) < 0.2.0)
BuildRequires:  (crate(users) >= 0.6.0 with crate(users) < 0.7.0)
BuildRequires:  (crate(zoneinfo_compiled) >= 0.4.5 with crate(zoneinfo_compiled) < 0.5.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  %{_bindir}/cmake
BuildRequires:  bash-completion

%description
%{summary}.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%make_install PREFIX=/usr
make install-man PREFIX=/usr DESTDIR=%{buildroot}
make install-bash-completions DESTDIR=%{buildroot}
make install-zsh-completions DESTDIR=%{buildroot}
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
%{_datadir}/bash-completion/completions/exa
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/exa.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/vendor-completions
%{_datadir}/zsh/vendor-completions/_exa

%changelog
* Sat Oct 14 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.0-2
- Fix directories ownership
* Fri Oct 13 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.0-1
- Upstream release 0.8.0
* Sat Sep 02 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.7.0-2
- Update to Rust Packaging Guidelines
* Sat Aug 05 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.7.0-1
- Initial RPM package

