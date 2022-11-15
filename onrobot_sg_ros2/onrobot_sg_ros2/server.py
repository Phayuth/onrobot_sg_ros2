from onrobot_sg_ros2_srv.srv import Sg 
from .driver import SG
import rclpy
from rclpy.node import Node

# Color class for print in color
class bcolors:
	HEADER    = '\033[95m'
	OKBLUE    = '\033[94m'
	OKCYAN    = '\033[96m'
	OKGREEN   = '\033[92m'
	WARNING   = '\033[93m'
	FAIL      = '\033[91m'
	ENDC      = '\033[0m'
	BOLD      = '\033[1m'
	UNDERLINE = '\033[4m'


class Service(Node):

	def __init__(self):
		super().__init__('service')

		self.ip       = "192.168.1.1" #rospy.get_param('/gripper/ip')
		self.port     = 502           #rospy.get_param('/gripper/port')
		self.model_id = 3             #rospy.get_param('/gripper/model_id')
		self.gent     = True          #rospy.get_param('/gripper/gentle')

		self.get_logger().debug("Setting Up Connection")
		self.sg = SG(self.ip,self.port)
		self.sg.set_model_id(self.model_id)
		self.sg.set_init()
		self.sg.set_gentle(self.gent)
		self.get_logger().debug(bcolors.OKGREEN + "Gripper width is 110 to 750" + bcolors.ENDC)

		self.srv = self.create_service(Sg, 'Gripper_Command', self.execute_callback)


	def execute_callback(self, request, response):
		self.get_logger().debug('Incoming request %d' % request.desiredwidth)
		self.sg.set_target(request.desiredwidth)
		self.sg.set_move()
		response.status = "SUCCESS"
		return response

	def close_connection():
		self.sg.close_connection()
		print(bcolors.OKGREEN + "\nGripper connection is disconnected" + bcolors.ENDC)
		
def main(args=None):
	rclpy.init(args=args)
	service = Service()
	rclpy.spin(service)
	rclpy.shutdown()



if __name__ == '__main__':

	try:
		main()

	except Exception as e:
		raise e

	finally:
		pass