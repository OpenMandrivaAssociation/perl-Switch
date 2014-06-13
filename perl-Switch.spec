%define upstream_name    Switch
%define upstream_version 2.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A switch statement for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		Switch-2.16-perl514.patch

BuildRequires:	perl-devel
BuildRequires:	perl(Filter::Util::Call)
BuildRequires:	perl(Text::Balanced)

BuildArch:	noarch

%description
The Switch.pm module implements a generalized case mechanism that covers
most (but not all) of the numerous possible combinations of switch and case
values described above.

The module augments the standard Perl syntax with two new control
statements: 'switch' and 'case'. The 'switch' statement takes a single
scalar argument of any type, specified in parentheses. 'switch' stores this
value as the current switch value in a (localized) control variable. The
value is followed by a block which may contain one or more Perl statements
(including the 'case' statement described below). The block is
unconditionally executed once the switch value has been cached.

A 'case' statement takes a single scalar argument (in mandatory parentheses
if it's a variable; otherwise the parens are optional) and selects the
appropriate type of matching between that argument and the current switch
value. The type of matching used is determined by the respective types of
the switch value and the 'case' argument, as specified in Table 1. If the
match is successful, the mandatory block associated with the 'case'
statement is executed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 2.160.0-3mdv2011.0
+ Revision: 653620
- rebuild for updated spec-helper

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.160.0-2mdv2011.0
+ Revision: 562434
- rebuild

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2.160.0-1mdv2011.0
+ Revision: 460773
- update to 2.16

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 2.14-2mdv2010.0
+ Revision: 375899
- rebuild

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2.14-1mdv2010.0
+ Revision: 372657
- import perl-Switch


* Wed May 06 2009 cpan2dist 2.14-1mdv
- initial mdv release, generated with cpan2dist

