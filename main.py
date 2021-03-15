import csv
import matplotlib.pyplot as plt

rows = []

with open("data.csv", "r", encoding="UTF-8") as f:
  reader = csv.reader(f)

  for row in reader:
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

names = []
distances = []
masses = []
radiuses = []
gravity = []

for star_data in star_data_rows:
  if len(star_data) == 13:
    names.append(star_data[1])
    distances.append(star_data[2])
    masses.append(star_data[3])
    radiuses.append(star_data[4])
    gravity.append(star_data[12])

plt.bar(names, masses)
plt.title("Star Name vs Mass")
plt.xlabel("Name")
plt.ylabel("Mass")
plt.show()

plt.bar(names, radiuses)
plt.title("Star Name vs Radius")
plt.xlabel("Name")
plt.ylabel("Radius")
plt.show()

plt.bar(names, distances)
plt.title("Star Name vs Distance")
plt.xlabel("Name")
plt.ylabel("Distance")
plt.show()

plt.bar(names, gravity)
plt.title("Star Name vs Gravity")
plt.xlabel("Name")
plt.ylabel("Gravity")
plt.show()
