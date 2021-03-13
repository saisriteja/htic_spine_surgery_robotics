# Python Files

## SaiSriTeja Drive

I have written a python Script to replicat the free drive option that is present in UR5 Robot.
Force is taken as input and the for the dynamic change in postion of the robot I have tried commands of SpeedL and ForceMode to control the joint Positions.

In general a force of 15N is to be given to move the robot from rest state, but using the python Script we can move with minimal force of 4N using ForceMode and around 8N using SpeedL command.

### Pseudocode using forceMode
```
While True:
  get forcedata_TCP
  forcedata = forcedata + Threshold_force_value
  send forcedata_TCP
end
```

### PesudoCode using SpeedL
```
while True:
  get frocedata_TCP
  norm_force
  ee_speed = speedL( norm_force * Threshold_max_speed)
end
```

In the pseudocode above you need to tune the values of Threshold_force_value and Threshold_max_speed in the codes to increase or decrease stiffness of the robot.

The work done upto now helps to move the robot in translational way only, need to work with speedJ using inverse kinematics and Jacobian matrices to completly replicate the work.

[Code](https://github.com/saisriteja/htic_spine_surgery_robotics/blob/main/src/python_codes/freeDrive_code.py) for Free Drive using ForceMode and SpeedL commnads.
[Code](https://github.com/saisriteja/htic_spine_surgery_robotics/blob/main/src/python_codes/force_torque_DataCollection.py) to collect data from TCP and store the values in a .npy file.
[Code](https://github.com/saisriteja/htic_spine_surgery_robotics/blob/main/src/python_codes/force_torque_data_visual.py) to see the collected data from the .npy file. 


