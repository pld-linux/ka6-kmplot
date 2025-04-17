#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.04.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kmplot
Summary:	kmplot
Name:		ka6-%{kaname}
Version:	25.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	70123bf22a72a9cb1102fc0413779cde
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-kguiaddons-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kparts-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KmPlot is a program to draw graphs, their integrals or derivatives. It
supports different systems of coordinates like the Cartesian or the
polar coordinate system. The graphs can be colorized and the view is
scalable, so that you are able to zoom to the level you need.

%description -l pl.UTF-8
KmPlot jest programem rysującym wykresy funkcji, całek i pochodnych.
Obsługuje różne układy współrzędnych, np. Kartezjański czy biegunowy.
Wykresy są kolorowane i skalowalne, tak że jesteś w stanie powiększyć
je do poziomu, którego potrzebujesz.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmplot
%{_libdir}/qt6/plugins/kf6/parts/kmplotpart.so
%{_desktopdir}/org.kde.kmplot.desktop
%{_datadir}/config.kcfg/kmplot.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.KmPlot.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.MainDlg.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.Parser.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.View.xml
%{_iconsdir}/hicolor/*x*/apps/kmplot.png
%{_iconsdir}/hicolor/scalable/apps/kmplot.svgz
%{_datadir}/metainfo/org.kde.kmplot.appdata.xml
%lang(ca) %{_mandir}/ca/man1/kmplot.1*
%lang(de) %{_mandir}/de/man1/kmplot.1*
%lang(es) %{_mandir}/es/man1/kmplot.1*
%lang(et) %{_mandir}/et/man1/kmplot.1*
%lang(fr) %{_mandir}/fr/man1/kmplot.1*
%lang(gl) %{_mandir}/gl/man1/kmplot.1*
%lang(it) %{_mandir}/it/man1/kmplot.1*
%lang(C) %{_mandir}/man1/kmplot.1*
%lang(nl) %{_mandir}/nl/man1/kmplot.1*
%lang(pl) %{_mandir}/pl/man1/kmplot.1*
%lang(pt) %{_mandir}/pt/man1/kmplot.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kmplot.1*
%lang(ru) %{_mandir}/ru/man1/kmplot.1*
%lang(sl) %{_mandir}/sl/man1/kmplot.1*
%lang(sv) %{_mandir}/sv/man1/kmplot.1*
%lang(uk) %{_mandir}/uk/man1/kmplot.1*
