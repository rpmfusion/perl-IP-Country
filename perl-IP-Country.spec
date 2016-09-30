Name:           perl-IP-Country
Version:        2.26
Release:        9%{?dist}
Summary:        Fast lookup of country codes from IP addresses
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IP-Country/
Source0:        http://www.cpan.org/modules/by-module/IP/IP-Country-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
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
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description utils
ip2cc is a frontend to the IP::Country Perl module allowing fast lookups of
IP addresses and their corresponding countries based on available regional
NIC data.

ipcc_loader.pl can be used to rebuild the database with current dumps of
the RIPE/APNIC/ARIN et al data.

%prep
%setup -q -n IP-Country-%{version}
find -name '._*' | xargs rm -f

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*


%check
make test


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files utils
%defattr(-,root,root,-)
%doc dbmScripts INSTALL
%{_bindir}/ip2cc
%{_mandir}/man1/ip2cc.1*


%changelog
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
