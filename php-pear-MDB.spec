%include	/usr/lib/rpm/macros.php
%define		_class		MDB
%define		_pearname	%{_class}
%define		_status		stable

Summary:	%{_pearname} - unified database API
Summary(pl):	%{_pearname} - zunifikowane API baz danych
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	2.2
Epoch:		1
License:	BSD style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a5601b6d45ffede24647cd69cf425b85
URL:		http://pear.php.net/package/MDB/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MDB is a merge of PEAR's DB and Metabases that provides a unified DB
API. It also provides methods for DB portability and DB feature
emulation. Most notably it features a DB independent XML-Schema
manager.

In PEAR status of this package is: %{_status}.

%description -l pl
MDB to po³±czenie PEAR DB i Metabases, które daje ujednolicone API do
baz danych. Zawiera tak¿e metody zapewniaj±ce przeno¶no¶æ i emulacjê
w³a¶ciwo¶ci dla baz danych. Najwa¿niejsza cecha to niezale¿ny od bazy
danych zarz±dca schematów XML.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{name}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%prep
%pear_package_setup
 
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/{MAINTAINERS,README,TODO,doc/}
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Modules
%dir %{php_pear_dir}/%{_class}/Modules/Manager
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Modules/*.php
%{php_pear_dir}/%{_class}/Modules/Manager/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
