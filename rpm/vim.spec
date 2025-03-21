%define baseversion 9.1
%define vimdir vim91
%define patchlevel 1206

Summary: The VIM editor
URL:     https://github.com/sailfishos/vim
Name: vim
Version: %{baseversion}.%{patchlevel}
Release: 1
License: Vim
Source: %{name}-%{version}.tar.gz
Source4: vimrc
Source5: virc
Source12: vi_help.txt
Source14: spec-template

Patch2002: vim-7.0-fixkeys.patch
Patch2003: vim-7.4-specsyntax.patch

BuildRequires: ncurses-devel gettext
BuildRequires: libacl-devel autoconf

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.

%package common
Summary: The common files needed by any version of the VIM editor
# shared files between common and minimal
Requires: %{name}-data = %{version}-%{release}
Requires: %{name}-filesystem

%description common
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-common package contains files which every VIM binary will need in
order to run.

If you are installing vim-enhanced or vim-X11, you'll also need
to install the vim-common package.

%package data
Summary: Shared data for Vi and Vim
BuildArch: noarch

%description data
The subpackage is used for shipping files and directories, which need to be
shared between vim-minimal and vim-common packages.

%package minimal
Summary: A minimal version of the VIM editor
Provides: vi = %{version}-%{release}
# shared files between common and minimal
Requires: %{name}-data = %{version}-%{release}

%description minimal
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more. The
vim-minimal package includes a minimal version of VIM, providing
the commands vi, view, ex, rvi, and rview. NOTE: The online help is
only available when the vim-common package is installed.

%package enhanced
Summary: A version of the VIM editor which includes recent enhancements
Requires: vim-common = %{version}-%{release} which
Provides: vim = %{version}-%{release}

%description enhanced
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-enhanced package contains a version of VIM with extra, recently
introduced features like Python and Perl interpreters.

Install the vim-enhanced package if you'd like to use a version of the
VIM editor which includes recently added enhancements like
interpreters for the Python and Perl scripting languages.  You'll also
need to install the vim-common package.

%package filesystem
Summary: VIM filesystem layout
BuildArch: noarch

%Description filesystem
This package provides some directories which are required by other
packages that add vim files, p.e.  additional syntax files or filetypes.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Man pages for %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}/upstream
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk


%build
cd src
autoconf

export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"

sed -i 's/-l\$with_tlib/-ltinfo -l\$with_tlib/g' configure
sed -i 's/-l\$with_tlib/-ltinfo -l\$with_tlib/g' auto/configure
# dummy date value for reproducible builds
export SOURCE_DATE_EPOCH="unknown"

%configure CFLAGS="${CFLAGS} -DSYS_VIMRC_FILE='\"/etc/vimrc\"'" \
 --prefix=%{_prefix} --with-features=huge --enable-pythoninterp \
 --enable-perlinterp --disable-tclinterp --with-x=no \
 --enable-gui=no --exec-prefix=%{_prefix} --enable-multibyte \
 --enable-cscope \
 --with-tlib=ncurses \
 --with-compiledby=%_vendor \
  --disable-netbeans \
  --disable-selinux \
  --disable-rubyinterp \
  --disable-perlinterp  \
  --disable-pythoninterp 

%make_build
cp vim enhanced-vim
make clean

perl -pi -e "s/help.txt/vi_help.txt/"  os_unix.h ex_cmds.c
perl -pi -e "s/\/etc\/vimrc/\/etc\/virc/"  os_unix.h
%configure CFLAGS="${CFLAGS} -DSYS_VIMRC_FILE='\"/etc/virc\"'" \
  --prefix=%{_prefix} --with-features=small --with-x=no \
  --enable-multibyte \
  --disable-netbeans \
  --disable-selinux \
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=ncurses --enable-gui=no --disable-gpm --exec-prefix=%{_prefix} \
  --with-compiledby=%_vendor

