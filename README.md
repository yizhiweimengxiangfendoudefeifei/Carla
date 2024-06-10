# Carla
Carla-Ros-Bridge, Simulation for planning and control.

<a name="readme-top"></a>


<!-- ABOUT THE PROJECT -->
## About Carla-Ros-Bridge
根据carla-ros-bridge官方文档修改，使用launch文件一键启动仿真，控制需要接收车辆油门、刹车、方向盘转角（rad）三个参数。  

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
运行carla客户端
```
./CarlaUE4.sh --prefernvidia -quality-level=low -fps=20 -windowed -Resx=600 -Resy=480
```

编译成功本项目后，需要执行一下ROS命令：
```
source devel/setup.zsh && roslaunch carla_ros_bridge carla_pnc_bridge.launch
```
该脚本主要启动了以下脚本：
1. **carla_ros_bridge.launch**，主要涉及carla客户端的通讯和设置。  
2. **carla_example_ego_vehicle.launch**，启动自车以及相关传感器的配置。  
3. **carla_waypoint_publisher.launch**，生成一条全局路径，可以使用rviz重新设置路径起点和终点，具体可以参考[carla-ros-bridge](https://carla.readthedocs.io/projects/ros-bridge/en/latest/carla_waypoints)。
4. **carla_ad_demo.rviz**，打开rviz可视化。   

如果需要适配carla客户端，算法端需要发布的形式如下：
```
carla_msgs::CarlaEgoVehicleControl msg;
msg.steer = steer;
if (speed >= 0) {
    msg.throttle = speed;
    msg.brake = 0;
} else {
    msg.throttle = 0;
    msg.brake = -speed / 8;
}
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



