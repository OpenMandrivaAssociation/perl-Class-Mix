%define upstream_name    Class-Mix
%define upstream_version 0.005

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Dynamic class mixing
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/Class-Mix-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Params::Classify)
BuildRequires: perl(Test::More)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The 'mix_class' function provided by this module dynamically generates
`anonymous' classes with specified inheritance.

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
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.4.0-2mdv2011.0
+ Revision: 653557
- rebuild for updated spec-helper

* Fri Sep 03 2010 Jérôme Quelin <jquelin@mandriva.org> 0.4.0-1mdv2011.0
+ Revision: 575611
- adding missing buildrequires:
- update to 0.004

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 471087
- import perl-Class-Mix


* Sun Nov 29 2009 cpan2dist 0.003-1mdv
- initial mdv release, generated with cpan2dist

