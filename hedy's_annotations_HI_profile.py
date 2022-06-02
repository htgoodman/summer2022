import numpy as np 
import matplotlib.pyplot as plt

#Model for HI profile. 

#begin symmetric, idealized parameters 

#total mass
mHI = 10 #log (MHI/Msun) 
#mass of atomic hydrogen: from stevens et al. this appears as MHI/Msun 
print('log (m_HI/m_solar) = ', mHI)

#surface density parameters (i.e. mass per unit area)
E0 = 10.0 # units M_sun*pc^(-2), central Hi surface density 
Ec = 1.0 # units M_sun*pc^(-2)
# Equation 6 Stevens et al. log(HI_0) = log_10(E0) - log(E0/Ec) * r

#diameter of the hydrogen
logDHI = 0.5*mHI - 3.236 #log(DHI/1kpc) 
rHI = (10**logDHI)/2 #HI radius in kps
# Equation 4
#rs = rHi/( np.log(E0/Ec) )
#print('Exponential scale radius, rs =', rs)
print('HI radius: ', rHI)
r = np.arange(0, 2, 0.02) #r/rHI
#rrs = np.log(E0/Ec)*r

#units M_sun*pc^(-2) - HI surface density at a given radius.  
logEHI = np.log10(E0) - np.log(E0/Ec)*r
#plt.plot(r,logEHI)
#plt.xlabel('r/rHI')
#plt.ylabel('log Sigma HI')

Vc = 250 # mHi + Ms, in units of M_sun
Rt = 2 # in kpc
sout = 0
print('Rotation curve parameters, Vc; Rt and sout', Vc, Rt, sout)

r_Rt = (rHI*r)/Rt
#print('Division, r/Rt =', r_Rt)

Vr = Vc * np.tanh(r_Rt) + sout*r
#print('Rotation Curve fucnction, V(r) =', Vr)
#plt.plot(r, Vr, 'y')
#plt.title('Rotation Curve')
#plt.xlabel('r/RHI')
#plt.ylabel('V(r) [km s^(-1)]')

#Inclination in degrees
inc=80.0
print('Inclination',inc)

dr = 0.02
drpc = dr*rHI*1000
radius = np.arange(0, 2, dr) #r/rHI
dphi = 0.1
phideg= np.arange(0,360,dphi) #aximuth angle in degrees

HImass = []
LOSvel = []

for r in radius: 
    for phi in phideg: 
        #Area in pc^2
        rpc = r*rHI*1000
        Area = rpc*drpc*dphi*np.pi/180.0
            
        #Surface density of HI units M_sun*pc^(-2) - HI surface density at a given radius.  
        logEHI = np.log10(E0) - np.log(E0/Ec)*r
        
        #Mass HI in area segment
        MassHI = Area*(10**logEHI)

        # Circular velocity
        r_Rt = (rHI*r)/Rt
        Vr = Vc * np.tanh(r_Rt) + sout*r
        
        #LOS velocity
        vlos = Vr*np.sin(inc*np.pi/180.0)*np.cos(phi*np.pi/180.0)

        
        HImass.append(MassHI)
        LOSvel.append(vlos)
        

HImass=np.array(HImass)
LOSvel=np.array(LOSvel)
        
#print(LOSvel)
        
dv=5
minvel=-Vc-50.0
maxvel=Vc+50.0
channels = np.arange(minvel,maxvel,2*dv)

Flux=[]

for vel in channels:
        minv=vel-dv
        maxv=vel+dv
        #Slice1=HImass[(LOSvel>minv)]
        #vel=LOSvel[(LOSvel>minv)]
        #Slice2=Slice1[(vel<maxv)]
        totalmass=sum(HImass[(LOSvel>minv)&(LOSvel<maxv)])

        Flux.append(totalmass)
        
        
#print(channels)
#print(Flux)
plt.plot(channels,Flux)

plt.show()
