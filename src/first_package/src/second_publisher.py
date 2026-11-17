import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Second_Publisher(Node):
    def __init__(self):
        super().__init__("second_publisher") # Name for the node
        self.publisher = self.create_publisher(Int16, "chat2", 10) #Message type, topic name, queue size
        # msg = Int16
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # Timer to execute the callback below
        self.i = 0
    
    def timer_callback(self):
        msg = Int16()
        msg.data = self.i
        self.publisher.publish(msg)
        self.i += 1



def main(args = None):
    rclpy.init(args=args)
    second_publisher = Second_Publisher()
    rclpy.spin(second_publisher)
    second_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()