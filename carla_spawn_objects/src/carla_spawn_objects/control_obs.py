import carla

# 连接到Carla服务器
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)  # 设置超时为10秒

# 获取Carla的世界
world = client.get_world()

def get_vehicle_by_id(vehicle_id):
    for actor in world.get_actors():
        if 'vehicle' in actor.type_id and actor.attributes.get('id') == vehicle_id:
            return actor
    return None

vehicle = get_vehicle_by_id(210)

if vehicle:
    # 设定速度为10 m/s
    velocity = carla.Vector3D(10, 0, 0)  
    vehicle.set_velocity(velocity)
else:
    print("车辆未找到!")
