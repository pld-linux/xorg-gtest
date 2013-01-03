Summary:	X.Org GTest testing environment for Google Test
Summary(pl.UTF-8):	Środowisko testowe X.Org GTest dla szkieletu Google Test
Name:		xorg-gtest
Version:	0.7.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/test/%{name}-%{version}.tar.bz2
# Source0-md5:	c42a25bb8f10816cd283689f7d66460e
Patch0:		%{name}-noserver.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	evemu-devel >= 1.0.10
BuildRequires:	gtest-devel >= 1.6.0-3
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-util-util-macros >= 1.17
Requires:	evemu >= 1.0.10
Requires:	gtest-devel >= 1.6.0-3
Requires:	xorg-xserver-server
Requires:	xorg-driver-video-dummy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.Org GTest provides a Google Test environment for starting and
stopping a X server for testing purposes.

%description -l pl.UTF-8
X.Org GTest udostępnia środowisko Google Test do uruchamiania i
zatrzymywania serwera X do celów testowych.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# this belongs to system gtest
%{__rm} $RPM_BUILD_ROOT%{_includedir}/gtest/{gtest,gtest-spi}.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_includedir}/xorg/gtest
%{_prefix}/src/xorg-gtest
%{_pkgconfigdir}/xorg-gtest.pc
%{_aclocaldir}/xorg-gtest.m4
%dir %{_datadir}/xorg
%{_datadir}/xorg/gtest
%{_datadir}/X11/xorg.conf.d/99-virtual-test-devices.conf
%{_docdir}/xorg-gtest
