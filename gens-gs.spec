%define sname		gens

Name:		%{sname}-gs
Version:	2.16.7
Release:	4

Summary:	A Sega Genesis, Sega CD and Sega 32X emulator
License:	GPLv2+
Group:		Emulators
URL:		http://info.sonicretro.org/Gens/GS
Source0:	Gens-gs-r7.tar.bz2
Source1:	gens-gs.png
Patch0:		gens-gs-r7-gtk-deprecated.patch

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(gtkglextmm-1.2)
BuildRequires:	nasm
BuildRequires:	desktop-file-utils

Conflicts:	gens

ExclusiveArch:	%ix86

%description
Gens is an emulator for the Sega Genesis, Sega CD and Sega 32X.

Gens/GS is a version of Gens maintained by GerbilSoft.

The main goal of Gens/GS is to clean up the source code and combine features 
from various forks of Gens.

%prep
%setup -q -n %{name}-r7
%patch0 -p1

%build
autoreconf -i
%configure2_5x LDFLAGS='%{ldflags} -fuse-ld=bfd' CFLAGS='-ldl -lX11'
%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
 --remove-category="Application" \
 --remove-category="Game" \
 --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
 --dir %{buildroot}%{_datadir}/applications/ \
 %{buildroot}%{_datadir}/applications/*

rm -f %{buildroot}%{_libdir}/mdp/*.{a,la}

%files
%defattr(-,root,root,0755)
%doc AUTHORS.txt ChangeLog.txt NEWS.txt README.txt doc/*
%{_bindir}/gens
%{_bindir}/mdp_test
%dir %{_datadir}/gens/
%{_datadir}/gens/*
%{_datadir}/applications/gens.desktop
%{_libdir}/mdp/*.so
%{_docdir}/*

%changelog
* Sat Jul 30 2011 Andrey Bondrov <abondrov@mandriva.org> 2.16.7-2mdv2012.0
+ Revision: 692369
- Fix BuildRequires
- Rebuild
- Add patch0 to fix build
- Fix BuildRequires
- imported package gens-gs


* Tue Jul 19 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 2.16.6.93-1mdv2011.0
- Import from PLF
- Remove PLF reference

* Fri Sep 11 2009 Guillaume Bedot <littletux@zarb.org> 2.16.6.93-0.20090911plf2010.0
- today's git snapshot (r7 pre3 + fixes)

* Tue Jan  6 2009 Guillaume Bedot <littletux@zarb.org> 2.15.5-2plf2009.1
- 2.15.5 milestone 6

* Fri Oct 31 2008 Guillaume Bedot <littletux@zarb.org> 2.15.5-1plf2009.1
- First package of gens-gs for PLF
