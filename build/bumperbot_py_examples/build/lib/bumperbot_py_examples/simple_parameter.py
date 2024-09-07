import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter


class SimpleParameter(Node):
    def __init__(self):
        super().__init__("simple_parameter")

        self.declare_parameter("simple_init_param", 28)
        self.declare_parameter("simple_string_param", "Daniel")

        self.add_on_set_parameters_callback(self.param_change_callback)

    def param_change_callback(self, params):
        result = SetParametersResult()

        for param in params:
            if (
                param.name == "simple_init_param"
                and param.tppye_ == Parameter.Type.INTEGER
            ):
                self.get_logger().info(
                    f"Param simple_init_param changed! New value is {param.value}"
                )
                result.successful = True
            if (
                param.name == "simple_string_param"
                and param.type == Parameter.Type.STRING
            ):
                self.get_logger().info(
                    f"Param simple_string_param changed! New value is {param.value}"
                )
                result.successful = True
        return result


def main():
    rclpy.init()
    simple_parameter = SimpleParameter()
    rclpy.spin(simple_parameter)
    simple_parameter.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
