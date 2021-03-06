%define		_status		stable
%define		_pearname	MDB
Summary:	%{_pearname} - unified database API
Summary(pl.UTF-8):	%{_pearname} - zunifikowane API baz danych
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	8
Epoch:		1
License:	BSD style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a5601b6d45ffede24647cd69cf425b85
URL:		http://pear.php.net/package/MDB/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.0-0.b1
Requires:	php-pear-XML_Parser
Obsoletes:	php-pear-MDB-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MDB is a merge of PEAR's DB and Metabases that provides a unified DB
API. It also provides methods for DB portability and DB feature
emulation. Most notably it features a DB independent XML-Schema
manager.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
MDB to połączenie PEAR DB i Metabases, które daje ujednolicone API do
baz danych. Zawiera także metody zapewniające przenośność i emulację
właściwości dla baz danych. Najważniejsza cecha to niezależny od bazy
danych zarządca schematów XML.

Ta klasa ma w PEAR status: %{_status}.

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
%dir %{php_pear_dir}/MDB
%dir %{php_pear_dir}/MDB/Modules
%dir %{php_pear_dir}/MDB/Modules/Manager
%{php_pear_dir}/*.php
%{php_pear_dir}/MDB/*.php
%{php_pear_dir}/MDB/Modules/*.php
%{php_pear_dir}/MDB/Modules/Manager/*.php
