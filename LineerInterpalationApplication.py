# Known data points
x1 = 10.00  # 10:00
y1 = 18.00  # 18°C
x2 = 12.00  # 12:00
y2 = 24.00  # 24°C

# Target point (11:15 -> 11.25 in decimal hours)
x = 11.25

# Linear interpolation formula
y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)

# Display result
print(f"Estimated temperature at 11:15: {y:.2f} °C")

#You can use this topic any lineer situtaion