PKG_NAME := jdk-opencsv
URL := https://repo1.maven.org/maven2/net/sf/opencsv/opencsv/2.3/opencsv-2.3.jar
ARCHIVES := https://repo1.maven.org/maven2/net/sf/opencsv/opencsv/2.3/opencsv-2.3.pom %{buildroot}

include ../common/Makefile.common
