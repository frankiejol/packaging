%global commit ddbbf6f7b6cf9f1091b61748b6d44d1439d6f919
%global fontname aftertheflood-spark
%global fontconf 66-%{fontname}.conf

Name:       %{fontname}-fonts
Version:    20170907
Release:    1%{?dist}
Summary:    After the Flood Spark, a font to display charts within text
License:    MIT
URL:        http://aftertheflood.co/projects/atf-spark
Source0:    https://github.com/aftertheflood/spark/archive/%{commit}/%{name}-%{version}.tar.gz
Source1:    66-%{fontname}.conf
Source2:    %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
After the Flood Spark is a font that allows for the combination of text and 
visual data to show an idea and evidence in one headline. This builds on the 
principle of Sparklines defined by Edward Tufte and makes them easier to use.
Sparklines are currently available as plugins or javascript elements. By 
installing the Spark font you can use them immediately without the need for 
custom code.

Spark data needs to be formatted as comma-separated values, with curly brackets
at both ends of the set, e.g., {30,60,90}. You can also have numbers at the
beginning and end of the set, which are useful for providing the start and
end points, e.g., 123{30,60,90}456 – Spark has numerals built in.


%prep
%autosetup -n spark-%{commit}

%build

%install
mkdir -p %{buildroot}/%{_fontdir}
install -m 0644 Output/OpenType/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

appstream-util validate-relax --nonet \
               %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%license LICENSE
%doc README.md
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Sun Sep 17 2017 Robert-André Mauchin <zebob.m@gmail.com> - 20170907-1
- initial RPM release
