%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rmf-traffic-ros2
Version:        2.3.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rmf_traffic_ros2 package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       json-devel
Requires:       libuuid-devel
Requires:       proj-devel
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rmf-building-map-msgs
Requires:       ros-rolling-rmf-fleet-msgs
Requires:       ros-rolling-rmf-site-map-msgs
Requires:       ros-rolling-rmf-traffic
Requires:       ros-rolling-rmf-traffic-msgs
Requires:       ros-rolling-rmf-utils
Requires:       yaml-cpp-devel
Requires:       zlib-devel
Requires:       ros-rolling-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  json-devel
BuildRequires:  libuuid-devel
BuildRequires:  proj-devel
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rmf-building-map-msgs
BuildRequires:  ros-rolling-rmf-fleet-msgs
BuildRequires:  ros-rolling-rmf-site-map-msgs
BuildRequires:  ros-rolling-rmf-traffic
BuildRequires:  ros-rolling-rmf-traffic-msgs
BuildRequires:  ros-rolling-rmf-utils
BuildRequires:  yaml-cpp-devel
BuildRequires:  zlib-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-cmake-catch2
BuildRequires:  ros-rolling-ament-cmake-uncrustify
%endif

%description
A package containing messages used by the RMF traffic management system.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Mon Aug 28 2023 Grey <grey@openrobotics.org> - 2.3.2-1
- Autogenerated by Bloom

* Thu Aug 10 2023 Grey <grey@openrobotics.org> - 2.3.1-1
- Autogenerated by Bloom

* Thu Jun 08 2023 Grey <grey@openrobotics.org> - 2.3.0-1
- Autogenerated by Bloom

* Sun May 21 2023 Grey <grey@openrobotics.org> - 2.1.5-1
- Autogenerated by Bloom

* Fri May 19 2023 Grey <grey@openrobotics.org> - 2.1.4-1
- Autogenerated by Bloom

* Wed Apr 26 2023 Grey <grey@openrobotics.org> - 2.1.3-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Grey <grey@openrobotics.org> - 2.1.2-2
- Autogenerated by Bloom

