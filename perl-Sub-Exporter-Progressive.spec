#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Sub
%define		pnam	Exporter-Progressive
%include	/usr/lib/rpm/macros.perl
Summary:	Sub::Exporter::Progressive - Only use Sub::Exporter if you need it
Name:		perl-Sub-Exporter-Progressive
Version:	0.001010
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sub/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0350d9e12549112ae1f618cbff3ecbd9
URL:		http://search.cpan.org/dist/Sub-Exporter-Progressive/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sub::Exporter is an incredibly powerful module, but with that power comes
great responsibility, er- as well as some runtime penalties.  This module
is a Sub::Exporter wrapper that will let your users just use Exporter
if all they are doing is picking exports, but use Sub::Exporter if your
users try to use Sub::Exporter's more advanced features features, like
renaming exports, if they try to use them.

Note that this module will export @EXPORT, @EXPORT_OK and
%EXPORT_TAGS package variables for Exporter to work.  Additionally, if
your package uses advanced Sub::Exporter features like currying, this module
will only ever use Sub::Exporter, so you might as well use it directly.

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
%{perl_vendorlib}/Sub/Exporter/*.pm
%{_mandir}/man3/*
