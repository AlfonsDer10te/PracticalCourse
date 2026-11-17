import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
from std_msgs.msg import String # msg type

class Second_Subscriber(Node):
    def __init__(self):
        super().__init__("second_subscriber") # Name for the node
        self.publisher = self.create_publisher(Int16, "response", 10) #Message type, topic name, queue size
        self.subscription = self.create_subscription(
               Int16, # msg type
               "chat2", # topic to subscribe
               self.subscriber_callback, # function to execute when receiving a msg
               10)

    def subscriber_callback(self, msg):
        self.get_logger().info('I heard: "%i"' % msg.data)
        msg2 = Int16()
        msg2.data = msg.data * 10
        self.publisher.publish(msg2)



def main(args = None):
    rclpy.init(args=args)
    second_subscriber = Second_Subscriber()
    rclpy.spin(second_subscriber)
    second_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()