# HTIC Spine Robotics Surgery

This repository consists of works regarding serial robotics which includes ROS Simulations and sensors integration.

# OneNote Links for my Personal Documentation
* [Fundementals of ros](https://onedrive.live.com/view.aspx?resid=2DFBD8B4EE7A1CC5%21316&id=documents&wd=target%28complete%20work.one%7C59597DC3-98B0-4407-BB7D-2B3E11A300DE%2FFundementals%20of%20ROS%7CAFF9DDEA-4606-44F8-A711-B633C9F60F8E%2F%29onenote:https://d.docs.live.net/2dfbd8b4ee7a1cc5/Documents/Robotics/ros/complete%20work.one#Fundementals%20of%20ROS&section-id={59597DC3-98B0-4407-BB7D-2B3E11A300DE}&page-id={AFF9DDEA-4606-44F8-A711-B633C9F60F8E}&end)

* [ROS and Gazebo](https://onedrive.live.com/view.aspx?resid=2DFBD8B4EE7A1CC5%21316&id=documents&wd=target%28complete%20work.one%7C59597DC3-98B0-4407-BB7D-2B3E11A300DE%2FROS%20and%20Gazebo%7C62D8A1B6-A633-4B13-82A4-4C1D5DD598F6%2F%29
onenote:https://d.docs.live.net/2dfbd8b4ee7a1cc5/Documents/Robotics/ros/complete%20work.one#ROS%20and%20Gazebo&section-id={59597DC3-98B0-4407-BB7D-2B3E11A300DE}&page-id={62D8A1B6-A633-4B13-82A4-4C1D5DD598F6}&end)

* [ROS and Moveit](https://onedrive.live.com/view.aspx?resid=2DFBD8B4EE7A1CC5%21316&id=documents&wd=target%28complete%20work.one%7C59597DC3-98B0-4407-BB7D-2B3E11A300DE%2FROS%20and%20MoveIT%7C8DC7C664-3A28-4F9D-90F8-C8FECBF05927%2F%29
onenote:https://d.docs.live.net/2dfbd8b4ee7a1cc5/Documents/Robotics/ros/complete%20work.one#ROS%20and%20MoveIT&section-id={59597DC3-98B0-4407-BB7D-2B3E11A300DE}&page-id={8DC7C664-3A28-4F9D-90F8-C8FECBF05927}&end)

* [MoveIT and Realtime hardware](https://onedrive.live.com/view.aspx?resid=2DFBD8B4EE7A1CC5%21316&id=documents&wd=target%28complete%20work.one%7C59597DC3-98B0-4407-BB7D-2B3E11A300DE%2FMove-IT%20and%20real%20time%20hardware%7CA49547BE-EA92-47E5-9119-CBB48C590C89%2F%29
onenote:https://d.docs.live.net/2dfbd8b4ee7a1cc5/Documents/Robotics/ros/complete%20work.one#Move-IT%20and%20real%20time%20hardware&section-id={59597DC3-98B0-4407-BB7D-2B3E11A300DE}&page-id={A49547BE-EA92-47E5-9119-CBB48C590C89}&end)

* [Making a custom 3d robot](https://onedrive.live.com/view.aspx?resid=2DFBD8B4EE7A1CC5%21316&id=documents&wd=target%28complete%20work.one%7C59597DC3-98B0-4407-BB7D-2B3E11A300DE%2FMaking%20a%203d%20robot%7CB55E3C99-EC55-49D4-BE90-78C6E75D7BBB%2F%29
onenote:https://d.docs.live.net/2dfbd8b4ee7a1cc5/Documents/Robotics/ros/complete%20work.one#Making%20a%203d%20robot&section-id={59597DC3-98B0-4407-BB7D-2B3E11A300DE}&page-id={B55E3C99-EC55-49D4-BE90-78C6E75D7BBB}&end)

* [Industrial Robotics](https://onedrive.live.com/view.aspx?resid=2DFBD8B4EE7A1CC5%21316&id=documents&wd=target%28complete%20work.one%7C59597DC3-98B0-4407-BB7D-2B3E11A300DE%2FIndustrial%20Robotics%7C6DB47C2A-7C9A-4C2D-A889-D6B6A2C50982%2F%29
onenote:https://d.docs.live.net/2dfbd8b4ee7a1cc5/Documents/Robotics/ros/complete%20work.one#Industrial%20Robotics&section-id={59597DC3-98B0-4407-BB7D-2B3E11A300DE}&page-id={6DB47C2A-7C9A-4C2D-A889-D6B6A2C50982}&end)

* [Integration of 3D sensors](https://onedrive.live.com/view.aspx?resid=2DFBD8B4EE7A1CC5%21316&id=documents&wd=target%28complete%20work.one%7C59597DC3-98B0-4407-BB7D-2B3E11A300DE%2F3D%20sensors%7C067EBAEF-0471-42F4-B655-009E2941512E%2F%29
onenote:https://d.docs.live.net/2dfbd8b4ee7a1cc5/Documents/Robotics/ros/complete%20work.one#3D%20sensors&section-id={59597DC3-98B0-4407-BB7D-2B3E11A300DE}&page-id={067EBAEF-0471-42F4-B655-009E2941512E}&end)

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











