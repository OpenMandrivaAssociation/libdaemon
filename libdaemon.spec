%define major	0
%define libname %mklibname daemon %{major}
%define develname %mklibname daemon -d

Summary:	Lightweight C library which eases the writing of UNIX daemons
Name:		libdaemon
Version:	0.12
Release:	%mkrel 1
License:	GPL
Group:		System/Libraries
URL:		http://0pointer.de/lennart/projects/libdaemon/
Source0:	http://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.bz2
BuildRequires:	lynx
BuildRequires:	doxygen


%description
libdaemon is a lightweight C library which eases the writing of UNIX daemons.
It consists of the following parts:
    * A wrapper around fork() which does the correct daemonization procedure
      of a process
    * A wrapper around syslog() for simpler and compatible log output to
      Syslog or STDERR
    * An API for writing PID files
    * An API for serializing UNIX signals into a pipe for usage with
      select() or poll()

Routines like these are included in most of the daemon software available. It
is not that simple to get it done right and code duplication cannot be a goal.

%package -n 	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries
Provides:	daemon = %{version}-%{release}
Obsoletes:	daemon

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides: 	daemon-devel = %{version}-%{release}
Provides: 	%{name}-devel = %{version}-%{release}
Obsoletes: 	%{libname}-devel

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
