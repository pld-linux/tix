%define		major 8.4
Summary:	Many metawidgets (such as notepads) for Tk
Summary(de):	Zahlreiche Metawidgets (wie etwa Notepads) f�r Tk
Summary(fr):	Nombreux meta-widgets (comme les bloc-notes) pour Tk
Summary(pl):	Wiele widget�w (takich jak notepad) dla Tk
Summary(tr):	Tk i�in ek aray�z elemanlar� (not defterleri v.b.)
Name:		tix
Version:	%{major}.0
Release:	1
Epoch:		1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tix/%{name}-%{version}.tar.gz
# Source0-md5:	7fcd84a1a6e27e432cb07284b7a34317
Patch0:		%{name}-scriptpaths.patch
Patch1:		%{name}-tcl85_hack.patch
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
Summary:	Tix development documentation
Summary(pl):	Dokumentacja programisty do rozszerzenia Tix
Group:		Development/Languages/Tcl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Tix development documentation.

%description devel -l pl
Dokumentacja programisty do rozszerzenia Tix.

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

%build
%{__aclocal} -I tclconfig
%{__autoconf}
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/mann
install man/*.n $RPM_BUILD_ROOT%{_mandir}/mann

cp -af demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{_libdir}/Tix%{major}/bitmaps/mktransgif.tcl*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT.html ChangeLog README.txt index.html license.terms docs/FAQ.html
%dir %{_libdir}/Tix%{major}
%attr(755,root,root) %{_libdir}/Tix%{major}/libTix%{major}.so
%{_libdir}/Tix%{major}/*.tcl
%{_libdir}/Tix%{major}/bitmaps
%{_libdir}/Tix%{major}/pref

%files devel
%defattr(644,root,root,755)
%doc docs/*.txt docs/{pdf,tix-book}
%{_mandir}/mann/*

%files demo
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%dir %{_examplesdir}/%{name}-%{version}/demos
%{_examplesdir}/%{name}-%{version}/demos/Mk*.tcl
%{_examplesdir}/%{name}-%{version}/demos/bitmaps
%{_examplesdir}/%{name}-%{version}/demos/samples
%{_examplesdir}/%{name}-%{version}/demos/tclIndex
%{_examplesdir}/%{name}-%{version}/demos/widget
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/demos/tixwidgets.tcl
