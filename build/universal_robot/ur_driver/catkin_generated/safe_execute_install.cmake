execute_process(COMMAND "/home/saisriteja/htic_spine_surgery_robotics/build/universal_robot/ur_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/saisriteja/htic_spine_surgery_robotics/build/universal_robot/ur_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
