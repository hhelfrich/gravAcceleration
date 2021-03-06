import particle
import numpy as np
import math

G = 6.67E-11
h = 1E-8
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
        if (r > h/2):   
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

a, b, c = input("Where do you want to calculate the gravitational acceleration?: ").split(" ")
a = float(a)
b = float(b)
c = float(c)
point = np.array([a, b, c])
#point.extend([a, b, c])

x = 0
y = 0
z = 0
m = 0
f_x = 0
f_y = 0
f_z = 0
#phi = gravPotential(point, particles)

f = gravPotential(point, particles)

f_x = centraldifferencegrav3D(gravPotential, point, h, 0, particles)

f_y = centraldifferencegrav3D(gravPotential, point, h, 1, particles)

f_z = centraldifferencegrav3D(gravPotential, point, h, 2, particles)

gradient = [f_x, f_y, f_z]

#masstotal = 0
#for p in particles:
    #masstotal += p.m


acceleration = [0, 0, 0]
acceleration = gradient

print(str(acceleration))