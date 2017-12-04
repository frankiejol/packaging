# Generated by rust2rpm
%bcond_without check

%global crate ripgrep

Name:           %{crate}
Version:        0.7.1
Release:        1%{?dist}
Summary:        Line oriented search tool using Rust's regex library. Combines the raw performance of grep with the usability of the silver searcher.

License:        Unlicense or MIT
URL:            https://crates.io/crates/ripgrep
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No simd
# * Bump memmap to 0.6, https://github.com/BurntSushi/ripgrep/pull/657
# * Bump bytecount to 0.2, https://github.com/BurntSushi/ripgrep/pull/679
Patch0:         ripgrep-0.7.1-fix-metadata.patch
# Really make code compatible with memmap v0.6
Patch1:         0001-Update-to-memmap-0.6.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(atty) >= 0.2.2 with crate(atty) < 0.3.0)
BuildRequires:  (crate(bytecount) >= 0.2.0 with crate(bytecount) < 0.3.0)
BuildRequires:  (crate(clap) >= 2.26.0 with crate(clap) < 3.0.0)
BuildRequires:  (crate(encoding_rs) >= 0.7.0 with crate(encoding_rs) < 0.8.0)
BuildRequires:  (crate(env_logger) >= 0.4.0 with crate(env_logger) < 0.5.0)
BuildRequires:  (crate(grep) >= 0.1.7 with crate(grep) < 0.2.0)
BuildRequires:  (crate(ignore) >= 0.3.1 with crate(ignore) < 0.4.0)
BuildRequires:  (crate(lazy_static) >= 0.2.0 with crate(lazy_static) < 0.3.0)
BuildRequires:  (crate(libc) >= 0.2.0 with crate(libc) < 0.3.0)
BuildRequires:  (crate(log) >= 0.3.0 with crate(log) < 0.4.0)
BuildRequires:  (crate(memchr) >= 2.0.0 with crate(memchr) < 3.0.0)
BuildRequires:  (crate(memmap) >= 0.6.0 with crate(memmap) < 0.7.0)
BuildRequires:  (crate(num_cpus) >= 1.0.0 with crate(num_cpus) < 2.0.0)
BuildRequires:  (crate(regex) >= 0.2.1 with crate(regex) < 0.3.0)
BuildRequires:  (crate(same-file) >= 1.0.0 with crate(same-file) < 2.0.0)
BuildRequires:  (crate(termcolor) >= 0.3.3 with crate(termcolor) < 0.4.0)
# [build-dependencies]
BuildRequires:  (crate(clap) >= 2.26.0 with crate(clap) < 3.0.0)
BuildRequires:  (crate(lazy_static) >= 0.2.0 with crate(lazy_static) < 0.3.0)
Requires:       bash-completion

%description
Line oriented search tool using Rust's regex library. Combines
the raw performance of grep with the usability of the silver searcher.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install
install -D -p -m0644 doc/rg.1 %{buildroot}%{_mandir}/man1/rg.1

# bash completion
install -D -p -m 644 target/release/build/%{name}-*/out/rg.bash-completion \
    %{buildroot}%{_datadir}/bash-completion/completions/rg

# fish completion
install -D -p -m 644 target/release/build/%{name}-*/out/rg.fish \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/rg.fish

# zsh completion
install -D -p -m 644 complete/_rg %{buildroot}%{_datadir}/zsh/vendor-completions/_rg

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE-MIT UNLICENSE COPYING
%doc README.md CHANGELOG.md
%{_bindir}/rg
%{_datadir}/bash-completion/completions/rg
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/rg.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/vendor-completions
%{_datadir}/zsh/vendor-completions/_rg
%{_mandir}/man1/rg.1*

%changelog
* Tue Nov 14 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.1-1
- Upstream release 0.7.1
* Sat Oct 14 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.0-2
- Fix directories ownership
* Sat Oct 14 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.0-1
- Initial package
