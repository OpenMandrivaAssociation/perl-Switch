%define upstream_name    Switch
%define upstream_version 2.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    A switch statement for Perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl(Text::Balanced)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
