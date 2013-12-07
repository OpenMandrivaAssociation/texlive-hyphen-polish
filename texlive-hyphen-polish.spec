# revision 25990
# category TLCore
# catalog-ctan /language/polish/plhyph.tex
# catalog-date 2009-10-07 21:35:42 +0200
# catalog-license knuth
# catalog-version 3.0a
Name:		texlive-hyphen-polish
Version:	3.0a
Release:	7
Summary:	Polish hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/polish/plhyph.tex
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-polish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Polish in QX and UTF-8 encodings.
These patterns are also used by Polish TeX formats MeX and
LaMeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-polish
%_texmf_language_def_d/hyphen-polish
%_texmf_language_lua_d/hyphen-polish

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-polish <<EOF
\%% from hyphen-polish:
polish loadhyph-pl.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-polish
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-polish <<EOF
\%% from hyphen-polish:
\addlanguage{polish}{loadhyph-pl.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-polish
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-polish <<EOF
-- from hyphen-polish:
	['polish'] = {
		loader = 'loadhyph-pl.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-pl.pat.txt',
		hyphenation = 'hyph-pl.hyp.txt',
	},
EOF


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.0a-4
+ Revision: 804805
- Update to latest release.

* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.0a-3
+ Revision: 767571
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.0a-2
+ Revision: 759931
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.0a-1
+ Revision: 718673
- texlive-hyphen-polish
- texlive-hyphen-polish
- texlive-hyphen-polish
- texlive-hyphen-polish

