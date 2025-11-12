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
from pybricks.hubs import PrimeHub

def mission_eight(r):
    print("Running Mission 8")
    # TEST CODE
    #492
    r.robot.settings(800,800, 200, 200)
    r.robot.straight(427)
    r.ram.run_time(200,1700)
    wait(1500)
    r.robot.straight(31)
    #r.robot.drive(50,0)
    #while not r.robot.stalled():
    #    wait(10)
    #r.robot.stop()
    r.robot.straight(-50)
    r.robot.straight(52)
    r.robot.straight(-50)
    r.robot.straight(52)
    r.robot.straight(-50)
    r.robot.straight(52)
    r.robot.straight(-50)
    r.robot.straight(52)
    r.robot.straight(-50)
    r.robot.straight(52)
    r.robot.straight(-50)
    r.robot.straight(52)
    r.robot.straight(-50)
    r.robot.straight(52)
    r.robot.straight(-50)
    r.robot.straight(52)
    r.robot.straight(-50)
    #r.robot.straight(-800)
    #new stuff
    r.robot.straight(-392)
    r.lam.run_time(800,1529, wait=False)
    r.ram.run_time(-800,2000)
    r.lam.run_time(200,2529, wait=False)
    r.robot.drive(200, 30)
    wait(2500)
    r.robot.stop()
    r.robot.drive(-670,0)
    wait(1000)
    r.robot.stop()
    r.lam.run_time(-800,2000, wait=False)
    r.robot.drive(-1067,0)
    wait(1500)
    r.robot.stop()
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()