%define name socketlock 
%define version 0.2
%define release %mkrel 4

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


