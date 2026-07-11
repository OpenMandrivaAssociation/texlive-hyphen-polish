%global tl_name hyphen-polish
%global tl_revision 78069

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0b
Release:	%{tl_revision}.1
Summary:	Polish hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/polish/plhyph.tex
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-polish.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Polish in QX and UTF-8 encodings. These
patterns are also used by Polish TeX formats MeX and LaMeX.

