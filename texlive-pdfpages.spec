# revision 25883
# category Package
# catalog-ctan /macros/latex/contrib/pdfpages
# catalog-date 2012-04-08 13:49:02 +0200
# catalog-license lppl
# catalog-version 0.4s
Name:		texlive-pdfpages
Version:	0.4s
Release:	1
Summary:	Include PDF documents in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfpages
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpages.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpages.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpages.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-eso-pic

%description
This package simplifies the inclusion of external multi-page
PDF documents in LaTeX documents. Pages may be freely selected
and similar to psnup it is possible to put several logical
pages onto each sheet of paper. Furthermore a lot of hypertext
features like hyperlinks and article threads are provided. The
package supports pdfTeX (pdflatex) and VTeX. With VTeX it is
even possible to use this package to insert PostScript files,
in addition to PDF files.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdfpages/pdfpages.sty
%{_texmfdistdir}/tex/latex/pdfpages/ppdvipdfm.def
%{_texmfdistdir}/tex/latex/pdfpages/ppdvips.def
%{_texmfdistdir}/tex/latex/pdfpages/ppnull.def
%{_texmfdistdir}/tex/latex/pdfpages/pppdftex.def
%{_texmfdistdir}/tex/latex/pdfpages/ppvtex.def
%{_texmfdistdir}/tex/latex/pdfpages/ppxetex.def
%doc %{_texmfdistdir}/doc/latex/pdfpages/dummy-l.pdf
%doc %{_texmfdistdir}/doc/latex/pdfpages/dummy.pdf
%doc %{_texmfdistdir}/doc/latex/pdfpages/pdf-ex.tex
%doc %{_texmfdistdir}/doc/latex/pdfpages/pdf-hyp.tex
%doc %{_texmfdistdir}/doc/latex/pdfpages/pdf-toc.tex
%doc %{_texmfdistdir}/doc/latex/pdfpages/pdfpages.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pdfpages/README
%doc %{_texmfdistdir}/source/latex/pdfpages/pdfpages.dtx
%doc %{_texmfdistdir}/source/latex/pdfpages/pdfpages.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4s-1
+ Revision: 790733
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4r-1
+ Revision: 787729
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4p-2
+ Revision: 754763
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4p-1
+ Revision: 719221
- texlive-pdfpages
- texlive-pdfpages
- texlive-pdfpages
- texlive-pdfpages

