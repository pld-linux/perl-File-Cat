%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Cat
Summary:	File::Cat - Perl implementation of cat(1)
Summary(pl):	File::Cat - implementacja cat(1) w Perlu
Name:		perl-File-Cat
Version:	1.2
Release:	9
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	300600b3786cec4360e88947f775f4fb
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Cat module - Perl implementation of cat(1).

File::Cat is a module of adventure, danger, and low cunning. With it,
you will explore some of the most inane programs ever seen by mortals.
No computer should be without one!

%description -l pl
Modu� File::Cat - implementacja cat(1) w Perlu.

File::Cat jest modu�em z przygodami, niebezpiecznym i ma�o pomys�owym.
Przy jego pomocy mo�na stworzy� kilka spo�r�d najg�upszych program�w
jakie widzieli �miertelnicy. Na ka�dym komputerze powinien by� cho�
jeden taki!

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
