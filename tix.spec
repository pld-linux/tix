%define		major 8.1
%define		tkmajor 8.4
Summary:	Many metawidgets (such as notepads) for Tk
Summary(de):	Zahlreiche Metawidgets (wie etwa Notepads) f�r Tk
Summary(fr):	Nombreux meta-widgets (comme les bloc-notes) pour Tk
Summary(pl):	Wiele widget�w (takich jak notepad) dla Tk
Summary(tr):	Tk i�in ek aray�z elemanlar� (not defterleri v.b.)
Name:		tix
Version:	%{major}.4
Release:	8
Epoch:		1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tix/%{name}-%{version}.tar.gz
# Source0-md5:	128a74718d6d9e10fac40cdf11c661a3
Patch0:		%{name}-scriptpaths.patch
Patch1:		%{name}-fhs.patch
Patch2:		%{name}-autoconf.patch
Patch3:		%{name}-soname.patch
URL:		http://tix.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl-devel >= 8.4.6
BuildRequires:	tk-devel >= 8.4.6
BuildRequires:	which
Requires:	tcl >= 8.4.6
Requires:	tk >= 8.4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tix is a add on for the Tk widget set which adds many complex widgets
which are built from Tk building blocks. The extra widgets include
combo box, file selection, notebooks, paned windows, spin controls,
and hierarchical list boxes.

%description -l de
Tix ist ein Zusatzprogramm f�r den 'Tk widget set', das viele komplexe
Widgets hinzuf�gt, die aus Tk-Bausteinen bestehen, z.B.
Kombinationsfelder, Dateiauswahl, Notizbl�cke, �berlappende Fenster,
Drehkn�pfe und hierarchische Listenfelder.

%description -l fr
tix est un ajout � l'ensemble des widgets Tk qui apporte de nombreux
widgets complexes construits � partir des briques de Tk. Les widgets
suppl�mentaires incluent les combo box, la s�lection de fichiers, les
notebooks, les fen�tres � paned � et les listes hi�rarchis�es.

%description -l pl
Tix jest dodatkiem dla Tk, zawieraj�cym wiele interesuj�cych widget�w.

%description -l tr
Tix, Tk yap�ta�lar� kullan�larak olu�turulmu� bir �ok karma��k aray�z
eleman� bulunduran bir eklemedir. Bu yeni elemanlar aras�nda �oktan
se�meli kutular, dosya se�im kutular�, not defterleri, �ok k�s�ml�
pencereler yer almaktad�r.

%package devel
Summary:	Tix header files and development documentation
Summary(pl):	Pliki nag��wkowe oraz dokumentacja do Tix
Group:		Development/Languages/Tcl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Tix header files and development documentation

%description devel -l pl
Pliki nag��wkowe oraz dokumentacja do Tix.

%package demo
Summary:	Tix - demo programs
Summary(pl):	Tix - programy demostracjne
Group:		Development/Languages/Tcl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demo
Tix - demo programs.

%description demo -l pl
Tix - programy demostracjne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cd unix
%{__aclocal} -I ../config
%{__autoconf}
%configure \
	--disable-cdemos \
	--enable-shared

cd tk%{tkmajor}
%{__aclocal} -I ../../config
%{__autoconf}
%configure \
	--disable-cdemos \
	--enable-sam \
	--enable-shared

%{__make} \
	CFLAGS="%{rpmcflags} -D_REENTRANT -w"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_examplesdir}/%{name}-%{version}}

cd unix
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} \
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	LIB_DIR=$RPM_BUILD_ROOT%{_libdir} \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	TIX_LIBRARY=$RPM_BUILD_ROOT%{_datadir}/tix%{major}

mv -f $RPM_BUILD_ROOT%{_mandir}/mann/tixwish.1 \
	$RPM_BUILD_ROOT%{_mandir}/man1

mv -f $RPM_BUILD_ROOT%{_datadir}/tix%{major}/demos \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv -f $RPM_BUILD_ROOT%{_bindir}/tixwish%{major}.%{tkmajor} \
	$RPM_BUILD_ROOT%{_bindir}/tixwish

ln -sf `cd $RPM_BUILD_ROOT%{_libdir}; echo libtix%{major}*.so.*.*` \
	$RPM_BUILD_ROOT%{_libdir}/libtix.so
ln -sf `cd $RPM_BUILD_ROOT%{_libdir}; echo libtixsam%{major}*.so.*.*` \
	$RPM_BUILD_ROOT%{_libdir}/libtixsam.so
ln -sf `cd $RPM_BUILD_ROOT%{_libdir}; echo libtix%{major}*.so.*.*` \
	$RPM_BUILD_ROOT%{_libdir}/libtix%{major}.so
ln -sf `cd $RPM_BUILD_ROOT%{_libdir}; echo libtixsam%{major}*.so.*.*` \
	$RPM_BUILD_ROOT%{_libdir}/libtixsam%{major}.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*

%dir %{_datadir}/tix%{major}
%{_datadir}/tix%{major}/*.tcl
%{_datadir}/tix%{major}/tclIndex

%{_datadir}/tix%{major}/bitmaps
%{_datadir}/tix%{major}/pref
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc docs/*.txt docs/{pdf,tix-book}
%attr(755,root,root) %{_libdir}/tixConfig.sh
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*.h
%{_mandir}/man[3n]/*

%files demo
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%dir %{_examplesdir}/%{name}-%{version}/demos
%{_examplesdir}/%{name}-%{version}/demos/Mk*.tcl
%{_examplesdir}/%{name}-%{version}/demos/README
%{_examplesdir}/%{name}-%{version}/demos/bitmaps
%{_examplesdir}/%{name}-%{version}/demos/samples
%{_examplesdir}/%{name}-%{version}/demos/tclIndex
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/demos/tixwidgets.tcl
