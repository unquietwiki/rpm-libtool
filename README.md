rpm-libtool
===========

An RPM spec file to build and install libtool.

To Build:

`sudo yum -y install rpmdevtools m4 && rpmdev-setuptree`

`wget https://raw.github.com/nmilford/rpm-libtool/master/libtool.spec -O ~/rpmbuild/SPECS/libtool.spec`

`wget http://ftp.gnu.org/gnu/libtool/libtool-2.4.2.tar.gz -O  ~/rpmbuild/SOURCES/libtool-2.4.2.tar.gz`

`rpmbuild -bb ~/rpmbuild/SPECS/libtool.spec`