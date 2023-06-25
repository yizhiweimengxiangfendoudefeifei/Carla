#!/usr/bin/env python
#
# Copyright (c) 2020 Intel Corporation
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.
#
"""
handle a odom sensor
"""
import tf.transformations as tf
import math
from carla_ros_bridge.pseudo_actor import PseudoActor

from nav_msgs.msg import Odometry


class OdometrySensor(PseudoActor):

    """
    Pseudo odometry sensor
    """

    def __init__(self, uid, name, parent, node):
        """
        Constructor

        :param uid: unique identifier for this object
        :type uid: int
        :param name: name identiying this object
        :type name: string
        :param carla_world: carla world object
        :type carla_world: carla.World
        :param parent: the parent of this
        :type parent: carla_ros_bridge.Parent
        :param node: node-handle
        :type node: carla_ros_bridge.CarlaRosBridge
        """

        super(OdometrySensor, self).__init__(uid=uid,
                                             name=name,
                                             parent=parent,
                                             node=node)

        self.odometry_publisher = node.new_publisher(Odometry,
                                                     self.get_topic_prefix(),
                                                     qos_profile=10)

    def destroy(self):
        super(OdometrySensor, self).destroy()
        self.node.destroy_publisher(self.odometry_publisher)

    @staticmethod
    def get_blueprint_name():
        """
        Get the blueprint identifier for the pseudo sensor
        :return: name
        """
        return "sensor.pseudo.odom"

    def update(self, frame, timestamp):
        """
        Function (override) to update this object.
        """
        odometry = Odometry(header=self.parent.get_msg_header("map", timestamp=timestamp))
        odometry.child_frame_id = self.parent.get_prefix()
        try:
            odometry.pose.pose = self.parent.get_current_ros_pose()
            # odometry.twist.twist = self.parent.get_current_ros_twist_rotated()
            # print("vx = %f vy = %f vz = %f"%(odometry.twist.twist.linear.x, odometry.twist.twist.linear.y, odometry.twist.twist.linear.z))
            # print("x = %f y = %f z= %f"%(odometry.pose.pose.position.x,odometry.pose.pose.position.y,odometry.pose.pose.position.z))
            # quaternion = (odometry.pose.pose.orientation.x,
            #                 odometry.pose.pose.orientation.y,
            #                 odometry.pose.pose.orientation.z,
            #                 odometry.pose.pose.orientation.w)
            # _, _, yaw = tf.euler_from_quaternion(quaternion)
            # print("vx = %f"%(odometry.twist.twist.linear.x * math.cos(yaw) - odometry.twist.twist.linear.y * math.sin(yaw)))
            # print("vy = %f"%(odometry.twist.twist.linear.y * math.cos(yaw) + odometry.twist.twist.linear.x * math.sin(yaw)))


        except AttributeError:
            # parent actor disappeared, do not send tf
            self.node.logwarn(
                "OdometrySensor could not publish. parent actor {} not found".format(self.parent.uid))
            return
        self.odometry_publisher.publish(odometry)
