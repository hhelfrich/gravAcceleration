import particle
import numpy as np
import math

class Location:
    def __init__(self, X, Y, Z):
        self.X = X 
        self.Y = Y
        self.Z = Z
    
G = 6.67*10**-11
h = .000002
particles = []
file1 = open("particlesLarge.txt", "r")
for line in file1:
    x, y, z, m = line.split(" ") 
    x = float(x)
    y = float(y)
    z = float(z)
    m = float(m)
    #p = particle.Particle(x, y, z, m)
    particles.append(particle.Particle(x, y, z, m))
file1.close()

def gravPotential(point, particles):
    phi = 0.0
    file1 = open("particleSmall.txt", "r")
    for p in particles:
        r = math.sqrt((p.x - point[0])**2 + (p.y - point[1])**2 + (p.z - point[2])**2)
        phi += -G*p.m/r
    return phi

def centraldifferencegrav3D(f, point, h, i, particles):
    x_1 = [0,0,0]
    x_2 = [0,0,0]
    for j in range(0,3):
        x_1[j] = point[j]
        x_2[j] = point[j]
        if (j == i):
            x_1[j] -= h/2
            x_2[j] += h/2
    return (f(x_2, particles) - f(x_1, particles))/h

point = []
for p in particles:
    point.extend([p.x, p.y, p.z])
#a, b, c = input("Where do you want to calculate the gravitational acceleration?: ").split(" ")
#a = float(a)
#b = float(b)
#c = float(c)
#point = np.array([a, b, c])
#point.extend([a, b, c])

x = 0
y = 0
z = 0
m = 0
f_x = 0
f_y = 0
f_z = 0
gradient = []
#phi = gravPotential(point, particles)
f = gravPotential(point, particles)
for position in point:

    i = 0
    f_x = centraldifferencegrav3D(gravPotential, position., h, i, particles)

    i = 1
    f_y = centraldifferencegrav3D(gravPotential, position, h, i, particles)

    i = 2
    f_z = centraldifferencegrav3D(gravPotential, position, h, i, particles)

    gradient.extend([f_x, f_y, f_z])

#masstotal = 0
#for p in particles:
    #masstotal += p.m

acceleration = gradient

print(str(acceleration))