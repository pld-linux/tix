Summary:	Many metawidgets (such as notepads) for tk
Summary(de):	Zahlreiche Metawidgets (wie etwa Notepads) f�r tk
Summary(fr):	Nombreux meta-widgets (comme les bloc-notes) pour tk
Summary(pl):	Wiele widget�w (takich jak notepad) dla tk
Summary(tr):	Tk i�in ek aray�z elemanlar� (not defterleri v.b.)
Name:		tix
Version:	8.1.4
Release:	1
Epoch:		1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tix/%{name}-%{version}.tar.gz
Patch0:		%{name}-scriptpaths.patch
Patch1:		%{name}-fhs.patch
Patch2:		%{name}-autoconf.patch
URL:		http://tix.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl-devel >= 8.3.2
BuildRequires:	tk-devel >= 8.3.2
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tix is a add on for the tk widget set which adds many complex widgets
which are built from tk building blocks. The extra widgets include
combo box, file selection, notebooks, paned windows, spin controls,
and hierarchical list boxes.

%description -l de
Tix ist ein Zusatzprogramm f�r den 'tk widget set', das viele komplexe
Widgets hinzuf�gt, die aus tk-Bausteinen bestehen, z.B.
Kombinationsfelder, Dateiauswahl, Notizbl�cke, �berlappende Fenster,
Drehkn�pfe und hierarchische Listenfelder.

%description -l fr
tix est un ajout � l'ensemble des widgets Tk qui apporte de nombreux
widgets complexes construits � partir des briques de tk. Les widgets
suppl�mentaires incluent les combo box, la s�lection de fichiers, les
notebooks, les fen�tres � paned � et les listes hi�rarchis�es.

%description -l pl
Tix jest dodatkiem dla tk, zawieraj�cym wiele interesuj�cych widget�w.

%description -l tr
Tix, tk yap�ta�lar� kullan�larak olu�turulmu� bir �ok karma��k aray�z
eleman� bulunduran bir eklemedir. Bu yeni elemanlar aras�nda �oktan
se�meli kutular, dosya se�im kutular�, not defterleri, �ok k�s�ml�
pencereler yer almaktad�r.

%package devel
Summary:	Tix header files and development documentation
Summary(pl):	Pliki nag��wkowe oraz dokumentacja do Tix
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}

%description devel
Tix header files and development documentation

%description devel -l pl
Pliki nag��wkowe oraz dokumentacja do Tix.

%package demo
Summary:	Tix - demo programs
Summary(pl):	Tix - programy demostracjne
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}

%description demo
Tix - demo programs.

%description demo -l pl
Tix - programy demostracjne.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd unix
%{__aclocal}
%{__autoconf}
%configure \
	--disable-cdemos \
	--enable-shared

cd tk8.3
%{__aclocal}
%{__autoconf}
%configure \
	--disable-cdemos \
	--enable-shared

%{__make} CFLAGS="%{rpmcflags} -D_REENTRANT -w"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_prefix}/src/examples/%{name}}

cd unix
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} \
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	LIB_DIR=$RPM_BUILD_ROOT%{_libdir} \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	TIX_LIBRARY=$RPM_BUILD_ROOT%{_datadir}/tix8.1

mv -f $RPM_BUILD_ROOT%{_mandir}/mann/tixwish.1 \
	$RPM_BUILD_ROOT%{_mandir}/man1

cd tk8.3
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} \
	LIB_DIR=$RPM_BUILD_ROOT%{_libdir} \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir}
cd ../..

#mv -f	$RPM_BUILD_ROOT%{_bindir}/tixwish4.1.8.0 \
#	$RPM_BUILD_ROOT%{_bindir}/tixwish

mv -f $RPM_BUILD_ROOT%{_datadir}/tix8.1/demos \
	$RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}
mv -f $RPM_BUILD_ROOT%{_bindir}/tixwish8.1.8.3 \
	$RPM_BUILD_ROOT%{_bindir}/tixwish

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so

%dir %{_datadir}/tix8.1
%{_datadir}/tix8.1/*.tcl
%{_datadir}/tix8.1/tclIndex

%{_datadir}/tix8.1/bitmaps
%{_datadir}/tix8.1/pref
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc docs/*.txt docs/{pdf,tix-book}
%attr(755,root,root) %{_libdir}/tixConfig.sh
%{_includedir}/*.h
%{_mandir}/man[3n]/*

%files demo
%defattr(644,root,root,755)
%dir %{_prefix}/src/examples/%{name}
%attr(-,root,root) %{_prefix}/src/examples/%{name}/*
