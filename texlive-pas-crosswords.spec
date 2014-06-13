# revision 32313
# category Package
# catalog-ctan /macros/latex/contrib/pas-crosswords
# catalog-date 2013-12-03 15:28:55 +0100
# catalog-license lppl
# catalog-version 1.03
Name:		texlive-pas-crosswords
Version:	1.03
Release:	3
Summary:	Creating crossword grids, using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pas-crosswords
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pas-crosswords.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pas-crosswords.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
