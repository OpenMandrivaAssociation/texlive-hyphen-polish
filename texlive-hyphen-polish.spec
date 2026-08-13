%global tl_name hyphen-polish
%global tl_revision 78069
%global tl_version 3.0b

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Polish in QX and UTF-8 encodings. These
patterns are also used by Polish TeX formats MeX and LaMeX.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-polish:
polish loadhyph-pl.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-polish:
\addlanguage{polish}{loadhyph-pl.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-polish:
['polish'] = {
	loader = 'loadhyph-pl.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-pl.pat.txt',
	hyphenation = 'hyph-pl.hyp.txt',
},
TL_HYPHEN_EOF
