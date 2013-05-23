%define major 0
%define libname %mklibname daemon %{major}
%define develname %mklibname daemon -d
%bcond_with	crosscompile

Summary:	Lightweight C library which eases the writing of UNIX daemons
Name:		libdaemon
Version:	0.14
Release:	7
License:	LGPLv2.1+
Group:		System/Libraries
URL:		http://0pointer.de/lennart/projects/libdaemon
Source0:	http://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.gz
Patch0:		libdaemon-0.14-better-handling-of-stale-pidfiles.patch
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
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Provides:	daemon = %{version}-%{release}

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	daemon-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel < 0.14-6

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
%apply_patches

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
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc



%changelog
* Fri Apr 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.14-4
+ Revision: 793725
- rebuild
-cleaned up spec

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.14-3
+ Revision: 660232
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.14-2mdv2011.0
+ Revision: 602533
- rebuild

* Sat Nov 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.14-1mdv2010.1
+ Revision: 462262
- update to new version 0.14

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.13-2mdv2010.0
+ Revision: 425527
- rebuild

* Sun Aug 17 2008 Emmanuel Andry <eandry@mandriva.org> 0.13-1mdv2009.0
+ Revision: 272912
- New version
- fix license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.12-3mdv2009.0
+ Revision: 222530
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.12-2mdv2008.1
+ Revision: 150510
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jul 11 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.12-1mdv2008.0
+ Revision: 51114
- new version
- adjust provides

* Sat Jun 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.11-1mdv2008.0
+ Revision: 43348
- new version
- new devel library policy


* Tue Feb 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10-4mdv2007.0
+ Revision: 120244
- Import libdaemon

* Sat Apr 08 2006 Austin Acton <austin@mandriva.org> 0.10-3mdk
- fix obsoletes (bug 21914)

* Tue Jan 17 2006 Olivier Blin <oblin@mandriva.com> 0.10-2mdk
- fix devel provides

* Sun Dec 04 2005 Austin Acton <austin@mandriva.org> 0.10-1mdk
- New release 0.10

* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 0.8-1mdk
- 0.8
- source URL
- remove patch (applied upstream)

* Sun Dec 19 2004 Mandrakelinux Team <http://www.mandrakeexpert.com> 0.7-1mdk
- New release 0.7

* Fri Oct 01 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.6-2mdk
- lib64 fixes to pkgconfig files

* Sun Jun 06 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.6-1mdk
- 0.6
- do libtoolize again

