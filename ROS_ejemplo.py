#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('talker',anonymous=True)
    pub = rospy.Publisher('chatter',String,queue_size=10)

    rate = rospy.Rate(10)  #10Hz  -  probar tmb con 4Hz
    counter=0
    while not rospy.is_shutdown():  #para cerrar ctrl+C
        hello_str='hello world %d' % counter
        counter+=1
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass