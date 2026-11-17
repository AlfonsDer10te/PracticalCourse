"""Fill each TODO before running this node. None marks an unfinished blank."""

import cv2
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image


class GrayscaleNode(Node):
    def __init__(self):
        super().__init__('grayscale_node')
        self.bridge = CvBridge()

        # TODO 1: Replace None with the ROS message type for an image.
        image_type = Image
        # TODO 2: Replace None with the input topic name (a string).
        input_topic = "/rs/Image/Color"
        # TODO 3: Replace None with the output topic name (a string).
        output_topic = "/grayscale_image"


        self.publisher = self.create_publisher(image_type, output_topic, 10)
        self.subscription = self.create_subscription(
            image_type, input_topic, self.image_callback, qos_profile_sensor_data
        )

    def image_callback(self, msg):
        # Convert the ROS image message into an OpenCV BGR image.
        color_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Convert the three-channel BGR image into a single-channel image.
        gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

        # Convert back to a ROS image message and preserve timestamp/frame.
        gray_msg = self.bridge.cv2_to_imgmsg(gray_image, encoding='mono8')
        gray_msg.header = msg.header

        self.publisher.publish(gray_msg)


def main(args=None):
    rclpy.init(args=args)
    node = None
    try:
        node = GrayscaleNode()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node is not None:
            node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
