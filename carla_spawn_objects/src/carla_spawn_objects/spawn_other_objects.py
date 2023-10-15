import carla

# 连接到CARLA服务器
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)  # 设置超时时间，单位为秒

# 获取当前的世界
world = client.get_world()

# 获取某个车辆蓝图
blueprint_library = world.get_blueprint_library()
vehicle_bp = blueprint_library.find('vehicle.tesla.model3')  # 以Tesla Model 3为例

# 使用蓝图创建一个车辆（这是临时的，目的是获取其边界框）
spawn_point = carla.Transform(carla.Location(x=230, y=230, z=40))
vehicle = world.spawn_actor(vehicle_bp, spawn_point)

# 获取车辆边界框并提取宽度
bounding_box = vehicle.bounding_box
width = bounding_box.extent.y * 2  # extent是从中心到边界的距离，因此要乘以2

print("Vehicle width:", width)

# 如果不再需要，删除车辆
vehicle.destroy()
