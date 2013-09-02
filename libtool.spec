# To Build:
#
# sudo yum -y install rpmdevtools m4 && rpmdev-setuptree
# wget https://raw.github.com/nmilford/rpm-libtool/master/libtool.spec -O ~/rpmbuild/SPECS/libtool.spec
# wget http://ftp.gnu.org/gnu/libtool/libtool-2.4.2.tar.gz -O  ~/rpmbuild/SOURCES/libtool-2.4.2.tar.gz
# rpmbuild -bb ~/rpmbuild/SPECS/libtool.spec

Name:       libtool
Version:    2.4.2
Release:    1
Summary:    The GNU libtool, which simplifies the use of shared libraries
Group:      Development/Tools
License:    GNU GPL
URL:        http://www.gnu.org/software/libtool/
Source0:    http://ftp.gnu.org/gnu/libtool//libtool-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gcc 
Requires:   gcc

%description
The libtool package contains the GNU libtool, a set of shell scripts which
automatically configure UNIX and UNIX-like architectures to generically build
shared libraries.  Libtool provides a consistent, portable interface which
simplifies the process of using shared libraries.

%package -n libltdl
Summary:    Shared library files for %{name}
Group:      Development/Libraries

%description -n libltdl
Shared library files for libtool DLL library from the libtool package.

%package -n libltdl-devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   libltdl = %{version}-%{release}

%description -n libltdl-devel
This package contains static libraries and header files need for development.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"
%makeinstall

%clean
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

%post
%install_info %{name}.info

%preun
%uninstall_info %{name}.info

%post -n libltdl -p /sbin/ldconfig
%postun -n libltdl -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/libtool
%{_bindir}/libtoolize
%dir %{_datadir}/libtool/
%dir %{_datadir}/libtool/config
%{_datadir}/libtool/config/compile
%{_datadir}/libtool/config/config.guess
%{_datadir}/libtool/config/config.sub
%{_datadir}/libtool/config/depcomp
%{_datadir}/libtool/config/install-sh
%{_datadir}/libtool/config/ltmain.sh
%{_datadir}/libtool/config/missing
%{_datadir}/aclocal/argz.m4
%{_datadir}/aclocal/libtool.m4
%{_datadir}/aclocal/ltoptions.m4
%{_datadir}/aclocal/ltsugar.m4
%{_datadir}/aclocal/ltversion.m4
%{_datadir}/aclocal/lt~obsolete.m4
%{_infodir}/%{name}.info*
%{_mandir}/man1/libtool.1.gz
%{_mandir}/man1/libtoolize.1.gz
%doc AUTHORS COPYING

%files -n libltdl
%defattr(-,root,root)
%dir %{_datadir}/libtool/libltdl/
%{_datadir}/libtool/libltdl/*
%{_libdir}/libltdl.so.*

%files -n libltdl-devel
%defattr(-,root,root)
%{_includedir}/ltdl.h
%{_includedir}/libltdl
%{_libdir}/libltdl.a
%{_libdir}/libltdl.la
%{_libdir}/libltdl.so
%{_datadir}/aclocal/ltdl.m4
%doc ChangeLog* NEWS README THANKS TODO doc/PLATFORMS

%changelog
* Mon Sep 02 2013 Nathan Milford <nathan@milford.io> 2.4.2-1
- First shot.