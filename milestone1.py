import math

def read_file_value_alone(filename, value_name):
  with open(filename, "r") as f:
    for line in f:
      words = line.split()
      for word in words:
        if word == value_name:
          return word

  return None

wdr = read_file_value_alone("Testcase1.txt", "WaferDiameter")
npr = read_file_value_alone("Testcase1.txt", "NumberOfPoints")
Angler = read_file_value_alone("Testcase1.txt","Angle")

print(wdr,npr)

wd = int(input())
n_p = int(input())
Angle = float(input())
Angle_r = Angle * (3.14 / 180)
start_x , start_y = 0 , 0

r = wd/2

"""

r_np = n_p/2
x = start_x + r*math.cos(Angle)
y = start_y + r*math.sin(Angle)
"""
distance_bw_the_points = wd/(n_p)

x = start_x + r*math.cos(Angle_r)
y = start_y + r*math.sin(Angle_r)
print(x,y)


with open("outputtrial.txt", "w") as f1:
    for i in range(0,n_p):
        start_x_x = distance_bw_the_points*math.cos(Angle_r)
        start_y_y =  distance_bw_the_points*math.sin(Angle_r)
        f1.writelines(str((start_x_x,start_y_y)))
        f1.write('\n')
        
        if start_x_x == x or start_x_x > x  and start_y_y == y or start_y_y > y:
           break


'''
r = wd/2
print(x1,y1)
print(x,y)
'''
'''
for i in range(0,wd):
     print(r*math.sin(Angle) , r*math.cos(Angle))
'''     