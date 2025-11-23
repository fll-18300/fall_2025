################################################################################
# mission_seven.py
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

def mission_seven(r):
    print("Running Mission 7")
    # THIS IS CAMS CODE NO TOUCH
    r.robot.straight(740)
    r.robot.straight(-160)
    r.robot.straight(160)
    r.robot.turn(-35)
    r.robot.straight(50)
    r.robot.straight(57)
    r.ram.run_time(1000,500)
    r.robot.straight(-150)
    r.robot.turn(42)
    r.robot.straight(-20)
    r.robot.turn(20)
    r.robot.straight(-70)
    wait(500)
    #r.lam.run_time(500,500)
    r.lam.run_time(-400,1000)
    r.lam.run_time(400,700)
    r.robot.straight(-400)
    r.robot.turn(30)
    r.robot.straight(-400)
   

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()