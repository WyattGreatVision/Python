from time import sleep


#Force is in Newtons F = M*A
Force = 0
#Mass is in Kg 
Mass = 0
#Acceleration is Meters / Sec^2
Acceleration = 0
#Delta is in Meters
Delta = 100
#Time is in Seconds
Time = 10
#Velocity is in Meters / Sec
Velocity = 0
#DvDt is the chnge in velocity per second
DvDt = 10



#Constants 
S = 1
M = 5
L = 10
XL = 25
XXL = 50
XXXL = 100

Gravity = 9.8




def calcForce(mass, acceleration):
    Force = mass * acceleration
    return Force

def calcVelocity(delta, time):
    Velocity = delta/time
    return Velocity

def calcAcceleration(DvDt, Time):
    Acceleration = delta/time
    return Velocity  

def calcAcceleration(dvdt, time):
    Acceleration = dvdt/time
    return Acceleration

    
#Acceleration = Gravity

Velocity = calcVelocity(Delta, Time)
print("The calculated Velocity is: ",Velocity, " M/s")
sleep(1)

Acceleration = calcAcceleration(DvDt, Time)
print("Acceleration set to: " ,Acceleration, " M/s^2")
sleep(1)

Mass = L
print("Mass set to: ", Mass, " Kg")
sleep(1)

Force = calcForce(Mass, Acceleration)
print("The calculated Force is: ",Force, " Newtons")
sleep(1)






