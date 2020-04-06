#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fwupd
Version  : 1.3.6
Release  : 44
URL      : https://github.com/hughsie/fwupd/archive/1.3.6/fwupd-1.3.6.tar.gz
Source0  : https://github.com/hughsie/fwupd/archive/1.3.6/fwupd-1.3.6.tar.gz
Source1  : fwupd.tmpfiles
Summary  : A simple daemon to allow session software to update firmware
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: fwupd-bin = %{version}-%{release}
Requires: fwupd-config = %{version}-%{release}
Requires: fwupd-data = %{version}-%{release}
Requires: fwupd-lib = %{version}-%{release}
Requires: fwupd-libexec = %{version}-%{release}
Requires: fwupd-license = %{version}-%{release}
Requires: fwupd-locales = %{version}-%{release}
Requires: fwupd-man = %{version}-%{release}
Requires: fwupd-services = %{version}-%{release}
Requires: glib
Requires: gsettings-desktop-schemas
BuildRequires : Pillow
BuildRequires : bash-completion-dev
BuildRequires : buildreq-meson
BuildRequires : clear-font
BuildRequires : fontconfig
BuildRequires : gcab
BuildRequires : glib
BuildRequires : glibc-bin
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : gnu-efi-staticdev
BuildRequires : gobject-introspection-dev
BuildRequires : gpgme-dev
BuildRequires : gsettings-desktop-schemas
BuildRequires : gtk-doc
BuildRequires : help2man
BuildRequires : libgpg-error-dev
BuildRequires : libsmbios-dev
BuildRequires : libxslt
BuildRequires : pkgconfig(appstream-glib)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(colorhug)
BuildRequires : pkgconfig(efivar)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(gusb)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libelf)
BuildRequires : pkgconfig(libgcab-1.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(tss2-esys)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(xmlb)
BuildRequires : popt-dev
BuildRequires : pycairo
BuildRequires : pygobject
BuildRequires : pygobject-dev
BuildRequires : python3-dev
BuildRequires : vala
BuildRequires : valgrind
Patch1: 0001-Guard-against-option-rom-read.patch
Patch2: 0002-fwupd-metadata-pki-files-are-under-usr-share-fwupd-p.patch

%description
This project aims to make updating firmware on Linux automatic, safe and
reliable. Additional information is available at the website: https://fwupd.org

%package autostart
Summary: autostart components for the fwupd package.
Group: Default

%description autostart
autostart components for the fwupd package.


%package bin
Summary: bin components for the fwupd package.
Group: Binaries
Requires: fwupd-data = %{version}-%{release}
Requires: fwupd-libexec = %{version}-%{release}
Requires: fwupd-config = %{version}-%{release}
Requires: fwupd-license = %{version}-%{release}
Requires: fwupd-services = %{version}-%{release}

%description bin
bin components for the fwupd package.


%package config
Summary: config components for the fwupd package.
Group: Default

%description config
config components for the fwupd package.


%package data
Summary: data components for the fwupd package.
Group: Data

%description data
data components for the fwupd package.


%package dev
Summary: dev components for the fwupd package.
Group: Development
Requires: fwupd-lib = %{version}-%{release}
Requires: fwupd-bin = %{version}-%{release}
Requires: fwupd-data = %{version}-%{release}
Provides: fwupd-devel = %{version}-%{release}
Requires: fwupd = %{version}-%{release}

%description dev
dev components for the fwupd package.


%package lib
Summary: lib components for the fwupd package.
Group: Libraries
Requires: fwupd-data = %{version}-%{release}
Requires: fwupd-libexec = %{version}-%{release}
Requires: fwupd-license = %{version}-%{release}

%description lib
lib components for the fwupd package.


%package libexec
Summary: libexec components for the fwupd package.
Group: Default
Requires: fwupd-config = %{version}-%{release}
Requires: fwupd-license = %{version}-%{release}

%description libexec
libexec components for the fwupd package.


%package license
Summary: license components for the fwupd package.
Group: Default

%description license
license components for the fwupd package.


%package locales
Summary: locales components for the fwupd package.
Group: Default

%description locales
locales components for the fwupd package.


%package man
Summary: man components for the fwupd package.
Group: Default

%description man
man components for the fwupd package.


%package services
Summary: services components for the fwupd package.
Group: Systemd services

%description services
services components for the fwupd package.


%package tests
Summary: tests components for the fwupd package.
Group: Default
Requires: fwupd = %{version}-%{release}

%description tests
tests components for the fwupd package.


%prep
%setup -q -n fwupd-1.3.6
cd %{_builddir}/fwupd-1.3.6
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586882108
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgtkdoc=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/fwupd
cp %{_builddir}/fwupd-1.3.6/COPYING %{buildroot}/usr/share/package-licenses/fwupd/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/fwupd-1.3.6/contrib/debian/signing-template/copyright %{buildroot}/usr/share/package-licenses/fwupd/c1a12b921301c21ba9b3dc26e7db1d859bb8259d
cp %{_builddir}/fwupd-1.3.6/data/tests/thunderbolt/COPYING %{buildroot}/usr/share/package-licenses/fwupd/c10b5d1532bdbc2ceae3a33e7ecc8ecbb7f7d260
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang fwupd
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/fwupd.conf
## Remove excluded files
rm -f %{buildroot}/var/lib/fwupd/builder/README.md
## install_append content
rm -fr %{buildroot}/usr/share/fwupd/dbus-1
rm %{buildroot}/usr/lib/systemd/system/system-update.target.wants/fwupd-offline-update.service
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../fwupd.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/fwupd.service
mv %{buildroot}/etc/pki %{buildroot}/usr/share/fwupd/pki
mkdir -p %{buildroot}/usr/share/defaults
mv %{buildroot}/etc/fwupd %{buildroot}/usr/share/defaults/fwupd
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system-preset/fwupd-refresh.preset
/usr/lib/systemd/system-shutdown/fwupd.shutdown

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/fwupd.service

%files bin
%defattr(-,root,root,-)
/usr/bin/dfu-tool
/usr/bin/fwupdmgr

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/fwupd.conf
/usr/lib/udev/rules.d/90-fwupd-devices.rules

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Fwupd-2.0.typelib
/usr/lib64/girepository-1.0/FwupdPlugin-1.0.typelib
/usr/share/bash-completion/completions/fwupdagent
/usr/share/bash-completion/completions/fwupdmgr
/usr/share/bash-completion/completions/fwupdtool
/usr/share/dbus-1/interfaces/org.freedesktop.fwupd.xml
/usr/share/dbus-1/system-services/org.freedesktop.fwupd.service
/usr/share/dbus-1/system.d/org.freedesktop.fwupd.conf
/usr/share/defaults/fwupd/daemon.conf
/usr/share/defaults/fwupd/redfish.conf
/usr/share/defaults/fwupd/remotes.d/dell-esrt.conf
/usr/share/defaults/fwupd/remotes.d/fwupd-tests.conf
/usr/share/defaults/fwupd/remotes.d/lvfs-testing.conf
/usr/share/defaults/fwupd/remotes.d/lvfs.conf
/usr/share/defaults/fwupd/remotes.d/vendor-directory.conf
/usr/share/defaults/fwupd/remotes.d/vendor.conf
/usr/share/defaults/fwupd/thunderbolt.conf
/usr/share/defaults/fwupd/uefi.conf
/usr/share/fwupd/add_capsule_header.py
/usr/share/fwupd/firmware_packager.py
/usr/share/fwupd/install_dell_bios_exe.py
/usr/share/fwupd/metainfo/org.freedesktop.fwupd.remotes.lvfs-testing.metainfo.xml
/usr/share/fwupd/metainfo/org.freedesktop.fwupd.remotes.lvfs.metainfo.xml
/usr/share/fwupd/pki/fwupd-metadata/GPG-KEY-Linux-Foundation-Metadata
/usr/share/fwupd/pki/fwupd-metadata/GPG-KEY-Linux-Vendor-Firmware-Service
/usr/share/fwupd/pki/fwupd-metadata/LVFS-CA.pem
/usr/share/fwupd/pki/fwupd/GPG-KEY-Hughski-Limited
/usr/share/fwupd/pki/fwupd/GPG-KEY-Linux-Foundation-Firmware
/usr/share/fwupd/pki/fwupd/GPG-KEY-Linux-Vendor-Firmware-Service
/usr/share/fwupd/pki/fwupd/LVFS-CA.pem
/usr/share/fwupd/quirks.d/altos.quirk
/usr/share/fwupd/quirks.d/ata.quirk
/usr/share/fwupd/quirks.d/colorhug.quirk
/usr/share/fwupd/quirks.d/coreboot.quirk
/usr/share/fwupd/quirks.d/csr-aiaiai.quirk
/usr/share/fwupd/quirks.d/dell-dock.quirk
/usr/share/fwupd/quirks.d/dell.quirk
/usr/share/fwupd/quirks.d/dfu.quirk
/usr/share/fwupd/quirks.d/ebitdo.quirk
/usr/share/fwupd/quirks.d/emmc.quirk
/usr/share/fwupd/quirks.d/fastboot.quirk
/usr/share/fwupd/quirks.d/jabra.quirk
/usr/share/fwupd/quirks.d/logitech-hidpp.quirk
/usr/share/fwupd/quirks.d/nitrokey.quirk
/usr/share/fwupd/quirks.d/nvme.quirk
/usr/share/fwupd/quirks.d/optionrom.quirk
/usr/share/fwupd/quirks.d/rts54hid.quirk
/usr/share/fwupd/quirks.d/rts54hub.quirk
/usr/share/fwupd/quirks.d/solokey.quirk
/usr/share/fwupd/quirks.d/steelseries.quirk
/usr/share/fwupd/quirks.d/superio.quirk
/usr/share/fwupd/quirks.d/synaptics-cxaudio.quirk
/usr/share/fwupd/quirks.d/synaptics-mst.quirk
/usr/share/fwupd/quirks.d/synaptics-prometheus.quirk
/usr/share/fwupd/quirks.d/synaptics-rmi.quirk
/usr/share/fwupd/quirks.d/thelio-io.quirk
/usr/share/fwupd/quirks.d/tpm.quirk
/usr/share/fwupd/quirks.d/uefi-recovery.quirk
/usr/share/fwupd/quirks.d/uefi.quirk
/usr/share/fwupd/quirks.d/vli-usbhub-lenovo.quirk
/usr/share/fwupd/quirks.d/vli-usbhub.quirk
/usr/share/fwupd/quirks.d/wacom-raw.quirk
/usr/share/fwupd/quirks.d/wacom-usb.quirk
/usr/share/fwupd/remotes.d/dell-esrt/metadata.xml
/usr/share/fwupd/remotes.d/vendor/firmware/README.md
/usr/share/fwupd/simple_client.py
/usr/share/gir-1.0/*.gir
/usr/share/icons/hicolor/scalable/apps/org.freedesktop.fwupd.svg
/usr/share/locale/ca/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/da/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/da/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/da/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/da/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/da/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/da/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/da/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/da/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/de/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/de/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/de/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/de/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/de/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/de/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/de/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/de/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/lt/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/lt/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/lt/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/lt/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/lt/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/lt/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/lt/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/lt/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/metainfo/org.freedesktop.fwupd.metainfo.xml
/usr/share/polkit-1/actions/org.freedesktop.fwupd.policy
/usr/share/polkit-1/rules.d/org.freedesktop.fwupd.rules
/usr/share/vala/vapi/fwupd.deps
/usr/share/vala/vapi/fwupd.vapi
/usr/share/vala/vapi/fwupdplugin.deps
/usr/share/vala/vapi/fwupdplugin.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/fwupd-1/fwupd.h
/usr/include/fwupd-1/fwupdplugin.h
/usr/include/fwupd-1/libfwupd/fwupd-client.h
/usr/include/fwupd-1/libfwupd/fwupd-common.h
/usr/include/fwupd-1/libfwupd/fwupd-deprecated.h
/usr/include/fwupd-1/libfwupd/fwupd-device.h
/usr/include/fwupd-1/libfwupd/fwupd-enums.h
/usr/include/fwupd-1/libfwupd/fwupd-error.h
/usr/include/fwupd-1/libfwupd/fwupd-release.h
/usr/include/fwupd-1/libfwupd/fwupd-remote.h
/usr/include/fwupd-1/libfwupd/fwupd-version.h
/usr/include/fwupd-1/libfwupdplugin/fu-archive.h
/usr/include/fwupd-1/libfwupdplugin/fu-chunk.h
/usr/include/fwupd-1/libfwupdplugin/fu-common-cab.h
/usr/include/fwupd-1/libfwupdplugin/fu-common-guid.h
/usr/include/fwupd-1/libfwupdplugin/fu-common-version.h
/usr/include/fwupd-1/libfwupdplugin/fu-common.h
/usr/include/fwupd-1/libfwupdplugin/fu-device-locker.h
/usr/include/fwupd-1/libfwupdplugin/fu-device-metadata.h
/usr/include/fwupd-1/libfwupdplugin/fu-device.h
/usr/include/fwupd-1/libfwupdplugin/fu-dfu-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-firmware-common.h
/usr/include/fwupd-1/libfwupdplugin/fu-firmware-image.h
/usr/include/fwupd-1/libfwupdplugin/fu-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-hwids.h
/usr/include/fwupd-1/libfwupdplugin/fu-ihex-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-io-channel.h
/usr/include/fwupd-1/libfwupdplugin/fu-plugin-vfuncs.h
/usr/include/fwupd-1/libfwupdplugin/fu-plugin.h
/usr/include/fwupd-1/libfwupdplugin/fu-quirks.h
/usr/include/fwupd-1/libfwupdplugin/fu-smbios.h
/usr/include/fwupd-1/libfwupdplugin/fu-srec-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-udev-device.h
/usr/include/fwupd-1/libfwupdplugin/fu-usb-device.h
/usr/lib64/libfwupd.so
/usr/lib64/libfwupdplugin.so
/usr/lib64/pkgconfig/fwupd.pc
/usr/lib64/pkgconfig/fwupdplugin.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/fwupd-plugins-3/libfu_plugin_altos.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_amt.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_ata.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_colorhug.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_coreboot.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_csr.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_dell.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_dell_dock.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_dell_esrt.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_dfu.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_ebitdo.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_emmc.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_fastboot.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_jabra.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_logitech_hidpp.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_nitrokey.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_nvme.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_optionrom.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_redfish.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_rts54hid.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_rts54hub.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_solokey.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_steelseries.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_superio.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_synaptics_cxaudio.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_synaptics_mst.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_synaptics_prometheus.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_synaptics_rmi.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_thelio_io.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_thunderbolt.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_thunderbolt_power.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_tpm.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_tpm_eventlog.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_uefi.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_uefi_recovery.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_upower.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_vli_usbhub.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_wacom_raw.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_wacom_usb.so
/usr/lib64/libfwupd.so.2
/usr/lib64/libfwupd.so.2.0.0
/usr/lib64/libfwupdplugin.so.1
/usr/lib64/libfwupdplugin.so.1.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/fwupd/efi/fwupdx64.efi
/usr/libexec/fwupd/fwupd
/usr/libexec/fwupd/fwupdagent
/usr/libexec/fwupd/fwupdate
/usr/libexec/fwupd/fwupdoffline
/usr/libexec/fwupd/fwupdtool
/usr/libexec/fwupd/fwupdtpmevlog

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fwupd/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/fwupd/c10b5d1532bdbc2ceae3a33e7ecc8ecbb7f7d260
/usr/share/package-licenses/fwupd/c1a12b921301c21ba9b3dc26e7db1d859bb8259d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dfu-tool.1
/usr/share/man/man1/fwupdmgr.1

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/fwupd.service
/usr/lib/systemd/system/fwupd-offline-update.service
/usr/lib/systemd/system/fwupd-refresh.service
/usr/lib/systemd/system/fwupd-refresh.timer
/usr/lib/systemd/system/fwupd.service

%files tests
%defattr(-,root,root,-)
/usr/share/installed-tests/fwupd/fakedevice123.cab
/usr/share/installed-tests/fwupd/fakedevice124.cab
/usr/share/installed-tests/fwupd/fwupd-tests.xml
/usr/share/installed-tests/fwupd/fwupdmgr.sh
/usr/share/installed-tests/fwupd/fwupdmgr.test
/usr/share/installed-tests/fwupd/hardware.py

%files locales -f fwupd.lang
%defattr(-,root,root,-)

