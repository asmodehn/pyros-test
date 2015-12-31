#!/usr/bin/env python


import rospy
import python_setup_testpkg

##############################################################################
# Main
##############################################################################


if __name__ == '__main__':
    rospy.init_node('pyros_setup_testnode')
    node = python_test.EchoNode()
    node.spin()


