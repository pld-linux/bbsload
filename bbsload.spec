Summary:	A system load mozitor designed for blackbox
Summary(pl):	Monitor obci±¿enia systemu zaprojektowany dla blackboksa
Name:		bbsload
Version:	0.2.5
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-sysconfdir.patch
URL:		http://bbtools.windsofstorm.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
bbsload monitors system, and memory load.
It is highly integrated with blackbox window manager (can use it's theme
settings), but can work also with other WM.

%description -l pl
bbsload monitoruje obci±¿enie systemu i zajêto¶æ pamiêci.
Jest zintegrowany z blackboxem (u¿ywa jego ustawieñ wygl±du), aczkolwiek
mo¿e te¿ pracowaæ z innym zarz±d± okien.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c -f
%configure
%{__make} CXX="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf BUGS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/bb*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bbtools/%{name}.*
