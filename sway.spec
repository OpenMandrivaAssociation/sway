Summary:	SirCmpwn's Wayland window manager
Name:           sway
Version:        0.10
Release:        1
License:        GPLv2+
Group:          Monitoring
Url:		https://github.com/SirCmpwn/sway
# git clone https://github.com/SirCmpwn/sway.git
# git archive --format=tar --prefix sway-0.5-$(date +%Y%m%d)/ HEAD | xz -vf > ../sway-0.5-$(date +%Y%m%d).tar.xz
# Source0:	https://github.com/SirCmpwn/sway/archive/%{name}-%{version}-%{date}.tar.xz
Source0:	https://github.com/SirCmpwn/sway/archive/%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(wlc)
BuildRequires:	pkgconfig(chck)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libinput)
BuildRequires:	pcre-devel
BuildRequires:	pam-devel
BuildRequires:	a2x
BuildRequires:	xsltproc
BuildRequires:	docbook-dtds
BuildRequires:	ffmpeg-devel

%description
"SirCmpwn's Wayland window manager" is a work in progress
i3-compatible window manager for Wayland.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_INSTALL_SYSCONFDIR=/etc
%make

%install
%makeinstall_std -C build

%files
%{_sysconfdir}/%{name}/config
%{_sysconfdir}/pam.d/swaylock
%{_bindir}/sway*
%{_mandir}/man5/%{name}*.*
%{_mandir}/man1/%{name}*.*
%{_datadir}/%{name}/
%{_datadir}/wayland-sessions/sway.desktop
