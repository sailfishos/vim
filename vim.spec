%define baseversion 7.3
%define vimdir vim73
%define patchlevel 177

Summary: The VIM editor
URL:     http://www.vim.org/
Name: vim
Version: %{baseversion}.%{patchlevel}
Release: 1
License: Vim
Group: Applications/Editors
Source0: ftp://ftp.vim.org/pub/vim/unix/vim-%{baseversion}.tar.bz2
Source4: vimrc
Source5: virc
#Source5: ftp://ftp.vim.org/pub/vim/patches/README.patches
Source11: Changelog.rpm
Source12: vi_help.txt
Source14: spec-template
Source15: http://www.cvjb.de/comp/vim/forth.vim

# remove this for the next major version, CVE fixes:
Source16: ftp://ftp.vim.org/vol/2/vim/runtime/plugin/netrwPlugin.vim
Source17: ftp://ftp.vim.org/vol/2/vim/runtime/plugin/gzip.vim
Source18: ftp://ftp.vim.org/vol/2/vim/runtime/filetype.vim
Source19: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/zip.vim
Source20: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/tar.vim
Source21: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/netrwFileHandlers.vim
Source22: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/netrw.vim
Source23: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/netrwSettings.vim

Patch2002: vim-7.0-fixkeys.patch
Patch2003: vim-6.2-specsyntax.patch
Patch2004: vim-7.0-crv.patch
# for i in `seq 1 14`; do printf "Patch%03d: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.%03d\n" $i $i; done
Patch001: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.001
Patch002: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.002
Patch003: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.003
Patch004: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.004
Patch005: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.005
Patch006: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.006
Patch007: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.007
Patch008: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.008
Patch009: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.009
Patch010: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.010
Patch011: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.011
Patch012: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.012
Patch013: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.013
Patch014: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.014
Patch015: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.015
Patch016: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.016
Patch017: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.017
Patch018: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.018
Patch019: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.019
Patch020: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.020
Patch021: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.021
Patch022: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.022
Patch023: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.023
Patch024: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.024
Patch025: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.025
Patch026: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.026
Patch027: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.027
Patch028: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.028
Patch029: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.029
Patch030: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.030
Patch031: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.031
Patch032: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.032
Patch033: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.033
Patch034: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.034
Patch035: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.035
Patch036: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.036
Patch037: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.037
Patch038: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.038
Patch039: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.039
Patch040: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.040
Patch041: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.041
Patch042: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.042
Patch043: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.043
Patch044: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.044
Patch045: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.045
Patch046: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.046
Patch047: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.047
Patch048: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.048
Patch049: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.049
Patch050: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.050
Patch051: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.051
Patch052: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.052
Patch053: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.053
Patch054: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.054
Patch055: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.055
Patch056: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.056
Patch057: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.057
Patch058: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.058
Patch059: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.059
Patch060: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.060
Patch061: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.061
Patch062: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.062
Patch063: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.063
Patch064: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.064
Patch065: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.065
Patch066: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.066
Patch067: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.067
Patch068: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.068
Patch069: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.069
Patch070: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.070
Patch071: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.071
Patch072: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.072
Patch073: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.073
Patch074: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.074
Patch075: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.075
Patch076: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.076
Patch077: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.077
Patch078: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.078
Patch079: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.079
Patch080: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.080
Patch081: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.081
Patch082: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.082
Patch083: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.083
Patch084: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.084
Patch085: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.085
Patch086: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.086
Patch087: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.087
Patch088: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.088
Patch089: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.089
Patch090: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.090
Patch091: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.091
Patch092: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.092
Patch093: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.093
Patch094: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.094
Patch095: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.095
Patch096: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.096
Patch097: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.097
Patch098: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.098
Patch099: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.099
Patch100: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.100
Patch101: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.101
Patch102: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.102
Patch103: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.103
Patch104: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.104
Patch105: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.105
Patch106: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.106
Patch107: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.107
Patch108: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.108
Patch109: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.109
Patch110: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.110
Patch111: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.111
Patch112: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.112
Patch113: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.113
Patch114: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.114
Patch115: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.115
Patch116: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.116
Patch117: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.117
Patch118: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.118
Patch119: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.119
Patch120: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.120
Patch121: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.121
Patch122: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.122
Patch123: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.123
Patch124: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.124
Patch125: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.125
Patch126: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.126
Patch127: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.127
Patch128: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.128
Patch129: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.129
Patch130: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.130
Patch131: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.131
Patch132: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.132
Patch133: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.133
Patch134: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.134
Patch135: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.135
Patch136: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.136
Patch137: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.137
Patch138: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.138
Patch139: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.139
Patch140: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.140
Patch141: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.141
Patch142: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.142
Patch143: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.143
Patch144: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.144
Patch145: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.145
Patch146: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.146
Patch147: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.147
Patch148: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.148
Patch149: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.149
Patch150: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.150
Patch151: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.151
Patch152: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.152
Patch153: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.153
Patch154: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.154
Patch155: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.155
Patch156: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.156
Patch157: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.157
Patch158: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.158
Patch159: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.159
Patch160: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.160
Patch161: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.161
Patch162: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.162
Patch163: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.163
Patch164: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.164
Patch165: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.165
Patch166: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.166
Patch167: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.167
Patch168: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.168
Patch169: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.169
Patch170: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.170
Patch171: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.171
Patch172: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.172
Patch173: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.173
Patch174: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.174
Patch175: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.175
Patch176: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.176
Patch177: ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.177

