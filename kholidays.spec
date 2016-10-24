%define major 5
%define libname %mklibname KF5Holidays %{major}
%define devname %mklibname KF5Holidays -d

Name: kholidays
Version:	16.08.2
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for holiday handling
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)

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
%ninja_install -C build

%files
%{_datadir}/kf5/libkholidays

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/qt5/qml/org/kde/kholidays

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri