import rclpy
from rclpy.node import Node
from std_msgs.msg import String 

class FirstPublisher(Node):
    def __init__(self):
        super().__init__("first_publisher") # Name for the node
        self.publisher = self.create_publisher(String, "chat", 10) #Message type, topic name, queue size

        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # Timer to execute the callback below
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = "Hello World: %d" % self.i
        self.publisher.publish(msg)
        self.i += 1

def main(args = None):
    rclpy.init(args=args)
    first_publisher = FirstPublisher()
    rclpy.spin(first_publisher)
    first_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()