%global _dwz_low_mem_die_limit 0

Name:           powerline-go
Version:        1.5.1
Release:        1%{?dist}
Summary:        A beautiful and useful low-latency prompt for your shell, written in go
License:        GPLv3 
URL:            https://github.com/justjanne/powerline-go
Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/text/width)

%description
A Powerline like prompt for Bash, ZSH and Fish.

 - Shows some important details about the git/hg branch
 - Changes color if the last command exited with a failure code
 - If you're too deep into a directory tree, shortens the displayed 
   path with an ellipsis
 - Shows the current Python virtualenv environment
 - It's easy to customize and extend.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
mkdir -p ./_build/src/github.com/justjanne/
ln -s $(pwd) ./_build/src/github.com/justjanne/powerline-go
export GOPATH=$(pwd)/_build:%{gopath}

%gobuild -o powerline-go


%install
install -p -D -m 0755 ./powerline-go %{buildroot}%{_bindir}/powerline-go


%files
%license LICENSE.md
%doc README.md
%{_bindir}/powerline-go


%changelog
* Sat Sep 02 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.1-1
- Upstream release v1.5.1
* Fri Sep 01 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.0-1
- Initial RPM release

