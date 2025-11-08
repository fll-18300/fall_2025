################################################################################
# mission_five.py
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

def mission_five(r):
    print("Running Mission 5")
    # Jackson's pole vaulter 2.0
    r.robot.straight(422)
    r.ram.run_time(200,1700)
    r.robot.straight(31)
    r.robot.straight(-50)
    r.robot.straight(50)
    r.robot.straight(-50)
    r.robot.straight(50)
    r.robot.straight(-50)
    r.robot.straight(50)
    r.robot.straight(-50)
    r.robot.straight(50)
    r.robot.straight(-50)
    r.robot.straight(50)
    r.robot.straight(-50)
    r.robot.straight(50)
    r.robot.straight(-50)
    r.robot.straight(50)
    r.robot.straight(-50)
    r.robot.straight(50)
    r.robot.straight(-50)
    #r.robot.straight(-800)
    #new stuff
    r.robot.straight(-273)
    r.robot.turn(6)
    r.lam.run_time(800,1529)
    r.robot.drive(200, 0)
    wait(2500)
    r.robot.stop()
    r.robot.straight(-498)
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()