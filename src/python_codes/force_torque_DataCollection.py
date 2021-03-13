#!/usr/bin/env python

import rtde_control
import rtde_io
import rtde_receive

import time
import numpy as np
import time

import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ip = "172.16.101.225"

rtde_io = rtde_io.RTDEIOInterface(ip)
rtde_c = rtde_control.RTDEControlInterface(ip)
rtde_r = rtde_receive.RTDEReceiveInterface(ip)

print("connection established")
print("enter the name of the file")

def save(file_name,data):
    '''
    save data in numpy array
    '''
    np.save(file_name+'.npy',data)

def get_forceandtorque():
    '''
    returns TCP Force
    '''
    return np.array(np.array(rtde_r.getActualTCPForce())) 

def get_joint_velocities():
    '''
    return joint velocities
    '''
    return np.array(rtde_r.getActualQd())

def get_ee_position():
    '''
    returns the position of EE
    '''
    return np.array(rtde_r.getActualTCPPose())

def get_ee_speed():
    '''
    return the speed of EE
    '''
    return np.array(rtde_r.getActualTCPSpeed())

def get_norm_force():
    ''' this give output of normalized force from the end effector of the UR5 Robot
        Input: None
        Output: Normalized Force from the EE of UR5
    '''

    force_torque = np.array(rtde_r.getActualTCPForce())
    time.sleep(1)
    force_resultant = np.linalg.norm(force_torque[:3])
    if force_resultant == 0:
        normalized_force = force_torque[:3]
    else:
        normalized_force = force_torque[:3] / (force_resultant)
    print('original force',force_torque[0:3],'normalized force',normalized_force)
    return normalized_force

def velocity_force_vector(norm_force,max_speed = 0.08):
    ''' this function helps to design the veloctiy of the end effector
    input -- normalized force and maximum speed that a joint should move
    output -- a speedl function that moves the robot in the applied force direction'''
    return max_speed * norm_force

fx = []
fy = []
fz = []
tx = []
ty = []
tz = []

velocities_joints = []
endeffector_position = []
endeffector_speed = []

def animate_force_plotting(i):
    force_norm = get_forceandtorque()
    joint_v = get_joint_velocities()
    ee_pos = get_ee_position()
    ee_speed = get_ee_speed()

    global fx
    global fy
    global fz
    global tx
    global ty
    global tz
    global velocities_joints
    global endeffector_position
    global endeffector_speed
 

    fx.append(force_norm[0])
    fy.append(force_norm[1]) #+ random.randint(0,10))
    fz.append(force_norm[2]) #+ random.randint(0,10))
    tx.append(force_norm[3])
    ty.append(force_norm[4]) #+ random.randint(0,10))
    tz.append(force_norm[5]) #+ random.randint(0,10))
    velocities_joints.append(joint_v)
    endeffector_position.append(ee_pos)
    endeffector_speed.append(ee_speed)
    

    data = np.array([fx,fy,fz,tx,ty,tz,velocities_joints,endeffector_position,endeffector_speed])

    save('circle',data)
    
    plt.subplot(3,3,1)
    plt.plot(fx,'r')
    plt.title('Fx')

    plt.subplot(3,3,2)
    plt.plot(fy,'g')
    plt.title('Fy')

    plt.subplot(3,3,3)
    plt.plot(fz,'b')
    plt.title('Tx')

    plt.subplot(3,3,5)
    plt.plot(ty,'g')
    plt.title('Ty')

    plt.subplot(3,3,6)
    plt.plot(tz,'b')
    plt.title('Tz')

    plt.subplot(3,3,7)
    plt.plot(np.array(endeffector_position)[:,3],'r')
    plt.title('ee_r_x')

    plt.subplot(3,3,8)
    plt.plot(np.array(endeffector_position)[:,4],'g')
    plt.title('ee_r_y')

    plt.subplot(3,3,9)
    plt.plot(np.array(endeffector_position)[:,5],'b')
    plt.title('ee_r_z')


# while(True):
    # get_norm_force()    

    
plt.style.use('fivethirtyeight')



ani = FuncAnimation(plt.gcf(),animate_force_plotting,interval = 800)
plt.tight_layout()
plt.show()
plt.clf()
time.sleep(1)




