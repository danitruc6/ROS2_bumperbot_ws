import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    joy_teleop = Node(
        package="joy_teleop",
        executable="joy_teleop",
        parameters=[
            os.path.join(
                get_package_share_directory("bumperbot_controller"),
                "config",
                "joy_teleop.yaml",
            )
        ],
    )

    teleop_twist_joy = Node(
        package="teleop_twist_joy",
        executable="teleop_twist_joy",
        parameters=[
            os.path.join(
                get_package_share_directory("bumperbot_controller"),
                "config",
                "teleop_twist_joy.yaml",
            )
        ],
    )

    joy_node = Node(
        package="joy",
        executable="joy_node",
        name="joystick",
        parameters=[
            os.path.join(
                get_package_share_directory("bumperbot_controller"),
                "config",
                "joy_config.yaml",
            )
        ],
    )

    return LaunchDescription([teleop_twist_joy, joy_node])
