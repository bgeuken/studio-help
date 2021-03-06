#
# spec file for package 
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           studio-help
Version:        1.2.70
Release:        1.0
License:        GFDL
Summary:        SUSE Studio documentation
Url:            https://github.com/susestudio/studio-help
Group:          Documentation/HTML
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  rubygem-bundler, apache2, fdupes
Requires:       apache2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is the content of the SUSE Studio Online documentation.

%prep
%setup -q

%build
bundle install --deployment
mkdir -p html
bundle exec ./do_create html

%install
mkdir -p %{buildroot}/srv/studio-help
cp -r html %{buildroot}/srv/studio-help
mkdir -p %{buildroot}/etc/apache2/vhosts.d/
cp studio-help.conf.example %{buildroot}/etc/apache2/vhosts.d/
%fdupes -s %{buildroot}/srv/studio-help

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%config /etc/apache2/vhosts.d/studio-help.conf.example
/srv/studio-help

%changelog

