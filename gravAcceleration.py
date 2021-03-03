import particle
import numpy as np

def gravPotential(x, y, z, m, point):
    particles = []
    phi = 0.0
    file1 = open("particleSmall.txt", "r")
    for line in file1:
        x, y, z, m = line.split(" ") 
        #p = particle.Particle(x, y, z, m)
        particles.append(particle.Particle())
    for p in particles:
        r = math.sqrt((p.x - point(0))**2 + (p.y - point(1))**2 + (p.z - point(2))**2)
        phi += -G*p.mass/r
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

x, y, z = input("Where do you want to calculate the gravitational acceleration?: ").split(" ")
x = float(x)
y = float(y)
z = float(z)
point.extend([x, y, z])

m = 0
f_x = 0
f_y = 0
f_z = 0
phi = gravPotential(x, y, z, m, point)

f = phi
i = 0
f_x = centraldifferencegrav3D(f, x_1, x_2, h, i, particles)

i = 1
f_y = centraldifferencegrav3D(f, x_1, x_2, h, i, particles)

i = 2
f_z = centraldifferencegrav3D(f, x_1, x_2, h, i, particles)

gradient = [f_x, f_y, f_z]

masstotal = 0
for p in particles:
    masstotal += particles.m


acceleration = [0, 0, 0]
acceleration = gradient/masstotal

print(str(acceleration))


    
