################################################################################
# mission_eight.py
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

def mission_eight(r):
    print("Running Mission 8")
    # Your code goes here...
    r.robot.straight(400)
    r.robot.arc(320,90)
    r.robot.straight(170)
    r.robot.turn(-90)
    r.robot.straight(-120)
    r.lam.run_time(600,2000)
    r.ram.run_time(-600,2000)
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()