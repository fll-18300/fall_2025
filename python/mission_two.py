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
    #moves up to da hammer mission
    r.robot.straight (425)
    #hammer mission (4 times)
    #(1)
    r.ram.run_time(400,1000)
    r.ram.run_time(-400,1000)
    #(2)
    r.ram.run_time(400,1000)
    r.ram.run_time(-400,1000)
    #(3)
    r.ram.run_time(400,1000)
    r.ram.run_time(-400,1000)
    #(4)
    r.ram.run_time(400,1000)
    r.ram.run_time(-400,1000)
    # moves it to da rock mission
    r.robot.turn(-45)
    r.robot.straight(300)
    r.robot.turn(100)
    # da rock mission 
    r.robot.straight(78)
    r.robot.straight(-10)
    r.robot.turn(-43)
    #adjusts its self to da island thingy
    r.robot.straight(28)
    #does da island thingy
    r.robot.turn(-32)
    #end of da mission so it moves back a little
    r.robot.straight(-200)
    #END OF DA MISSION
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()