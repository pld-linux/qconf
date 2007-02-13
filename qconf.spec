Summary:	qconf - configuring qmake-based project
Summary(pl.UTF-8):	qconf - konfiguracja dla projektów opartych o qmake
Name:		qconf
Version:	1.2
Release:	0.cvs.11072005.1
License:	GPL
Group:		Development/Building
Source0:	%{name}-%{version}.tgz
URL:		http://delta.affinix.com/qconf/
BuildRequires:	QtCore-devel
BuildRequires:	qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QConf allows you to have a nice configure script for your qmake-based
project. It is intended for developers who don't need (or want) to
use the more complex GNU autotools.
      
Scripts generated by QConf are meant for unix. This means it should
only be used with projects based on Qt/X11, Qt/Mac, or Qt/Embedded. No
effort has been made in supporting Qt/Windows based projects (yet).

%description -l pl.UTF-8
QConf umożliwia posiadanie ładnych skryptów configure dla projektów
opartych o qmake. Jest przeznaczony dla programistów nie
potrzebujących (albo nie chcących) używać bardziej złożonych GNU
autotools.

Skrypty generowane przez QConfa są przeznaczone dla uniksów. Oznacza
to, że powinny być używane tylko w projektach opartych na Qt/X11,
Qt/Mac i Qt/Embedded. Nie było żadnych prób obsługiwania projektów
opartych na Qt/Windows (jak na razie).

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--datadir=%{_datadir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/qconf/conf/CVS
rm -rf $RPM_BUILD_ROOT%{_datadir}/qconf/modules/CVS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/qconf
%dir %{_datadir}/qconf/conf
%dir %{_datadir}/qconf/modules
%{_datadir}/qconf/conf/*
%{_datadir}/qconf/modules/*
