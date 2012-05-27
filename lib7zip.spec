Summary:	A library using 7z.dll/7z.so (from 7-Zip) to handle different archive types
Summary(pl.UTF-8):	Biblioteka wykorzystująca 7z.dll/7z.so (z 7-zipa) do obsługi różnych rodzajów archiwów
Name:		lib7zip
Version:	1.4.1
Release:	0.1
License:	- (enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://lib7zip.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	79ef69fc5c8ddce040387377b6dbbdcc
URL:		http://code.google.com/p/lib7zip/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library using 7z.dll/7z.so (from 7-Zip) to handle different archive
types.

%description -l pl.UTF-8
Biblioteka wykorzystująca 7z.dll/7z.so (z 7-zipa) do obsługi różnych
rodzajów archiwów.

%prep
%setup -q

%build
export P7ZIP_SOURCE_DIR="$(pwd)"
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
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
