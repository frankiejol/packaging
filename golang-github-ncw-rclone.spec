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
%global project         ncw
%global repo            rclone
# https://github.com/ncw/rclone
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          1ecf2bcbd55b714771165876b8cd6100ec3213d1
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        !!!!FILL!!!!
# Detected licences
# - MIT/X11 (BSD like) at 'COPYING'
License:        !!!!FILL!!!!
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
BuildRequires: golang(bazil.org/fuse)
BuildRequires: golang(bazil.org/fuse/fs)
BuildRequires: golang(github.com/Unknwon/goconfig)
BuildRequires: golang(github.com/VividCortex/ewma)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/corehandlers)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
BuildRequires: golang(github.com/billziss-gh/cgofuse/fuse)
BuildRequires: golang(github.com/jlaffaye/ftp)
BuildRequires: golang(github.com/ncw/dropbox-sdk-go-unofficial/dropbox)
BuildRequires: golang(github.com/ncw/dropbox-sdk-go-unofficial/dropbox/files)
BuildRequires: golang(github.com/ncw/go-acd)
BuildRequires: golang(github.com/ncw/swift)
BuildRequires: golang(github.com/nsf/termbox-go)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(github.com/pkg/sftp)
BuildRequires: golang(github.com/rfjakob/eme)
BuildRequires: golang(github.com/skratchdot/open-golang/open)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/cobra/doc)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(github.com/stretchr/testify/require)
BuildRequires: golang(github.com/xanzy/ssh-agent)
BuildRequires: golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires: golang(golang.org/x/crypto/scrypt)
BuildRequires: golang(golang.org/x/crypto/ssh)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(golang.org/x/text/unicode/norm)
BuildRequires: golang(golang.org/x/time/rate)
BuildRequires: golang(google.golang.org/api/drive/v2)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(google.golang.org/api/storage/v1)
%endif

Requires:      golang(bazil.org/fuse)
Requires:      golang(bazil.org/fuse/fs)
Requires:      golang(github.com/Unknwon/goconfig)
Requires:      golang(github.com/VividCortex/ewma)
Requires:      golang(github.com/aws/aws-sdk-go/aws)
Requires:      golang(github.com/aws/aws-sdk-go/aws/awserr)
Requires:      golang(github.com/aws/aws-sdk-go/aws/corehandlers)
Requires:      golang(github.com/aws/aws-sdk-go/aws/credentials)
Requires:      golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
Requires:      golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
Requires:      golang(github.com/aws/aws-sdk-go/aws/request)
Requires:      golang(github.com/aws/aws-sdk-go/aws/session)
Requires:      golang(github.com/aws/aws-sdk-go/service/s3)
Requires:      golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
Requires:      golang(github.com/billziss-gh/cgofuse/fuse)
Requires:      golang(github.com/jlaffaye/ftp)
Requires:      golang(github.com/ncw/dropbox-sdk-go-unofficial/dropbox)
Requires:      golang(github.com/ncw/dropbox-sdk-go-unofficial/dropbox/files)
Requires:      golang(github.com/ncw/go-acd)
Requires:      golang(github.com/ncw/swift)
Requires:      golang(github.com/nsf/termbox-go)
Requires:      golang(github.com/pkg/errors)
Requires:      golang(github.com/pkg/sftp)
Requires:      golang(github.com/rfjakob/eme)
Requires:      golang(github.com/skratchdot/open-golang/open)
Requires:      golang(github.com/spf13/cobra)
Requires:      golang(github.com/spf13/cobra/doc)
Requires:      golang(github.com/spf13/pflag)
Requires:      golang(github.com/stretchr/testify/assert)
Requires:      golang(github.com/stretchr/testify/require)
Requires:      golang(github.com/xanzy/ssh-agent)
Requires:      golang(golang.org/x/crypto/nacl/secretbox)
Requires:      golang(golang.org/x/crypto/scrypt)
Requires:      golang(golang.org/x/crypto/ssh)
Requires:      golang(golang.org/x/crypto/ssh/terminal)
Requires:      golang(golang.org/x/net/context)
Requires:      golang(golang.org/x/net/html)
Requires:      golang(golang.org/x/oauth2)
Requires:      golang(golang.org/x/oauth2/google)
Requires:      golang(golang.org/x/sys/unix)
Requires:      golang(golang.org/x/text/unicode/norm)
Requires:      golang(golang.org/x/time/rate)
Requires:      golang(google.golang.org/api/drive/v2)
Requires:      golang(google.golang.org/api/googleapi)
Requires:      golang(google.golang.org/api/storage/v1)

