Summary:	Many metawidgets (such as notepads) for tk
Summary(de):	Zahlreiche Metawidgets (wie etwa Notepads) f�r tk 
Summary(fr):	Nombreux meta-widgets (comme les bloc-notes) pour tk
Summary(pl):	Wiele widget�w (takich jak notepad) dla tk
Summary(tr):	Tk i�in ek aray�z elemanlar� (not defterleri v.b.)
Name:		tix
Version:	4.1.0.007
Release:	3
Serial:		1
Source:		ftp://ftp.xpi.com/pub/ioi/Tix%{version}.tar.gz
Copyright:	BSD
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Patch0:		tix-scriptpaths.patch
Patch1:		tix-fhs.patch
Patch2:		tix-autoconf.patch
BuildRequires:	XFree86-devel
BuildRequires:	tcl-devel >= 8.0.5-31
BuildRequires:	tk-devel >= 8.0.5-31
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
Tix is a add on for the tk widget set which adds many complex widgets which
are built from tk building blocks. The extra widgets include combo box,
file selection, notebooks, paned windows, spin controls, and hierarchical
list boxes.

%description -l de 
Tix ist ein Zusatzprogramm f�r den 'tk widget set', das viele komplexe Widgets
hinzuf�gt, die aus tk-Bausteinen bestehen, z.B. Kombinationsfelder,
Dateiauswahl, Notizbl�cke, �berlappende Fenster, Drehkn�pfe und
hierarchische Listenfelder.

%description -l fr 
tix est un ajout � l'ensemble des widgets Tk qui apporte de nombreux widgets
complexes construits � partir des briques de tk. Les widgets suppl�mentaires
incluent les combo box, la s�lection de fichiers, les notebooks, les fen�tres
� paned � et les listes hi�rarchis�es.

%description -l pl
Tix jest dodatkiem dla tk, zawieraj�cym wiele interesuj�cych widget�w.

%description -l tr 
Tix, tk yap�ta�lar� kullan�larak olu�turulmu� bir �ok karma��k aray�z eleman�
bulunduran bir eklemedir. Bu yeni elemanlar aras�nda �oktan se�meli kutular,
dosya se�im kutular�, not defterleri, �ok k�s�ml� pencereler yer almaktad�r.

%package devel
Summary:	Tix header files and development documentation
Summary(pl):	Pliki nag��wkowe oraz dokumentacja do Tix
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Requires:	%{name} = %{version}

%description devel
Tix header files and development documentation

%description -l pl devel
Pliki nag��wkowe oraz dokumentacja do Tix.

%package demo
Summary:	Tix - demo programs
Summary(pl):	Tix - programy demostracjne
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Requires:	%{name} = %{version}

%description demo
Tix - demo programs.

%description demo -l pl
Tix - programy demostracjne.

%prep
%setup  -q -n Tix%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd unix
aclocal; autoconf
%configure \
	--disable-cdemos \
	--enable-shared

cd tk8.0
aclocal; autoconf
%configure \
	--disable-cdemos \
	--enable-shared

make CFLAGS="$RPM_OPT_FLAGS -D_REENTRANT -w"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},/usr/src/examples/%{name}}

(cd unix 
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} \
make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	LIB_DIR=$RPM_BUILD_ROOT%{_libdir} \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir}

mv $RPM_BUILD_ROOT%{_mandir}/mann/tixwish.1 \
	$RPM_BUILD_ROOT%{_mandir}/man1

(cd tk8.0
make install prefix=$RPM_BUILD_ROOT%{_prefix} \
	LIB_DIR=$RPM_BUILD_ROOT%{_libdir} \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} ) )

mv	$RPM_BUILD_ROOT%{_bindir}/tixwish4.1.8.0 \
	$RPM_BUILD_ROOT%{_bindir}/tixwish

strip $RPM_BUILD_ROOT%{_bindir}/tixwish
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so

mv $RPM_BUILD_ROOT%{_libdir}/tix4.1/demos $RPM_BUILD_ROOT/usr/src/examples/%{name}

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[1n]/* \
	docs/{*.txt,pguide-tix4.0.ps}

%post   -p /sbin/ldconfig 
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755) 
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so

%dir %{_libdir}/tix4.1
%{_libdir}/tix4.1/*.tcl
%{_libdir}/tix4.1/tclIndex

%{_libdir}/tix4.1/bitmaps
%{_libdir}/tix4.1/pref
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc docs/*.gz
%{_includedir}/*.h
%{_mandir}/mann/*

%files demo
%defattr(644,root,root,755)
%dir /usr/src/examples/%{name}
%attr(-,root,root) /usr/src/examples/%{name}/*
