Name:           libspiro
Version:        20150131
Release:        8%{?dist}
Summary:        Library to simplify the drawing of beautiful curves

# The files that are used to compile this library are all in GPLv3+
# https://github.com/fontforge/libspiro/issues/8
License:        GPLv3+
URL:            https://github.com/fontforge/libspiro/
Source0:        https://github.com/fontforge/libspiro/archive/0.3.20150131.tar.gz
BuildRequires: automake autoconf libtool

%description
This library will take an array of spiro control points and 
convert them into a series of bézier splines which can then 
be used in the myriad of ways the world has come to use béziers. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n libspiro-0.3.20150131

%build
autoreconf -i
automake --foreign -Wall
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc README* ChangeLog AUTHORS
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libspiro.pc

%changelog
* Mon Jul 09 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 20150131-8
- Correct the License to GPLv3+

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150131-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150131-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150131-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150131-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150131-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150131-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 01 2015 Kevin Fenzi <kevin@scrye.com> 20150131-1
- Update to 20150131

* Mon Dec 08 2014 Nils Philippsen <nils@redhat.com> - 20130930-4
- explicitly link against libm

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130930-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130930-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 02 2013 Kevin Fenzi <kevin@scrye.com> 20130930-1
- Update to 20130930 version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Kevin Fenzi <kevin@scrye.com> 20071029-10
- Add patch to add aarch64 support. Fixes bug #925890

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Parag <paragn AT fedoraproject DOT org> - 20071029-8
- Resolves:rh#879153 - spec cleanup for recent packaging guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 20071029-6
- rebuild for gcc 4.7

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 15 2009 Parag <paragn AT fedoraproject.org> - 20071029-4
- Fix rpmlint error "libspiro.src:53: E: files-attr-not-set"

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Kevin Fenzi <kevin@tummy.com> - 20071029-1
- Initial version for Fedora
