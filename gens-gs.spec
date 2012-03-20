%define		sname		gens
%define		gitdate		20090911

Name:		%{sname}-gs
Version:	2.16.7
Release:	%mkrel 2
Summary:	A Sega Genesis, Sega CD and Sega 32X emulator
License:	GPLv2+
Group:		Emulators
URL:		http://info.sonicretro.org/Gens/GS
Source0:	Gens-gs-r7.tar.bz2
Source1:	gens-gs.png
Patch0:		gens-gs-r7-gtk-deprecated.patch
BuildRequires:	gtk2-devel
BuildRequires:	SDL-devel
BuildRequires:	zlib-devel
BuildRequires:	png-devel
BuildRequires:	gtkglextmm-devel
BuildRequires:	nasm
BuildRequires:	desktop-file-utils
Conflicts:	gens
ExclusiveArch:	%{ix86}

%description
Gens is an emulator for the Sega Genesis, Sega CD and Sega 32X.
Gens/GS is a version of Gens maintained by GerbilSoft.
The main goal of Gens/GS is to clean up the source code and combine
features from various forks of Gens.

%prep
%setup -q -n %{name}-r7
%patch0 -p1

%build
autoreconf -i
%configure
%make

%install
%__rm -rf %{buildroot}
%makeinstall

desktop-file-install --vendor="" \
 --remove-category="Application" \
 --remove-category="Game" \
 --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
 --dir %{buildroot}%{_datadir}/applications/ \
 %{buildroot}%{_datadir}/applications/*

%__rm -f %{buildroot}%{_libdir}/mdp/*.{a,la}

%clean
%__rm -rf %{buildroot}

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

