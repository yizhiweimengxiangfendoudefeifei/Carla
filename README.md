# Carla
Carla-Ros-Bridge, Simulation for planning and control.

<a name="readme-top"></a>


<!-- ABOUT THE PROJECT -->
## About Carla-Ros-Bridge
根据carla-ros-bridge官方文档修改，使用launch文件一键启动仿真，控制方式使用carla_ackermann_control，控制需要接收车辆速度、和方向盘转角（rad）两个参数。  

<!-- GETTING STARTED -->

## Prerequisites

1. 安装Carla仿真软件，我这里使用的是Carla-0.9.12版本。
2. 克隆本仓库并编译。
```
git@github.com:yizhiweimengxiangfendoudefeifei/Carla.git
pip install -r requirements.txt
catkin build
```
## Contents
编译成功本项目后，需要执行一下ROS命令：
```
roslaunch carla_ros_bridge carla_pnc_bridge.launch
```
该脚本主要启动了以下脚本：
1. **carla_ros_bridge.launch**，主要涉及carla客户端的通讯和设置。  
2. **carla_example_ego_vehicle.launch**，启动自车以及相关传感器的配置。  
3. **carla_waypoint_publisher.launch**，生成一条全局路径，可以使用rviz重新设置路径起点和终点，具体可以参考[carla-ros-bridge](https://carla.readthedocs.io/projects/ros-bridge/en/latest/carla_waypoints)。
4. **carla_ackermann_control.launch**，对控制命令进行了转换，具体来说该package订阅ROS话题"/carla/ego_vehicle/ackermann_cmd"，如果需要适配该控制命令，需要发布的命令形式如下：
```
ackermann_msgs::AckermannDrive msg;
msg.steering_angle = steer;// 前轮转向角，弧度制
msg.steering_angle_velocity = 0.0;
msg.speed = speed;// 期望的速度,m/s
msg.acceleration = 0.0;
msg.jerk = 0.0;
control_pub.publish(msg);
```






<!-- LICENSE -->
## License

Distributed under the Apache-2.0 License. See `LICENSE.txt` for more information.

In addition, We have kept the LICENSE of project [Carla-Ros-Bridge](https://github.com/yizhiweimengxiangfendoudefeifei/Carla) in Carla-Ros-Bridge directory.





<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

The co-simulation is modified on the basis of the following, thank you here.

* [Carla](https://github.com/carla-simulator/carla)
* [ros-bridge](https://github.com/carla-simulator/ros-bridge)



