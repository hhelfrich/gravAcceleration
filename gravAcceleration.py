import particle
import numpy as np

def gravPotential(x, y, z, m, Particle):
    particles = []
    phi = 0.0
    file1 = open("particleSmall.txt", "r")
    for line in file1:
        x, y, z, m = line.split(" ") 
        p = Particle(x, y, z, m)
        particles.append(p)
    for particle in particles:
        r = math.sqrt((particle.x - point.x)**2 + (particle.y - point.y)**2 + (particle.z - point.z)**2)
        phi += -G*particle.mass/r
    return phi

def centraldifferencegrav3D(f, x, y, z, h, i, particles):
    i = 0
    x_1 = [0,0,0]
    x_2 = [0,0,0]
    for j in range(0,3):
        x_1[j] = point[j]
        if (j == i):
            x_1[j] -= h/2
            x_2[j] += h/2
    return (f(x_2, particles) - f(x_1, particles))/h

point = []
x, y, z = float(input("Where do you want to calculate the gravitational acceleration?: ").split(" ")
po = Point(x, y, z)
point.append(po)

f_x = 0
f_y = 0
f_z = 0
phi = gravPotential(x, y, z, m, Particle)

f = phi
i = 0
f_x = centraldifferencegrav3D(f, x_1, x_2, h, i, particles)

i = 1
f_y = centraldifferencegrav3D(f, x_1, x_2, h, i, particles)

i = 2
f_z = centraldifferencegrav3D(f, x_1, x_2, h, i, particles)

gradient = [f_x, f_y, f_z]

masstotal = 0
for particle in particles:
    masstotal += particle.m


acceleration = [0, 0, 0]
acceleration = gradient/masstotal

print(str(acceleration))


    
