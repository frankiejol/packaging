# Build with debug info rpm
%global with_debug 0

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

Name:           jid
Version:        0.7.2
Release:        1%{?dist}
Summary:        Json Incremental Digger
License:        MIT
URL:            https://github.com/simeji/jid
Source0:        https://github.com/simeji/jid/archive/%{version}/%{name}-%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

BuildRequires: golang(github.com/bitly/go-simplejson)
BuildRequires: golang(github.com/fatih/color)
BuildRequires: golang(github.com/mattn/go-runewidth)
BuildRequires: golang(github.com/nsf/termbox-go)
BuildRequires: golang(github.com/nwidger/jsoncolor)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(github.com/shiena/ansicolor)

%description
Json Incremental Digger is a very simple json querying tool.

You can drill down JSON interactively by using filtering queries like jq.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir -p ./_build/src/github.com/simeji/
ln -s $(pwd) ./_build/src/github.com/simeji/jid
export GOPATH=$(pwd)/_build:%{gopath}

%gobuild -o jid ./cmd/jid

%install
install -p -D -m 0755 ./jid %{buildroot}%{_bindir}/jid

%files
%license LICENSE
%doc ChangeLog README.md
%{_bindir}/jid

%changelog
* Sat Nov 25 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.2-1
- First package for Fedora

