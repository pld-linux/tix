%define		major 8.4
Summary:	Many metawidgets (such as notepads) for Tk
Summary(de.UTF-8):	Zahlreiche Metawidgets (wie etwa Notepads) für Tk
Summary(fr.UTF-8):	Nombreux meta-widgets (comme les bloc-notes) pour Tk
Summary(pl.UTF-8):	Wiele widgetów (takich jak notepad) dla Tk
Summary(tr.UTF-8):	Tk için ek arayüz elemanları (not defterleri v.b.)
Name:		tix
Version:	%{major}.3
Release:	2
Epoch:		1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://download.sourceforge.net/tix/Tix%{version}-src.tar.gz
# Source0-md5:	2b8bf4b10a852264678182652f477e59
Patch0:		%{name}-scriptpaths.patch
Patch2:		fixInterpResult.patch
URL:		http://tix.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	groff
BuildRequires:	tcl-devel >= 8.4.6
BuildRequires:	tk-devel >= 8.4.6
BuildRequires:	which
BuildRequires:	xorg-lib-libX11-devel
Requires:	tcl >= 8.4.6
Requires:	tk >= 8.4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		groff_version	%(rpm -q --qf %{V} groff)

%description
Tix is a add on for the Tk widget set which adds many complex widgets
which are built from Tk building blocks. The extra widgets include
combo box, file selection, notebooks, paned windows, spin controls,
and hierarchical list boxes.

%description -l de.UTF-8
Tix ist ein Zusatzprogramm für den 'Tk widget set', das viele komplexe
Widgets hinzufügt, die aus Tk-Bausteinen bestehen, z.B.
Kombinationsfelder, Dateiauswahl, Notizblöcke, überlappende Fenster,
Drehknöpfe und hierarchische Listenfelder.

%description -l fr.UTF-8
tix est un ajout à l'ensemble des widgets Tk qui apporte de nombreux
widgets complexes construits à partir des briques de Tk. Les widgets
supplémentaires incluent les combo box, la sélection de fichiers, les
notebooks, les fenêtres « paned » et les listes hiérarchisées.

%description -l pl.UTF-8
Tix jest dodatkiem dla Tk, zawierającym wiele interesujących widgetów.

%description -l tr.UTF-8
Tix, Tk yapıtaşları kullanılarak oluşturulmuş bir çok karmaşık arayüz
elemanı bulunduran bir eklemedir. Bu yeni elemanlar arasında çoktan
seçmeli kutular, dosya seçim kutuları, not defterleri, çok kısımlı
pencereler yer almaktadır.

%package devel
Summary:	Tix development documentation
Summary(pl.UTF-8):	Dokumentacja programisty do rozszerzenia Tix
Group:		Development/Languages/Tcl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Tix development documentation.

%description devel -l pl.UTF-8
Dokumentacja programisty do rozszerzenia Tix.

%package demo
Summary:	Tix - demo programs
Summary(pl.UTF-8):	Tix - programy demostracjne
Group:		Development/Languages/Tcl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demo
Tix - demo programs.

%description demo -l pl.UTF-8
Tix - programy demostracjne.

%prep
%setup -q -n Tix%{version}
%patch0 -p1
%patch2 -p1

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

install -d $RPM_BUILD_ROOT%{_datadir}/groff/%{groff_version}/tmac
sed -i -e 's/.so man.macros/.mso tix.tmac/g' $RPM_BUILD_ROOT%{_mandir}/mann/*.n
install man/man.macros $RPM_BUILD_ROOT%{_datadir}/groff/%{groff_version}/tmac/tix.tmac

cp -af demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{_libdir}/Tix%{major}/bitmaps/mktransgif.tcl*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT.html ChangeLog README.txt index.html license.terms docs/FAQ.html
%dir %{_libdir}/Tix%{version}
%attr(755,root,root) %{_libdir}/Tix%{version}/libTix%{version}.so
%{_libdir}/Tix%{version}/*.tcl
%{_libdir}/Tix%{version}/bitmaps
%{_libdir}/Tix%{version}/pref

%files devel
%defattr(644,root,root,755)
%doc docs/*.txt docs/{pdf,tix-book}
%{_mandir}/mann/TixIntro.n*
%{_mandir}/mann/compound.n*
%{_mandir}/mann/pixmap.n*
%{_mandir}/mann/tix*.n*
%{_datadir}/groff/%{groff_version}/tmac/tix.tmac

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
