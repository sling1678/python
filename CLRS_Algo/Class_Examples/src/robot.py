"""
An example that illustrates class method and private attributes.

Also we see the illustration of sys.argv
"""

class Robot:
    __counter = 0   # private attribute

    def __init__(self):
        type(self).__counter += 1

    @classmethod
    def RobotInstances(cls): # does not need self and does not require an instance
        return cls, Robot.__counter


if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())
    import sys
    for i in range(len(sys.argv)):
        if i == 0:
            print("Function name: %s" % sys.argv[0])
        else:
            print("%d. argument: %s" % (i, sys.argv[i]))