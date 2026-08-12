import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class ControllerNode(Node):
    """Subscribe to /target and print a simple control state."""

    def __init__(self):
        super().__init__('controller_node')

        self.subscription = self.create_subscription(
            Bool,
            '/target',
            self.target_callback,
            10
        )

        self.get_logger().info(
            'controller_node started: subscribing to /target'
        )

    def target_callback(self, msg):
        if msg.data:
            self.get_logger().info('Tracking target!')
        else:
            self.get_logger().info('No target.')


def main(args=None):
    rclpy.init(args=args)

    node = ControllerNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
