from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped
import rclpy
from rclpy.node import Node


class TrajectoryDrawer(Node):
    def __init__(self) -> None:
        super().__init__("trajectory_drawer")
        self.declare_parameter("odom_topic", "bumperbot_controller/odom")
        odom_topic_ = self.get_parameter("odom_topic").value
        self.odom_sub_ = self.create_subscription(
            Odometry, str(odom_topic_), self.odomCallback, 10
        )
        self.trajectory_pub_ = self.create_publisher(
            Path, "/bumperbot_controller/trajectory", 10
        )
        self.trajectory_ = Path()

    def odomCallback(self, msg):
        current_pose = PoseStamped()
        current_pose.header.frame_id = msg.header.frame_id
        current_pose.header.stamp = msg.header.stamp
        current_pose.pose = msg.pose.pose
        self.trajectory_.poses.append(current_pose)

        self.trajectory_pub_.publish(self.trajectory_)


def main():
    rclpy.init()
    trajectory_drawer = TrajectoryDrawer()
    rclpy.spin(trajectory_drawer)
    trajectory_drawer.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
