# Install script for directory: /home/saisriteja/htic_spine_surgery_robotics/src/staubli/staubli_rx160_support

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/saisriteja/htic_spine_surgery_robotics/build/staubli/staubli_rx160_support/catkin_generated/installspace/staubli_rx160_support.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/staubli_rx160_support/cmake" TYPE FILE FILES
    "/home/saisriteja/htic_spine_surgery_robotics/build/staubli/staubli_rx160_support/catkin_generated/installspace/staubli_rx160_supportConfig.cmake"
    "/home/saisriteja/htic_spine_surgery_robotics/build/staubli/staubli_rx160_support/catkin_generated/installspace/staubli_rx160_supportConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/staubli_rx160_support" TYPE FILE FILES "/home/saisriteja/htic_spine_surgery_robotics/src/staubli/staubli_rx160_support/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/staubli_rx160_support/config" TYPE DIRECTORY FILES "/home/saisriteja/htic_spine_surgery_robotics/src/staubli/staubli_rx160_support/config/")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/staubli_rx160_support/launch" TYPE DIRECTORY FILES "/home/saisriteja/htic_spine_surgery_robotics/src/staubli/staubli_rx160_support/launch/")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/staubli_rx160_support/meshes" TYPE DIRECTORY FILES "/home/saisriteja/htic_spine_surgery_robotics/src/staubli/staubli_rx160_support/meshes/")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/staubli_rx160_support/urdf" TYPE DIRECTORY FILES "/home/saisriteja/htic_spine_surgery_robotics/src/staubli/staubli_rx160_support/urdf/")
endif()

