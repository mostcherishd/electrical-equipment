import csv

MAX_AMPS = 200
total_load = 0

with open('appliances.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        amps = float(row['Amps'])
        total_load += amps
        if amps >= 30:
            print(f"Heavy Load Found: {row['Appliance']} uses {amps} Amps")

            

print(f"\nTotal Electrical Load: {total_load} Amps")

if total_load > MAX_AMPS:
    print("⚠️ WARNING: OVERLOAD DETECTED! Risk of fire. Upgrade panel required.")
else:
    print("✅ SAFE: The load is within the 200A limit.")