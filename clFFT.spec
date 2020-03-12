#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clFFT
Version  : 2.12.2
Release  : 2
URL      : https://github.com/clMathLibraries/clFFT/archive/v2.12.2.tar.gz
Source0  : https://github.com/clMathLibraries/clFFT/archive/v2.12.2.tar.gz
Summary  : Open source OpenCL FFT library
Group    : Development/Tools
License  : Apache-2.0
Requires: clFFT-data = %{version}-%{release}
Requires: clFFT-lib = %{version}-%{release}
Requires: clFFT-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : ocl-icd
BuildRequires : ocl-icd-dev
BuildRequires : opencl-headers-dev

%description
﻿## Build Status
| Build branch | master | develop |
|-----|-----|-----|
| GCC/Clang x64 | [![Build Status](https://travis-ci.org/clMathLibraries/clFFT.svg?branch=master)](https://travis-ci.org/clMathLibraries/clFFT/branches) | [![Build Status](https://travis-ci.org/clMathLibraries/clFFT.svg?branch=develop)](https://travis-ci.org/clMathLibraries/clFFT/branches) |
| Visual Studio x64 |  |[![Build status](https://ci.appveyor.com/api/projects/status/facii32v72y98opv/branch/develop?svg=true)](https://ci.appveyor.com/project/kknox/clfft-whc3m/branch/develop) |

%package data
Summary: data components for the clFFT package.
Group: Data

%description data
data components for the clFFT package.


%package dev
Summary: dev components for the clFFT package.
Group: Development
Requires: clFFT-lib = %{version}-%{release}
Requires: clFFT-data = %{version}-%{release}
Provides: clFFT-devel = %{version}-%{release}
Requires: clFFT = %{version}-%{release}

%description dev
dev components for the clFFT package.


%package lib
Summary: lib components for the clFFT package.
Group: Libraries
Requires: clFFT-data = %{version}-%{release}
Requires: clFFT-license = %{version}-%{release}

%description lib
lib components for the clFFT package.


%package license
Summary: license components for the clFFT package.
Group: Default

%description license
license components for the clFFT package.


%prep
%setup -q -n clFFT-2.12.2
cd %{_builddir}/clFFT-2.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581452760
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ../src/
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581452760
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clFFT
cp %{_builddir}/clFFT-2.12.2/LICENSE %{buildroot}/usr/share/package-licenses/clFFT/2b8b815229aa8a61e483fb4ba0588b8b6c491890
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/clFFT/examples/fft1d
/usr/share/clFFT/examples/fft1d.c
/usr/share/clFFT/examples/fft2d
/usr/share/clFFT/examples/fft2d.c
/usr/share/clFFT/examples/fft3d
/usr/share/clFFT/examples/fft3d.c

%files dev
%defattr(-,root,root,-)
/usr/include/clAmdFft.h
/usr/include/clAmdFft.version.h
/usr/include/clFFT.h
/usr/include/clFFT.version.h
/usr/lib64/cmake/clFFT/clFFTConfig.cmake
/usr/lib64/cmake/clFFT/clFFTConfigVersion.cmake
/usr/lib64/cmake/clFFT/clFFTTargets-relwithdebinfo.cmake
/usr/lib64/cmake/clFFT/clFFTTargets.cmake
/usr/lib64/libStatTimer.so
/usr/lib64/libclFFT.so
/usr/lib64/pkgconfig/clFFT.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libStatTimer.so.2
/usr/lib64/libStatTimer.so.2.12.2
/usr/lib64/libclFFT.so.2
/usr/lib64/libclFFT.so.2.12.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clFFT/2b8b815229aa8a61e483fb4ba0588b8b6c491890
