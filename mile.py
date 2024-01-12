
"""
def find_equidistant_points_along_line(diameter, n):
    d_step = diameter / (n - 1)

    equidistant_points = []
    for i in range(1, n + 1):
        x_i = (i - 1) * d_step - diameter / 2
        y_i = 0

        equidistant_points.append((x_i, y_i))

    return equidistant_points

# Example usage:
diameter = 300
n = 30
result = find_equidistant_points_along_line(diameter, n)
print(result)

"""
import math

def read_file_values(filename):
    wafer_diameter = None
    n = None
    angle = None
    
    with open(filename, "r") as f:
        for line in f:
            key, value = line.strip().split(":")
            key = key.strip()
            value = value.strip()
            
            if key == "WaferDiameter":
                wafer_diameter = int(value)
            elif key == "NumberOfPoints":
                n = int(value)
            elif key == "Angle":
                angle = float(value)

    return wafer_diameter, n, angle

# Example usage:
filename = "Testcase1.txt"
wafer_diameter, n, angle = read_file_values(filename)

print("Wafer Diameter:", wafer_diameter)
print("Number of Points:", n)
print("Angle:", angle)

"""
diameter = 200
angle = 150
n = 31
"""



def line(start, stop, num_points):
    step = (stop - start) / (num_points - 1)
    return [start + i * step for i in range(num_points)]

def find_equidistant_points_with_angle(diameter, angle, n):
    r = diameter / 2.0
    distances = line(-r, r, n)
    
    x_coords = [d * math.cos(math.radians(angle)) for d in distances]
    y_coords = [d * math.sin(math.radians(angle)) for d in distances]
    
    return x_coords, y_coords

x, y = find_equidistant_points_with_angle(wafer_diameter, angle, n)

with open("outputtrial.txt", 'w') as file:
    for i in range(n):
        file.write(f"({x[i]:.4f}, {y[i]:.4f})\n")

