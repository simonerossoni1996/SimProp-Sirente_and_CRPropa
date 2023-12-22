import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# Data loading
data = np.genfromtxt("events_evolv.txt")

# Data reading 
logE = np.log10(data[:,3]) + 18.0
logE0 = np.log10(data[:,5]) + 18.0

# Weigths creation
w = np.zeros(len(logE))
for i in np.arange(len(logE)) :
    w[i] = ((10.0**logE0[i])**(-2.6))/((10.0**logE0[i])**(-1.0))

# Energy parameters
logE_min = np.log10(1e16)
logE_max = 22.0
dlogE = 0.05
log_bin = np.arange(logE_min,logE_max+dlogE,dlogE)
lE_cen = (log_bin[1:]+log_bin[:-1])/2.0
dE = 10.0**log_bin[1:]-10.0**log_bin[:-1]

# Energy histogram
hist_E = plt.hist(logE,bins=log_bin,weights=w)[0]/(dE*sum(w))

# Histogram saving
f = open("spectrum.txt","w")
row = ""
for j in (np.arange(len(hist_E))) :
    row = row + str(hist_E[j]) + " "
    row = row + "\n"
    f.write(row)
f.close()

# Beniamino
data_b = np.genfromtxt("Beniamino_spectrum_noCutoff_2.6_0_3.txt")
E_b = data_b[:,0]
hist_b = data_b[:,1]

# Scaling for Beniamino
N = hist_E[0]/hist_b[0]
hist_b = N*hist_b

# Plot generation 
x = lE_cen
plt.plot(10.0**x,((10.0**x)**3.0)*hist_E,"kv",markersize=3,label="CRPropa")
plt.plot(E_b,((E_b)**3.0)*hist_b,"r",markersize=3,label="SimProp-Beniamino")
plt.axis([1e17,1e21,1e30,1e34])
plot_title = "Energy Spectrum"
plt.title(plot_title)
plt.yscale("log")
plt.xscale("log")
plt.ylabel("$E^{3}/N dN/dE$ (eV$^2$)")
plt.xlabel("E (eV)")
plt.legend(loc="upper right")

# Plot saving
plt.savefig("spectrum.pdf")
