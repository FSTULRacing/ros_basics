#!/usr/bin/env python

import random
import rospy
from ros_basics.srv import *

def rectange_area_client(x, y):
    rospy.wait_for_service('Rectangle_area')
    try:
        service = rospy.ServiceProxy('Rectangle_area', RectangleArea)
        resp = service(x, y)
        return resp.area
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
        
def main():
   
    while not rospy.is_shutdown():
        
            rospy.init_node('Rectangle_area_client',anonymous=True)   
            x = float(random.randint(1,9))
            y = float(random.randint(1,9))
            print "Requesting %s*%s"%(x, y)
            print "%s * %s = %s"%(x, y, rectange_area_client(x, y))
            rospy.sleep(1)
   

if __name__ == "__main__":
   main()