Patch3004: vim-7.0-rclocation.patch
Patch3006: vim-6.4-checkhl.patch
Patch3009: vim-7.0-syncolor.patch
Patch3010: vim-7.0-specedit.patch

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: ncurses-devel gettext
BuildRequires: libacl-devel autoconf

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.

%package common
Summary: The common files needed by any version of the VIM editor
Group: Applications/Editors
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

%package minimal
Summary: A minimal version of the VIM editor
Group: Applications/Editors
Provides: vi = %{version}-%{release}

%description minimal
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more. The
vim-minimal package includes a minimal version of VIM, which is
installed into /bin/vi for use when only the root partition is
present. NOTE: The online help is only available when the vim-common
package is installed.

%package enhanced
Summary: A version of the VIM editor which includes recent enhancements
Group: Applications/Editors
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
Group: Applications/Editors

%Description filesystem
This package provides some directories which are required by other
packages that add vim files, p.e.  additional syntax files or filetypes.


%prep
%setup -q -b 0 -n %{vimdir}
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2002 -p1
%patch2003 -p1
%patch2004 -p1
perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

# Base patches...
# for i in `seq 1 14`; do printf "%%patch%03d -p0 \n" $i; done
%patch001 -p0
%patch002 -p0
%patch003 -p0
%patch004 -p0
%patch005 -p0
%patch006 -p0
%patch007 -p0
%patch008 -p0
%patch009 -p0
%patch010 -p0
%patch011 -p0
%patch012 -p0
%patch013 -p0
%patch014 -p0
%patch015 -p0
%patch016 -p0
%patch017 -p0
%patch018 -p0
%patch019 -p0
%patch020 -p0
%patch021 -p0
%patch022 -p0
%patch023 -p0
%patch024 -p0
%patch025 -p0
%patch026 -p0
%patch027 -p0
%patch028 -p0
%patch029 -p0
%patch030 -p0
%patch031 -p0
%patch032 -p0
%patch033 -p0
%patch034 -p0
%patch035 -p0
%patch036 -p0
%patch037 -p0
%patch038 -p0
%patch039 -p0
%patch040 -p0
%patch041 -p0
%patch042 -p0
%patch043 -p0
%patch044 -p0
%patch045 -p0
%patch046 -p0
%patch047 -p0
%patch048 -p0
%patch049 -p0
%patch050 -p0
%patch051 -p0
%patch052 -p0
%patch053 -p0
%patch054 -p0
%patch055 -p0
%patch056 -p0
%patch057 -p0
%patch058 -p0
%patch059 -p0
%patch060 -p0
%patch061 -p0
%patch062 -p0
%patch063 -p0
%patch064 -p0
%patch065 -p0
%patch066 -p0
%patch067 -p0
%patch068 -p0
%patch069 -p0
%patch070 -p0
%patch071 -p0
%patch072 -p0
%patch073 -p0
%patch074 -p0
%patch075 -p0
%patch076 -p0
%patch077 -p0
%patch078 -p0
%patch079 -p0
%patch080 -p0
%patch081 -p0
%patch082 -p0
%patch083 -p0
%patch084 -p0
%patch085 -p0
%patch086 -p0
%patch087 -p0
%patch088 -p0
%patch089 -p0
%patch090 -p0
%patch091 -p0
%patch092 -p0
%patch093 -p0
%patch094 -p0
%patch095 -p0
%patch096 -p0
%patch097 -p0
%patch098 -p0
%patch099 -p0
%patch100 -p0
%patch101 -p0
%patch102 -p0
%patch103 -p0
%patch104 -p0
%patch105 -p0
%patch106 -p0
%patch107 -p0
%patch108 -p0
%patch109 -p0
%patch110 -p0
%patch111 -p0
%patch112 -p0
%patch113 -p0
%patch114 -p0
%patch115 -p0
%patch116 -p0
%patch117 -p0
%patch118 -p0
%patch119 -p0
%patch120 -p0
%patch121 -p0
%patch122 -p0
%patch123 -p0
%patch124 -p0
%patch125 -p0
%patch126 -p0
%patch127 -p0
%patch128 -p0
%patch129 -p0
%patch130 -p0
%patch131 -p0
%patch132 -p0
%patch133 -p0
%patch134 -p0
%patch135 -p0
%patch136 -p0
%patch137 -p0
%patch138 -p0
%patch139 -p0
%patch140 -p0
%patch141 -p0
%patch142 -p0
%patch143 -p0
%patch144 -p0
%patch145 -p0
%patch146 -p0
%patch147 -p0
%patch148 -p0
%patch149 -p0
%patch150 -p0
%patch151 -p0
%patch152 -p0
%patch153 -p0
%patch154 -p0
%patch155 -p0
%patch156 -p0
%patch157 -p0
%patch158 -p0
%patch159 -p0
%patch160 -p0
%patch161 -p0
%patch162 -p0
%patch163 -p0
%patch164 -p0
%patch165 -p0
%patch166 -p0
%patch167 -p0
%patch168 -p0
%patch169 -p0
%patch170 -p0
%patch171 -p0
%patch172 -p0
%patch173 -p0
%patch174 -p0
%patch175 -p0
%patch176 -p0
%patch177 -p0

