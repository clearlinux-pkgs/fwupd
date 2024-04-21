#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v10
# autospec commit: 5905be9
#
Name     : fwupd
Version  : 1.9.16
Release  : 80
URL      : https://github.com/hughsie/fwupd/archive/1.9.16/fwupd-1.9.16.tar.gz
Source0  : https://github.com/hughsie/fwupd/archive/1.9.16/fwupd-1.9.16.tar.gz
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
BuildRequires : gi-docgen
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
BuildRequires : pkgconfig(fwupd-efi)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(gusb)
BuildRequires : pkgconfig(jcat)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libdrm_amdgpu)
BuildRequires : pkgconfig(libelf)
BuildRequires : pkgconfig(libprotobuf-c)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(mbim-glib)
BuildRequires : pkgconfig(mm-glib)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(qmi-glib)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(xmlb)
BuildRequires : popt-dev
BuildRequires : pycairo
BuildRequires : pygobject
BuildRequires : pygobject-dev
BuildRequires : pygobject-extras
BuildRequires : pypi(pillow)
BuildRequires : python3-dev
BuildRequires : python3-xz-lzma
BuildRequires : vala
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
Requires: systemd

%description services
services components for the fwupd package.


%package tests
Summary: tests components for the fwupd package.
Group: Default
Requires: fwupd = %{version}-%{release}

%description tests
tests components for the fwupd package.


%prep
%setup -q -n fwupd-1.9.16
cd %{_builddir}/fwupd-1.9.16
%patch -P 1 -p1
pushd ..
cp -a fwupd-1.9.16 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713663103
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddocs=none \
-Dplugin_tpm=false \
-Dlzma=disabled  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddocs=none \
-Dplugin_tpm=false \
-Dlzma=disabled  builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/fwupd
cp %{_builddir}/fwupd-%{version}/COPYING %{buildroot}/usr/share/package-licenses/fwupd/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/fwupd-%{version}/plugins/thunderbolt/tests/COPYING %{buildroot}/usr/share/package-licenses/fwupd/c10b5d1532bdbc2ceae3a33e7ecc8ecbb7f7d260 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system-shutdown/fwupd.shutdown

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/fwupd.service

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/dbxtool
/V3/usr/bin/fwupdmgr
/V3/usr/bin/fwupdtool
/usr/bin/dbxtool
/usr/bin/fwupdmgr
/usr/bin/fwupdtool

