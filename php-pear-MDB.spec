%include	/usr/lib/rpm/macros.php
%define		_class		MDB
%define		_pearname	%{_class}
Summary:	%{_pearname} - unified database API
Summary(pl):	%{_pearname} - zunifikowane API baz danych
Name:		php-pear-%{_pearname}
Version:	1.1.2
Release:	1
Epoch:		1
License:	BSD style
Group:		Development/Languages/PHP
# Source0-md5:	09dc12461a29cb2864f7ed4b43c9090b
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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
danych zarz±dca schematów XML.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

rm $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/*test.php
rm $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Var_Dump.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%doc %{_pearname}-%{version}/{*.{txt,schema,html,xsl},*test.php,Var_Dump.php}
%{php_pear_dir}/%{_class}/*.php
