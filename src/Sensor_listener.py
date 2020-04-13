#!/usr/bin/env python

import rospy
from ros_basics.msg import TempHumSensor


def sensor_callback(sensor_msg):
    rospy.loginfo("Recieved msg from: {} \t ID: {}".format(sensor_msg.name, sensor_msg.id))
    rospy.loginfo("Temperature: {} C".format(sensor_msg.temperature))
    rospy.loginfo("Humidity: {} %".format(sensor_msg.humidity))

if __name__ == "__main__":
    rospy.init_node("Sensor_listener", anonymous=True)

    sensor_topic = "/sensor"
    sensor_sub = rospy.Subscriber(sensor_topic, TempHumSensor, sensor_callback)

    rospy.spin()
    