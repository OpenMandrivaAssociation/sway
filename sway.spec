%define _disable_ld_no_undefined 1

Summary:	SirCmpwn's Wayland window manager
Name:           sway
Version:        0.5
Release:        7
License:        GPLv2+
Group:          Monitoring
Url:		https://github.com/SirCmpwn/sway
Source0:	https://github.com/SirCmpwn/sway/archive/%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(wlc)
BuildRequires:	pkgconfig(chck)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libinput)
BuildRequires:	pcre-devel
BuildRequires:	pam-devel
BuildRequires:	a2x
BuildRequires:	ffmpeg-devel

%description
"SirCmpwn's Wayland window manager" is a work in progress
i3-compatible window manager for Wayland.

%package	zsh-completion
Summary:	zsh-completion for %{name}
Group:		Editors

%description	zsh-completion
Zsh completion for %{name}

%prep
%setup -q

%build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_INSTALL_SYSCONFDIR=/etc
%make

%install
%makeinstall_std

%files
%{_sysconfdir}/%{name}/config
%{_sysconfdir}/pam.d/swaylock
%{_bindir}/sway*
%{_mandir}/man5/%{name}*.*
%{_mandir}/man1/%{name}*.*
%{_datadir}/%{name}/
%{_datadir}/wayland-sessions/sway.desktop

%files zsh-completion
%{_datadir}/zsh/site-functions/_sway*

