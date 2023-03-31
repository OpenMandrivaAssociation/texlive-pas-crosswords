Name:		texlive-pas-crosswords
Version:	32313
Release:	2
Summary:	Creating crossword grids, using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pas-crosswords
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pas-crosswords.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pas-crosswords.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package produces crossword grids, using a wide variety of
colours and decorations of the grids and the text in them. The
package uses TikZ for its graphical output.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pas-crosswords/pas-crosswords.sty
%doc %{_texmfdistdir}/doc/latex/pas-crosswords/README
%doc %{_texmfdistdir}/doc/latex/pas-crosswords/pas-crosswords.pdf
%doc %{_texmfdistdir}/doc/latex/pas-crosswords/pas-crosswords.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
