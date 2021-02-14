# Install script for directory: /home/saisriteja/htic_spine_surgery_robotics/src/staubli/staubli_rx160_moveit_plugins

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/saisriteja/htic_spine_surgery_robotics/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/saisriteja/htic_spine_surgery_robotics/build/staubli/staubli_rx160_moveit_plugins/catkin_generated/installspace/staubli_rx160_moveit_plugins.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/staubli_rx160_moveit_plugins/cmake" TYPE FILE FILES
    "/home/saisriteja/htic_spine_surgery_robotics/build/staubli/staubli_rx160_moveit_plugins/catkin_generated/installspace/staubli_rx160_moveit_pluginsConfig.cmake"
    "/home/saisriteja/htic_spine_surgery_robotics/build/staubli/staubli_rx160_moveit_plugins/catkin_generated/installspace/staubli_rx160_moveit_pluginsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/staubli_rx160_moveit_plugins" TYPE FILE FILES "/home/saisriteja/htic_spine_surgery_robotics/src/staubli/staubli_rx160_moveit_plugins/package.xml")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/saisriteja/htic_spine_surgery_robotics/build/staubli/staubli_rx160_moveit_plugins/rx160_kinematics/cmake_install.cmake")

endif()

