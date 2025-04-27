import csv

def generate_challan(vehicle_number, speed, filename='challans.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([vehicle_number, speed, 'Fine Paid:No'])
    print(f"💸 Challan generated for {vehicle_number} | Speed: {speed} km/h")
