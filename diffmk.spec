%include	/usr/lib/rpm/macros.perl
Summary:	Sun's XML difference tool in Perl
Summary(pl):	Perlowe narzêdzie Suna do znajdowania ró¿nic w plikach XML
Name:		diffmk
Version:	1.0
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://wwws.sun.com/software/xml/developers/%{name}/%{name}-%{version}.zip
# Source0-md5:	41f3ab2d63d73a28ba2f328c0998e4b7
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	unzip
Requires:	perl-XML-DOM
Requires:	perl-Algorithm-Diff
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
diffmk makes intelligently formatted output for showing changes in XML
documents.

%description -l pl
diffmk generuje inteligentnie sformatowane wyj¶cie ukazuj±ce zmiany w
dokumentach XML.

%prep
%setup -c -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{perl_vendorlib}}

install diffmk $RPM_BUILD_ROOT%{_bindir}
install diffmk.xml $RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/*
