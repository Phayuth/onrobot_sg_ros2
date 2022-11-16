from setuptools import setup
# from glob import glob
# import os
package_name = 'onrobot_sg_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # (os.path.join('share',package_name,'launch'),glob('launch/*.py')), use this to install launch.py so we call use : ros2 launch name_pkg name_launch https://www.youtube.com/watch?v=RDoig5qEHRM
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
        'gripper_cli = onrobot_sg_ros2.client:main',
        ],
    },
)
