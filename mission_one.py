################################################################################
# mission_one.py
#
# Description:
# [Describe What your mission does here]
#
# Author(kyle): [Your Name(kyle)]
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

def mission_one(r):
    print("Running Mission 1")
    # Kyles code
    # Sample Code: Run attachment motors and drive motors
    r.robot.straight(400)
    r.robot.turn(-42)
    r.robot.straight(113.67)
    r.lam.run_time(500,2529)
    r.robot.straight(-225)
    r.robot.straight(30)
    r.lam.run_time(-650,2029)
    r.robot.turn(-23)
    r.robot.straight(80)
    #r.lam.run_time(500,2029, then=Stop.HOLD)
    r.lam.run_time(1500,7029, wait=False)
    wait(1500)
    r.robot.turn(-35)
    r.robot.straight(-600)
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()