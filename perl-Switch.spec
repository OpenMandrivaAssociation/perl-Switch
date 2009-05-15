
%define realname   Switch
%define version    2.14
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    A switch statement for Perl
Source:     http://www.cpan.org/modules/by-module//%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl(Text::Balanced)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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


