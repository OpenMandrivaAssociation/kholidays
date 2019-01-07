%define major 5
%define libname %mklibname KF5Holidays %{major}
%define devname %mklibname KF5Holidays -d

Name: kholidays
Version:	5.54.0
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Release:	1
Epoch:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: KDE library for holiday handling
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)

%description
KDE library for holiday handling.

%package -n %{libname}
Summary: KDE library for holiday handling
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for holiday handling.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches

%build
%cmake_kde5
cd ../
%ninja -C build

%install
TOPDIR="$(pwd)"
%ninja_install -C build

cd %{buildroot}
find .%{_datadir}/locale -name "*.qm" |while read r; do
	echo "%lang($(echo $r |cut -d/ -f5)) $(echo $r |cut -b2-)" >>${TOPDIR}/%{name}.lang
done

%files -f %{name}.lang

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/qt5/qml/org/kde/kholidays

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
