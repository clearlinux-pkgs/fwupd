#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fwupd
Version  : 1.8.1
Release  : 57
URL      : https://github.com/hughsie/fwupd/archive/1.8.1/fwupd-1.8.1.tar.gz
Source0  : https://github.com/hughsie/fwupd/archive/1.8.1/fwupd-1.8.1.tar.gz
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
Requires: udisks2
BuildRequires : bash-completion-dev
BuildRequires : buildreq-meson
BuildRequires : clear-font
BuildRequires : curl-dev
BuildRequires : fontconfig
BuildRequires : gcab
BuildRequires : glibc-bin
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : gnu-efi-staticdev
BuildRequires : gobject-introspection-dev
BuildRequires : gpgme-dev
BuildRequires : gtk-doc
BuildRequires : help2man
BuildRequires : libgpg-error-dev
BuildRequires : libsmbios-dev
BuildRequires : libxslt
BuildRequires : pkgconfig(appstream-glib)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(colorhug)
BuildRequires : pkgconfig(efiboot)
BuildRequires : pkgconfig(efivar)
BuildRequires : pkgconfig(fwupd-efi)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(gusb)
BuildRequires : pkgconfig(jcat)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libelf)
BuildRequires : pkgconfig(libgcab-1.0)
BuildRequires : pkgconfig(libprotobuf-c)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(mbim-glib)
BuildRequires : pkgconfig(mm-glib)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(qmi-glib)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(tss2-esys)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(xmlb)
BuildRequires : popt-dev
BuildRequires : pycairo
BuildRequires : pygobject
BuildRequires : pygobject-dev
BuildRequires : pypi(pillow)
BuildRequires : python3-dev
BuildRequires : vala
Patch1: 0001-pki-files-are-moved-under-datadir.patch

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


%package doc
Summary: doc components for the fwupd package.
Group: Documentation
Requires: fwupd-man = %{version}-%{release}

%description doc
doc components for the fwupd package.


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
%setup -q -n fwupd-1.8.1
cd %{_builddir}/fwupd-1.8.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653661629
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddocs=none \
-Dplugin_tpm=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/fwupd
cp %{_builddir}/fwupd-1.8.1/COPYING %{buildroot}/usr/share/package-licenses/fwupd/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/fwupd-1.8.1/plugins/thunderbolt/tests/COPYING %{buildroot}/usr/share/package-licenses/fwupd/c10b5d1532bdbc2ceae3a33e7ecc8ecbb7f7d260
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang fwupd
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/fwupd.conf
## Remove excluded files
rm -f %{buildroot}*/var/lib/fwupd/builder/README.md
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
/usr/bin/dbxtool
/usr/bin/dfu-tool
/usr/bin/fwupdagent
/usr/bin/fwupdate
/usr/bin/fwupdmgr
/usr/bin/fwupdtool

