%include	/usr/lib/rpm/macros.php
%define		_class		MDB
%define		_pearname	%{_class}
%define		_status		stable
Summary:	%{_pearname} - unified database API
Summary(pl):	%{_pearname} - zunifikowane API baz danych
Name:		php-pear-%{_pearname}
Version:	1.1.3
Release:	1
Epoch:		1
License:	BSD style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	36e989e08b512e3dbb91a915ee03174c
URL:		http://pear.php.net/package/MDB/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MDB is a merge of PEAR's DB and Metabases that provides a unified DB
API. It also provides methods for DB portability and DB feature
emulation. Most notably it features a DB independent XML-Schema
manager.

This class has in PEAR status: %{_status}.

%description -l pl
MDB to po³±czenie PEAR DB i Metabases, które daje ujednolicone API do
baz danych. Zawiera tak¿e metody zapewniaj±ce przeno¶no¶æ i emulacjê
w³a¶ciwo¶ci dla baz danych. Najwa¿niejsza cecha to niezale¿ny od bazy
danych zarz±dca schematów XML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{,Modules/{,Manager}}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/
install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/%{_class}/Modules/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Modules/
install %{_pearname}-%{version}/%{_class}/Modules/Manager/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Modules/Manager/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Modules
%dir %{php_pear_dir}/%{_class}/Modules/Manager
%doc %{_pearname}-%{version}/{MAINTAINERS,README,TODO,doc/,tests/}
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Modules/*.php
%{php_pear_dir}/%{_class}/Modules/Manager/*.php
