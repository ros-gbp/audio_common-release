%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-audio-capture
Version:        0.3.11
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS audio_capture package

License:        BSD
URL:            http://ros.org/wiki/audio_capture
Source0:        %{name}-%{version}.tar.gz

Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-ugly
Requires:       ros-noetic-audio-common-msgs
Requires:       ros-noetic-roscpp
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  ros-noetic-audio-common-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-roscpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Transports audio from a source to a destination. Audio sources can come from a
microphone or file. The destination can play the audio or save it to an mp3
file.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Apr 08 2021 Austin Hendrix <namniart@gmail.com> - 0.3.11-1
- Autogenerated by Bloom

* Thu Jan 07 2021 Austin Hendrix <namniart@gmail.com> - 0.3.10-1
- Autogenerated by Bloom

* Thu Oct 22 2020 Austin Hendrix <namniart@gmail.com> - 0.3.9-1
- Autogenerated by Bloom

* Sun Sep 13 2020 Austin Hendrix <namniart@gmail.com> - 0.3.8-1
- Autogenerated by Bloom

* Sat Aug 08 2020 Austin Hendrix <namniart@gmail.com> - 0.3.7-1
- Autogenerated by Bloom

* Fri May 29 2020 Austin Hendrix <namniart@gmail.com> - 0.3.6-1
- Autogenerated by Bloom

* Tue Apr 28 2020 Austin Hendrix <namniart@gmail.com> - 0.3.5-1
- Autogenerated by Bloom

