%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Cat
Summary:	File::Cat perl module
Summary(pl):	Modu³ perla File::Cat
Name:		perl-File-Cat
Version:	1.2
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	300600b3786cec4360e88947f775f4fb
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Cat perl module - Perl implementation of cat(1).

%description -l pl
Modu³ perla File::Cat - cat(1) dla perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/File/Cat.pm
%{_mandir}/man3/*
