import inspect
import json
from os import mkdir
from os.path import abspath, dirname, exists, join

physics_starter = '''
#
# See the documentation for more details on how this works
#
# Documentation can be found at https://robotpy.readthedocs.io/projects/pyfrc/en/latest/physics.html
#
# The idea here is you provide a simulation object that overrides specific
# pieces of WPILib, and modifies motors/sensors accordingly depending on the
# state of the simulation. An example of this would be measuring a motor
# moving for a set period of time, and then changing a limit switch to turn
# on after that period of time. This can help you do more complex simulations
# of your robot code without too much extra effort.
#
# Examples can be found at https://github.com/robotpy/examples

import wpilib.simulation

from pyfrc.physics.core import PhysicsInterface
from pyfrc.physics import motor_cfgs, tankmodel
from pyfrc.physics.units import units

import typing

if typing.TYPE_CHECKING:
    from robot import MyRobot


class PhysicsEngine:
    """
    Simulates a 4-wheel robot using Tank Drive joystick control
    """

    def __init__(self, physics_controller: PhysicsInterface, robot: "MyRobot"):
        """
        :param physics_controller: `pyfrc.physics.core.Physics` object
                                   to communicate simulation effects to
        :param robot: your robot objet
        """

        self.physics_controller = physics_controller

        print("TODO: modify simulation for my robot")

        """
        # Change these parameters to fit your robot!

        # Motors
        self.l_motor = wpilib.simulation.PWMSim(1)
        self.r_motor = wpilib.simulation.PWMSim(2)

        bumper_width = 3.25 * units.inch

        self.drivetrain = tankmodel.TankModel.theory(
            motor_cfgs.MOTOR_CFG_CIM,           # motor configuration
            110 * units.lbs,                    # robot mass
            10.71,                              # drivetrain gear ratio \omega In/\omega Out
            2,                                  # motors per side
            22 * units.inch,                    # robot wheelbase
            23 * units.inch + bumper_width * 2, # robot width
            32 * units.inch + bumper_width * 2, # robot length
            6 * units.inch,                     # wheel diameter
        )
        """

    def update_sim(self, now, tm_diff):
        """
        Called when the simulation parameters for the program need to be
        updated.

        :param now: The current time as a float
        :param tm_diff: The amount of time that has passed since the last
                        time that this function was called
        """

        """
        # Simulate the drivetrain
        l_motor = self.l_motor.getSpeed()
        r_motor = self.r_motor.getSpeed()

        transform = self.drivetrain.calculate(l_motor, r_motor, tm_diff)
        pose = self.physics_controller.move_robot(transform)
        """

'''


class PyFrcCreatePhysics:
    def __init__(self, parser=None):
        pass

    def run(self, options, robot_class, **static_options):

        robot_file = abspath(inspect.getfile(robot_class))
        robot_path = dirname(robot_file)
        sim_path = join(robot_path, "sim")

        physics_file = join(robot_path, "physics.py")
        if exists(physics_file):
            print("- physics.py already exists")
        else:
            with open(physics_file, "w") as fp:
                fp.write(physics_starter)
            print("- physics file created at", physics_file)

        print()
        print("Robot simulation can be run via 'python3 robot.py sim'")
