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
    r.robot.settings(800,800, 200, 200)
    r.robot.straight(422)
    r.ram.run_time(200,1700)
    wait(1500)
    r.robot.straight(36)
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
    #r.robot.straight(-412)
    #reset the distance counter
    r.robot.reset()
    #drive backwards with a slight curveee
    r.robot.drive(-201,5)
    #keep driving until we hit the distance 
    while abs(r.robot.distance()) < 412:
        pass
    r.robot.stop()
    r.lam.run_time(800,1529, wait=False)
    r.ram.run_time(-800,1529)
    r.robot.drive(200, 21)
    wait(2500)
    r.robot.stop()
    r.lam.run_time(-800,1567,wait=False)
    r.robot.straight(-500)
    r.robot.settings(500,500, 300, 200)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()