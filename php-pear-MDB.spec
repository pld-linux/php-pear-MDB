%include	/usr/lib/rpm/macros.php
%define		_class		MDB
%define		_pearname	%{_class}
Summary:	%{_class} - Unified Database API
Summary(pl):	%{_class} - Zunifikowane API baz danych
Name:		php-pear-%{_pearname}
Version:	0.9.8
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Patch0:		%{name}-location.patch
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MDB is a merge of PEAR's DB and Metabases that provides a unified DB
API. It also provides methods for DB portability and DB feature
emulation. Most notably it features a DB independent XML-Schema
manager.

%description -l pl
MDB to po³±czenie PEAR DB i Metabases, które daje ujednolicone API do
baz danych. Zawiera tak¿e metody zapewniaj±ce przeno¶no¶æ i emulacjê
w³a¶ciwo¶ci dla baz danych. Najwa¿niejsza cecha to niezale¿ny od bazy
danych menad¿er schematów XML.

%prep
%setup -q -c
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%doc %{_pearname}-%{version}/*.{txt,schema}
%{php_pear_dir}/%{_class}/*.php
