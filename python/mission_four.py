################################################################################
# mission_four.py
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

def mission_four(r):
    print("Running Mission 4")
    # Your code goes here...
    # Sample code: Test the speaker
    r.robot.straight(470)
    r.robot.straight(-70)
    r.robot.turn(-48)
    r.robot.turn(48)
    r.robot.straight(-480)
    ################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()