%make_build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/vimfiles/{after,autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
mkdir -p %{buildroot}/%{_datadir}/%{name}/vimfiles/after/{autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
cp -f %{SOURCE14} %{buildroot}/%{_datadir}/%{name}/vimfiles/template.spec
# Those aren't Linux info files but some binary files for Amiga:
rm -f README*.info


cd src
# Adding STRIP=/bin/true, because Vim wants to strip the binaries by himself
# and put the stripped files into correct dirs. Build system (koji/brew)
# does it for us, so there is no need to do it in Vim
%make_install BINDIR=%{_bindir} STRIP=/bin/true
install -m755 vim %{buildroot}%{_bindir}/vi
install -m755 enhanced-vim %{buildroot}%{_bindir}/vim

( cd %{buildroot}
  rm -f .%{_bindir}/rvim
  ln -sf vi .%{_bindir}/rvi
  ln -sf vi .%{_bindir}/ex
  ln -sf vim .%{_bindir}/rvim
  ln -sf vim .%{_bindir}/vimdiff
  perl -pi -e "s,%{buildroot},," .%{_mandir}/man1/%{name}.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  ln -sf vim.1.gz .%{_mandir}/man1/vi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/vimdiff.1.gz

  # ja_JP.ujis is obsolete, ja_JP.eucJP is recommended.
  ( cd ./%{_datadir}/%{name}/%{vimdir}/lang; \
    ln -sf menu_ja_jp.ujis.vim menu_ja_jp.eucjp.vim )
)

# Dependency cleanups
chmod 644 %{buildroot}/%{_datadir}/%{name}/%{vimdir}/doc/vim2html.pl \
 %{buildroot}/%{_datadir}/%{name}/%{vimdir}/tools/*.pl \
 %{buildroot}/%{_datadir}/%{name}/%{vimdir}/tools/vim132
chmod 644 ../runtime/doc/vim2html.pl

mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
cat >%{buildroot}/%{_sysconfdir}/profile.d/%{name}.sh <<EOF
if [ -n "\$BASH_VERSION" -o -n "\$KSH_VERSION" -o -n "\$ZSH_VERSION" ]; then
  [ -x /%{_bindir}/id ] || return
  [ \`/%{_bindir}/id -u\` -le 200 ] && return
  # for bash and zsh, only if no alias is already set
  alias vi >/dev/null 2>&1 || alias vi=vim
fi
EOF
cat >%{buildroot}/%{_sysconfdir}/profile.d/vim.csh <<EOF
[ -x /%{_bindir}/id ] || exit
[ \`/%{_bindir}/id -u\` -gt 200 ] && alias vi vim
EOF
chmod 0644 %{buildroot}/%{_sysconfdir}/profile.d/*
install -p -m644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/vimrc
install -p -m644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/virc
(cd %{buildroot}/%{_datadir}/%{name}/%{vimdir}/doc;
 gzip -9 *.txt
 gzip -d help.txt.gz version7.txt.gz sponsor.txt.gz
 cp %{SOURCE12} .
 cat tags | sed -e 's/\t\(.*.txt\)\t/\t\1.gz\t/;s/\thelp.txt.gz\t/\thelp.txt\t/;s/\tversion7.txt.gz\t/\tversion7.txt\t/;s/\tsponsor.txt.gz\t/\tsponsor.txt\t/' > tags.new; mv -f tags.new tags
cat >> tags << EOF
vi_help.txt	vi_help.txt	/*vi_help.txt*
vi-author.txt	vi_help.txt	/*vi-author*
vi-Bram.txt	vi_help.txt	/*vi-Bram*
vi-Moolenaar.txt	vi_help.txt	/*vi-Moolenaar*
vi-credits.txt	vi_help.txt	/*vi-credits*
EOF
LANG=C sort tags > tags.tmp; mv tags.tmp tags
 )
rm -f %{buildroot}/%{_datadir}/%{name}/%{vimdir}/macros/maze/maze*.c
rm -rf %{buildroot}/%{_datadir}/%{name}/%{vimdir}/tools
rm -rf %{buildroot}/%{_datadir}/%{name}/%{vimdir}/doc/vim2html.pl
rm -f %{buildroot}/%{_datadir}/%{name}/%{vimdir}/tutor/tutor.gr.utf-8~
( cd %{buildroot}/%{_mandir}
  for i in `find ??/ -type f`; do
    bi=`basename $i`
    iconv -f latin1 -t UTF8 $i > %{buildroot}/$bi
    mv -f %{buildroot}/$bi $i
  done
)

# Remove not UTF-8 manpages
for i in pl.ISO8859-2 it.ISO8859-1 ru.KOI8-R fr.ISO8859-1 da.ISO8859-1 de.ISO8859-1 tr.ISO8859-9; do
  rm -rf %{buildroot}/%{_mandir}/$i
done

# use common man1/ru directory
mv %{buildroot}/%{_mandir}/ru.UTF-8 %{buildroot}/%{_mandir}/ru

# Remove duplicate man pages
for i in fr.UTF-8 it.UTF-8 pl.UTF-8 da.UTF-8 de.UTF-8 tr.UTF-8; do
  rm -rf %{buildroot}/%{_mandir}/$i
done
rm -rf %{buildroot}/bin/gvimtutor
rm -rf %{buildroot}%{_bindir}/vimtutor

# Remove desktop files, we have no use for them.
rm %{buildroot}/%{_datadir}/applications/gvim.desktop
rm %{buildroot}/%{_datadir}/applications/vim.desktop
# Remove icons, needed by desktop files
rm -rf %{buildroot}/%{_datadir}/icons

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        README*

# upstream now tries to install LICENSE and README into VIMDIR
# but we ship them in licensedir and docdir, so we remove the dupes
# from VIMDIR
rm %{buildroot}%{_datadir}/%{name}/%{vimdir}/LICENSE
rm %{buildroot}%{_datadir}/%{name}/%{vimdir}/README.txt

%files common
%config(noreplace) %{_sysconfdir}/vimrc
%{_datadir}/%{name}/%{vimdir}/autoload
%{_datadir}/%{name}/%{vimdir}/colors
%{_datadir}/%{name}/%{vimdir}/compiler
%{_datadir}/%{name}/%{vimdir}/pack
%{_datadir}/%{name}/%{vimdir}/doc
%{_datadir}/%{name}/%{vimdir}/*.vim
%{_datadir}/%{name}/%{vimdir}/ftplugin
%{_datadir}/%{name}/%{vimdir}/import/dist/vimhelp.vim
%{_datadir}/%{name}/%{vimdir}/import/dist/vimhighlight.vim
%{_datadir}/%{name}/%{vimdir}/indent
%{_datadir}/%{name}/%{vimdir}/keymap
%{_datadir}/%{name}/%{vimdir}/lang/*.vim
%{_datadir}/%{name}/%{vimdir}/lang/*.txt
%dir %{_datadir}/%{name}/%{vimdir}/lang
%{_datadir}/%{name}/%{vimdir}/macros
%{_datadir}/%{name}/%{vimdir}/plugin
%{_datadir}/%{name}/%{vimdir}/print
%{_datadir}/%{name}/%{vimdir}/syntax
%{_datadir}/%{name}/%{vimdir}/tutor
%{_datadir}/%{name}/%{vimdir}/spell
%{_bindir}/xxd

%files data
%license LICENSE
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{vimdir}
%{_datadir}/%{name}/%{vimdir}/defaults.vim
%dir %{_datadir}/%{name}/vimfiles
%{_datadir}/%{name}/vimfiles/template.spec

%files minimal
%config(noreplace) %{_sysconfdir}/virc
%{_bindir}/ex
%{_bindir}/rvi
%{_bindir}/rview
%{_bindir}/vi
%{_bindir}/view

%files enhanced
%{_bindir}/rvim
%{_bindir}/vim
%{_bindir}/vimdiff
%config(noreplace) %{_sysconfdir}/profile.d/vim.*

%files filesystem
%dir %{_datadir}/%{name}/vimfiles
%dir %{_datadir}/%{name}/vimfiles/after
%dir %{_datadir}/%{name}/vimfiles/after/*
%dir %{_datadir}/%{name}/vimfiles/autoload
%dir %{_datadir}/%{name}/vimfiles/colors
%dir %{_datadir}/%{name}/vimfiles/compiler
%dir %{_datadir}/%{name}/vimfiles/doc
%dir %{_datadir}/%{name}/vimfiles/ftdetect
%dir %{_datadir}/%{name}/vimfiles/ftplugin
%dir %{_datadir}/%{name}/vimfiles/indent
%dir %{_datadir}/%{name}/vimfiles/keymap
%dir %{_datadir}/%{name}/vimfiles/lang
%dir %{_datadir}/%{name}/vimfiles/plugin
%dir %{_datadir}/%{name}/vimfiles/print
%dir %{_datadir}/%{name}/vimfiles/spell
%dir %{_datadir}/%{name}/vimfiles/syntax
%dir %{_datadir}/%{name}/vimfiles/tutor
%dir %{_datadir}/%{name}/%{vimdir}/import
%dir %{_datadir}/%{name}/%{vimdir}/import/dist

%files doc
%{_mandir}/man1/*
%{_docdir}/%{name}-%{version}
%lang(da) %{_mandir}/da/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(ru) %{_mandir}/ru/man1/*
%lang(tr) %{_mandir}/tr/man1/*
