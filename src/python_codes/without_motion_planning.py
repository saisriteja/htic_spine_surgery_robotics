#!/usr/bin/env python


import rospy
from std_msgs.msg import Int32
import rospy
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Time
from std_msgs.msg import Header
from std_msgs.msg import Duration
import numpy as np
from math import *
import time
from matplotlib.pyplot import *
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
import math

rospy.init_node('topic_publisher')


pub = rospy.Publisher('/scaled_pos_joint_traj_controller/command',JointTrajectory,queue_size=10)
rate = rospy.Rate(2)
count = 0



# while not rospy.is_shutdown():
#  pub.publish(count)
#  count += 1
#  rate.sleep()

joints_str = JointTrajectory()
joints_str.header = Header()
joints_str.header.stamp = rospy.Time.now()
joints_str.joint_names = ["elbow_joint", "shoulder_lift_joint","shoulder_pan_joint", "wrist_1_joint", "wrist_2_joint","wrist_3_joint"]


from numpy import random
point=  JointTrajectoryPoint()

l = [0,-1.57,1.57,-3.14,-1.57,0]

point.positions = l


point.time_from_start = rospy.Duration(8)
joints_str.points.append(point)

import time
time.sleep(12)

pub.publish(joints_str)
rospy.loginfo("position updated")