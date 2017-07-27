# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 1
# Run tests in check section
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

Name:           rclone
Version:        1.37
Release:        1%{?dist}
Summary:        rsync for cloud storage
License:        MIT 
URL:            http://rclone.org/
Source0:        https://github.com/ncw/rclone/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  golang >= 1.5
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

%description
Rclone is a command line program to sync files and directories to and 
from various cloud services.


%prep
%autosetup -p1 -n %{name}-%{version}

%{__rm} -rf vendor

%build
mkdir -p ./_build/src/github.com/ncw/
ln -s $(pwd) ./_build/src/github.com/ncw/rclone
export GOPATH=$(pwd)/_build:%{gopath}

# *** ERROR: No build ID note found in /.../BUILDROOT/etcd-2.0.0-1.rc1.fc22.x86_64/usr/bin/etcd
function gobuild { go build -a -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')" -v -x "$@"; }

gobuild -o rclone


%install
install -p -D -m 0755 ./rclone %{buildroot}%{_bindir}/rclone
install -p -D -m 0644 ./rclone.1 %{buildroot}%{_mandir}/man1/rclone.1

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

%check
%if 0%{?with_check} && 0%{?with_unit_test}
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

%files
%license COPYING
%doc RELEASE.md README.md MANUAL.md MAINTAINERS.md ISSUE_TEMPLATE.md CONTRIBUTING.md
%{_bindir}/rclone
%{_mandir}/man1/rclone.1*


%changelog
* Sun Jul 23 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.37.1
- Update to version 1.37
* Thu Jul 20 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.36-2
- Update to Fedora Packaging Guidelines specification
* Sat Mar 25 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.36-1
- Update to version 1.36
* Fri Jan 06 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.35-1
- Update to version 1.35
* Sun Dec 11 2016 Robert-André Mauchin <zebob.m@gmail.com> - 1.34-1
- Initial RPM release