%files config
%defattr(-,root,root,-)
/usr/lib/modules-load.d/fwupd-msr.conf
/usr/lib/sysusers.d/fwupd.conf
/usr/lib/tmpfiles.d/fwupd.conf
/usr/lib/udev/rules.d/90-fwupd-devices.rules

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Fwupd-2.0.typelib
/usr/share/bash-completion/completions/fwupdmgr
/usr/share/bash-completion/completions/fwupdtool
/usr/share/dbus-1/interfaces/org.freedesktop.fwupd.xml
/usr/share/dbus-1/system-services/org.freedesktop.fwupd.service
/usr/share/dbus-1/system.d/org.freedesktop.fwupd.conf
/usr/share/defaults/fwupd/bios-settings.d/README.md
/usr/share/defaults/fwupd/fwupd.conf
/usr/share/defaults/fwupd/remotes.d/lvfs-testing.conf
/usr/share/defaults/fwupd/remotes.d/lvfs.conf
/usr/share/defaults/fwupd/remotes.d/vendor-directory.conf
/usr/share/fish/vendor_completions.d/fwupdmgr.fish
/usr/share/fwupd/add_capsule_header.py
/usr/share/fwupd/device-tests/8bitdo-nes30pro.json
/usr/share/fwupd/device-tests/8bitdo-sf30pro.json
/usr/share/fwupd/device-tests/8bitdo-sfc30.json
/usr/share/fwupd/device-tests/aiaiai-h05.json
/usr/share/fwupd/device-tests/bizlink-no-sku-vli.json
/usr/share/fwupd/device-tests/corsair-katar-pro-xt.json
/usr/share/fwupd/device-tests/corsair-sabre-pro.json
/usr/share/fwupd/device-tests/corsair-sabre-rgb-pro.json
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
/usr/share/fwupd/device-tests/ugreen-cm260.json
/usr/share/fwupd/device-tests/wacom-intuos-bt-m.json
/usr/share/fwupd/device-tests/wacom-intuos-bt-s.json
/usr/share/fwupd/firmware_packager.py
/usr/share/fwupd/host-emulate.d/thinkpad-p1-iommu.json.gz
/usr/share/fwupd/install_dell_bios_exe.py
/usr/share/fwupd/metainfo/org.freedesktop.fwupd.remotes.lvfs-testing.metainfo.xml
/usr/share/fwupd/metainfo/org.freedesktop.fwupd.remotes.lvfs.metainfo.xml
/usr/share/fwupd/pki/fwupd-metadata/GPG-KEY-Linux-Foundation-Metadata
/usr/share/fwupd/pki/fwupd-metadata/GPG-KEY-Linux-Vendor-Firmware-Service
/usr/share/fwupd/pki/fwupd-metadata/LVFS-CA.pem
/usr/share/fwupd/pki/fwupd/GPG-KEY-Linux-Foundation-Firmware
/usr/share/fwupd/pki/fwupd/GPG-KEY-Linux-Vendor-Firmware-Service
/usr/share/fwupd/pki/fwupd/LVFS-CA.pem
/usr/share/fwupd/quirks.d/builtin.quirk.gz
/usr/share/fwupd/remotes.d/fwupd-tests.conf
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
/usr/include/fwupd-1/libfwupd/fwupd-bios-setting.h
/usr/include/fwupd-1/libfwupd/fwupd-build.h
/usr/include/fwupd-1/libfwupd/fwupd-client-sync.h
/usr/include/fwupd-1/libfwupd/fwupd-client.h
/usr/include/fwupd-1/libfwupd/fwupd-common.h
/usr/include/fwupd-1/libfwupd/fwupd-device.h
/usr/include/fwupd-1/libfwupd/fwupd-enums.h
/usr/include/fwupd-1/libfwupd/fwupd-error.h
/usr/include/fwupd-1/libfwupd/fwupd-plugin.h
/usr/include/fwupd-1/libfwupd/fwupd-release.h
/usr/include/fwupd-1/libfwupd/fwupd-remote.h
/usr/include/fwupd-1/libfwupd/fwupd-report.h
/usr/include/fwupd-1/libfwupd/fwupd-request.h
/usr/include/fwupd-1/libfwupd/fwupd-security-attr.h
/usr/include/fwupd-1/libfwupd/fwupd-version.h
/usr/lib64/libfwupd.so
/usr/lib64/pkgconfig/fwupd.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/fwupd-1.9.16/libfu_plugin_modem_manager.so
/V3/usr/lib64/fwupd-1.9.16/libfwupdengine.so
/V3/usr/lib64/fwupd-1.9.16/libfwupdplugin.so
/V3/usr/lib64/fwupd-1.9.16/libfwupdutil.so
/V3/usr/lib64/libfwupd.so.2.0.0
/usr/lib64/fwupd-1.9.16/libfu_plugin_modem_manager.so
/usr/lib64/fwupd-1.9.16/libfwupdengine.so
/usr/lib64/fwupd-1.9.16/libfwupdplugin.so
/usr/lib64/fwupd-1.9.16/libfwupdutil.so
/usr/lib64/libfwupd.so.2
/usr/lib64/libfwupd.so.2.0.0

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/fwupd/fwupd
/V3/usr/libexec/fwupd/fwupd-detect-cet
/V3/usr/libexec/fwupd/fwupdoffline
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
/usr/share/man/man1/fwupdmgr.1
/usr/share/man/man1/fwupdtool.1
/usr/share/man/man5/fwupd-remotes.d.5
/usr/share/man/man5/fwupd.conf.5
/usr/share/man/man8/fwupd-refresh.service.8

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/fwupd.service
/usr/lib/systemd/system/fwupd-offline-update.service
/usr/lib/systemd/system/fwupd-refresh.service
/usr/lib/systemd/system/fwupd-refresh.timer
/usr/lib/systemd/system/fwupd.service

