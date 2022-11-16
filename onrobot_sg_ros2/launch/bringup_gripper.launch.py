from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription([
		Node(
			package='onrobot_sg_ros2',
			# namespace='',
			executable='gripper_srv',
			name='gripper'
		),
	])