%files config
%defattr(-,root,root,-)
/usr/lib/modules-load.d/fwupd-msr.conf
/usr/lib/modules-load.d/fwupd-redfish.conf
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
/usr/share/defaults/fwupd/msr.conf
/usr/share/defaults/fwupd/redfish.conf
/usr/share/defaults/fwupd/remotes.d/dell-esrt.conf
/usr/share/defaults/fwupd/remotes.d/fwupd-tests.conf
/usr/share/defaults/fwupd/remotes.d/lvfs-testing.conf
/usr/share/defaults/fwupd/remotes.d/lvfs.conf
/usr/share/defaults/fwupd/remotes.d/vendor-directory.conf
/usr/share/defaults/fwupd/remotes.d/vendor.conf
/usr/share/defaults/fwupd/thunderbolt.conf
/usr/share/defaults/fwupd/uefi_capsule.conf
/usr/share/fish/vendor_completions.d/fwupdmgr.fish
/usr/share/fwupd/add_capsule_header.py
/usr/share/fwupd/device-tests/8bitdo-nes30pro.json
/usr/share/fwupd/device-tests/8bitdo-sf30pro.json
/usr/share/fwupd/device-tests/8bitdo-sfc30.json
/usr/share/fwupd/device-tests/aiaiai-h05.json
/usr/share/fwupd/device-tests/bizlink-no-sku-vli.json
/usr/share/fwupd/device-tests/dell-kh08p.json
/usr/share/fwupd/device-tests/dell-wd19tb.json
/usr/share/fwupd/device-tests/fwupd-a3bu-xplained.json
/usr/share/fwupd/device-tests/fwupd-at90usbkey.json
/usr/share/fwupd/device-tests/hp-dock-g5.json
/usr/share/fwupd/device-tests/hughski-colorhug-plus.json
/usr/share/fwupd/device-tests/hughski-colorhug.json
/usr/share/fwupd/device-tests/hughski-colorhug2.json
/usr/share/fwupd/device-tests/hyper-no-sku-vli.json
/usr/share/fwupd/device-tests/jabra-speak-410.json
/usr/share/fwupd/device-tests/jabra-speak-510.json
/usr/share/fwupd/device-tests/jabra-speak-710.json
/usr/share/fwupd/device-tests/lenovo-03x7168.json
/usr/share/fwupd/device-tests/lenovo-03x7605.json
/usr/share/fwupd/device-tests/lenovo-03x7608-vli.json
/usr/share/fwupd/device-tests/lenovo-03x7609-cxaudio.json
/usr/share/fwupd/device-tests/lenovo-40au0065-vli.json
/usr/share/fwupd/device-tests/lenovo-GX90T33021-vli.json
/usr/share/fwupd/device-tests/logitech-bolt-receiver.json
/usr/share/fwupd/device-tests/logitech-k780.json
/usr/share/fwupd/device-tests/logitech-m650.json
/usr/share/fwupd/device-tests/logitech-m750.json
/usr/share/fwupd/device-tests/logitech-mr0077.json
/usr/share/fwupd/device-tests/logitech-rqr12-signed.json
/usr/share/fwupd/device-tests/logitech-rqr12.json
/usr/share/fwupd/device-tests/logitech-rqr24-signed.json
/usr/share/fwupd/device-tests/logitech-rqr24.json
/usr/share/fwupd/device-tests/nordic-hid-nrf52840-mcuboot.json
/usr/share/fwupd/device-tests/realtek-rts5423.json
/usr/share/fwupd/device-tests/realtek-rts5855.json
/usr/share/fwupd/device-tests/synaptics-prometheus.json
/usr/share/fwupd/device-tests/system76-thelio.json
/usr/share/fwupd/device-tests/ugreen-cm260.json
/usr/share/fwupd/device-tests/wacom-intuos-bt-m-bluetooth.json
/usr/share/fwupd/device-tests/wacom-intuos-bt-m-main.json
/usr/share/fwupd/device-tests/wacom-intuos-bt-m.json
/usr/share/fwupd/device-tests/wacom-intuos-bt-s.json
/usr/share/fwupd/firmware_packager.py
/usr/share/fwupd/install_dell_bios_exe.py
/usr/share/fwupd/metainfo/org.freedesktop.fwupd.remotes.lvfs-testing.metainfo.xml
/usr/share/fwupd/metainfo/org.freedesktop.fwupd.remotes.lvfs.metainfo.xml
/usr/share/fwupd/pki/fwupd-metadata/GPG-KEY-Linux-Foundation-Metadata
/usr/share/fwupd/pki/fwupd-metadata/GPG-KEY-Linux-Vendor-Firmware-Service
/usr/share/fwupd/pki/fwupd-metadata/LVFS-CA.pem
/usr/share/fwupd/pki/fwupd/GPG-KEY-Linux-Foundation-Firmware
/usr/share/fwupd/pki/fwupd/GPG-KEY-Linux-Vendor-Firmware-Service
/usr/share/fwupd/pki/fwupd/LVFS-CA.pem
/usr/share/fwupd/quirks.d/analogix.quirk
/usr/share/fwupd/quirks.d/ata.quirk
/usr/share/fwupd/quirks.d/bcm57xx.quirk
/usr/share/fwupd/quirks.d/ccgx-ids.quirk
/usr/share/fwupd/quirks.d/ccgx.quirk
/usr/share/fwupd/quirks.d/cfi.quirk
/usr/share/fwupd/quirks.d/cfu.quirk
/usr/share/fwupd/quirks.d/ch341a.quirk
/usr/share/fwupd/quirks.d/colorhug.quirk
/usr/share/fwupd/quirks.d/corsair.quirk
/usr/share/fwupd/quirks.d/cpu.quirk
/usr/share/fwupd/quirks.d/cros-ec.quirk
/usr/share/fwupd/quirks.d/dell-dock.quirk
/usr/share/fwupd/quirks.d/dell.quirk
/usr/share/fwupd/quirks.d/dfu-csr.quirk
/usr/share/fwupd/quirks.d/dfu.quirk
/usr/share/fwupd/quirks.d/ebitdo.quirk
/usr/share/fwupd/quirks.d/elanfp.quirk
/usr/share/fwupd/quirks.d/elantp.quirk
/usr/share/fwupd/quirks.d/emmc.quirk
/usr/share/fwupd/quirks.d/ep963x.quirk
/usr/share/fwupd/quirks.d/fastboot.quirk
/usr/share/fwupd/quirks.d/fresco-pd.quirk
/usr/share/fwupd/quirks.d/genesys.quirk
/usr/share/fwupd/quirks.d/goodixmoc.quirk
/usr/share/fwupd/quirks.d/gpio.quirk
/usr/share/fwupd/quirks.d/hailuck.quirk
/usr/share/fwupd/quirks.d/iommu.quirk
/usr/share/fwupd/quirks.d/jabra.quirk
/usr/share/fwupd/quirks.d/logitech-bulkcontroller.quirk
/usr/share/fwupd/quirks.d/logitech-hidpp.quirk
/usr/share/fwupd/quirks.d/modem-manager.quirk
/usr/share/fwupd/quirks.d/msr.quirk
/usr/share/fwupd/quirks.d/mtd.quirk
/usr/share/fwupd/quirks.d/nitrokey.quirk
/usr/share/fwupd/quirks.d/nordic-hid.quirk
/usr/share/fwupd/quirks.d/nvme.quirk
/usr/share/fwupd/quirks.d/optionrom.quirk
/usr/share/fwupd/quirks.d/parade-lspcon.quirk
/usr/share/fwupd/quirks.d/pci-bcr.quirk
/usr/share/fwupd/quirks.d/pci-mei.quirk
/usr/share/fwupd/quirks.d/pci-psp.quirk
/usr/share/fwupd/quirks.d/pixart-rf.quirk
/usr/share/fwupd/quirks.d/power.quirk
/usr/share/fwupd/quirks.d/realtek-mst.quirk
/usr/share/fwupd/quirks.d/redfish.quirk
/usr/share/fwupd/quirks.d/rts54hid.quirk
/usr/share/fwupd/quirks.d/rts54hub.quirk
/usr/share/fwupd/quirks.d/scsi.quirk
/usr/share/fwupd/quirks.d/steelseries.quirk
/usr/share/fwupd/quirks.d/superio.quirk
/usr/share/fwupd/quirks.d/synaptics-cape.quirk
/usr/share/fwupd/quirks.d/synaptics-cxaudio.quirk
/usr/share/fwupd/quirks.d/synaptics-mst.quirk
/usr/share/fwupd/quirks.d/synaptics-prometheus.quirk
/usr/share/fwupd/quirks.d/synaptics-rmi.quirk
/usr/share/fwupd/quirks.d/system76-launch.quirk
/usr/share/fwupd/quirks.d/test-ble.quirk
/usr/share/fwupd/quirks.d/thelio-io.quirk
/usr/share/fwupd/quirks.d/thunderbolt.quirk
/usr/share/fwupd/quirks.d/uefi-capsule.quirk
/usr/share/fwupd/quirks.d/uefi-dbx.quirk
/usr/share/fwupd/quirks.d/uefi-recovery.quirk
/usr/share/fwupd/quirks.d/uf2.quirk
/usr/share/fwupd/quirks.d/usi-dock.quirk
/usr/share/fwupd/quirks.d/vli-bizlink.quirk
/usr/share/fwupd/quirks.d/vli-dell.quirk
/usr/share/fwupd/quirks.d/vli-goodway.quirk
/usr/share/fwupd/quirks.d/vli-hyper.quirk
/usr/share/fwupd/quirks.d/vli-lenovo.quirk
/usr/share/fwupd/quirks.d/vli-samsung.quirk
/usr/share/fwupd/quirks.d/wacom-raw.quirk
/usr/share/fwupd/quirks.d/wacom-usb.quirk
/usr/share/fwupd/remotes.d/dell-esrt/metadata.xml
/usr/share/fwupd/remotes.d/vendor/firmware/README.md
/usr/share/fwupd/simple_client.py
/usr/share/fwupd/uefi-capsule-ux.tar.xz
/usr/share/gir-1.0/*.gir
/usr/share/icons/hicolor/scalable/apps/org.freedesktop.fwupd.svg
/usr/share/metainfo/org.freedesktop.fwupd.metainfo.xml
/usr/share/polkit-1/actions/org.freedesktop.fwupd.policy
/usr/share/polkit-1/rules.d/org.freedesktop.fwupd.rules
/usr/share/vala/vapi/fwupd.deps
/usr/share/vala/vapi/fwupd.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/fwupd-1/fwupd.h
/usr/include/fwupd-1/fwupdplugin.h
/usr/include/fwupd-1/libfwupd/fwupd-client-sync.h
/usr/include/fwupd-1/libfwupd/fwupd-client.h
/usr/include/fwupd-1/libfwupd/fwupd-common.h
/usr/include/fwupd-1/libfwupd/fwupd-deprecated.h
/usr/include/fwupd-1/libfwupd/fwupd-device.h
/usr/include/fwupd-1/libfwupd/fwupd-enums.h
/usr/include/fwupd-1/libfwupd/fwupd-error.h
/usr/include/fwupd-1/libfwupd/fwupd-plugin.h
/usr/include/fwupd-1/libfwupd/fwupd-release.h
/usr/include/fwupd-1/libfwupd/fwupd-remote.h
/usr/include/fwupd-1/libfwupd/fwupd-request.h
/usr/include/fwupd-1/libfwupd/fwupd-security-attr.h
/usr/include/fwupd-1/libfwupd/fwupd-version.h
/usr/include/fwupd-1/libfwupdplugin/fu-archive-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-archive.h
/usr/include/fwupd-1/libfwupdplugin/fu-backend.h
/usr/include/fwupd-1/libfwupdplugin/fu-bluez-device.h
/usr/include/fwupd-1/libfwupdplugin/fu-cabinet.h
/usr/include/fwupd-1/libfwupdplugin/fu-cfi-device.h
/usr/include/fwupd-1/libfwupdplugin/fu-cfu-common.h
/usr/include/fwupd-1/libfwupdplugin/fu-cfu-offer.h
/usr/include/fwupd-1/libfwupdplugin/fu-cfu-payload.h
/usr/include/fwupd-1/libfwupdplugin/fu-chunk.h
/usr/include/fwupd-1/libfwupdplugin/fu-common-cab.h
/usr/include/fwupd-1/libfwupdplugin/fu-common-guid.h
/usr/include/fwupd-1/libfwupdplugin/fu-common-version.h
/usr/include/fwupd-1/libfwupdplugin/fu-common.h
/usr/include/fwupd-1/libfwupdplugin/fu-context.h
/usr/include/fwupd-1/libfwupdplugin/fu-coswid-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-deprecated.h
/usr/include/fwupd-1/libfwupdplugin/fu-device-locker.h
/usr/include/fwupd-1/libfwupdplugin/fu-device-metadata.h
/usr/include/fwupd-1/libfwupdplugin/fu-device.h
/usr/include/fwupd-1/libfwupdplugin/fu-dfu-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-dfuse-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-efi-common.h
/usr/include/fwupd-1/libfwupdplugin/fu-efi-firmware-file.h
/usr/include/fwupd-1/libfwupdplugin/fu-efi-firmware-filesystem.h
/usr/include/fwupd-1/libfwupdplugin/fu-efi-firmware-section.h
/usr/include/fwupd-1/libfwupdplugin/fu-efi-firmware-volume.h
/usr/include/fwupd-1/libfwupdplugin/fu-efi-signature-list.h
/usr/include/fwupd-1/libfwupdplugin/fu-efi-signature.h
/usr/include/fwupd-1/libfwupdplugin/fu-efivar.h
/usr/include/fwupd-1/libfwupdplugin/fu-firmware-common.h
/usr/include/fwupd-1/libfwupdplugin/fu-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-fmap-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-hid-device.h
/usr/include/fwupd-1/libfwupdplugin/fu-hwids.h
/usr/include/fwupd-1/libfwupdplugin/fu-i2c-device.h
/usr/include/fwupd-1/libfwupdplugin/fu-ifd-bios.h
/usr/include/fwupd-1/libfwupdplugin/fu-ifd-common.h
/usr/include/fwupd-1/libfwupdplugin/fu-ifd-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-ifd-image.h
/usr/include/fwupd-1/libfwupdplugin/fu-ihex-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-io-channel.h
/usr/include/fwupd-1/libfwupdplugin/fu-plugin-vfuncs.h
/usr/include/fwupd-1/libfwupdplugin/fu-plugin.h
/usr/include/fwupd-1/libfwupdplugin/fu-progress.h
/usr/include/fwupd-1/libfwupdplugin/fu-quirks.h
/usr/include/fwupd-1/libfwupdplugin/fu-security-attrs.h
/usr/include/fwupd-1/libfwupdplugin/fu-smbios.h
/usr/include/fwupd-1/libfwupdplugin/fu-srec-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-udev-device.h
/usr/include/fwupd-1/libfwupdplugin/fu-usb-device.h
/usr/include/fwupd-1/libfwupdplugin/fu-uswid-firmware.h
/usr/include/fwupd-1/libfwupdplugin/fu-volume.h
/usr/lib64/libfwupd.so
/usr/lib64/libfwupdplugin.so
/usr/lib64/pkgconfig/fwupd.pc
/usr/lib64/pkgconfig/fwupdplugin.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/fwupd/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/fwupd-plugins-6/libfu_plugin_acpi_dmar.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_acpi_facp.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_acpi_ivrs.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_acpi_phat.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_amt.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_analogix.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_ata.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_bcm57xx.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_bios.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_ccgx.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_cfu.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_ch341a.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_colorhug.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_corsair.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_cpu.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_cros_ec.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_dell.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_dell_dock.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_dell_esrt.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_dfu.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_dfu_csr.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_ebitdo.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_elanfp.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_elantp.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_emmc.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_ep963x.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_fastboot.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_fresco_pd.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_genesys.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_goodixmoc.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_gpio.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_hailuck.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_iommu.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_jabra.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_lenovo_thinklmi.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_linux_lockdown.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_linux_sleep.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_linux_swap.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_linux_tainted.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_logind.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_logitech_bulkcontroller.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_logitech_hidpp.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_modem_manager.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_msr.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_mtd.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_nitrokey.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_nordic_hid.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_nvme.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_optionrom.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_parade_lspcon.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_pci_bcr.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_pci_mei.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_pci_psp.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_pixart_rf.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_powerd.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_realtek_mst.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_redfish.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_rts54hid.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_rts54hub.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_scsi.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_steelseries.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_superio.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_synaptics_cape.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_synaptics_cxaudio.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_synaptics_mst.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_synaptics_prometheus.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_synaptics_rmi.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_system76_launch.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_thelio_io.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_thunderbolt.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_uefi_capsule.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_uefi_dbx.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_uefi_pk.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_uefi_recovery.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_uf2.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_upower.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_usi_dock.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_vli.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_wacom_raw.so
/usr/lib64/fwupd-plugins-6/libfu_plugin_wacom_usb.so
/usr/lib64/libfwupd.so.2
/usr/lib64/libfwupd.so.2.0.0
/usr/lib64/libfwupdplugin.so.6
/usr/lib64/libfwupdplugin.so.6.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/fwupd/fwupd
/usr/libexec/fwupd/fwupd-detect-cet
/usr/libexec/fwupd/fwupdoffline

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fwupd/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/fwupd/c10b5d1532bdbc2ceae3a33e7ecc8ecbb7f7d260

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dbxtool.1
/usr/share/man/man1/dfu-tool.1
/usr/share/man/man1/fwupdagent.1
/usr/share/man/man1/fwupdate.1
/usr/share/man/man1/fwupdmgr.1
/usr/share/man/man1/fwupdtool.1

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/fwupd.service
/usr/lib/systemd/system/fwupd-offline-update.service
/usr/lib/systemd/system/fwupd-refresh.service
/usr/lib/systemd/system/fwupd-refresh.timer
/usr/lib/systemd/system/fwupd.service

%files tests
%defattr(-,root,root,-)
/usr/libexec/installed-tests/fwupd/acpi-dmar-self-test
/usr/libexec/installed-tests/fwupd/acpi-facp-self-test
/usr/libexec/installed-tests/fwupd/acpi-ivrs-self-test
/usr/libexec/installed-tests/fwupd/acpi-phat-self-test
/usr/libexec/installed-tests/fwupd/ata-self-test
/usr/libexec/installed-tests/fwupd/bcm57xx-self-test
/usr/libexec/installed-tests/fwupd/ccgx-self-test
/usr/libexec/installed-tests/fwupd/elantp-self-test
/usr/libexec/installed-tests/fwupd/fu-dfu-self-test
/usr/libexec/installed-tests/fwupd/fwupd.sh
/usr/libexec/installed-tests/fwupd/linux-swap-self-test
/usr/libexec/installed-tests/fwupd/mtd-self-test
/usr/libexec/installed-tests/fwupd/nitrokey-self-test
/usr/libexec/installed-tests/fwupd/nvme-self-test
/usr/libexec/installed-tests/fwupd/pxi-self-test
/usr/libexec/installed-tests/fwupd/redfish-self-test
/usr/libexec/installed-tests/fwupd/synaptics-mst-self-test
/usr/libexec/installed-tests/fwupd/synaptics-prometheus-self-test
/usr/libexec/installed-tests/fwupd/synaptics-rmi-self-test
/usr/libexec/installed-tests/fwupd/uefi-dbx-self-test
/usr/libexec/installed-tests/fwupd/uf2-self-test
/usr/libexec/installed-tests/fwupd/vli-self-test
/usr/libexec/installed-tests/fwupd/wacom-usb-self-test
/usr/share/installed-tests/fwupd/efi/efivars/CapsuleMax-39b68c46-f7fb-441b-b6ec-16b0f69821f3
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/capsule_flags
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/fw_class
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/fw_type
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/fw_version
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/last_attempt_status
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/last_attempt_version
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/lowest_supported_fw_version
/usr/share/installed-tests/fwupd/fakedevice123.cab
/usr/share/installed-tests/fwupd/fakedevice124.cab
/usr/share/installed-tests/fwupd/fwupd-tests.xml
/usr/share/installed-tests/fwupd/fwupd.test
/usr/share/installed-tests/fwupd/fwupdmgr-p2p.sh
/usr/share/installed-tests/fwupd/fwupdmgr-p2p.test
/usr/share/installed-tests/fwupd/fwupdmgr.sh
/usr/share/installed-tests/fwupd/fwupdmgr.test
/usr/share/installed-tests/fwupd/tests/bcm57xx.builder.xml
/usr/share/installed-tests/fwupd/tests/ccgx-dmc.builder.xml
/usr/share/installed-tests/fwupd/tests/ccgx.builder.xml
/usr/share/installed-tests/fwupd/tests/efi/efivars/RedfishIndications-16faa37e-4b6a-4891-9028-242de65a3b70
/usr/share/installed-tests/fwupd/tests/efi/efivars/RedfishOSCredentials-16faa37e-4b6a-4891-9028-242de65a3b70
/usr/share/installed-tests/fwupd/tests/elantp.builder.xml
/usr/share/installed-tests/fwupd/tests/pixart.builder.xml
/usr/share/installed-tests/fwupd/tests/redfish-smbios.bin
/usr/share/installed-tests/fwupd/tests/redfish.conf
/usr/share/installed-tests/fwupd/tests/synaptics-mst.builder.xml
/usr/share/installed-tests/fwupd/tests/synaptics-prometheus.builder.xml
/usr/share/installed-tests/fwupd/tests/synaptics-rmi-0x.builder.xml
/usr/share/installed-tests/fwupd/tests/synaptics-rmi-10.builder.xml
/usr/share/installed-tests/fwupd/tests/uf2.builder.xml
/usr/share/installed-tests/fwupd/tests/wacom-usb.builder.xml

%files locales -f fwupd.lang
%defattr(-,root,root,-)

