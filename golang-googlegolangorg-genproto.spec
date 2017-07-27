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

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif


%global provider        github
%global provider_tld    com
%global project         google
%global repo            go-genproto
# https://github.com/google/go-genproto
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     google.golang.org/genproto
%global commit          b0a3dcfcd1a9bd48e63634bd8802960804cf8315
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Go generated proto packages
# Detected licences
# - *No copyright* Apache (v2.0) at 'LICENSE'
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
# ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 ppc64le s390x
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}



%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires: golang(github.com/golang/protobuf/ptypes/any)
BuildRequires: golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires: golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires: golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/grpc)
%endif

Requires:      golang(github.com/golang/protobuf/proto)
Requires:      golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
Requires:      golang(github.com/golang/protobuf/ptypes/any)
Requires:      golang(github.com/golang/protobuf/ptypes/duration)
Requires:      golang(github.com/golang/protobuf/ptypes/empty)
Requires:      golang(github.com/golang/protobuf/ptypes/struct)
Requires:      golang(github.com/golang/protobuf/ptypes/timestamp)
Requires:      golang(github.com/golang/protobuf/ptypes/wrappers)
Requires:      golang(golang.org/x/net/context)
Requires:      golang(google.golang.org/grpc)

Provides:      golang(%{import_path}/googleapis/api) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/annotations) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/configchange) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/distribution) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/httpbody) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/label) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/metric) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/monitoredres) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/serviceconfig) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/servicecontrol/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/servicemanagement/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/appengine/legacy) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/appengine/logging/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/appengine/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/assistant/embedded/v1alpha1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/bigtable/admin/cluster/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/bigtable/admin/table/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/bigtable/admin/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/bigtable/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/bigtable/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/bytestream) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/audit) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/billing/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/dataproc/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/functions/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/language/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/language/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/language/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/ml/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/ml/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/runtimeconfig/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/speech/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/speech/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/support/common) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/support/v1alpha1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/videointelligence/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/vision/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/container/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/datastore/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/datastore/v1beta3) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/build/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/cloudbuild/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/clouddebugger/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/clouderrorreporting/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/cloudprofiler/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/cloudtrace/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/remoteexecution/v1test) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/source/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/sourcerepo/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/example/library/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/genomics/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/genomics/v1alpha2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/iam/admin/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/iam/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/logging/type) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/logging/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/longrunning) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/monitoring/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/privacy/dlp/v2beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/pubsub/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/pubsub/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/rpc/code) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/rpc/errdetails) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/rpc/status) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/spanner/admin/database/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/spanner/admin/instance/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/spanner/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/storagetransfer/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/streetview/publish/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/tracing/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/color) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/date) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/dayofweek) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/latlng) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/money) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/postaladdress) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/timeofday) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/watcher/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/protobuf/api) = %{version}-%{release}
Provides:      golang(%{import_path}/protobuf/field_mask) = %{version}-%{release}
Provides:      golang(%{import_path}/protobuf/ptype) = %{version}-%{release}
Provides:      golang(%{import_path}/protobuf/source_context) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

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

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md
%dir %{gopath}/src/google.golang.org
%endif

%changelog
* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.gitb0a3dcf
- First package for Fedora

