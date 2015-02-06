Summary:	Sega Genesis/Megadrive, Sega CD and Sega 32X emulator
Name:		gens-gs
Version:	2.16.7
Release:	8
License:	GPLv2+
Group:		Emulators
Url:		http://info.sonicretro.org/Gens/GS
Source0:	Gens-gs-r7.tar.bz2
Patch0:		gens-gs-r7-gtk-deprecated.patch
BuildRequires:	imagemagick
BuildRequires:	nasm
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkglextmm-1.2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)
Conflicts:	gens
ExclusiveArch:	%{ix86}

%description
Gens is an emulator for the Sega Genesis/Megadrive, Sega CD and Sega 32X.

Gens/GS is a version of Gens maintained by GerbilSoft.

The main goal of Gens/GS is to clean up the source code and combine features
from various forks of Gens.

%files
%doc AUTHORS.txt ChangeLog.txt NEWS.txt README.txt doc/*
%{_bindir}/%{name}
%{_bindir}/mdp_test
%dir %{_datadir}/gens/
%{_datadir}/gens/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_libdir}/mdp/*.so
%{_docdir}/*

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-r7
%patch0 -p1

%build
autoreconf -i
%configure2_5x LDFLAGS='%{ldflags} -fuse-ld=bfd' CFLAGS='-ldl -lX11'
%make

%install
%makeinstall_std

mv %{buildroot}%{_bindir}/gens %{buildroot}%{_bindir}/%{name}

rm -f %{buildroot}%{_libdir}/mdp/*.{a,la}

# install menu icons
for N in 16 32 48 64 128;
do
convert images/gensgs_48x48.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done

rm -f %{buildroot}%{_datadir}/applications/gens.desktop

install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Gens/GS
Comment=Sega Genesis/Megadrive, Sega CD and Sega 32X emulator
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF
