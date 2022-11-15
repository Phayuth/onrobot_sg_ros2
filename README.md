# onrobot Soft Gripper ROS Package
This package is written as the extension of the my onrobot_sg package for ROS2. [for mom!]

## Requirement
python package : pymodbus
```
sudo pip3 install -U pymodbus
```

## Installation
```
mkdir -p ws_gripper/src
cd ws_gripper/src
git clone 
cd ..
colcon build
```
Then source the workspace
```
source ~/ws_gripper/install/setup.bash
```


## Usage
<!-- Bring up the gripper
```
roslaunch onrobot_sg bringup_gripper.launch
```
Control the gripper via rosservice, where desired width is between 110mm and 800 mm
```
rosservice call /gripper_cmd "cmd_wd: desired_width"
```
Control via client service
```
rosrun onrobot_sg cmd_client.py desired_width
``` -->