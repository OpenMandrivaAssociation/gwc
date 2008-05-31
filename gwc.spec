%define name gwc
%define gwc_version 0.21
%define gwc_subversion 08
%define release %mkrel 1

Name:		%{name}
Version:	%{gwc_version}.%{gwc_subversion}
Release: 	%{release}
Summary: 	Audio restoration application
License: 	GPL
Group: 		Sound
URL: 		http://gwc.sourceforge.net/
Source0: 	http://downloads.sourceforge.net/gwc/%{name}-%{gwc_version}-%{gwc_subversion}.tar.bz2
Source1: 	%{name}_16.png
Source2: 	%{name}_32.png
Source3: 	%{name}_48.png
Patch0:		%{name}-0.21.08-fix-makefiles.patch
BuildRequires: 	libfftw2-devel libsndfile-devel libdb1-devel libgnome2-devel libgnomeui2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Gnome Wave Cleaner (GWC), is a tool for cleaning
up noisey audio files, in preparation for burning
to CD's.  The typical application is to record
the audio from vinyl LP's, 45's, 78's, etc to a
hard disk as a 16bit,stereo,44.1khz wave formated file,
and the use GWC to apply denoising and declicking
algorithms.

%prep
%setup -q -n %{name}-%{gwc_version}-%{gwc_subversion}
%patch0 -p 1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/applications

# Icons
mkdir -p ${RPM_BUILD_ROOT}{%_miconsdir,%_iconsdir,%_liconsdir}
install -m644 %{SOURCE1} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE2} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE3} -D %{buildroot}%{_liconsdir}/%{name}.png

# Menus
cat > ${RPM_BUILD_ROOT}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=GWC
GenericName=Gnome Wave Cleaner
GenericName[nl]=Gnome Audio Restauratie Gereedschap
Comment=Dehiss, denoise and declick WAV audio files
Comment[nl]=Ontruisen en 'declicken' van WAV audio bestanden
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=AudioVideo;Audio;AudioVideoEditing;
MimeType=audio/x-wav;
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING Changelog
%doc %dir %{_datadir}/gnome/help/%{name}
%doc %dir %{_datadir}/gnome/help/%{name}/C
%doc %{_datadir}/gnome/help/%{name}/C/*
%{_bindir}/%{name}
%{_iconsdir}/gwc.png
%{_miconsdir}/gwc.png
%{_liconsdir}/gwc.png
%{_datadir}/pixmaps/gwc-logo.png
%{_datadir}/applications/mandriva-%{name}.desktop

