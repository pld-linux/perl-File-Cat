%include	/usr/lib/rpm/macros.perl
Summary:	File-Cat perl module
Summary(pl):	Modu³ perla File-Cat
Name:		perl-File-Cat
Version:	1.2
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Cat-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-Cat perl module - Perl implementation of cat(1).

%description -l pl
Modu³ perla File-Cat - cat(1) dla perla.

%prep
%setup -q -n File-Cat-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/File/Cat.pm
%{_mandir}/man3/*