%files tests
%defattr(-,root,root,-)
/V3/usr/libexec/installed-tests/fwupd/acpi-dmar-self-test
/V3/usr/libexec/installed-tests/fwupd/acpi-facp-self-test
/V3/usr/libexec/installed-tests/fwupd/acpi-ivrs-self-test
/V3/usr/libexec/installed-tests/fwupd/acpi-phat-self-test
/V3/usr/libexec/installed-tests/fwupd/ata-self-test
/V3/usr/libexec/installed-tests/fwupd/bcm57xx-self-test
/V3/usr/libexec/installed-tests/fwupd/ccgx-dmc-self-test
/V3/usr/libexec/installed-tests/fwupd/ccgx-self-test
/V3/usr/libexec/installed-tests/fwupd/elantp-self-test
/V3/usr/libexec/installed-tests/fwupd/fu-dfu-self-test
/V3/usr/libexec/installed-tests/fwupd/linux-swap-self-test
/V3/usr/libexec/installed-tests/fwupd/mtd-self-test
/V3/usr/libexec/installed-tests/fwupd/nitrokey-self-test
/V3/usr/libexec/installed-tests/fwupd/nvme-self-test
/V3/usr/libexec/installed-tests/fwupd/pxi-self-test
/V3/usr/libexec/installed-tests/fwupd/redfish-self-test
/V3/usr/libexec/installed-tests/fwupd/synaptics-mst-self-test
/V3/usr/libexec/installed-tests/fwupd/synaptics-prometheus-self-test
/V3/usr/libexec/installed-tests/fwupd/synaptics-rmi-self-test
/V3/usr/libexec/installed-tests/fwupd/uefi-dbx-self-test
/V3/usr/libexec/installed-tests/fwupd/uf2-self-test
/V3/usr/libexec/installed-tests/fwupd/vli-self-test
/V3/usr/libexec/installed-tests/fwupd/wacom-usb-self-test
/usr/libexec/installed-tests/fwupd/acpi-dmar-self-test
/usr/libexec/installed-tests/fwupd/acpi-facp-self-test
/usr/libexec/installed-tests/fwupd/acpi-ivrs-self-test
/usr/libexec/installed-tests/fwupd/acpi-phat-self-test
/usr/libexec/installed-tests/fwupd/ata-self-test
/usr/libexec/installed-tests/fwupd/bcm57xx-self-test
/usr/libexec/installed-tests/fwupd/ccgx-dmc-self-test
/usr/libexec/installed-tests/fwupd/ccgx-self-test
/usr/libexec/installed-tests/fwupd/elantp-self-test
/usr/libexec/installed-tests/fwupd/fu-dfu-self-test
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
/usr/share/installed-tests/fwupd/chassis_type
/usr/share/installed-tests/fwupd/efi/efivars/CapsuleMax-39b68c46-f7fb-441b-b6ec-16b0f69821f3
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/capsule_flags
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/fw_class
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/fw_type
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/fw_version
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/last_attempt_status
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/last_attempt_version
/usr/share/installed-tests/fwupd/efi/esrt/entries/entry0/lowest_supported_fw_version
/usr/share/installed-tests/fwupd/fakedevice123.cab
/usr/share/installed-tests/fwupd/fakedevice124.bin
/usr/share/installed-tests/fwupd/fakedevice124.cab
/usr/share/installed-tests/fwupd/fakedevice124.jcat
/usr/share/installed-tests/fwupd/fakedevice124.metainfo.xml
/usr/share/installed-tests/fwupd/firmware.zip
/usr/share/installed-tests/fwupd/fwupd-tests.xml
/usr/share/installed-tests/fwupd/fwupd.sh
/usr/share/installed-tests/fwupd/fwupd.test
/usr/share/installed-tests/fwupd/fwupdmgr-p2p.sh
/usr/share/installed-tests/fwupd/fwupdmgr-p2p.test
/usr/share/installed-tests/fwupd/fwupdmgr.sh
/usr/share/installed-tests/fwupd/fwupdmgr.test
/usr/share/installed-tests/fwupd/fwupdtool.sh
/usr/share/installed-tests/fwupd/fwupdtool.test
/usr/share/installed-tests/fwupd/sys_vendor
/usr/share/installed-tests/fwupd/tests/bcm57xx.builder.xml
/usr/share/installed-tests/fwupd/tests/ccgx-dmc.builder.xml
/usr/share/installed-tests/fwupd/tests/ccgx.builder.xml
/usr/share/installed-tests/fwupd/tests/dmi/tables/DMI
/usr/share/installed-tests/fwupd/tests/dmi/tables/smbios_entry_point
/usr/share/installed-tests/fwupd/tests/dmi/tables64/DMI
/usr/share/installed-tests/fwupd/tests/dmi/tables64/smbios_entry_point
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

