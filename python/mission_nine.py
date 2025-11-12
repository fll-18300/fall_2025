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
     r.robot.straight(355)
     r.robot.arc(320,90)
     r.robot.straight(180)
     r.robot.turn(-85)
     r.robot.straight(-140)
     r.lam.run_angle(600,230, wait=False)
     r.ram.run_angle(-600,230)
     r.robot.straight(95)
     wait(100)
     r.robot.straight(-35)
     r.lam.run_angle(-100,100, wait=False)
     r.ram.run_angle(100,100, wait=False)
     wait(500)
     r.robot.straight(70)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()