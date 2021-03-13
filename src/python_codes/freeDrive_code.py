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

def get_norm_force(force):
    ''' this give output of normalized force from the end effector of the UR5 Robot
        Input: None
        Output: Normalized Force from the EE of UR5
    '''
    force_resultant = np.linalg.norm(force)
    if force_resultant == 0:
        normalized_force = force
    else:
        normalized_force = force / (force_resultant)
    print('original force',force,'normalized force',normalized_force)
    return normalized_force

def velocity_force_torque_vector(norm_force,norm_torque,max_speed = 0.08):
    ''' this function helps to design the veloctiy of the end effector
    input -- normalized force and maximum speed that a joint should move
    output -- a speedl function that moves the robot in the applied force direction'''
    
    
    ff = max_speed * norm_force
    tt = max_speed * norm_torque

    return np.array([ff[0],ff[1],ff[2],tt[0],tt[1],tt[2]])



def dynamic_force_allocation():
    force_torque = np.array(rtde_r.getActualTCPForce())

    force = force_torque[:3] + 6
    torque = force_torque[3:]

    force_torque =  [force[0],force[1],force[2],torque[0],torque[1],torque[2]]


    
    force_resultant = np.linalg.norm(force)
    torque_resultant = np.linalg.norm(torque)

    #force mode
    task_frame = [0,0,0,0,0,0]#np.array(rtde_r.getActualTCPPose)  #force frame relative to base frame
    selection_vector = np.array([1,1,1,1,1,1]) 

    force_type = 2
    limits = [2,2,1.5,1,1,1]





    if force_resultant > 4 and torque_resultant > 0.18:

        print("triggered")
        
        norm_force = get_norm_force(force)
        norm_torque = get_norm_force(torque)
        # ee_velocity = velocity_force_torque_vector(norm_force,norm_torque,1)

        rtde_c.forceMode(task_frame,selection_vector,force_torque,force_type,limits)

        # rtde_c.speedL(ee_velocity,0.06)





    else:

        # if no force stop 
        force_torque = [0,0,0,0,0,0]
        rtde_c.forceMode(task_frame,selection_vector,force_torque,force_type,limits)
while True:
    dynamic_force_allocation()
    
rtde_c.stopScript()




        





