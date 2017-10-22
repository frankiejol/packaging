%global _hardened_build 1

Name:       suex
Version:    0.2.2
Release:    1%{?dist}
Summary:    Execute commands as another user 
License:    MIT

URL:        https://github.com/odedlaz/suex/
Source0:    %{url}archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:     suex-0.2.2-fix_dirs.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libdw)
BuildRequires:  rubygem-ronn

%description
suex is a utility that is aimed to replace sudo for most ordinary use cases. 

Project Goals:

 - Secure. User's must not be able to abuse the utility, and it should 
   protect the user from making stupid mistakes.
 - Easy. The utility should be easy to audit, to maintain, to extend 
   and to contribute to.
 - Friendly. Rule creation should be straight forward. Rule should be easy
   to understand and easy to debug.
 - Powerful. Rules should be short, concise and allow find-grained control.
 - Feature Parity. This project should have complete feature parity 
   with the original utility.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
mkdir build && pushd build
export LANG=C.UTF-8
%cmake -DCMAKE_BUILD_TYPE=Debug  -DCMAKE_POSITION_INDEPENDENT_CODE=ON ..
%make_build
popd


%install
pushd build
%make_install
popd


%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*


%changelog
* Sun Oct 22 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.2-1
- Upstream release 0.2.2
* Sun Oct 22 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.1-1
- First RPM release
