Summary: Service Management Tools
Name: sm-tools
Version: 1.0
Release: %{tis_patch_ver}%{?_tis_dist}
License: Apache-2.0
Group: base
Packager: Wind River <info@windriver.com>
URL: unknown
Source0: %{name}-%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: python
BuildRequires: python-setuptools
BuildRequires: python2-pip
BuildRequires: python2-wheel
Requires: python-libs

%prep
%setup -q

%build
%{__python2} setup.py build
%py2_build_wheel

%install
%global _buildsubdir %{_builddir}/%{name}-%{version}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
mkdir -p $RPM_BUILD_ROOT/wheels
install -m 644 dist/*.whl $RPM_BUILD_ROOT/wheels/

%description
Service Management Tools

#%package -n sm-tools-py-src-tar
#Summary: Service Management Tools source tarball 
#Group: base

#%description -n sm-tools-py-src-tar
#Service Management Tools source tarball 


#%post -n sm-tools-py-src-tar
## sm-tools-py-src-tar - postinst
#	if [ -f $D/usr/src/sm-tools-1.0.tar.bz2 ] ; then
#		( cd $D/ && tar -xf $D/usr/src/sm-tools-1.0.tar.bz2 )
#	fi


%files
%defattr(-,root,root,-)
%dir "/usr/lib/python2.7/site-packages/sm_tools"
/usr/lib/python2.7/site-packages/sm_tools/*
%dir "/usr/lib/python2.7/site-packages/sm_tools-1.0.0-py2.7.egg-info"
/usr/lib/python2.7/site-packages/sm_tools-1.0.0-py2.7.egg-info/*
/usr/bin/*

#%files -n sm-tools-py-src-tar
#%defattr(-,-,-,-)
#"/usr/src/sm-tools-1.0.tar.bz2"

%package wheels
Summary: %{name} wheels

%description wheels
Contains python wheels for %{name}

%files wheels
/wheels/*
