%define __provides_exclude_from ^%{_libdir}/apulse/.*.so.*$

Name:     apulse
Version:	0.1.14
Release:	1
Summary:	PulseAudio emulation for ALSA
License:	MIT and LGPL-2.1+
Group:		System/Libraries
URL:      https://github.com/i-rinat/apulse
Source:		https://github.com/i-rinat/apulse/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(alsa)

%description
The program provides an alternative partial implementation of the
PulseAudio API.

It consists of a wrapper script and a number of shared libraries with
the same names as from original PulseAudio, so applications could
dynamically load them and think they are talking to
PulseAudio. Internally, no separate sound mixing daemon is used.

%prep
%setup -q
%autopatch -p1

%build
%cmake \
	-DAPULSEPATH:PATH=%{_libdir}/%{name} \
	-DAPULSE_SEARCH_PATHS:PATH=%{_libdir}/%{name} \
	-DUSE_BUNDLED_PULSEAUDIO_HEADERS:BOOL=ON \
  -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install -C build

ln -sf libpulsecommon-5.0.so \
    %{buildroot}%{_libdir}/%{name}/libpulsecommon-4.0.so

%files
%doc LICENSE.MIT README*
%{_bindir}/*
%{_libdir}/*
%{_mandir}/man1/apulse.1.*
