%define		p7zip_version	9.20.1
Summary:	A library using 7z.dll/7z.so (from 7-Zip) to handle different archive types
Summary(pl.UTF-8):	Biblioteka wykorzystująca 7z.dll/7z.so (z 7-zipa) do obsługi różnych rodzajów archiwów
Name:		lib7zip
Version:	1.6.3
Release:	1
License:	MPL v1.1
Group:		Libraries
#Source0Download: http://code.google.com/p/lib7zip/downloads/list
Source0:	http://lib7zip.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	6413c398a8def15ac9dda392b41353b7
Source1:	http://downloads.sourceforge.net/p7zip/p7zip_%{p7zip_version}_src_all.tar.bz2
# Source1-md5:	bd6caaea567dc0d995c990c5cc883c89
Patch0:		%{name}-link.patch
URL:		http://code.google.com/p/lib7zip/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.0
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library using 7z.dll/7z.so (from 7-Zip) to handle different archive
types.

%description -l pl.UTF-8
Biblioteka wykorzystująca 7z.dll/7z.so (z 7-zipa) do obsługi różnych
rodzajów archiwów.

%package devel
Summary:	Development files for lib7zip library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki lib7zip
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Development files for lib7zip library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki lib7zip.

%package static
Summary:	Static lib7zip library
Summary(pl.UTF-8):	Statyczna biblioteka lib7zip
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lib7zip library.

%description static -l pl.UTF-8
Statyczna biblioteka lib7zip.

%prep
%setup -q -a1
%patch0 -p1

# remove it when "linking libtool libraries using a non-POSIX archiver ..." warning is gone
# (after lib7zip or libtool change)
%{__sed} -i -e '/AM_INIT_AUTOMAKE/s/-Werror//' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
export P7ZIP_SOURCE_DIR="$(pwd)/p7zip_%{p7zip_version}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# test programs
%{__rm} $RPM_BUILD_ROOT%{_bindir}/test7z*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib7zip.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib7zip.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib7zip.so
%{_libdir}/lib7zip.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib7zip.a
