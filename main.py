import os
import time
import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing

DRONE_IP = os.environ.get("DRONE_IP", "20.97.199.124")

def test_connection():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    assert drone(TakeOff()).wait().success()
    time.sleep(10)
    assert drone(Landing()).wait().success()    
    drone.disconnect()

if __name__ == "__main__":
    test_connection()
