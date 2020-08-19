Name:           perl-IP-Country
Version:        2.28
Release:        10%{?dist}
Summary:        Fast lookup of country codes from IP addresses
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/IP-Country
Source0:        https://cpan.metacpan.org/modules/by-module/IP/IP-Country-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Utils
BuildRequires:  perl(Geography::Countries)
# Test Suite
BuildRequires:  perl(Test)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
IP::Country allows fast lookups of IP addresses and their corresponding
countries based on available regional NIC data.
Although the country of assignment will probably be the country associated
with a large ISP rather than the client herself, this is probably good 
enough for most log analysis applications, and under test has proved to be as
accurate as reverse-DNS and WHOIS lookup.


%package utils
Summary:        Utility to query and rebuild the IP::Country database
Requires:       %{name} = %{version}-%{release}

%description utils
ip2cc is a front-end to the IP::Country Perl module allowing fast lookups of
IP addresses and their corresponding countries based on available regional
NIC data.

ipcc_loader.pl can be used to rebuild the database with current dumps of
the RIPE/APNIC/ARIN et al data.

%prep
%setup -q -n IP-Country-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}


%check
make test


%files
%doc CHANGES README
%{perl_vendorlib}/IP/
%{_mandir}/man3/IP::Authority.3*
%{_mandir}/man3/IP::Country.3*
%{_mandir}/man3/IP::Country::Fast.3*
%{_mandir}/man3/IP::Country::MaxMind.3*
%{_mandir}/man3/IP::Country::Medium.3*
%{_mandir}/man3/IP::Country::Slow.3*

%files utils
%doc dbmScripts INSTALL
%{_bindir}/ip2cc
%{_mandir}/man1/ip2cc.1*


%changelog
* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  1 2020 Paul Howarth <paul@city-fan.org> - 2.28-9
- Spec clean-up
  - Drop legacy Group: and BuildRoot: tags
  - Switch upstream from search.cpan.org to metacpan.org
  - Be verbose when removing files and fixing permissions
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Simplify find command using -delete
  - Don't need to remove empty directories from the buildroot
  - Drop redundant file deletion in %%prep section
  - Drop redundant buildroot cleaning in %%install section
  - Drop redundant %%clean section
  - Drop redundant %%defattr from %%files lists
  - Make %%files list more explicit

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.28-5
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 2.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Sérgio Basto <sergio@serjux.com> - 2.28-1
- Update to IP-Country-2.28

* Sun Jun 18 2017 Paul Howarth <paul@city-fan.org> - 2.26-12
- Perl 5.26 rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.26-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 01 2016 Sérgio Basto <sergio@serjux.com> - 2.26-10
- Add perl-generators to get proper requires/provides on F-25 and later

* Fri Sep 30 2016 Sérgio Basto <sergio@serjux.com> - 2.26-9
- Rebuild for Perl with locale (buildroot with glibc-all-langpacks)

* Wed Jul 20 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.26-8
- add buildrequires perl-Test

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 2.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Oct 08 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.26-6
- Rebuilt for Perl in F-20

* Wed Oct 10 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.26-5
- Rebuilt for perl

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 20 2010 Nicolas Chauvet <kwizart@gmail.com> - 2.26-3
- Rebuild for perl 5.12

* Thu Feb 19 2009 Andreas Thienemann <andreas@bawue.net> 2.26-2
- Removed dotfiles, added %%defattr to -utils

* Thu Feb 19 2009 Andreas Thienemann <andreas@bawue.net> 2.26-1
- Updated to upstream release 2.26

* Mon Feb 18 2008 Andreas Thienemann <athienem@redhat.com> 2.23-1
- Specfile autogenerated by cpanspec 1.74.
- Fixed up for fedora
