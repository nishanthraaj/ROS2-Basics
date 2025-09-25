#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Publisher(Node):
    def __init__(self):
        super().__init__("node_name")
        self.publisher_ = self.create_publisher(String, "Publisher", 10)
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = "GitHub is Cool"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = Publisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
