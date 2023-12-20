from crpropa import *
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

m_p = 1e9       # eV
c = 3e8         # m/s

energy_low = 16.0
energy_high = 22.0
energy_space = 0.05
energy = np.arange(energy_low,energy_high+energy_space,energy_space)


one_over_beta_pp_p_cmb_0 = np.zeros(len(energy))          # m
one_over_beta_pp_p_ebl_0 = np.zeros(len(energy))          # m
one_over_beta_pi_p_cmb_0 = np.zeros(len(energy))          # m
one_over_beta_pi_p_ebl_0 = np.zeros(len(energy))          # m

one_over_beta_pp_p_cmb_05 = np.zeros(len(energy))          # m
one_over_beta_pp_p_ebl_05 = np.zeros(len(energy))          # m
one_over_beta_pi_p_cmb_05 = np.zeros(len(energy))          # m
one_over_beta_pi_p_ebl_05 = np.zeros(len(energy))          # m

one_over_beta_pp_p_cmb_1 = np.zeros(len(energy))          # m
one_over_beta_pp_p_ebl_1 = np.zeros(len(energy))          # m
one_over_beta_pi_p_cmb_1 = np.zeros(len(energy))          # m
one_over_beta_pi_p_ebl_1 = np.zeros(len(energy))          # m

one_over_beta_pp_p_cmb_2 = np.zeros(len(energy))          # m
one_over_beta_pp_p_ebl_2 = np.zeros(len(energy))          # m
one_over_beta_pi_p_cmb_2 = np.zeros(len(energy))          # m
one_over_beta_pi_p_ebl_2 = np.zeros(len(energy))          # m

one_over_beta_pp_p_cmb_3 = np.zeros(len(energy))          # m
one_over_beta_pp_p_ebl_3 = np.zeros(len(energy))          # m
one_over_beta_pi_p_cmb_3 = np.zeros(len(energy))          # m
one_over_beta_pi_p_ebl_3 = np.zeros(len(energy))          # m

one_over_beta_pp_p_cmb_5 = np.zeros(len(energy))          # m
one_over_beta_pp_p_ebl_5 = np.zeros(len(energy))          # m
one_over_beta_pi_p_cmb_5 = np.zeros(len(energy))          # m
one_over_beta_pi_p_ebl_5 = np.zeros(len(energy))          # m

one_over_beta_pp_p_cmb_10 = np.zeros(len(energy))          # m
one_over_beta_pp_p_ebl_10 = np.zeros(len(energy))          # m
one_over_beta_pi_p_cmb_10 = np.zeros(len(energy))          # m
one_over_beta_pi_p_ebl_10 = np.zeros(len(energy))          # m

k=0
for e in energy :
	one_over_beta_pp_p_cmb_0[k] = ElectronPairProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,0.0)
	one_over_beta_pp_p_ebl_0[k] = ElectronPairProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,0.0)
	one_over_beta_pi_p_cmb_0[k] = PhotoPionProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,0.0)
	one_over_beta_pi_p_ebl_0[k] = PhotoPionProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,0.0)
        
        one_over_beta_pp_p_cmb_05[k] = ElectronPairProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,0.5)
        one_over_beta_pp_p_ebl_05[k] = ElectronPairProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,0.5)
        one_over_beta_pi_p_cmb_05[k] = PhotoPionProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,0.5)
        one_over_beta_pi_p_ebl_05[k] = PhotoPionProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,0.5)

        one_over_beta_pp_p_cmb_1[k] = ElectronPairProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,1.0)
        one_over_beta_pp_p_ebl_1[k] = ElectronPairProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,1.0)
        one_over_beta_pi_p_cmb_1[k] = PhotoPionProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,1.0)
        one_over_beta_pi_p_ebl_1[k] = PhotoPionProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,1.0)

        one_over_beta_pp_p_cmb_2[k] = ElectronPairProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,2.0)
        one_over_beta_pp_p_ebl_2[k] = ElectronPairProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,2.0)
        one_over_beta_pi_p_cmb_2[k] = PhotoPionProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,2.0)
        one_over_beta_pi_p_ebl_2[k] = PhotoPionProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,2.0)

        one_over_beta_pp_p_cmb_3[k] = ElectronPairProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,3.0)
        one_over_beta_pp_p_ebl_3[k] = ElectronPairProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,3.0)
        one_over_beta_pi_p_cmb_3[k] = PhotoPionProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,3.0)
        one_over_beta_pi_p_ebl_3[k] = PhotoPionProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,3.0)

        one_over_beta_pp_p_cmb_5[k] = ElectronPairProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,5.0)
        one_over_beta_pp_p_ebl_5[k] = ElectronPairProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,5.0)
        one_over_beta_pi_p_cmb_5[k] = PhotoPionProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,5.0)
        one_over_beta_pi_p_ebl_5[k] = PhotoPionProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,5.0)

        one_over_beta_pp_p_cmb_10[k] = ElectronPairProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,10.0)
        one_over_beta_pp_p_ebl_10[k] = ElectronPairProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,10.0)
        one_over_beta_pi_p_cmb_10[k] = PhotoPionProduction(CMB()).lossLength(nucleusId(1,1),(10.0**e)/m_p,10.0)
        one_over_beta_pi_p_ebl_10[k] = PhotoPionProduction(IRB_Dominguez11()).lossLength(nucleusId(1,1),(10.0**e)/m_p,10.0)

	k += 1
	msg = "Energy-log : "+str(e)+" (eV)"
	print(msg)

