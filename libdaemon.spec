%define major	0
%define libname %mklibname daemon %{major}
%define devname %mklibname daemon -d
%bcond_with	crosscompile

Summary:	Lightweight C library which eases the writing of UNIX daemons
Name:		libdaemon
Version:	0.14
Release:	13
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://0pointer.de/lennart/projects/libdaemon
Source0:	http://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.gz
Patch0:		libdaemon-0.14-better-handling-of-stale-pidfiles.patch
BuildRequires:	doxygen
BuildRequires:	lynx

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
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Provides:	daemon = %{version}-%{release}

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	daemon-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel < 0.14-6

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
%apply_patches
autoreconf -fiv

%build
%if %{with crosscompile}
export ac_cv_func_setpgrp_void=yes
%endif
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

#(tpg) useless
rm -rf %{buildroot}%{_datadir}/doc/libdaemon

%files -n %{libname}
%{_libdir}/libdaemon.so.%{major}*

%files -n %{devname}
%doc README
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