%patch3004 -p1
%patch3006 -p1
%patch3009 -p1
%patch3010 -p1

cp -f %{SOURCE15} runtime/syntax/forth.vim
cp -f %{SOURCE16} runtime/plugin/netrwPlugin.vim
cp -f %{SOURCE17} runtime/plugin/gzip.vim
cp -f %{SOURCE18} runtime/plugin/filetype.vim
cp -f %{SOURCE19} runtime/autoload/zip.vim
cp -f %{SOURCE20} runtime/autoload/tar.vim
cp -f %{SOURCE21} runtime/autoload/netrwFileHandlers.vim
cp -f %{SOURCE22} runtime/autoload/netrw.vim
cp -f %{SOURCE23} runtime/autoload/netrwSettings.vim

%build
cd src
autoconf

sed -e "s+VIMRCLOC	= \$(VIMLOC)+VIMRCLOC	= /etc+" Makefile > Makefile.tmp
mv -f Makefile.tmp Makefile

export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"

sed -i 's/-l\$with_tlib/-ltinfo -l\$with_tlib/g' configure
sed -i 's/-l\$with_tlib/-ltinfo -l\$with_tlib/g' auto/configure

%configure --prefix=%{_prefix} --with-features=huge --enable-pythoninterp \
 --enable-perlinterp --disable-tclinterp --with-x=no \
 --enable-gui=no --exec-prefix=%{_prefix} --enable-multibyte \
 --enable-cscope --with-modified-by="<bugzilla@meego.com>" \
 --with-tlib=ncurses \
 --with-compiledby="<bugzilla@meego.com>" \
  --disable-netbeans \
  --disable-selinux \
  --disable-rubyinterp \
  --disable-perlinterp  \
  --disable-pythoninterp 

make VIMRCLOC=/etc VIMRUNTIMEDIR=/usr/share/vim/%{vimdir} %{?_smp_mflags}
cp vim enhanced-vim
make clean

perl -pi -e "s/help.txt/vi_help.txt/"  os_unix.h ex_cmds.c
perl -pi -e "s/\/etc\/vimrc/\/etc\/virc/"  os_unix.h
%configure --prefix=%{_prefix} --with-features=small --with-x=no \
  --enable-multibyte \
  --disable-netbeans \
  --disable-selinux \
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=ncurses --enable-gui=no --disable-gpm --exec-prefix=/ \
  --with-compiledby="<bugzilla@meego.com>" \
  --with-modified-by="<bugzilla@meego.com>"

