%define major	0
%define libname %mklibname daemon %{major}

Name:		libdaemon
Summary:	Lightweight C library which eases the writing of UNIX daemons
Version:	0.10
Release:	%mkrel 4
License:	GPL
Group:		System/Libraries
URL:		http://0pointer.de/lennart/projects/libdaemon/
Source0:	http://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.bz2
BuildRequires:	lynx doxygen
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot


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

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} = %{version}
Provides: 	daemon-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%{name}-devel

%description -n %{libname}-devel
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

%files -n %{libname}-devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc


