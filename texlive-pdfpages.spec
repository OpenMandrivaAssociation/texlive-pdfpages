Name:		texlive-pdfpages
Version:	71386
Release:	1
Summary:	Include PDF documents in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfpages
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpages.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpages.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpages.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/pdfpages
%doc %{_texmfdistdir}/doc/latex/pdfpages
#- source
%doc %{_texmfdistdir}/source/latex/pdfpages

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
