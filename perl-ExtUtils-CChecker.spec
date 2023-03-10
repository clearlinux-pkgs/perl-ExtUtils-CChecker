#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-ExtUtils-CChecker
Version  : 0.11
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/ExtUtils-CChecker-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/ExtUtils-CChecker-0.11.tar.gz
Summary  : 'configure-time utilities for using C headers,'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-ExtUtils-CChecker-license = %{version}-%{release}
Requires: perl-ExtUtils-CChecker-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Fatal)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
ExtUtils::CChecker - configure-time utilities for using C headers,
libraries, or OS features

%package dev
Summary: dev components for the perl-ExtUtils-CChecker package.
Group: Development
Provides: perl-ExtUtils-CChecker-devel = %{version}-%{release}
Requires: perl-ExtUtils-CChecker = %{version}-%{release}

%description dev
dev components for the perl-ExtUtils-CChecker package.


%package license
Summary: license components for the perl-ExtUtils-CChecker package.
Group: Default

%description license
license components for the perl-ExtUtils-CChecker package.


%package perl
Summary: perl components for the perl-ExtUtils-CChecker package.
Group: Default
Requires: perl-ExtUtils-CChecker = %{version}-%{release}

%description perl
perl components for the perl-ExtUtils-CChecker package.


%prep
%setup -q -n ExtUtils-CChecker-0.11
cd %{_builddir}/ExtUtils-CChecker-0.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-ExtUtils-CChecker
cp %{_builddir}/ExtUtils-CChecker-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-ExtUtils-CChecker/67825508da0c86b98557cec241ae7036d3165a11 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/ExtUtils::CChecker.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-ExtUtils-CChecker/67825508da0c86b98557cec241ae7036d3165a11

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
