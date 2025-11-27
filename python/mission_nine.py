################################################################################
# mission_nine.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): [Katherine and Wesley]
# Date: [YYYY-MM-DD]
# Version: 3.0
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
     # Katherine and Wesle's Minecart and Statue Mission
     # Put bar down, incase Wesley doesn't set it up right.      
     r.lam.run_time(-5,500, wait=False)
     r.ram.run_time(5,500)
     # Drive towards the statue
     r.robot.straight(375)
     r.robot.arc(320,90)
     r.robot.straight(180)
     # Turn towards the Minecart and backup into the statue
     r.robot.turn(-85)
     r.lam.run_time(-20,500, wait=False)
     r.ram.run_time(20,500)
     r.robot.straight(-140)
     # Flip the bar from back to front to lift the statue
     r.lam.run_angle(600,130, wait=False)
     r.ram.run_angle(-600,130)
     r.robot.straight(-45)
     r.lam.run_angle(600,100, wait=False)
     r.ram.run_angle(-600,100)
     # Drive foward towards the Minecart
     r.robot.straight(130)
     wait(100)
     # Back away from the Minecart
     r.robot.straight(-35)
     # Lift bar to send the Cart to the other side, while driving foward
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