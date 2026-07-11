%global tl_name pdfpages
%global tl_revision 78558

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6h
Release:	%{tl_revision}.1
Summary:	Include PDF documents in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfpages
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpages.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpages.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpages.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(eso-pic)
Requires:	texlive(graphics)
Requires:	texlive(oberdiek)
Requires:	texlive(pdflscape)
Requires:	texlive(tools)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package simplifies the inclusion of external multi-page PDF
documents in LaTeX documents. Pages may be freely selected and similar
to psnup it is possible to put several logical pages onto each sheet of
paper. Furthermore a lot of hypertext features like hyperlinks and
article threads are provided. The package supports pdfTeX (pdfLaTeX) and
VTeX. With VTeX it is even possible to use this package to insert
PostScript files, in addition to PDF files.

