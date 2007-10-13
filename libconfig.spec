Summary:	C/C++ Configuration File Library
Name:		libconfig
Version:	1.1.3
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://www.hyperrealm.com/libconfig/%{name}-%{version}.tar.gz
# Source0-md5:	c0cd4b5ed44bbc1dca32eafaac377e33
URL:		http://www.hyperrealm.com/main.php?s=libconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libconfig is a simple library for manipulating structured
configuration files.

Libconfig is very compact . just 25K for the stripped C shared library
(one-fifth the size of the expat XML parser library) and 39K for the
stripped C++ shared library. This makes it well-suited for
memory-constrained systems like handheld devices.

The library includes bindings for both the C and C++ languages. It
works on POSIX-compliant UNIX systems (GNU/Linux, Mac OS X, Solaris,
FreeBSD) and Windows (2000, XP and later).

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

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libconfig.h*
%{_pkgconfigdir}/*.pc
%{_infodir}/libconfig*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
