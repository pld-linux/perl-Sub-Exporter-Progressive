#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Sub
%define		pnam	Exporter-Progressive
Summary:	Sub::Exporter::Progressive - Only use Sub::Exporter if you need it
Summary(pl.UTF-8):	Sub::Exporter::Progressive - użycie Sub::Exporter tylko w razie potrzeby
Name:		perl-Sub-Exporter-Progressive
Version:	0.001013
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sub/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	72cf6acdd2a0a8b105821a4db98e4ebe
URL:		https://metacpan.org/release/Sub-Exporter-Progressive
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sub::Exporter is an incredibly powerful module, but with that power
comes great responsibility, er- as well as some runtime penalties.
This module is a Sub::Exporter wrapper that will let your users just
use Exporter if all they are doing is picking exports, but use
Sub::Exporter if your users try to use Sub::Exporter's more advanced
features features, like renaming exports, if they try to use them.

Note that this module will export @EXPORT, @EXPORT_OK and
%EXPORT_TAGS package variables for Exporter to work.  Additionally, if
your package uses advanced Sub::Exporter features like currying, this module
will only ever use Sub::Exporter, so you might as well use it directly.

%description -l pl.UTF-8
Sub::Exporter to zaskakująco potężny moduł, ale wraz z mocą wiąże się
odpowiedzialność - tzn. pewne narzuty w czasie działania. Niniejszy
moduł obudowuje Sub::Exporter w ten sposób, że użyje modułu Exporter
do samego pobierania eksportów, ale modułu Sub::Exporter w przypadku
próby użycia bardziej zaawansowanych możliwości, takich jak zmiana
nazw eksportów.

Uwaga: ten moduł eksportuje zmienne pakietu @EXPORT, @EXPORT_OK oraz
%EXPORT_TAGS, aby mógł działać Exporter. Ponadto, jeśli używający go
pakiet wykorzystuje zaawansowane możliwości modułu Sub::Exporter,
takie jak curry, ten moduł będzie używał wyłącznie modułu
Sub::Exporter, więc równie dobrze można używać go bezpośrednio.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sub/Exporter/Progressive.pm
%{_mandir}/man3/Sub::Exporter::Progressive.3pm*