Provides:      golang(%{import_path}/amazonclouddrive) = %{version}-%{release}
Provides:      golang(%{import_path}/b2) = %{version}-%{release}
Provides:      golang(%{import_path}/b2/api) = %{version}-%{release}
Provides:      golang(%{import_path}/box) = %{version}-%{release}
Provides:      golang(%{import_path}/box/api) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/all) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/authorize) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/cat) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/check) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/cleanup) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/cmount) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/config) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/copy) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/copyto) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/cryptcheck) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/dbhashsum) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/dedupe) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/delete) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/genautocomplete) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/gendocs) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/info) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/listremotes) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/ls) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/ls2) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/lsd) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/lsjson) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/lsl) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/md5sum) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/memtest) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/mkdir) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/mount) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/mountlib) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/mountlib/mounttest) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/move) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/moveto) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/ncdu) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/ncdu/scan) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/obscure) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/purge) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/rmdir) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/rmdirs) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/sha1sum) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/size) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/sync) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/version) = %{version}-%{release}
Provides:      golang(%{import_path}/crypt) = %{version}-%{release}
Provides:      golang(%{import_path}/crypt/pkcs7) = %{version}-%{release}
Provides:      golang(%{import_path}/dircache) = %{version}-%{release}
Provides:      golang(%{import_path}/drive) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/dbhash) = %{version}-%{release}
Provides:      golang(%{import_path}/fs) = %{version}-%{release}
Provides:      golang(%{import_path}/fs/all) = %{version}-%{release}
Provides:      golang(%{import_path}/fstest) = %{version}-%{release}
Provides:      golang(%{import_path}/fstest/fstests) = %{version}-%{release}
Provides:      golang(%{import_path}/ftp) = %{version}-%{release}
Provides:      golang(%{import_path}/googlecloudstorage) = %{version}-%{release}
Provides:      golang(%{import_path}/http) = %{version}-%{release}
Provides:      golang(%{import_path}/hubic) = %{version}-%{release}
Provides:      golang(%{import_path}/local) = %{version}-%{release}
Provides:      golang(%{import_path}/oauthutil) = %{version}-%{release}
Provides:      golang(%{import_path}/onedrive) = %{version}-%{release}
Provides:      golang(%{import_path}/onedrive/api) = %{version}-%{release}
Provides:      golang(%{import_path}/pacer) = %{version}-%{release}
Provides:      golang(%{import_path}/rest) = %{version}-%{release}
Provides:      golang(%{import_path}/s3) = %{version}-%{release}
Provides:      golang(%{import_path}/sftp) = %{version}-%{release}
Provides:      golang(%{import_path}/swift) = %{version}-%{release}
Provides:      golang(%{import_path}/yandex) = %{version}-%{release}
Provides:      golang(%{import_path}/yandex/api) = %{version}-%{release}

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
%endif


%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%{__rm} -rf vendor

%build
%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go" | grep -v "vendor") ; do
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
for file in $(find . -iname "*_test.go" | grep -v "vendor") ; do
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
# Since we aren't packaging up the vendor directory we need to link
# back to it somehow. Hack it up so that we can add the vendor
# directory from BUILD dir as a gopath to be searched when executing
# tests from the BUILDROOT dir.
ln -s ./ ./vendor/src # ./vendor/src -> ./vendor

export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/amazonclouddrive
%gotest %{import_path}/b2
%gotest %{import_path}/b2/api
%gotest %{import_path}/box
%gotest %{import_path}/cmd/cmount
%gotest %{import_path}/cmd/mount
%gotest %{import_path}/crypt
%gotest %{import_path}/crypt/pkcs7
%gotest %{import_path}/drive
%gotest %{import_path}/dropbox
%gotest %{import_path}/dropbox/dbhash
%gotest %{import_path}/fs
%gotest %{import_path}/ftp
%gotest %{import_path}/googlecloudstorage
%gotest %{import_path}/http
%gotest %{import_path}/hubic
%gotest %{import_path}/local
%gotest %{import_path}/onedrive
%gotest %{import_path}/pacer
%gotest %{import_path}/s3
%gotest %{import_path}/sftp
%gotest %{import_path}/swift
%gotest %{import_path}/yandex
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%license COPYING
%doc RELEASE.md README.md MANUAL.md MAINTAINERS.md ISSUE_TEMPLATE.md CONTRIBUTING.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license COPYING
%doc RELEASE.md README.md MANUAL.md MAINTAINERS.md ISSUE_TEMPLATE.md CONTRIBUTING.md
%endif

%changelog* Mon Jul 24 2017 root - 0-0.1.git1ecf2bc
- First package for Fedora

