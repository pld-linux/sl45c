Summary:	SL45c - Siemens SL45 Control Center & Datasuite v0.5
Name:	sl45c	
Version:	0.5.1
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0: http://www.sl45i.nl/sl45c/%{name}-%{version}.tar.gz
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SL45c is a Linux/Unix tool suite for Siemens SL45(i) mobile phones

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

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
