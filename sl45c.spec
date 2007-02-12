Summary:	SL45c - Siemens SL45 Control Center & Datasuite
Summary(pl.UTF-8):   SL45c - narzędzia dla telefonów Siemens SL45
Name:		sl45c
Version:	0.7
Release:	0.1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	http://www.freshdot.net/sl45c/%{name}-%{version}.tar.gz
# Source0-md5:	ac59a372d1d297bb0d1ed85e1c78f4f8
URL:		http://www.freshdot.net/sl45c/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SL45c is a Linux/Unix tool suite for Siemens SL45(i) mobile phones.

%description -l pl.UTF-8
SL45c to zestaw linuksowych/uniksowych narzędzi dla telefonów
komórkowych Siemens SL45(i).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/sl45c.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/FORMATS doc/vCard.format THANKS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
