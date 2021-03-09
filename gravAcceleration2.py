import particle
import numpy as np
import math
    
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
    file1 = open("particlesLarge.txt", "r")
    for p in particles:
        if math.sqrt((p.x - point[0])**2 + (p.y - point[1])**2 + (p.z - point[2])**2) > h/2:
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
#f = gravPotential(point, particles)
for p in particles:
    pos = np.array([p.x, p.y, p.z])

    i = 0
    f_x = centraldifferencegrav3D(gravPotential, pos, h, i, particles)

    i = 1
    f_y = centraldifferencegrav3D(gravPotential, pos, h, i, particles)

    i = 2
    f_z = centraldifferencegrav3D(gravPotential, pos, h, i, particles)

    gradient.append([f_x, f_y, f_z])

#acceleration = gradient

outFile = open("gravAcceleration.txt", "w")
outFile.write(str(gradient))
outFile.close()
