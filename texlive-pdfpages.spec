Name:		texlive-pdfpages
Version:	0.4p
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
Requires(post):	texlive-tlpkg
Requires:	texlive-eso-pic
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package simplifies the inclusion of external multi-page
PDF documents in LaTeX documents. Pages may be freely selected
and similar to psnup it is possible to put several logical
pages onto each sheet of paper. Furthermore a lot of hypertext
features like hyperlinks and article threads are provided. The
package supports pdfTeX (pdflatex) and VTeX. With VTeX it is
even possible to use this package to insert PostScript files,
in addition to PDF files.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
