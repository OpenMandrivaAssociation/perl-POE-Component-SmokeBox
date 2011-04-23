%define upstream_name    POE-Component-SmokeBox
%define upstream_version 0.44

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    A backend for CPAN::Reporter::Smoker smokers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Env::Sanctify)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Object::Accessor)
BuildRequires: perl(POE)
BuildRequires: perl(Params::Check)
BuildRequires: perl(String::Perl::Warnings)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README LICENSE META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


