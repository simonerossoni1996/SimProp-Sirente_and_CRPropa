from crpropa import *
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# Parameters
m_p = 1e9       # eV
c = 3e8         # m/s

# Energy range
energy_low = 16.0
energy_high = 22.0
energy_space = 0.05

# Pair production CMB
# Loading data
data = np.genfromtxt("energy_loss_length-pair_production-cmb-p.txt")
energy = data[:,0]
one_over_beta_pp_p_cmb_0 = 10.0**data[:,1]
one_over_beta_pp_p_cmb_05 = 10.0**data[:,2]
one_over_beta_pp_p_cmb_1 = 10.0**data[:,3]
one_over_beta_pp_p_cmb_2 = 10.0**data[:,4]
one_over_beta_pp_p_cmb_3 = 10.0**data[:,5]
one_over_beta_pp_p_cmb_5 = 10.0**data[:,6]
one_over_beta_pp_p_cmb_10 = 10.0**data[:,7]

# Plot
plt.plot(10.0**energy,one_over_beta_pp_p_cmb_0,"k-",label="z=0")
plt.plot(10.0**energy,one_over_beta_pp_p_cmb_05,"r-",label="z=0.5")
plt.plot(10.0**energy,one_over_beta_pp_p_cmb_1,"b-",label="z=1")
plt.plot(10.0**energy,one_over_beta_pp_p_cmb_2,"g-",label="z=2")
plt.plot(10.0**energy,one_over_beta_pp_p_cmb_3,"y-",label="z=3")
plt.plot(10.0**energy,one_over_beta_pp_p_cmb_5,"c-",label="z=5")
plt.plot(10.0**energy,one_over_beta_pp_p_cmb_10,"m-",label="z=10")
plt.axis([10.0**16.0,10.0**energy_high,1e-3,1e6])
plt.xscale("log")
plt.yscale("log")
plot_title = "Energy Loss Lengths - Pair production CMB"
plt.title(plot_title)
plt.ylabel("Energy Loss Length (Mpc)")
plt.xlabel("Energy (eV)")
plt.legend(loc="best",ncol=2)

# Plot saving
plt.savefig("energy_loss_length-pair_production-cmb-p.pdf")
plt.close()

# Pair production EBL
# Loading data
data = np.genfromtxt("energy_loss_length-pair_production-ebl-p.txt")
energy = data[:,0]
one_over_beta_pp_p_ebl_0 = 10.0**data[:,1]
one_over_beta_pp_p_ebl_05 = 10.0**data[:,2]
one_over_beta_pp_p_ebl_1 = 10.0**data[:,3]
one_over_beta_pp_p_ebl_2 = 10.0**data[:,4]
one_over_beta_pp_p_ebl_3 = 10.0**data[:,5]
one_over_beta_pp_p_ebl_5 = 10.0**data[:,6]
one_over_beta_pp_p_ebl_10 = 10.0**data[:,7]

# Plot
plt.plot(10.0**energy,one_over_beta_pp_p_ebl_0,"k-",label="z=0")
plt.plot(10.0**energy,one_over_beta_pp_p_ebl_05,"r-",label="z=0.5")
plt.plot(10.0**energy,one_over_beta_pp_p_ebl_1,"b-",label="z=1")
plt.plot(10.0**energy,one_over_beta_pp_p_ebl_2,"g-",label="z=2")
plt.plot(10.0**energy,one_over_beta_pp_p_ebl_3,"y-",label="z=3")
plt.plot(10.0**energy,one_over_beta_pp_p_ebl_5,"c-",label="z=5")
plt.plot(10.0**energy,one_over_beta_pp_p_ebl_10,"m-",label="z=10")
plt.axis([10.0**16.0,10.0**energy_high,1e-3,1e6])
plt.xscale("log")
plt.yscale("log")
plot_title = "Energy Loss Lengths - Pair production EBL"
plt.title(plot_title)
plt.ylabel("Energy Loss Length (Mpc)")
plt.xlabel("Energy (eV)")
plt.legend(loc="best",ncol=2)

