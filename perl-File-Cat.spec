#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Cat
Summary:	File::Cat - Perl implementation of cat(1)
Summary(pl.UTF-8):	File::Cat - implementacja cat(1) w Perlu
Name:		perl-File-Cat
Version:	1.2
Release:	11
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	300600b3786cec4360e88947f775f4fb
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Cat module - Perl implementation of cat(1).

File::Cat is a module of adventure, danger, and low cunning. With it,
you will explore some of the most inane programs ever seen by mortals.
No computer should be without one!

%description -l pl.UTF-8
Moduł File::Cat - implementacja cat(1) w Perlu.

File::Cat jest modułem z przygodami, niebezpiecznym i mało pomysłowym.
Przy jego pomocy można stworzyć kilka spośród najgłupszych programów
jakie widzieli śmiertelnicy. Na każdym komputerze powinien być choć
jeden taki!

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/File/Cat.pm
%{_mandir}/man3/*
