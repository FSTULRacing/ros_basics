#!/usr/bin/env python

from ros_basics.srv import RectangleArea,RectangleAreaResponse
import rospy

def handle_rectangle_area(req):
    print "Returning [%s * %s = %s]"%(req.width, req.height, (req.width * req.height))
    return RectangleAreaResponse(req.width*req.height)

def rectangle_area_server():
    rospy.init_node('Rectangle_area')
    s = rospy.Service('Rectangle_area',RectangleArea,handle_rectangle_area)
    print "Arrived to service"
    rospy.spin()

if __name__ == "__main__":
    rectangle_area_server()