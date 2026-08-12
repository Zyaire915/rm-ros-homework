import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SensorNode(Node):
    """Publish a deterministic simulated sensor value once per second."""

    def __init__(self):
        super().__init__('sensor_node')

        self.publisher = self.create_publisher(
            Float32,
            '/sensor_data',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.timer_callback
        )

        # Deterministic values make the classroom demo reproducible.
        self.values = [0.15, 0.35, 0.55, 0.75, 0.95, 0.75, 0.55, 0.35]
        self.index = 0

        self.get_logger().info(
            'sensor_node started: publishing /sensor_data at 1 Hz'
        )

    def timer_callback(self):
        msg = Float32()
        msg.data = float(self.values[self.index])

        self.publisher.publish(msg)

        self.get_logger().info(
            f'sensor = {msg.data:.2f}'
        )

        self.index = (self.index + 1) % len(self.values)


def main(args=None):
    rclpy.init(args=args)

    node = SensorNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
