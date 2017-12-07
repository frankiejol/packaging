# Build with debug info rpm
%global with_debug 0

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

Name:           micro
Version:        1.3.4
Release:        1%{?dist}
Summary:        A modern and intuitive terminal-based text editor
License:        MIT 
URL:            https://micro-editor.github.io/
Source0:        https://github.com/zyedidia/micro/archive/v%{version}/%{name}-%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

BuildRequires: golang(gopkg.in/yaml.v2)
BuildRequires: golang(github.com/blang/semver)
BuildRequires: golang(github.com/dustin/go-humanize)
BuildRequires: golang(github.com/flynn/json5)
BuildRequires: golang(github.com/gdamore/encoding)
BuildRequires: golang(github.com/go-errors/errors)
BuildRequires: golang(github.com/lucasb-eyer/go-colorful)
BuildRequires: golang(github.com/mattn/go-isatty)
BuildRequires: golang(github.com/mattn/go-runewidth)
BuildRequires: golang(github.com/mitchellh/go-homedir)
BuildRequires: golang(github.com/sergi/go-diff)
BuildRequires: golang(github.com/yuin/gopher-lua)
BuildRequires: golang(github.com/zyedidia/clipboard)
BuildRequires: golang(github.com/zyedidia/glob)
BuildRequires: golang(github.com/zyedidia/poller)
BuildRequires: golang(github.com/zyedidia/tcell)
BuildRequires: golang(layeh.com/gopher-luar)


%description
Micro is a terminal-based text editor that aims to be easy to use and 
intuitive, while also taking advantage of the full capabilities of modern 
terminals. It comes as one single, batteries-included, static binary with no 
dependencies, and you can download and use it right now.

As the name indicates, micro aims to be somewhat of a successor to the nano 
editor by being easy to install and use in a pinch, but micro also aims to be 
enjoyable to use full time, whether you work in the terminal because you prefer 
it (like me), or because you need to (over ssh).


%prep
%autosetup -p1 -n %{name}-%{version}

rm -rf micro/cmd/micro/vendor/


%build
mkdir -p ./_build/src/github.com/zyedidia/
ln -s $(pwd) ./_build/src/github.com/zyedidia/micro
export GOPATH=$(pwd)/_build:%{gopath}

%gobuild -o micro ./cmd/micro


%install
install -p -D -m 0755 ./micro %{buildroot}%{_bindir}/micro


%files
%license LICENSE
%doc README.md
%{_bindir}/micro


%changelog
* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.4-1
- Upstream release 1.3.4

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.3-1
- Initial RPM release

