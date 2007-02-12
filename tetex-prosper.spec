%define short_name prosper
Summary:	LaTeX class for writing transparencies
Summary(pl.UTF-8):   Klasa LaTeXa do tworzenia slajdów
Name:		tetex-prosper
Version:	1.00.4
Release:	2
License:	GPL
Group:		Applications/Publishing/TeX
Source0:	http://dl.sourceforge.net/prosper/%{short_name}-%{version}.tar.bz2
# Source0-md5:	279a7e291cb78064e90d9f78cbbe9632
URL:		http://prosper.sourceforge.net/
Requires:	tetex-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

%description
Prosper is a LaTeX class for writing transparencies. It is written on
top of the seminar class by Timothy Van Zandt. It aims at offering an
environment for easily creating slides for both presentations with an
overhead projector and a video projector. Slides prepared for a
presentation with a computer and a video projector may integrate
animation effects, incremental display, and such.

%description -l pl.UTF-8
Prosper to klasa LaTeXa do tworzenia slajdów. Jest napisana w oparciu
o klasę seminar Timothego Van Zandta. Celem jest zaoferowanie
środowiska do łatwego tworzenia slajdów do prezentacji zarówno na
rzutniku, jak i projektorze video. Slajdy tworzone do prezentacji na
komputerze z projektorem video mogą zawierać efekty animacji,
wyświetlania przyrostowego i podobne.

%prep
%setup -q -n %{short_name}
find . -type d -name CVS | xargs rm -rf
find . -type f -empty | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install %{short_name}.cls $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install contrib/*.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
cp -r img $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
rm -f contrib/*.sty

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{texhash}

%postun
%{texhash}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ INSTALL NEWS README TODO TROUBLESHOOTINGS
%doc doc contrib designer
%{_datadir}/texmf/tex/latex/%{short_name}
