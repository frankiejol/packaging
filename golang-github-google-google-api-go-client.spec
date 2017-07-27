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
%global project         google
%global repo            google-api-go-client
# https://github.com/google/google-api-go-client
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     google.golang.org/api
%global commit          295e4bb0ade057ae2cfb9876ab0b54635dbfcea4
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Google APIs Client Library for Go
# Detected licences
# - BSD (3 clause) at 'LICENSE'
License:        BSD
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
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/context/ctxhttp)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/sync/semaphore)
BuildRequires: golang(google.golang.org/appengine/socket)
BuildRequires: golang(google.golang.org/appengine/urlfetch)
BuildRequires: golang(google.golang.org/genproto/googleapis/bytestream)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/credentials/oauth)
BuildRequires: golang(google.golang.org/grpc/naming)
%endif

Requires:      golang(golang.org/x/net/context)
Requires:      golang(golang.org/x/net/context/ctxhttp)
Requires:      golang(golang.org/x/oauth2)
Requires:      golang(golang.org/x/oauth2/google)
Requires:      golang(golang.org/x/sync/semaphore)
Requires:      golang(google.golang.org/appengine/socket)
Requires:      golang(google.golang.org/appengine/urlfetch)
Requires:      golang(google.golang.org/genproto/googleapis/bytestream)
Requires:      golang(google.golang.org/grpc)
Requires:      golang(google.golang.org/grpc/codes)
Requires:      golang(google.golang.org/grpc/credentials)
Requires:      golang(google.golang.org/grpc/credentials/oauth)
Requires:      golang(google.golang.org/grpc/naming)

