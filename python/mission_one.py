################################################################################
# mission_one.py
#
# Description:
# My mission does cool stuff
#
# Author(kyle): [Your Name(kyle)]
# Date: [today]
# Version: 67.0
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
    r.robot.straight(350)
    #drive to the shop
    r.robot.turn(-44)
    r.robot.straight(195.67)
    r.lam.run_time(500,2529)
    r.robot.straight(-225)
    #raise the shop anad the roof
    r.robot.straight(30)
    r.lam.run_time(-650,2029)
    #r.robot.turn(-19)
    #r.robot.straight(80)
    #r.lam.run_time(1500,7029, wait=False)
    #hook the water thing
    #wait(1500)
    #r.robot.turn(-35)
    #pull the water thing out from the scale
    #r.robot.straight(-300)
    #r.robot.turn(30)
    #go back to home withwater thingy
    r.robot.straight(-611) 

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()