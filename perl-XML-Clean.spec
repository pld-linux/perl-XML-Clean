#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	XML
%define	pnam	Clean
Summary:	XML::Clean - Ensure, that (HTML) text pass throught an XML parser
Summary(pl.UTF-8):	XML::Clean - sprawdzanie czy tekst (HTML) przechodzi przez analizator XML-a
Name:		perl-XML-Clean
Version:	1.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1429eec26fdecc974086b3808a450501
URL:		http://search.cpan.org/dist/XML-Clean/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ultimate quest of this module is to produce from non-XML text
text, that will will most probably pass throught any XML parser one
could find. 

Basic cleaning is just XML tag matching (for every opening tag there
will be closing tag as well, and they will form a tree structure). 

When you add some extra parameters, you will receive complete XML
text, including XML head and root element (if none were defined in
text, then some will be added).

%description -l pl.UTF-8
Zasadniczym zadaniem tego modułu jest stworzenie z nie-XML-owego
tekstu tekstu, który z dużym prawdopodobieństwem przejdzie przez
dowolny analizator XML-a.

Podstawowe czyszczenie to tylko dopasowywanie znaczników XML (dla
każdego otwierającego znacznika musi istnieć także znacznik zamykający
i muszą tworzyć strukturę drzewiastą).

W przypadku dodania dodatkowych parametrów otrzymujemy kompletny tekst
XML, zawierający nagłówek i główny element (jeśli nie zostały
zdefiniowane w tekście, zostaną dodane).

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
%doc ChangeLog
%{perl_vendorlib}/XML/*.pm
%{_mandir}/man3/*
