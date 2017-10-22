# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 1
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 0
# Run tests in check section
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif


%global provider        github
%global provider_tld    com
%global project         zyedidia
%global repo            tcell
# https://github.com/zyedidia/tcell
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          c47e75564a5c5e7fb5c7e5ec5b341c7902d551bc
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20170919

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Alternate terminal package, similar to termbox
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}



%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/gdamore/encoding)
BuildRequires: golang(github.com/lucasb-eyer/go-colorful)
BuildRequires: golang(github.com/mattn/go-runewidth)
BuildRequires: golang(golang.org/x/text/encoding)
BuildRequires: golang(golang.org/x/text/encoding/charmap)
BuildRequires: golang(golang.org/x/text/encoding/japanese)
BuildRequires: golang(golang.org/x/text/encoding/korean)
BuildRequires: golang(golang.org/x/text/encoding/simplifiedchinese)
BuildRequires: golang(golang.org/x/text/encoding/traditionalchinese)
BuildRequires: golang(golang.org/x/text/transform)
%endif

Requires:      golang(github.com/gdamore/encoding)
Requires:      golang(github.com/lucasb-eyer/go-colorful)
Requires:      golang(github.com/mattn/go-runewidth)
Requires:      golang(golang.org/x/text/encoding)
Requires:      golang(golang.org/x/text/encoding/charmap)
Requires:      golang(golang.org/x/text/encoding/japanese)
Requires:      golang(golang.org/x/text/encoding/korean)
Requires:      golang(golang.org/x/text/encoding/simplifiedchinese)
Requires:      golang(golang.org/x/text/encoding/traditionalchinese)
Requires:      golang(golang.org/x/text/transform)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/encoding) = %{version}-%{release}
Provides:      golang(%{import_path}/termbox) = %{version}-%{release}
Provides:      golang(%{import_path}/views) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/smartystreets/goconvey/convey)
%endif

Requires:      golang(github.com/smartystreets/goconvey/convey)

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%autosetup -n %{repo}-%{commit}

%build
%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
# No dependency directories so far

export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc TERMINALS.md README.md AUTHORS
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc TERMINALS.md README.md AUTHORS
%endif

%changelog
* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170919git7095cc1
- First package for Fedora

