Summary:	SirCmpwn's Wayland window manager
Name:		sway
Version:	1.10~rc1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://swaywm.org/
# git clone https://github.com/SirCmpwn/sway.git
# git archive --format=tar --prefix sway-0.5-$(date +%Y%m%d)/ HEAD | xz -vf > ../sway-0.5-$(date +%Y%m%d).tar.xz
# Source0:	https://github.com/SirCmpwn/sway/archive/%{name}-%{version}-%{date}.tar.xz
Source0:	https://github.com/swaywm/sway/archive/1.10-rc1/%{name}-1.10-rc1.tar.gz

BuildRequires:	meson
BuildRequires:	egl-devel
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(wlroots) >= 0.17.0
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	scdoc
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(libcap)
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	pcre-devel
BuildRequires:	pam-devel
BuildRequires:	xsltproc
BuildRequires:	docbook-dtds

Requires(pre):	libcap-utils
Requires:	imagemagick
# update it too next time
Requires:	swaylock
Requires:	swayidle
Requires:	rofi
Requires:	grim
Requires:	slurp
Requires:	swaybg
Requires:	kitty
Requires:	mako
Requires:	wl-clipboard
Requires:	pavucontrol-qt
Requires:	fonts-ttf-liberation

Recommends:	sway-systemd
Recommends:	dri-drivers
Recommends:	qt5-qtwayland
Recommends:	distro-release-theme
Recommends:	xwayland
Recommends:	kitty
Recommends:	fontconfig

%description
"SirCmpwn's Wayland window manager" is a work in progress
i3-compatible window manager for Wayland.

%prep
%autosetup -n %{name}-1.10-rc1 -p1

%build
export CFLAGS="%{optflags} -O3"
%meson -Dsd-bus-provider=libsystemd
%meson_build

%install
%meson_install
# use kitty terminal
sed -i 's!urxvt!kitty!g' %{buildroot}/etc/sway/config
# set our background
sed -i "s|^output \* bg .*|output * bg /usr/share/mdk/backgrounds/default.png fill|" %{buildroot}%{_sysconfdir}/sway/config
# Create directory for extra config snippets
install -d -m755 -pv %{buildroot}%{_sysconfdir}/sway/config.d

%post
%{_sbindir}/setcap cap_sys_ptrace=eip %{_bindir}/sway

%files
%config(noreplace)%{_sysconfdir}/%{name}/config
%dir %{_sysconfdir}/sway/config.d
%{_bindir}/sway*
%{_mandir}/man5/%{name}*.*
%{_mandir}/man7/sway*.7.*
%{_mandir}/man1/%{name}*.*
%{_datadir}/backgrounds/%{name}/
%{_datadir}/wayland-sessions/sway.desktop
%{_datadir}/bash-completion/completions/*
%{_datadir}/fish/vendor_completions.d/*
%{_datadir}/zsh/site-functions/*
