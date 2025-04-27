import random
import time
from photo_capture import capture_vehicle_photo_from_video
from challan_generator import generate_challan

def traffic_light_simulator():
    lights = ['Red', 'Green', 'Yellow']
    for light in lights:
        print(f"🚦 Traffic Light: {light}")
        time.sleep(2)

def speed_check():
    vehicle_speed = random.randint(30, 120)
    print(f"🛻 Vehicle Speed Detected: {vehicle_speed} km/h")

    if vehicle_speed > 60:
        print("⚠️ Speeding Detected! Generating Challan & Capturing Photo...")
        capture_vehicle_photo_from_video()
        generate_challan('BR01AB1234', vehicle_speed)

if __name__ == '__main__':
    while True:
        traffic_light_simulator()
        speed_check()

        next_vehicle = input("Next vehicle? (y/n): ").strip().lower()
        if next_vehicle != 'y':
            print("🚗 Traffic monitoring stopped.")
            break
