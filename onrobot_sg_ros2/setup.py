from setuptools import setup

package_name = 'onrobot_sg_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ub20',
    maintainer_email='yuth@todo.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'gripper_srv = onrobot_sg_ros2.server:main',
        # 'msg_sub = custom_srv_msg_use_py.msg_sub:main',
        ],
    },
)
