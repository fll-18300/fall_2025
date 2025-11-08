################################################################################
# mission_two.py
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

def mission_two(r):
    print("Running Mission 2")
    # Your code goes here...
    r.robot.straight (425)
    #ITS HAMMER TIME Yippee
    r.ram.run_time(400,1000)
    r.ram.run_time(-400,1000)
    r.ram.run_time(400,1000)
    r.ram.run_time(-400,1000)
    r.ram.run_time(400,1000)
    r.ram.run_time(-400,1000)
    r.ram.run_time(-400,1000)
    r.robot.turn(-45)
    r.robot.straight(300)
    r.robot.turn(100)
    r.robot.straight(75)
    r.robot.straight(-10)
    r.robot.turn(40)
    r.robot.turn(-40)
    r.lam.run_time(400,1500)
    r.robot.turn(20)
    r.robot.turn(-20)
    r.lam.run_time(-400,1500)
    r.robot.turn(-43)
    r.robot.straight(28)
    r.robot.turn(-30)
    r.robot.straight(-1000)
    #r.robot.turn (10)
    #r.robot.drive(200,-100)
    # r.robot.stop()
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()