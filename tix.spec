Summary:	many metawidgets (such as notepads) for tk
Summary(de):	zahlreiche Metawidgets (wie etwa Notepads) f�r tk 
Summary(fr):	Nombreux meta-widgets (comme les bloc-notes) pour tk
Summary(pl):	Wiele widget�w (takich jak notepad) dla tk
Summary(tr):	tk i�in ek aray�z elemanlar� (not defterleri v.b.)
Name:		tix
Version:	4.1.0
Release:	3
Source:		ftp://ftp.xpi.com/pub/ioi/Tix4.1.0.006.tar.gz
Copyright:	BSD
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Patch0:		%{name}-scriptpaths.patch
Patch1:		%{name}-fhs.patch
Buildroot:	/tmp/%{name}-%{version}-root

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

%prep

%setup  -q -n Tix%{version}
%patch0 -p1
%patch1 -p1

%build
cd unix
aclocal && autoconf

./configure \
    --disable-cdemos \
    --enable-shared \
    --prefix=%{_prefix} \
    %{_target_platform}

cd tk8.0
./configure \
    --disable-cdemos \
    --enable-shared \
    --with-tcl=../../../tcl8.0.5 \
    --with-tk=../../../tk8.0.5 \
    --prefix=%{_prefix} \
    %{_target_platform}

make CFLAGS="$RPM_OPT_FLAGS -D_REENTRANT -w"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}

cd unix 
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} \

make prefix=$RPM_BUILD_ROOT%{_prefix} install

mv $RPM_BUILD_ROOT%{_mandir}/mann/tixwish.1 \
    $RPM_BUILD_ROOT%{_mandir}/man1/tixwish.1

cd tk8.0

make prefix=$RPM_BUILD_ROOT%{_prefix} install

ln -sf tixwish4.1.8.0 $RPM_BUILD_ROOT%{_bindir}/tixwish

strip $RPM_BUILD_ROOT%{_bindir}/* || :
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[1n]/* ../../{*.txt,*.html}

%post -p /sbin/ldconfig 
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755) 
%doc *.html.gz *.txt.gz

%attr(755,root,root) %{_bindir}/*

%{_includedir}/*.h

%attr(755,root,root) %{_libdir}/*.so

%dir %{_libdir}/tix4.1
%{_libdir}/tix4.1/*.tcl
%{_libdir}/tix4.1/tclIndex

%dir %{_libdir}/tix4.1/bitmaps
%{_libdir}/tix4.1/bitmaps/*

%dir %{_libdir}/tix4.1/demos
%attr(-,root,root) %{_libdir}/tix4.1/demos/*

%dir %{_libdir}/tix4.1/pref
%{_libdir}/tix4.1/pref/*

%{_mandir}/man[1n]/*

%changelog
* Wed Jun 16 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
- major changes -- buil for 1.3 PLD  

* Sun Jan 31 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
- added Group(pl),
  
  by Maciek R�ycki <macro@ds2.amg.gda.pl>

- added small patch.

* Sun Nov 15 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [4.1.0-1d]
- build for Linux PLD,
- major changes.
