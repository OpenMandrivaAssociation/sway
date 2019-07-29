Summary:	SirCmpwn's Wayland window manager
Name:           sway
Version:        1.1.1
Release:        1
License:        GPLv2+
Group:          Monitoring
Url:		https://github.com/SirCmpwn
# git clone https://github.com/SirCmpwn/sway.git
# git archive --format=tar --prefix sway-0.5-$(date +%Y%m%d)/ HEAD | xz -vf > ../sway-0.5-$(date +%Y%m%d).tar.xz
# Source0:	https://github.com/SirCmpwn/sway/archive/%{name}-%{version}-%{date}.tar.xz
Source0:	https://github.com/SirCmpwn/sway/archive/%{version}.tar.gz
Requires(pre):	libcap-utils
Requires:	imagemagick
# update it too next time
Requires:	swaylock
Requires:	swayidle
Requires:	rofi
Requires:	grim
Requires:	slurp
Requires:	swaybg

BuildRequires:	meson
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(wlroots)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  scdoc
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:	pcre-devel
BuildRequires:	pam-devel
BuildRequires:	xsltproc
BuildRequires:	docbook-dtds

%description
"SirCmpwn's Wayland window manager" is a work in progress
i3-compatible window manager for Wayland.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%meson
%meson_build

%install
%meson_install


%post
%{_sbindir}/setcap cap_sys_ptrace=eip %{_bindir}/sway

%files
%config(noreplace)%{_sysconfdir}/%{name}/config
%{_sysconfdir}/%{name}/security.d/00-defaults
%{_bindir}/sway*
%{_mandir}/man5/%{name}*.*
%{_mandir}/man7/sway-ipc.7.*
%{_mandir}/man1/%{name}*.*
%{_datadir}/backgrounds/%{name}/
%{_datadir}/wayland-sessions/sway.desktop
%{_datadir}/bash-completion/completions/*
%{_datadir}/fish/completions/sway*
%{_datadir}/zsh/site-functions/*
