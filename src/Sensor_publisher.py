#!/usr/bin/env python
import random
import rospy
from ros_basics.msg import TempHumSensor


def talker():
    rospy.init_node('Sensor_talker', anonymous=True)
    pub = rospy.Publisher('/sensor', TempHumSensor) 

    r = rospy.Rate(10)  # 10hz

    msg = TempHumSensor()
    msg.id = rospy.get_param("sensor_id")
    msg.name = rospy.get_param("sensor_name")

    while not rospy.is_shutdown():
        msg.humidity = float(random.randint(3, 10))
        msg.temperature =float(random.randint(3,10))
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':

        try:
            talker()
        except rospy.ROSInterruptException:
            pass