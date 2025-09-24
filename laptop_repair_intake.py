from array import array

daily_repairs = [10, 14, 9, 12, 11, 16, 13]

total_repairs = sum(daily_repairs)
average_repairs = total_repairs / len(daily_repairs)
min_repairs = min(daily_repairs)
max_repairs = max(daily_repairs)

print(f"Total laptops repaired this week: {total_repairs}")
print(f"Average daily repairs: {average_repairs:.2f}")

report = (
    f"\n--- Laptop Repair Weekly Report ---\n"
    f"Maximum in a day: {max_repairs}\n"
    f"Minimum in a day: {min_repairs}\n"
)
print(report)

THRESHOLD = 12


if average_repairs > THRESHOLD and max_repairs >= 15:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

laptop_models = ["Dell", "HP", "Lenovo", "Acer", "Asus"]
print("\nOriginal laptop models list:", laptop_models)

laptop_models.append("MSI")

if "Acer" in laptop_models:
    laptop_models.remove("Acer")

print("Modified and sorted laptop models list:", sorted(laptop_models))

repair_subset = array('i', daily_repairs[:5])
array_sum = sum(repair_subset)

print(f"\nSum of repairs (first 5 days using array): {array_sum}")
print(f"Sum of full list repairs: {total_repairs}")

laptop_intake_records = [
    {"id": 1, "name": "Dell", "value": 4},
    {"id": 2, "name": "HP", "value": 3},
    {"id": 3, "name": "Lenovo", "value": 2},
    {"id": 4, "name": "Asus", "value": 5},
]


for record in laptop_intake_records:
    if record["name"] == "HP":
        record["value"] += 1  

laptop_intake_records = [record for record in laptop_intake_records if record["name"] != "Lenovo"]

total_value = sum(record["value"] for record in laptop_intake_records)

print("\nUpdated Laptop Intake Records:")
for record in laptop_intake_records:
    print(record)

print(f"\nTotal intake value across all records: {total_value}")
