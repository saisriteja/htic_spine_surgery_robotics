# htic_spine_surgery_robotics




# Simulation of UR5

## Using GUI 
The following lines of code can bring up the Gazebo, Rviz with ur5 bot in it.

```
roslaunch ur_gazebo ur5.launch limited:=true
roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true limited:=true
roslaunch ur5_moveit_config moveit_rviz.launch config:=true
```

for more information regarding the UR5 and simualtions go to [UR_ROS_tutorial](http://wiki.ros.org/universal_robot/Tutorials/Getting%20Started%20with%20a%20Universal%20Robot%20and%20ROS-Industrial), [Universal_robot_github](https://github.com/ros-industrial/universal_robot) 


#### demo

[![UR5 using GUI](images/ur5_rviz_gazebo.png)](https://vimeo.com/512432352 "UR5 using GUI - Click to Watch!")



# Simulation of Staubli RX160
The following lines of code can bring up the Gazebo, Rviz with ur5 bot in it.

```
roslaunch stuabli_rx160_moveit_config demo_gazebo.launch
```

I had made changes for the moveit_config file, since there is no gazebo launch files prewittern in the original staubli repository.

Note1: If you want to make you own changes for the moveit_config file from strach then follow this [tutorial](https://www.youtube.com/watch?v=O7nBa7mnfW4), [github](https://github.com/lFatality/ros_moveit_gazebo_ws) (even the video is in Malayalam you can understand the sequence of step in a perfect way).


#### demo

[![Staubli using GUI](images/staubli_rviz_gazebo.png)](https://vimeo.com/512432400 "staubli using GUI - Click to Watch!")


# Simulation of Intel RealSense depth camera D435
The following lines of code can bring up the Gazebo, Rviz with realsense camera in it. 

```
roslaunch realsense2_description view_d435_model_rviz_gazebo.launch
```


Note1: you need to add the 3d objects in the gazebo which are available on top of the menu bar. In rviz you can see the depth and the camera perception.

Note2:  The gazebo plugin is readily available with the [IntelRealSense](https://github.com/IntelRealSense/realsense-ros) repo. So this took to me another [repo](https://github.com/pal-robotics/realsense_gazebo_plugin) by pal robotics. However for the complete setup I have been following the this [tutorial](https://www.youtube.com/watch?v=hpUCG6K5muI), [modified_realsense_description2](https://github.com/issaiass/realsense2_description), [gazebo_plugin](https://github.com/issaiass/realsense_gazebo_plugin). I could tell that the last 2 repositories would be enough to simulate the necessary stuff.


#### demo

[![Intel RealSense](images/realsense_rviz_gazebo.png)](https://vimeo.com/512432308 "Intel RealSense D435 - Click to Watch!")