# Conversions 
one_over_beta_pp_p_cmb_0 = one_over_beta_pp_p_cmb_0/Mpc              # Mpc
one_over_beta_pp_p_ebl_0 = one_over_beta_pp_p_ebl_0/Mpc              # Mpc
one_over_beta_pi_p_cmb_0 = one_over_beta_pi_p_cmb_0/Mpc              # Mpc
one_over_beta_pi_p_ebl_0 = one_over_beta_pi_p_ebl_0/Mpc              # Mpc
#one_over_beta_pp_p = ((one_over_beta_pp_p_cmb)**(-1.0)+(one_over_beta_pp_p_ebl)**(-1.0))**(-1.0)
#one_over_beta_pi_p = ((one_over_beta_pi_p_cmb)**(-1.0)+(one_over_beta_pi_p_ebl)**(-1.0))**(-1.0)
#one_over_beta_p = ((one_over_beta_ad)**(-1.0)+(one_over_beta_pp_p_cmb)**(-1.0)+(one_over_beta_pp_p_ebl)**(-1.0)+(one_over_beta_pi_p_cmb)**(-1.0)+(one_over_beta_pi_p_ebl)**(-1.0))**(-1.0)

one_over_beta_pp_p_cmb_05 = one_over_beta_pp_p_cmb_05/Mpc              # Mpc
one_over_beta_pp_p_ebl_05 = one_over_beta_pp_p_ebl_05/Mpc              # Mpc
one_over_beta_pi_p_cmb_05 = one_over_beta_pi_p_cmb_05/Mpc              # Mpc
one_over_beta_pi_p_ebl_05 = one_over_beta_pi_p_ebl_05/Mpc              # Mpc

one_over_beta_pp_p_cmb_1 = one_over_beta_pp_p_cmb_1/Mpc              # Mpc
one_over_beta_pp_p_ebl_1 = one_over_beta_pp_p_ebl_1/Mpc              # Mpc
one_over_beta_pi_p_cmb_1 = one_over_beta_pi_p_cmb_1/Mpc              # Mpc
one_over_beta_pi_p_ebl_1 = one_over_beta_pi_p_ebl_1/Mpc              # Mpc

one_over_beta_pp_p_cmb_2 = one_over_beta_pp_p_cmb_2/Mpc              # Mpc
one_over_beta_pp_p_ebl_2 = one_over_beta_pp_p_ebl_2/Mpc              # Mpc
one_over_beta_pi_p_cmb_2 = one_over_beta_pi_p_cmb_2/Mpc              # Mpc
one_over_beta_pi_p_ebl_2 = one_over_beta_pi_p_ebl_2/Mpc              # Mpc

one_over_beta_pp_p_cmb_3 = one_over_beta_pp_p_cmb_3/Mpc              # Mpc
one_over_beta_pp_p_ebl_3 = one_over_beta_pp_p_ebl_3/Mpc              # Mpc
one_over_beta_pi_p_cmb_3 = one_over_beta_pi_p_cmb_3/Mpc              # Mpc
one_over_beta_pi_p_ebl_3 = one_over_beta_pi_p_ebl_3/Mpc              # Mpc

one_over_beta_pp_p_cmb_5 = one_over_beta_pp_p_cmb_5/Mpc              # Mpc
one_over_beta_pp_p_ebl_5 = one_over_beta_pp_p_ebl_5/Mpc              # Mpc
one_over_beta_pi_p_cmb_5 = one_over_beta_pi_p_cmb_5/Mpc              # Mpc
one_over_beta_pi_p_ebl_5 = one_over_beta_pi_p_ebl_5/Mpc              # Mpc

one_over_beta_pp_p_cmb_10 = one_over_beta_pp_p_cmb_10/Mpc              # Mpc
one_over_beta_pp_p_ebl_10 = one_over_beta_pp_p_ebl_10/Mpc              # Mpc
one_over_beta_pi_p_cmb_10 = one_over_beta_pi_p_cmb_10/Mpc              # Mpc
one_over_beta_pi_p_ebl_10 = one_over_beta_pi_p_ebl_10/Mpc              # Mpc

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
plt.legend(loc="lower right",ncol=2)

# Plot saving
plt.savefig("typical_lengths_pp_cmb.pdf")
plt.close()

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
plt.legend(loc="lower right",ncol=2)

# Plot saving
plt.savefig("typical_lengths_pp_ebl.pdf")
plt.close()

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
plt.legend(loc="lower left",ncol=2)

# Plot saving
plt.savefig("typical_lengths_pi_cmb.pdf")
plt.close()

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
plt.legend(loc="lower right",ncol=2)

# Plot saving
plt.savefig("typical_lengths_pi_ebl.pdf")
plt.close()
