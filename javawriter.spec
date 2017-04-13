%{?scl:%scl_package javawriter}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 1

Name:          %{?scl_prefix}javawriter
Version:       2.5.1
Release:       3.%{baserelease}%{?dist}
Summary:       A Java API for generating .java source files
License:       ASL 2.0
URL:           https://github.com/square/javapoet
Source0:       https://github.com/square/javapoet/archive/%{pkg_name}-%{version}.tar.gz

BuildRequires: %{?scl_prefix_maven}maven-local
BuildRequires: %{?scl_prefix_maven}mvn(org.sonatype.oss:oss-parent:pom:)

%if 0
# Test deps
BuildRequires: %{?scl_prefix_java_common}mvn(junit:junit)
# Unavailable test deps
BuildRequires: mvn(org.easytesting:fest-assert-core:2.0M8)
%endif

BuildArch:     noarch

%description
A utility class which aids in generating Java source files.

%package javadoc
Summary:       Javadoc for %{pkg_name}

%description javadoc
This package contains javadoc for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -q -n javapoet-%{pkg_name}-%{version}

%pom_xpath_remove "pom:dependency[pom:scope = 'test']" 

%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file : %{pkg_name}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x

# Unavailable test deps: org.easytesting:fest-assert-core:2.0M8
%mvn_build -f
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc CHANGELOG.md CONTRIBUTING.md README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Jan 19 2017 Mat Booth <mat.booth@redhat.com> - 2.5.1-3.1
- Auto SCL-ise package for rh-eclipse46 collection

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 gil cattaneo <puntogil@libero.it> 2.5.1-1
- initial rpm