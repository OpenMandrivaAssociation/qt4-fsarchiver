Name:		qt4-fsarchiver
Version:	0.6.17
Release:	2

Summary:	Safe and flexible file-system backup/deployment tool
Group:		Archiving/Backup
License:	GPLv2
URL:		http://www.fsarchiver.org
Source0:  	http://downloads.sourceforge.net/%{name}/%{name}-%{version}-4.tar.gz
Requires:	fsarchiver

BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(blkid)
BuildRequires:	e2fsprogs
BuildRequires:	attr-devel
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	bzip2-devel
BuildRequires:	liblzo-devel
BuildRequires:	pkgconfig(liblzma)

%description
FSArchiver is a system tool that allows you to save the contents of a 
file-system to a compressed archive file. The file-system can be restored 
on a partition which has a different size and it can be restored on a 
different file-system. Unlike tar/dar, FSArchiver also creates the 
file-system when it extracts the data to partitions. Everything is 
checksummed in the archive in order to protect the data. If the archive 
is corrupt, you just loose the current file, not the whole archive.

%prep
%setup -qn %{name}

%build
%qmake_qt4 
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

#clean doc directory from backup files
rm -rf %{buildroot}/usr/share/doc/qt4-fsarchiver/doc/*~

mkdir -p %{buildroot}/%{_iconsdir}
mv %{buildroot}%{_datadir}/app-install/icons/harddrive.png  %{buildroot}/%{_iconsdir}/

#we use our desktop file, because we don't use sudo
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Qt4-Fsarchiver
Comment=%{summary}
Exec=gksu /usr/sbin/qt4-fsarchiver
Icon=%{_iconsdir}/harddrive.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Archiving;X-MandrakeLinux-System-Archiving;
EOF

install -m 0644 -p translations/*.ts ${RPM_BUILD_ROOT}%{_datadir}/qt4/translations/
qmake

%files
%{_sbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/harddrive.png
%{_docdir}/%{name}/doc/*
%{_datadir}/qt4/translations/%{name}*.qm
%{_datadir}/qt4/translations/%{name}*.ts
