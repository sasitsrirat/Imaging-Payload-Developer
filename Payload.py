import matplotlib.pyplot as plt
from numpy import array as np
from pandas import DataFrame
from random import randint


numbera = [] #focal
numberb = [] #alt
numberc = [] #gsd
numberd = [] #altd
numbere = []
numberf = []

#Pixel size and Sensor
pxp = 0.0000053 #Refer from Pentax 645Z
size = 7000.00


#Focal Length
print("_______________________________________________________________")
gsd = float(input("Maximum gsd(m) = ? :  "))
alt = float(input("Minimum Altitude(m) = ? :  "))
print("_______________________________________________________________")
print("F.Length @ %.3f  \t\tAltitude"% gsd)
for i in range(31):
    n = 10000
    f = ((alt+(n*i)) * pxp / gsd)
    altd = (alt + (n * i))
    print("%d.) %.3f m \t\t %.3f m" % (i,f,altd))
    #เก็บค่า
    a = float((f))
    numbera.append(a)
    b = float((altd))
    numberb.append(b)
print("_______________________________________________________________")
#GSD and Coverage Area
fol = float(input("Set focal length (m) = ? : "))
alt = float(input("Start Altitude(m) = ? :  "))
print("_______________________________________________________________")
print("GSD   \t\t\t\tAltitude \t\t\t\tCoverage Area ")
for i in range(31):
    n = 10000
    altd = (alt - (n * i))
    gsd = ((alt-(n*i)) * pxp / fol)
    carea = gsd*size
    print("%d.) %.3f m \t\t%.3f m \t\t%.3f m x %.3f m" %(i,gsd,altd,carea,carea))
    #เก็บค่า
    c = float((gsd))
    numberc.append(c)
    d = float((altd))
    numberd.append(d)
    e = float((carea))
    numbere.append(e)
print("_______________________________________________________________")
print("================Develop for Gistda Project 2021================")

#print(numberc) #gsd
#print(numberd) #altd
#print(numbere[0:5]) #carea
#print('Min number = %d' % min(numbere>6500))
print("")

plt.xlabel("Altitude (m)")
plt.ylabel("Focal Length (m)")
plt.scatter(numberb, numbera, c='r', label='Focal Length')
plt.plot(numberb,numbera)
plt.legend()
plt.grid()
plt.show()

plt.xlabel("GSD (m)")
plt.ylabel("Altitude (m)")
plt.scatter(numberc, numberd, c='r', label='GSD')
plt.plot(numberc,numberd)
plt.legend()
plt.grid()
plt.axis([max(numberc),min(numberc),min(numberd),max(numberd)]) #inverseแกน
plt.show()

plt.ylabel("GSD (m)")
plt.xlabel("Coverage Area (km)")
plt.scatter(numbere, numberc, c='c', label='Coverage Area')
plt.plot(numbere,numberc)
plt.axis([max(numbere),min(numbere),min(numberc),max(numberc)]) #inverseแกน
plt.legend()
plt.grid()
plt.show()

print("\n")
