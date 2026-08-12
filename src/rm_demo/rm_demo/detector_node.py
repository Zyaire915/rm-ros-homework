import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Float32


class DetectorNode(Node):
    """Subscribe to /sensor_data and publish whether a target is detected."""

    def __init__(self):
        super().__init__('detector_node')

        # Runtime-adjustable ROS parameter.
        self.declare_parameter('threshold', 0.6)

        self.subscription = self.create_subscription(
            Float32,
            '/sensor_data',
            self.sensor_callback,
            10
        )

        self.publisher = self.create_publisher(
            Bool,
            '/target',
            10
        )

        threshold = self.get_parameter('threshold').value
        self.get_logger().info(
            f'detector_node started: threshold={threshold:.2f}'
        )

    def sensor_callback(self, msg):
        # Read the current parameter every callback so ros2 param set
        # takes effect immediately without restarting the node.
        threshold = float(
            self.get_parameter('threshold').value
        )

        target_msg = Bool()
        target_msg.data = bool(msg.data > threshold)

        self.publisher.publish(target_msg)

        self.get_logger().info(
            f'value={msg.data:.2f}, '
            f'threshold={threshold:.2f}, '
            f'target={target_msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = DetectorNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
