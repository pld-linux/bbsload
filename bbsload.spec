Summary:	A system load mozitor designed for blackbox
Summary(pl.UTF-8):	Monitor obciążenia systemu zaprojektowany dla blackboksa
Name:		bbsload
Version:	0.2.8
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
# Source0-md5:	beef63c4a4cefaad5d02ffd7e133f6ae
Patch0:		%{name}-sysconfdir.patch
URL:		http://bbtools.windsofstorm.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bbsload monitors system, and memory load.
It is highly integrated with blackbox window manager (can use it's theme
settings), but can work also with other WM.

%description -l pl.UTF-8
bbsload monitoruje obciążenie systemu i zajętość pamięci.
Jest zintegrowany z blackboxem (używa jego ustawień wyglądu), aczkolwiek
może też pracować z innym zarządcą okien.

%prep
%setup -q
%patch -P0 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README TODO
%attr(755,root,root) %{_bindir}/bb*
%dir %{_sysconfdir}/bbtools
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bbtools/%{name}.*
