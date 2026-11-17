import rclpy
from rclpy.node import Node
from std_msgs.msg import String # msg type

class FirstSubscriber(Node):
    def __init__(self):
        super().__init__('first_subscriber')
        self.subscription = self.create_subscription(
        String, # msg type
        "chat", # topic to subscribe
        self.subscriber_callback, # function to execute when receiving a msg
        10)
        self.subscription # prevent unused variable warning
    def subscriber_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    first_subscriber = FirstSubscriber()
    rclpy.spin(first_subscriber)
    first_subscriber.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()