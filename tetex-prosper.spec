%define short_name prosper
Summary:	LaTeX class for writing transparencies
Summary(pl):	Klasa LaTeXa do tworzenia slajd�w
Name:		tetex-prosper
Version:	1.00.4
Release:	1
License:	GPL
Group:		Applications/Publishing/TeX
Source0:	http://telia.dl.sourceforge.net/sourceforge/prosper/%{short_name}-%{version}.tar.bz2
# Source0-md5:	279a7e291cb78064e90d9f78cbbe9632
URL:		http://prosper.sourceforge.net/
Requires:	tetex-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Prosper is a LaTeX class for writing transparencies. It is written on
top of the seminar class by Timothy Van Zandt. It aims at offering an
environment for easily creating slides for both presentations with an
overhead projector and a video projector. Slides prepared for a
presentation with a computer and a video projector may integrate
animation effects, incremental display, and such.

%description -l pl
Prosper to klasa LaTeXa do tworzenia slajd�w. Jest napisana w oparciu
o klas� seminar Timothego Van Zandta. Celem jest zaoferowanie
�rodowiska do �atwego tworzenia slajd�w do prezentacji zar�wno na
rzutniku, jak i projektorze video. Slajdy tworzone do prezentacji na
komputerze z projektorem video mog� zawiera� efekty animacji,
wy�wietlania przyrostowego i podobne.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{short_name}
find . -type d -name CVS | xargs rm -rf
find . -type f -empty | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install %{short_name}.cls $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install contrib/*.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
cp -r img $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
rm -f contrib/*.sty

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p %{_bindir}/mktexlsr
%postun	-p %{_bindir}/mktexlsr

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ INSTALL NEWS README TODO TROUBLESHOOTINGS
%doc doc contrib designer
%{_datadir}/texmf/tex/latex/%{short_name}
