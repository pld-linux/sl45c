Summary:	SL45c - Siemens SL45 Control Center & Datasuite
Summary(pl):	SL45c - narzêdzia dla telefonów Siemens SL45
Name:		sl45c
Version:	0.5.1
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	http://www.freshdot.net/sl45c/%{name}-%{version}.tar.gz
# Source0-md5:	07a8831e5dfc3fa9a7e8783120fdb7ef
URL:		http://www.freshdot.net/sl45c/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SL45c is a Linux/Unix tool suite for Siemens SL45(i) mobile phones.

%description -l pl
SL45c to zestaw linuksowych/uniksowych narzêdzi dla telefonów
komórkowych Siemens SL45(i).

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install doc/sl45c.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/FORMATS doc/vCard.format THANKS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
