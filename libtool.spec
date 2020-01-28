# To Build:
#
# sudo yum -y install rpmdevtools m4 && rpmdev-setuptree
# wget https://raw.github.com/nmilford/rpm-libtool/master/libtool.spec -O ~/rpmbuild/SPECS/libtool.spec
# wget http://ftp.gnu.org/gnu/libtool/libtool-2.4.6.tar.gz -O  ~/rpmbuild/SOURCES/libtool-2.4.6.tar.gz
# rpmbuild -bb ~/rpmbuild/SPECS/libtool.spec

Name:       libtool
Version:    2.4.6
Release:    1
Summary:    The GNU libtool, which simplifies the use of shared libraries
Group:      Development/Tools
License:    GNU GPL
URL:        http://www.gnu.org/software/libtool/
Source0:    http://ftp.gnu.org/gnu/libtool/libtool-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gcc 
Requires:   gcc

%description
The libtool package contains the GNU libtool, a set of shell scripts which
automatically configure UNIX and UNIX-like architectures to generically build
shared libraries.  Libtool provides a consistent, portable interface which
simplifies the process of using shared libraries.

%package -n libtool-ltdl
Summary:    Shared library files for %{name}
Group:      Development/Libraries

%description -n libtool-ltdl
Shared library files for libtool DLL library from the libtool package.

%package -n libtool-ltdl-devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   libtool-ltdl = %{version}-%{release}

%description -n libtool-ltdl-devel
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

%post -n libtool-ltdl -p /sbin/ldconfig
%postun -n libtool-ltdl -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/libtool
%{_bindir}/libtoolize
%dir %{_datadir}/libtool/
%{_datadir}/aclocal/libtool.m4
%{_datadir}/aclocal/ltoptions.m4
%{_datadir}/aclocal/ltsugar.m4
%{_datadir}/aclocal/ltversion.m4
%{_datadir}/aclocal/lt~obsolete.m4
%{_infodir}/%{name}.info*
%{_mandir}/man1/libtool.1.gz
%{_mandir}/man1/libtoolize.1.gz
%doc AUTHORS COPYING
%exclude %{_datadir}/info/dir

%files -n libtool-ltdl
%defattr(-,root,root)
%dir %{_datadir}/libtool/libltdl/
%{_datadir}/libtool/libltdl/*
%{_libdir}/libltdl.so.*
%exclude %{_datadir}/info/dir

%files -n libtool-ltdl-devel
%defattr(-,root,root)
%{_includedir}/ltdl.h
%{_includedir}/libltdl
%{_libdir}/libltdl.a
%{_libdir}/libltdl.la
%{_libdir}/libltdl.so
%{_datadir}/aclocal/ltdl.m4
%{_datadir}/aclocal/ltargz.m4
%{_datadir}/libtool/build-aux/*
%{_datadir}/libtool/loaders/*
%{_datadir}/libtool/Makefile.*
%{_datadir}/libtool/*.in
%{_datadir}/libtool/*.c
%{_datadir}/libtool/*.h
%{_datadir}/libtool/*.mk
%{_datadir}/libtool/aclocal.m4
%{_datadir}/libtool/configure
%{_datadir}/libtool/configure.ac
%{_datadir}/libtool/README
%{_datadir}/libtool/COPYING.LIB
%doc ChangeLog* NEWS README THANKS TODO doc/PLATFORMS
%exclude %{_datadir}/info/dir

%changelog
* Tue Jan 28 2020 Michael Adams <unquietwiki@gmail.com> 2.4.6-1
- Updated to latest version.
- Re-aligned naming with CentOS packages for upgradability.
* Mon Sep 02 2013 Nathan Milford <nathan@milford.io> 2.4.2-1
- First shot.
