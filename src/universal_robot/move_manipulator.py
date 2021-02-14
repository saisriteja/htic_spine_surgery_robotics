#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list


def wait_for_state_update(box_name, scene, box_is_known=False, box_is_attached=False, timeout=4):
    start = rospy.get_time()
    seconds = rospy.get_time()

    print('-'.center(100,'-'))
    print('we are here')

    while (seconds - start < timeout) and not rospy.is_shutdown():
      attached_objects = scene.get_attached_objects([box_name])
      is_attached = len(attached_objects.keys()) > 0
      is_known = box_name in scene.get_known_object_names()
      if (box_is_attached == is_attached) and (box_is_known == is_known):
        print('collisio occurs')
        return True
      rospy.sleep(0.1)
      seconds = rospy.get_time()
    return False


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_manipulator', anonymous=True)
robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group = moveit_commander.MoveGroupCommander("manipulator")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
moveit_msgs.msg.DisplayTrajectory)

planning_frame = group.get_planning_frame()
pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 1.0
pose_target.position.x = 0.1   #0.1
pose_target.position.y = 0.2   #0.2
pose_target.position.z = 0.6   #0.6
group.set_pose_target(pose_target)

plan1 = group.plan()
rospy.sleep(5)

group.go(wait=True)
group.clear_pose_targets()



joint_goal = group.get_current_joint_values()
print('before',joint_goal)
from math import pi
joint_goal[0] = 0
joint_goal[1] = -pi/4
joint_goal[2] = 0
joint_goal[3] = -pi/2
joint_goal[4] = 0
joint_goal[5] = pi/3



group.go(joint_goal,wait=True)
group.stop()

print('after')
print(joint_goal)
group.clear_pose_targets()

move_group = group
scale = 1.0

waypoints = []

wpose = move_group.get_current_pose().pose
wpose.position.z -= scale * 0.1  # First move up (z)
wpose.position.y += scale * 0.2  # and sideways (y)
waypoints.append(copy.deepcopy(wpose))

wpose.position.x += scale * 0.1  # Second move forward/backwards in (x)
waypoints.append(copy.deepcopy(wpose))

wpose.position.y -= scale * 0.1  # Third move sideways (y)
waypoints.append(copy.deepcopy(wpose))

# We want the Cartesian path to be interpolated at a resolution of 1 cm
# which is why we will specify 0.01 as the eef_step in Cartesian
# translation.  We will disable the jump threshold by setting it to 0.0,
# ignoring the check for infeasible jumps in joint space, which is sufficient
# for this tutorial.
(plan, fraction) = move_group.compute_cartesian_path(
                                   waypoints,   # waypoints to follow
                                   0.01,        # eef_step
                                   0.0)         # jump_threshold


print "============ Waiting while RVIZ displays plan3..."
rospy.sleep(5)

display_trajectory = moveit_msgs.msg.DisplayTrajectory()
display_trajectory.trajectory_start = robot.get_current_state()
display_trajectory.trajectory.append(plan)
# Publish
display_trajectory_publisher.publish(display_trajectory);



move_group.execute(plan, wait=True)

print('entered box leveling')

box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = "wrist_1_link"
box_pose.pose.orientation.w = 1.0
box_pose.pose.position.z = 0.5 # slightly above the end effector
box_pose.pose.position.x = 0.6
box_name = "box1"
scene.add_box(box_name, box_pose, size=(0.1, 0.1, 0.1))
# rospy.loginfo(wait_for_state_update(box_name,scene,box_is_known=True))


# create the attached object we will be putting in collision with the box
box_name = 'tool'
box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = "wrist_3_link"
box_pose.pose.orientation.w = 1.0
box_pose.pose.position.z = 0.3
scene.add_box(box_name, box_pose, size=(0.1, 0.1, 0.1))

    # create the box we will be using to check for collision detection
# box_name = 'box2'
# box_pose = geometry_msgs.msg.PoseStamped()
# box_pose.header.frame_id = "shoulder_link"
# box_pose.pose.orientation.w = 1.0
# box_pose.pose.position.z = 0.2
# box_pose.pose.position.x = 0.6
# scene.add_box(box_name, box_pose, size=(0.4, 0.4, 0.4))
# rospy.loginfo(wait_for_state_update(box_name, scene, box_is_known=True))



print('collison apperance if true else false')


print('program completed')