%define name socketlock 
%define version 0.2
%define release 7

%define libname %_lib%name

Summary: A library wraper for libc's bind() and connect() functions
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://mega.ist.utl.pt/~luis/socketlock/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Servers
Url: http://mega.ist.utl.pt/~luis/socketlock/ 
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
socketlock is a dynamic library that wraps libc's bind() and connect()
functions. Its purpose is to force bad programs to bind to specific IP's 
on multihomed machines. Both listening sockets and outbound sockets are
supported.

The idea was taken from a similar tool called socketbind. There were serious
problems and lack of features, so this I written this new tool.

To use it simply run:

export LD_PRELOAD=libsocketlock.so
export BINDTO=<ipaddress>

<start program>

%package -n %libname
Group: System/Servers
Summary: A library wraper for libc's bind() and connect() functions
Provides: %name = %version-%release

%description -n %libname
socketlock is a dynamic library that wraps libc's bind() and connect()
functions. Its purpose is to force bad programs to bind to specific IP's 
on multihomed machines. Both listening sockets and outbound sockets are
supported.

The idea was taken from a similar tool called socketbind. There were serious
problems and lack of features, so this I written this new tool.

To use it simply run:

export LD_PRELOAD=%_libdir/libsocketlock.so
export BINDTO=<ipaddress>

<start program>

%prep
%setup -q

%build
gcc $RPM_OPT_FLAGS -c -rdynamic -fPIC socketlock.c
gcc $RPM_OPT_FLAGS -shared -rdynamic -fPIC -ldl socketlock.o -o libsocketlock.so
# strip libsocketlock.so 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_libdir
install -m 755 libsocketlock.so %buildroot%_libdir/libsocketlock.so

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%doc TODO README.txt
%_libdir/libsocketlock.so




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.2-6mdv2010.0
+ Revision: 433985
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2-5mdv2009.0
+ Revision: 260874
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2-4mdv2009.0
+ Revision: 252722
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.2-2mdv2008.1
+ Revision: 140829
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 16:44:39 (54898)
- rebuild

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 16:43:46 (54897)
Import socketlock

* Fri May 13 2005 Olivier Thauvin <nanardon@mandriva.org> 0.2-1mdk
- 0.2

* Sat Dec 13 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.1-1mdk
- 1mdk spec

