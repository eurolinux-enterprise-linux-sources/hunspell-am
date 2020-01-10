Name: hunspell-am
Summary: Amharic hunspell dictionaries
%define upstreamid 20090704
Version: 0.%{upstreamid}
Release: 6%{?dist}
Source: http://www.cs.ru.nl/~biniam/geez/dict/am_ET.zip
Group: Applications/Text
URL: http://www.cs.ru.nl/~biniam/geez/index.php
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+
BuildArch: noarch

Requires: hunspell

%description
Amharic hunspell dictionaries.

%prep
%setup -q -n am_ET

%build
tr -d '\r' < README.txt > README.txt.new
touch -r README.txt README.txt.new
mv -f README.txt.new README.txt

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p am_ET.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.txt
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090704-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090704-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090704-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090704-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090704-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090704-1
- initial version
