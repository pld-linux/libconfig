Summary:	C Configuration File Library
Summary(pl.UTF-8):	Biblioteka C do plików konfiguracyjnych
Name:		libconfig
Version:	1.7.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/hyperrealm/libconfig/releases
Source0:	https://github.com/hyperrealm/libconfig/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	898fbd4ccac2eb3913a86883ab9b2e6c
Patch0:		%{name}-info.patch
URL:		http://www.hyperrealm.com/main.php?s=libconfig
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.0
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libconfig is a simple library for manipulating structured
configuration files.

Libconfig is very compact, which makes it well-suited for
memory-constrained systems like handheld devices.

The library includes bindings for both the C and C++ languages. It
works on POSIX-compliant UNIX systems (GNU/Linux, Mac OS X, Solaris,
FreeBSD) and Windows (2000, XP and later).

%description -l pl.UTF-8
libconfig to prosta biblioteka do obróbki plików konfiguracyjnych
mających strukturę.

Jest bardzo mała, dzięki czemu dobrze nadaje się do systemów
ograniczonych pamięciowo, takich jak palmtopy.

Biblioteka ma dowiązania do języków C i C++. Działa na systemach
uniksowych zgodnych z POSIX (GNU/Linux, Mac OS X, Solaris, FreeBSD)
oraz Windows (2000, XP i późniejszych).

%package devel
Summary:	Header files for libconfig library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libconfig
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libconfig library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libconfig.

%package static
Summary:	Static libconfig library
Summary(pl.UTF-8):	Statyczna biblioteka libconfig
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libconfig library.

%description static -l pl.UTF-8
Statyczna biblioteka libconfig.

%package c++
Summary:	C++ Configuration File Library
Summary(pl.UTF-8):	Biblioteka C++ do plików konfiguracyjnych
Group:		Libraries
# doesn't require base, common code included in library

%description c++
libconfig++ is the C++ binding for libconfig library.

%description c++ -l pl.UTF-8
libconfig++ to dowiązanie C++ biblioteki libconfig.

%package c++-devel
Summary:	Header files for libconfig++ library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libconfig++
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files for libconfig++ library.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libconfig++.

%package c++-static
Summary:	Static libconfig++ library
Summary(pl.UTF-8):	Statyczna biblioteka libconfig++
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static libconfig++ library.

%description c++-static -l pl.UTF-8
Statyczna biblioteka libconfig++.

%prep
%setup -q
%patch -P0 -p1

# force regeneration, included files are outdated
%{__rm} lib/scanner.[ch]

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
# -j1 to workaround flex rebuild race
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libconfig*.la

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/libconfig.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libconfig.so.11

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libconfig.so
%{_includedir}/libconfig.h
%{_pkgconfigdir}/libconfig.pc
%{_libdir}/cmake/libconfig
%{_infodir}/libconfig.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libconfig.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libconfig++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libconfig++.so.11

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libconfig++.so
%{_includedir}/libconfig.h++
%{_pkgconfigdir}/libconfig++.pc
%{_libdir}/cmake/libconfig++

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libconfig++.a
