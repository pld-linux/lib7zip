%define		p7zip_version	16.02
Summary:	A library using 7z.dll/7z.so (from 7-Zip) to handle different archive types
Summary(pl.UTF-8):	Biblioteka wykorzystująca 7z.dll/7z.so (z 7-zipa) do obsługi różnych rodzajów archiwów
Name:		lib7zip
Version:	3.0.0
Release:	1
License:	MPL v2.0
Group:		Libraries
#Source0Download: https://github.com/stonewell/lib7zip/releases
Source0:	https://github.com/stonewell/lib7zip/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2e7b0ec5f609f46f89e205a040a4aa5a
Source1:	http://downloads.sourceforge.net/p7zip/p7zip_%{p7zip_version}_src_all.tar.bz2
# Source1-md5:	a0128d661cfe7cc8c121e73519c54fbf
Patch0:		%{name}-install.patch
URL:		https://github.com/stonewell/lib7zip
BuildRequires:	cmake >= 2.8
# -std=c++14
BuildRequires:	libstdc++-devel >= 6:5.0
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
Requires:	libstdc++-devel >= 6:5.0

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
%patch -P0 -p1

%if "%{cc_version}" < "8"
# earlier versions don't know it
%{__sed} -i -e 's/ -Wno-class-memaccess//' CMakeLists.txt
%endif

%build
TOPDIR=$(pwd)
install -d build
cd build
CXXFLAGS="%{rpmcxxflags} -Wno-error=unused-result"
%cmake .. \
	-DBUILD_SHARED_LIB=ON \
	-DP7ZIP_SOURCE_DIR="${TOPDIR}/p7zip_%{p7zip_version}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p src/lib7zip.h $RPM_BUILD_ROOT%{_includedir}

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
%{_includedir}/lib7zip.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib7zip.a
