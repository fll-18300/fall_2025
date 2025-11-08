################################################################################
# mission_nine.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): [Your Name(s)]
# Date: [YYYY-MM-DD]
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
#
################################################################################
from robot import robot
from pybricks.parameters import *
from pybricks.tools import *

def mission_nine(r):
     print("Running Mission 9")
     r.robot.straight(400)
     r.robot.arc(320,90)
     r.robot.straight(170)
     r.robot.turn(-90)
     r.robot.straight(-130)
     r.lam.run_angle(600,180, wait=False)
     r.ram.run_angle(-600,180)
     r.robot.straight(95)
     r.lam.run_angle(-600,80, wait=False)
     r.ram.run_angle(600,80)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()