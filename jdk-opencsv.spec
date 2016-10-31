Name     : jdk-opencsv
Version  : 2.3
Release  : 4
URL      : https://repo1.maven.org/maven2/net/sf/opencsv/opencsv/2.3/opencsv-2.3.jar
Source0  : https://repo1.maven.org/maven2/net/sf/opencsv/opencsv/2.3/opencsv-2.3.jar
Source1  : https://repo1.maven.org/maven2/net/sf/opencsv/opencsv/2.3/opencsv-2.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-opencsv-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-opencsv package.
Group: Data

%description data
data components for the jdk-opencsv package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/opencsv.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/opencsv.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/opencsv.xml \
%{buildroot}/usr/share/maven-poms/opencsv.pom \
%{buildroot}/usr/share/java/opencsv.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/opencsv.jar
/usr/share/maven-metadata/opencsv.xml
/usr/share/maven-poms/opencsv.pom
