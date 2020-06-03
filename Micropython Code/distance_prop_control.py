from spike import MotorPair
from spike import DistanceSensor
import utime

# small wheel to spike wheel ratio
wheel_gain = 55/30

# other init
target_dist = 10
last_dist = 10
kp = 5
wall_detector = DistanceSensor('E')
motor_pair = MotorPair('B','A')

# move panda forward
while True:
    try:
        dist = wall_detector.get_distance_percentage()
        if dist == None:
            dist = target_dist
        else:
            last_dist = dist
    except:
        dist = last_dist
    
    motor_power = (int(dist) - target_dist) * kp
    if motor_power > 50:
        motor_power = 50
    elif motor_power < -50:
        motor_power = -50
    print('speed:{} dist:{}'.format(dist, motor_power))
    
    motor_pair.start_at_power(motor_power)
    utime.sleep(0.1)





