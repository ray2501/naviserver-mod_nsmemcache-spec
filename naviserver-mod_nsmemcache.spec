#
# spec file for package naviserver nsmemcache module
#

Summary:        NaviServer nsmemcache module
Name:           naviserver-mod_nsmemcache
Version:        0.1
Release:        0
License:        MPL-1.1
Group:          Productivity/Networking/Web/Servers
Url:            http://bitbucket.org/naviserver/nsmemcache
BuildRequires:  make
BuildRequires:  naviserver
BuildRequires:  naviserver-devel
Requires:       naviserver
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is NaviServer module that implements client protocol to communicate with
memcached server.

%prep
%setup -q %{name}-%{version}

%build
make NAVISERVER=/var/lib/naviserver

%install
mkdir -p %buildroot/var/lib/naviserver/bin
make DESTDIR=%buildroot install NAVISERVER=/var/lib/naviserver

%clean
rm -rf %buildroot

%post -n naviserver-mod_nsmemcache
/sbin/ldconfig

%postun -n naviserver-mod_nsmemcache
/sbin/ldconfig

%files
%defattr(-,nsadmin,nsadmin,-)
/var/lib/naviserver/bin/nsmemcache.so

%changelog

