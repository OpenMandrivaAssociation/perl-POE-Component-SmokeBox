%define upstream_name    POE-Component-SmokeBox
%define upstream_version 0.48

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A backend for CPAN::Reporter::Smoker smokers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Env::Sanctify)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Pty)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Object::Accessor)
BuildRequires:	perl(POE)
BuildRequires:	perl(Params::Check)
BuildRequires:	perl(String::Perl::Warnings)
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
POE::Component::SmokeBox is a flexible CPAN Smoke testing framework which
provides an extensible method for testing CPAN distributions against
various different smoker backends.

A smoker backend is defined using a the POE::Component::SmokeBox::Smoker
manpage object and is basically the path to a 'perl' executable that is
configured for CPAN Testing and its associated environment settings.

The 'perl' executable must be configured appropriately to support CPAN
testing with any of the currently supported backends, the
CPANPLUS::YACSmoke manpage, the CPAN::YACSmoke manpage or the
CPAN::Reporter manpage. Additional backends may be supported by inheriting
and extending the backend base class the
POE::Component::SmokeBox::Backend::Base manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.480.0-1mdv2011.0
+ Revision: 677378
- update to new version 0.48

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.460.0-1
+ Revision: 660010
- update to new version 0.46

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.440.0-6
+ Revision: 658269
- rebuild

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.440.0-5
+ Revision: 658207
- more runtime req

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.440.0-4
+ Revision: 657677
- add req

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.440.0-3
+ Revision: 657342
- rebuild for updated spec-helper

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.440.0-2
+ Revision: 640774
- rebuild to obsolete old packages

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.440.0-1
+ Revision: 638941
- update to new version 0.44

* Tue Feb 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.420.0-1
+ Revision: 636849
- update to new version 0.42

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.400.0-1
+ Revision: 635213
- update to new version 0.40

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.380.0-1mdv2011.0
+ Revision: 625027
- import perl-POE-Component-SmokeBox