# Plot saving
plt.savefig("energy_loss_length-pair_production-ebl-p.pdf")
plt.close()

# Pion production CMB
# Loading data
data = np.genfromtxt("energy_loss_length-pion_production-cmb-p.txt")
energy = data[:,0]
one_over_beta_pi_p_cmb_0 = 10.0**data[:,1]
one_over_beta_pi_p_cmb_05 = 10.0**data[:,2]
one_over_beta_pi_p_cmb_1 = 10.0**data[:,3]
one_over_beta_pi_p_cmb_2 = 10.0**data[:,4]
one_over_beta_pi_p_cmb_3 = 10.0**data[:,5]
one_over_beta_pi_p_cmb_5 = 10.0**data[:,6]
one_over_beta_pi_p_cmb_10 = 10.0**data[:,7]

# Plot
plt.plot(10.0**energy,one_over_beta_pi_p_cmb_0,"k-",label="z=0")
plt.plot(10.0**energy,one_over_beta_pi_p_cmb_05,"r-",label="z=0.5")
plt.plot(10.0**energy,one_over_beta_pi_p_cmb_1,"b-",label="z=1")
plt.plot(10.0**energy,one_over_beta_pi_p_cmb_2,"g-",label="z=2")
plt.plot(10.0**energy,one_over_beta_pi_p_cmb_3,"y-",label="z=3")
plt.plot(10.0**energy,one_over_beta_pi_p_cmb_5,"c-",label="z=5")
plt.plot(10.0**energy,one_over_beta_pi_p_cmb_10,"m-",label="z=10")
plt.axis([10.0**16.0,10.0**energy_high,1e-3,1e6])
plt.xscale("log")
plt.yscale("log")
plot_title = "Energy Loss Lengths - Pion production CMB"
plt.title(plot_title)
plt.ylabel("Energy Loss Length (Mpc)")
plt.xlabel("Energy (eV)")
plt.legend(loc="best",ncol=2)

# Plot saving
plt.savefig("energy_loss_length-pion_production-cmb-p.pdf")
plt.close()

# Pion production EBL
# Loading data
data = np.genfromtxt("energy_loss_length-pion_production-ebl-p.txt")
energy = data[:,0]
one_over_beta_pi_p_ebl_0 = 10.0**data[:,1]
one_over_beta_pi_p_ebl_05 = 10.0**data[:,2]
one_over_beta_pi_p_ebl_1 = 10.0**data[:,3]
one_over_beta_pi_p_ebl_2 = 10.0**data[:,4]
one_over_beta_pi_p_ebl_3 = 10.0**data[:,5]
one_over_beta_pi_p_ebl_5 = 10.0**data[:,6]
one_over_beta_pi_p_ebl_10 = 10.0**data[:,7]

# Plot
plt.plot(10.0**energy,one_over_beta_pi_p_ebl_0,"k-",label="z=0")
plt.plot(10.0**energy,one_over_beta_pi_p_ebl_05,"r-",label="z=0.5")
plt.plot(10.0**energy,one_over_beta_pi_p_ebl_1,"b-",label="z=1")
plt.plot(10.0**energy,one_over_beta_pi_p_ebl_2,"g-",label="z=2")
plt.plot(10.0**energy,one_over_beta_pi_p_ebl_3,"y-",label="z=3")
plt.plot(10.0**energy,one_over_beta_pi_p_ebl_5,"c-",label="z=5")
plt.plot(10.0**energy,one_over_beta_pi_p_ebl_10,"m-",label="z=10")
plt.axis([10.0**16.0,10.0**energy_high,1e-3,1e6])
plt.xscale("log")
plt.yscale("log")
plot_title = "Energy Loss Lengths - Pion production EBL"
plt.title(plot_title)
plt.ylabel("Energy Loss Length (Mpc)")
plt.xlabel("Energy (eV)")
plt.legend(loc="best",ncol=2)

# Plot saving
plt.savefig("energy_loss_length-pion_production-ebl-p.pdf")
plt.close()
