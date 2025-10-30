#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
import tf

rospy.init_node('fake_odom_publisher')
odom_pub = rospy.Publisher('/odom', Odometry, queue_size=10)
rate = rospy.Rate(10)

x = 0.0
while not rospy.is_shutdown():
    odom = Odometry()
    odom.header.stamp = rospy.Time.now()
    odom.header.frame_id = "odom"
    odom.child_frame_id = "base_link"
    odom.pose.pose.position.x = x
    odom.pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0,0,0))
    odom.twist.twist.linear.x = 0.0
    odom.twist.twist.angular.z = 0.0
    odom_pub.publish(odom)
    x += 0.001
    rate.sleep()