Provides:      golang(%{import_path}/acceleratedmobilepageurl/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/adexchangebuyer/v1.2) = %{version}-%{release}
Provides:      golang(%{import_path}/adexchangebuyer/v1.3) = %{version}-%{release}
Provides:      golang(%{import_path}/adexchangebuyer/v1.4) = %{version}-%{release}
Provides:      golang(%{import_path}/adexchangebuyer2/v2beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/adexchangeseller/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/adexchangeseller/v1.1) = %{version}-%{release}
Provides:      golang(%{import_path}/adexchangeseller/v2.0) = %{version}-%{release}
Provides:      golang(%{import_path}/adexperiencereport/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/admin/datatransfer/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/admin/directory/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/admin/reports/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/adsense/v1.3) = %{version}-%{release}
Provides:      golang(%{import_path}/adsense/v1.4) = %{version}-%{release}
Provides:      golang(%{import_path}/adsensehost/v4.1) = %{version}-%{release}
Provides:      golang(%{import_path}/analytics/v2.4) = %{version}-%{release}
Provides:      golang(%{import_path}/analytics/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/analyticsreporting/v4) = %{version}-%{release}
Provides:      golang(%{import_path}/androidenterprise/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/androidpublisher/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/androidpublisher/v1.1) = %{version}-%{release}
Provides:      golang(%{import_path}/androidpublisher/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/appengine/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/appengine/v1alpha) = %{version}-%{release}
Provides:      golang(%{import_path}/appengine/v1beta) = %{version}-%{release}
Provides:      golang(%{import_path}/appengine/v1beta4) = %{version}-%{release}
Provides:      golang(%{import_path}/appengine/v1beta5) = %{version}-%{release}
Provides:      golang(%{import_path}/appsactivity/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/appstate/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/bigquery/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/bigquerydatatransfer/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/blogger/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/blogger/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/books/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/calendar/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/civicinfo/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/classroom/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/cloudbilling/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/cloudbuild/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/clouddebugger/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/clouderrorreporting/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/cloudfunctions/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/cloudfunctions/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/cloudkms/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/cloudmonitoring/v2beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/cloudresourcemanager/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/cloudresourcemanager/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/cloudresourcemanager/v2beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/cloudtrace/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/cloudtrace/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/clouduseraccounts/v0.alpha) = %{version}-%{release}
Provides:      golang(%{import_path}/clouduseraccounts/v0.beta) = %{version}-%{release}
Provides:      golang(%{import_path}/clouduseraccounts/vm_alpha) = %{version}-%{release}
Provides:      golang(%{import_path}/clouduseraccounts/vm_beta) = %{version}-%{release}
Provides:      golang(%{import_path}/compute/v0.alpha) = %{version}-%{release}
Provides:      golang(%{import_path}/compute/v0.beta) = %{version}-%{release}
Provides:      golang(%{import_path}/compute/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/consumersurveys/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/container/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/content/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/content/v2sandbox) = %{version}-%{release}
Provides:      golang(%{import_path}/customsearch/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/dataflow/v1b3) = %{version}-%{release}
Provides:      golang(%{import_path}/dataproc/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/dataproc/v1alpha1) = %{version}-%{release}
Provides:      golang(%{import_path}/dataproc/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/datastore/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/datastore/v1beta3) = %{version}-%{release}
Provides:      golang(%{import_path}/deploymentmanager/v0.alpha) = %{version}-%{release}
Provides:      golang(%{import_path}/deploymentmanager/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/deploymentmanager/v2beta) = %{version}-%{release}
Provides:      golang(%{import_path}/dfareporting/v2.7) = %{version}-%{release}
Provides:      golang(%{import_path}/dfareporting/v2.8) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/dlp/v2beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/dns/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/dns/v2beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/doubleclickbidmanager/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/doubleclicksearch/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/drive/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/drive/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/firebasedynamiclinks/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/firebaserules/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/fitness/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/fusiontables/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/fusiontables/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/games/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/gamesconfiguration/v1configuration) = %{version}-%{release}
Provides:      golang(%{import_path}/gamesmanagement/v1management) = %{version}-%{release}
Provides:      golang(%{import_path}/genomics/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/genomics/v1alpha2) = %{version}-%{release}
Provides:      golang(%{import_path}/gensupport) = %{version}-%{release}
Provides:      golang(%{import_path}/gmail/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapi) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapi/transport) = %{version}-%{release}
Provides:      golang(%{import_path}/groupsmigration/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/groupssettings/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/iam/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/identitytoolkit/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/iterator) = %{version}-%{release}
Provides:      golang(%{import_path}/iterator/testing) = %{version}-%{release}
Provides:      golang(%{import_path}/kgsearch/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/language/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/language/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/language/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/licensing/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/logging/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/logging/v2beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/manufacturers/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/mirror/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/ml/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/ml/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/monitoring/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/oauth2/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/oauth2/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/option) = %{version}-%{release}
Provides:      golang(%{import_path}/oslogin/v1alpha) = %{version}-%{release}
Provides:      golang(%{import_path}/pagespeedonline/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/pagespeedonline/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/partners/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/people/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/playmoviespartner/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/plus/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/plusdomains/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/prediction/v1.2) = %{version}-%{release}
Provides:      golang(%{import_path}/prediction/v1.3) = %{version}-%{release}
Provides:      golang(%{import_path}/prediction/v1.4) = %{version}-%{release}
Provides:      golang(%{import_path}/prediction/v1.5) = %{version}-%{release}
Provides:      golang(%{import_path}/prediction/v1.6) = %{version}-%{release}
Provides:      golang(%{import_path}/proximitybeacon/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/pubsub/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/pubsub/v1beta1a) = %{version}-%{release}
Provides:      golang(%{import_path}/pubsub/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/qpxexpress/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/replicapool/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/replicapool/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/replicapoolupdater/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/reseller/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/resourceviews/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/resourceviews/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/runtimeconfig/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/runtimeconfig/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/safebrowsing/v4) = %{version}-%{release}
Provides:      golang(%{import_path}/script/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/searchconsole/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/servicecontrol/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/servicemanagement/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/serviceuser/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/sheets/v4) = %{version}-%{release}
Provides:      golang(%{import_path}/siteverification/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/slides/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/sourcerepo/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/spanner/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/spectrum/v1explorer) = %{version}-%{release}
Provides:      golang(%{import_path}/speech/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/speech/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/sqladmin/v1beta3) = %{version}-%{release}
Provides:      golang(%{import_path}/sqladmin/v1beta4) = %{version}-%{release}
Provides:      golang(%{import_path}/storage/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/storage/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/storage/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/storagetransfer/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/support/bundler) = %{version}-%{release}
Provides:      golang(%{import_path}/surveys/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/tagmanager/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/tagmanager/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/taskqueue/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/taskqueue/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/tasks/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/toolresults/v1beta3) = %{version}-%{release}
Provides:      golang(%{import_path}/toolresults/v1beta3firstparty) = %{version}-%{release}
Provides:      golang(%{import_path}/tracing/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/translate/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/transport) = %{version}-%{release}
Provides:      golang(%{import_path}/transport/bytestream) = %{version}-%{release}
Provides:      golang(%{import_path}/transport/grpc) = %{version}-%{release}
Provides:      golang(%{import_path}/transport/http) = %{version}-%{release}
Provides:      golang(%{import_path}/urlshortener/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/videointelligence/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/vision/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/webfonts/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/webmasters/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/youtube/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/youtubeanalytics/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/youtubeanalytics/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/youtubereporting/v1) = %{version}-%{release}

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
BuildRequires: golang(google.golang.org/grpc/metadata)
%endif

Requires:      golang(google.golang.org/grpc/metadata)

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
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

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# packaging testdata
for file in $(find . -iname "testdata") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list
done
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

%gotest %{import_path}/gensupport
%gotest %{import_path}/google-api-go-generator
%gotest %{import_path}/google-api-go-generator/internal/disco
%gotest %{import_path}/googleapi
%gotest %{import_path}/googleapi/internal/uritemplates
# fail with "no buildable Go source files"
# %gotest %{import_path}/integration-tests/storage
%gotest %{import_path}/internal
%gotest %{import_path}/iterator
%gotest %{import_path}/iterator/testing
%gotest %{import_path}/option
%gotest %{import_path}/support/bundler
# golang-googlecode-goprotobuf is too old
# https://bugzilla.redhat.com/show_bug.cgi?id=1474510
# %gotest %{import_path}/transport/bytestream
# %gotest %{import_path}/transport/bytestream/internal
%gotest %{import_path}/transport/grpc
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md GettingStarted.md CONTRIBUTORS CONTRIBUTING.md AUTHORS
%dir %{gopath}/src/google.golang.org
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README.md GettingStarted.md CONTRIBUTORS CONTRIBUTING.md AUTHORS
%endif

%changelog
* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.git295e4bb
- First package for Fedora

