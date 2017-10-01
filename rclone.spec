%global _dwz_low_mem_die_limit 0

Name:           rclone
Version:        1.38
Release:        1%{?dist}
Summary:        rsync for cloud storage
License:        MIT 
URL:            http://rclone.org/
Source0:        https://github.com/ncw/rclone/archive/v%{version}/%{name}-%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

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
BuildRequires: golang(github.com/ncw/swift) >= 0-0.8.gitaf59a5a
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
BuildRequires: golang(golang.org/x/crypto/nacl/secretbox) >= 0-0.16.gite4e2799
BuildRequires: golang(golang.org/x/crypto/scrypt) >= 0-0.16.gite4e2799
BuildRequires: golang(golang.org/x/crypto/ssh) >= 0-0.16.gite4e2799
BuildRequires: golang(golang.org/x/crypto/ssh/terminal) >= 0-0.16.gite4e2799
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(golang.org/x/text/unicode/norm)
BuildRequires: golang(golang.org/x/time/rate)
BuildRequires: golang(google.golang.org/api/drive/v2) >= 0-0.19.git77f162b
BuildRequires: golang(google.golang.org/api/googleapi) >= 0-0.19.git77f162b
BuildRequires: golang(google.golang.org/api/storage/v1) >= 0-0.19.git77f162b


%description
Rclone is a command line program to sync files and directories to and 
from various cloud services.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
mkdir -p ./_build/src/github.com/ncw/
ln -s $(pwd) ./_build/src/github.com/ncw/rclone
export GOPATH=$(pwd)/_build:%{gopath}

%gobuild -o rclone


%install
install -p -D -m 0755 ./rclone %{buildroot}%{_bindir}/rclone
install -p -D -m 0644 ./rclone.1 %{buildroot}%{_mandir}/man1/rclone.1

%{__rm} -rf vendor

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%files
%license COPYING
%doc RELEASE.md README.md MANUAL.md
%{_bindir}/rclone
%{_mandir}/man1/rclone.1*


%changelog
* Sun Oct 01 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.38-1
- Update to version 1.38
* Fri Jul 28 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.37-2
- Unbundled revision
* Sun Jul 23 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.37-1
- Update to version 1.37
* Thu Jul 20 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.36-2
- Update to Fedora Packaging Guidelines specification
* Sat Mar 25 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.36-1
- Update to version 1.36
* Fri Jan 06 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.35-1
- Update to version 1.35
* Sun Dec 11 2016 Robert-André Mauchin <zebob.m@gmail.com> - 1.34-1
- Initial RPM release