make VIMRCLOC=/etc VIMRUNTIMEDIR=/usr/share/vim/%{vimdir} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/vimfiles/{after,autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/vimfiles/after/{autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
cp -f %{SOURCE11} .
cp -f %{SOURCE14} $RPM_BUILD_ROOT/%{_datadir}/%{name}/vimfiles/template.spec
cp runtime/doc/uganda.txt LICENSE
# Those aren't Linux info files but some binary files for Amiga:
rm -f README*.info


cd src
make install DESTDIR=$RPM_BUILD_ROOT BINDIR=/bin VIMRCLOC=/etc VIMRUNTIMEDIR=/usr/share/vim/%{vimdir}
make installgtutorbin  DESTDIR=$RPM_BUILD_ROOT BINDIR=/bin VIMRCLOC=/etc VIMRUNTIMEDIR=/usr/share/vim/%{vimdir}
mv $RPM_BUILD_ROOT/bin/xxd $RPM_BUILD_ROOT/%{_bindir}/xxd
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m755 enhanced-vim $RPM_BUILD_ROOT/%{_bindir}/vim

( cd $RPM_BUILD_ROOT
  mv ./bin/vimtutor ./%{_bindir}/vimtutor
  mv ./bin/vim ./bin/vi
  rm -f ./bin/rvim
  ln -sf vi ./bin/ex
  ln -sf vi ./bin/rvi
  ln -sf vi ./bin/rview
  ln -sf vi ./bin/view
  ln -sf vim ./%{_bindir}/ex
  ln -sf vim ./%{_bindir}/rvim
  ln -sf vim ./%{_bindir}/vimdiff
  perl -pi -e "s,$RPM_BUILD_ROOT,," .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  ln -sf vim.1.gz .%{_mandir}/man1/vi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/vimdiff.1.gz
  # ja_JP.ujis is obsolete, ja_JP.eucJP is recommended.
  ( cd ./%{_datadir}/%{name}/%{vimdir}/lang; \
    ln -sf menu_ja_jp.ujis.vim menu_ja_jp.eucjp.vim )
)

pushd $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tutor
mkdir conv
   iconv -f CP1252 -t UTF8 tutor.ca > conv/tutor.ca
   iconv -f CP1252 -t UTF8 tutor.it > conv/tutor.it
   #iconv -f CP1253 -t UTF8 tutor.gr > conv/tutor.gr
   iconv -f CP1252 -t UTF8 tutor.fr > conv/tutor.fr
   iconv -f CP1252 -t UTF8 tutor.es > conv/tutor.es
   iconv -f CP1252 -t UTF8 tutor.de > conv/tutor.de
   #iconv -f CP737 -t UTF8 tutor.gr.cp737 > conv/tutor.gr.cp737
   #iconv -f EUC-JP -t UTF8 tutor.ja.euc > conv/tutor.ja.euc
   #iconv -f SJIS -t UTF8 tutor.ja.sjis > conv/tutor.ja.sjis
   iconv -f UTF8 -t UTF8 tutor.ja.utf-8 > conv/tutor.ja.utf-8
   iconv -f UTF8 -t UTF8 tutor.ko.utf-8 > conv/tutor.ko.utf-8
   iconv -f CP1252 -t UTF8 tutor.no > conv/tutor.no
   iconv -f ISO-8859-2 -t UTF8 tutor.pl > conv/tutor.pl
   iconv -f ISO-8859-2 -t UTF8 tutor.sk > conv/tutor.sk
   iconv -f KOI8R -t UTF8 tutor.ru > conv/tutor.ru
   iconv -f CP1252 -t UTF8 tutor.sv > conv/tutor.sv
   mv -f tutor.ja.euc tutor.ja.sjis tutor.ko.euc tutor.pl.cp1250 tutor.zh.big5 tutor.ru.cp1251 tutor.zh.euc conv/
   rm -f tutor.ca tutor.de tutor.es tutor.fr tutor.gr tutor.it tutor.ja.utf-8 tutor.ko.utf-8 tutor.no tutor.pl tutor.sk tutor.ru tutor.sv
mv -f conv/* .
rmdir conv
popd

# Dependency cleanups
chmod 644 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/doc/vim2html.pl \
 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tools/*.pl \
 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tools/vim132
chmod 644 ../runtime/doc/vim2html.pl

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
cat >$RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/vim.sh <<EOF
if [ -n "\$BASH_VERSION" -o -n "\$KSH_VERSION" -o -n "\$ZSH_VERSION" ]; then
  [ -x /%{_bindir}/id ] || return
  [ \`/%{_bindir}/id -u\` -le 200 ] && return
  # for bash and zsh, only if no alias is already set
  alias vi >/dev/null 2>&1 || alias vi=vim
fi
EOF
cat >$RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/vim.csh <<EOF
[ -x /%{_bindir}/id ] || exit
[ \`/%{_bindir}/id -u\` -gt 200 ] && alias vi vim
EOF
chmod 0644 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/*
install -p -m644 %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/vimrc
install -p -m644 %{SOURCE5} $RPM_BUILD_ROOT/%{_sysconfdir}/virc
(cd $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/doc;
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
(cd ../runtime; rm -rf doc; ln -svf ../../vim/%{vimdir}/doc docs;) 
rm -f $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/macros/maze/maze*.c
rm -rf $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/tools
rm -rf $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/doc/vim2html.pl
rm -f $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/tutor/tutor.gr.utf-8~
( cd $RPM_BUILD_ROOT/%{_mandir}
  for i in `find ??/ -type f`; do
    bi=`basename $i`
    iconv -f latin1 -t UTF8 $i > $RPM_BUILD_ROOT/$bi
    mv -f $RPM_BUILD_ROOT/$bi $i
  done
)

# Remove not UTF-8 manpages
for i in pl.ISO8859-2 it.ISO8859-1 ru.KOI8-R fr.ISO8859-1; do
  rm -rf $RPM_BUILD_ROOT/%{_mandir}/$i
done

# use common man1/ru directory
mv $RPM_BUILD_ROOT/%{_mandir}/ru.UTF-8 $RPM_BUILD_ROOT/%{_mandir}/ru

# Remove duplicate man pages
for i in fr.UTF-8 it.UTF-8 pl.UTF-8; do
  rm -rf $RPM_BUILD_ROOT/%{_mandir}/$i
done
rm -rf %{buildroot}/bin/gvimtutor
rm -rf %{buildroot}%{_bindir}/vimtutor

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/vimrc
%doc README* LICENSE
%doc runtime/docs
%doc Changelog.rpm
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/vimfiles/template.spec
%{_datadir}/%{name}/%{vimdir}/autoload
%{_datadir}/%{name}/%{vimdir}/colors
%{_datadir}/%{name}/%{vimdir}/compiler
%{_datadir}/%{name}/%{vimdir}/doc
%{_datadir}/%{name}/%{vimdir}/*.vim
%{_datadir}/%{name}/%{vimdir}/ftplugin
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
%lang(af) %{_datadir}/%{name}/%{vimdir}/lang/af
%lang(ca) %{_datadir}/%{name}/%{vimdir}/lang/ca
%lang(cs) %{_datadir}/%{name}/%{vimdir}/lang/cs
%lang(de) %{_datadir}/%{name}/%{vimdir}/lang/de
%lang(en_GB) %{_datadir}/%{name}/%{vimdir}/lang/en_GB
%lang(eo) %{_datadir}/%{name}/%{vimdir}/lang/eo
%lang(es) %{_datadir}/%{name}/%{vimdir}/lang/es
%lang(fi) %{_datadir}/%{name}/%{vimdir}/lang/fi
%lang(fr) %{_datadir}/%{name}/%{vimdir}/lang/fr
%lang(ga) %{_datadir}/%{name}/%{vimdir}/lang/ga
%lang(it) %{_datadir}/%{name}/%{vimdir}/lang/it
%lang(ja) %{_datadir}/%{name}/%{vimdir}/lang/ja
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko.UTF-8
%lang(nb) %{_datadir}/%{name}/%{vimdir}/lang/nb
%lang(no) %{_datadir}/%{name}/%{vimdir}/lang/no
%lang(pl) %{_datadir}/%{name}/%{vimdir}/lang/pl
%lang(pt_BR) %{_datadir}/%{name}/%{vimdir}/lang/pt_BR
%lang(ru) %{_datadir}/%{name}/%{vimdir}/lang/ru
%lang(sk) %{_datadir}/%{name}/%{vimdir}/lang/sk
%lang(sv) %{_datadir}/%{name}/%{vimdir}/lang/sv
%lang(uk) %{_datadir}/%{name}/%{vimdir}/lang/uk
%lang(vi) %{_datadir}/%{name}/%{vimdir}/lang/vi
%lang(zh_CN) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN
%lang(zh_TW) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW
%lang(zh_CN.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.UTF-8
%lang(zh_TW.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW.UTF-8
/%{_bindir}/xxd
%{_mandir}/man1/vim.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/vi.*
%{_mandir}/man1/view.*
%{_mandir}/man1/rvi.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/xxd.*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(ru) %{_mandir}/ru/man1/*


%files minimal
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/virc
/bin/ex
/bin/vi
/bin/view
/bin/rvi
/bin/rview

%files enhanced
%defattr(-,root,root)
%{_bindir}/vim
%{_bindir}/rvim
%{_bindir}/vimdiff
%{_bindir}/ex
%config(noreplace) %{_sysconfdir}/profile.d/vim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*
%{_mandir}/man1/evim.*

%files filesystem
%defattr(-,root,root)
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

