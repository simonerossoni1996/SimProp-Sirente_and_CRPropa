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
energy = np.arange(energy_low,energy_high+energy_space,energy_space)

# Vectors definition
# z=0
#int_length_pp_p_cmb_0 = np.zeros(len(energy))          # m
#int_length_pp_p_ebl_0 = np.zeros(len(energy))          # m
int_length_pi_p_cmb_0 = np.zeros(len(energy))          # m
int_length_pi_p_ebl_0 = np.zeros(len(energy))          # m
# z=0.5
#int_length_pp_p_cmb_05 = np.zeros(len(energy))          # m
#int_length_pp_p_ebl_05 = np.zeros(len(energy))          # m
int_length_pi_p_cmb_05 = np.zeros(len(energy))          # m
int_length_pi_p_ebl_05 = np.zeros(len(energy))          # m
# z=1
#int_length_pp_p_cmb_1 = np.zeros(len(energy))          # m
#int_length_pp_p_ebl_1 = np.zeros(len(energy))          # m
int_length_pi_p_cmb_1 = np.zeros(len(energy))          # m
int_length_pi_p_ebl_1 = np.zeros(len(energy))          # m
# z=2
#int_length_pp_p_cmb_2 = np.zeros(len(energy))          # m
#int_length_pp_p_ebl_2 = np.zeros(len(energy))          # m
int_length_pi_p_cmb_2 = np.zeros(len(energy))          # m
int_length_pi_p_ebl_2 = np.zeros(len(energy))          # m
# z=3
#int_length_pp_p_cmb_3 = np.zeros(len(energy))          # m
#int_length_pp_p_ebl_3 = np.zeros(len(energy))          # m
int_length_pi_p_cmb_3 = np.zeros(len(energy))          # m
int_length_pi_p_ebl_3 = np.zeros(len(energy))          # m
# z=5
#int_length_pp_p_cmb_5 = np.zeros(len(energy))          # m
#int_length_pp_p_ebl_5 = np.zeros(len(energy))          # m
int_length_pi_p_cmb_5 = np.zeros(len(energy))          # m
int_length_pi_p_ebl_5 = np.zeros(len(energy))          # m
# z=10
#int_length_pp_p_cmb_10 = np.zeros(len(energy))          # m
#int_length_pp_p_ebl_10 = np.zeros(len(energy))          # m
int_length_pi_p_cmb_10 = np.zeros(len(energy))          # m
int_length_pi_p_ebl_10 = np.zeros(len(energy))          # m

# Extraction loop
k=0
for e in energy :
	#int_length_pp_p_cmb_0[k] = ElectronPairProduction(CMB()).nucleonMFP((10.0**e)/m_p,0.0,True)
	#int_length_pp_p_ebl_0[k] = ElectronPairProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,0.0,True)
	int_length_pi_p_cmb_0[k] = PhotoPionProduction(CMB()).nucleonMFP((10.0**e)/m_p,0.0,True)
	int_length_pi_p_ebl_0[k] = PhotoPionProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,0.0,True)
        
        #int_length_pp_p_cmb_05[k] = ElectronPairProduction(CMB()).nucleonMFP((10.0**e)/m_p,0.5,True)
        #int_length_pp_p_ebl_05[k] = ElectronPairProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,0.5,True)
        int_length_pi_p_cmb_05[k] = PhotoPionProduction(CMB()).nucleonMFP((10.0**e)/m_p,0.5,True)
        int_length_pi_p_ebl_05[k] = PhotoPionProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,0.5,True)

        #int_length_pp_p_cmb_1[k] = ElectronPairProduction(CMB()).nucleonMFP((10.0**e)/m_p,1.0,True)
        #int_length_pp_p_ebl_1[k] = ElectronPairProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,1.0,True)
        int_length_pi_p_cmb_1[k] = PhotoPionProduction(CMB()).nucleonMFP((10.0**e)/m_p,1.0,True)
        int_length_pi_p_ebl_1[k] = PhotoPionProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,1.0,True)

        #int_length_pp_p_cmb_2[k] = ElectronPairProduction(CMB()).nucleonMFP((10.0**e)/m_p,2.0,True)
        #int_length_pp_p_ebl_2[k] = ElectronPairProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,2.0,True)
        int_length_pi_p_cmb_2[k] = PhotoPionProduction(CMB()).nucleonMFP((10.0**e)/m_p,2.0,True)
        int_length_pi_p_ebl_2[k] = PhotoPionProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,2.0,True)

        #int_length_pp_p_cmb_3[k] = ElectronPairProduction(CMB()).nucleonMFP((10.0**e)/m_p,3.0,True)
        #int_length_pp_p_ebl_3[k] = ElectronPairProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,3.0,True)
        int_length_pi_p_cmb_3[k] = PhotoPionProduction(CMB()).nucleonMFP((10.0**e)/m_p,3.0,True)
        int_length_pi_p_ebl_3[k] = PhotoPionProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,3.0,True)

        #int_length_pp_p_cmb_5[k] = ElectronPairProduction(CMB()).nucleonMFP((10.0**e)/m_p,5.0,True)
        #int_length_pp_p_ebl_5[k] = ElectronPairProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,5.0,True)
        int_length_pi_p_cmb_5[k] = PhotoPionProduction(CMB()).nucleonMFP((10.0**e)/m_p,5.0,True)
        int_length_pi_p_ebl_5[k] = PhotoPionProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,5.0,True)

        #int_length_pp_p_cmb_10[k] = ElectronPairProduction(CMB()).nucleonMFP((10.0**e)/m_p,10.0,True)
        #int_length_pp_p_ebl_10[k] = ElectronPairProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,10.0,True)
        int_length_pi_p_cmb_10[k] = PhotoPionProduction(CMB()).nucleonMFP((10.0**e)/m_p,10.0,True)
        int_length_pi_p_ebl_10[k] = PhotoPionProduction(IRB_Dominguez11()).nucleonMFP((10.0**e)/m_p,10.0,True)

	k += 1
	msg = "Energy-log : "+str(e)+" (eV)"
	print(msg)

# Conversions in Mpc
# z=0   
#int_length_pp_p_cmb_0 = int_length_pp_p_cmb_0/Mpc              # Mpc
#int_length_pp_p_ebl_0 = int_length_pp_p_ebl_0/Mpc              # Mpc
int_length_pi_p_cmb_0 = int_length_pi_p_cmb_0/Mpc              # Mpc
int_length_pi_p_ebl_0 = int_length_pi_p_ebl_0/Mpc              # Mpc

# z=0.5   
#int_length_pp_p_cmb_05 = int_length_pp_p_cmb_05/Mpc              # Mpc
#int_length_pp_p_ebl_05 = int_length_pp_p_ebl_05/Mpc              # Mpc
int_length_pi_p_cmb_05 = int_length_pi_p_cmb_05/Mpc              # Mpc
int_length_pi_p_ebl_05 = int_length_pi_p_ebl_05/Mpc              # Mpc

# z=1   
#int_length_pp_p_cmb_1 = int_length_pp_p_cmb_1/Mpc              # Mpc
#int_length_pp_p_ebl_1 = int_length_pp_p_ebl_1/Mpc              # Mpc
int_length_pi_p_cmb_1 = int_length_pi_p_cmb_1/Mpc              # Mpc
int_length_pi_p_ebl_1 = int_length_pi_p_ebl_1/Mpc              # Mpc

# z=2   
#int_length_pp_p_cmb_2 = int_length_pp_p_cmb_2/Mpc              # Mpc
#int_length_pp_p_ebl_2 = int_length_pp_p_ebl_2/Mpc              # Mpc
int_length_pi_p_cmb_2 = int_length_pi_p_cmb_2/Mpc              # Mpc
int_length_pi_p_ebl_2 = int_length_pi_p_ebl_2/Mpc              # Mpc

# z=3   
#int_length_pp_p_cmb_3 = int_length_pp_p_cmb_3/Mpc              # Mpc
#int_length_pp_p_ebl_3 = int_length_pp_p_ebl_3/Mpc              # Mpc
int_length_pi_p_cmb_3 = int_length_pi_p_cmb_3/Mpc              # Mpc
int_length_pi_p_ebl_3 = int_length_pi_p_ebl_3/Mpc              # Mpc

# z=5   
#int_length_pp_p_cmb_5 = int_length_pp_p_cmb_5/Mpc              # Mpc
#int_length_pp_p_ebl_5 = int_length_pp_p_ebl_5/Mpc              # Mpc
int_length_pi_p_cmb_5 = int_length_pi_p_cmb_5/Mpc              # Mpc
int_length_pi_p_ebl_5 = int_length_pi_p_ebl_5/Mpc              # Mpc

# z=10   
#int_length_pp_p_cmb_10 = int_length_pp_p_cmb_10/Mpc              # Mpc
#int_length_pp_p_ebl_10 = int_length_pp_p_ebl_10/Mpc              # Mpc
int_length_pi_p_cmb_10 = int_length_pi_p_cmb_10/Mpc              # Mpc
int_length_pi_p_ebl_10 = int_length_pi_p_ebl_10/Mpc              # Mpc

# Data saving
# Pair production with CMB
"""
M = np.zeros((len(int_length_pp_p_cmb_0),8))
for i in (np.arange(len(int_length_pp_p_cmb_0))) :
    M[i,0] = energy[i]
    M[i,1] = np.log10(int_length_pp_p_cmb_0[i])
    M[i,2] = np.log10(int_length_pp_p_cmb_05[i])
    M[i,3] = np.log10(int_length_pp_p_cmb_1[i])
    M[i,4] = np.log10(int_length_pp_p_cmb_2[i])
    M[i,5] = np.log10(int_length_pp_p_cmb_3[i])
    M[i,6] = np.log10(int_length_pp_p_cmb_5[i])
    M[i,7] = np.log10(int_length_pp_p_cmb_10[i])
path_save_data = "energy_loss_length-pair_production-cmb-p.txt"
f = open(path_save_data,"w")
row = "# Energy loss lenght for pair production with CMB photons for protons \n"
f.write(row)
row = "# \n"
f.write(row)
row = "# Column 0: log_10 of energy (eV) \n"
f.write(row)
row = "# Column 1-7: log_10 of energy loss lengths (Mpc) for z=0, 0.5, 1, 2, 3, 5 and 10 \n"
f.write(row)
row = "# \n"
f.write(row)
row = "# \n"
f.write(row)
for i in (np.arange(len(int_length_pp_p_cmb_0))) :
    row = ""
    for j in (np.arange(8)) :
        row = row + str(M[i,j]) + " "
    row = row + "\n"
    f.write(row)
f.close()

# Pair production with EBL
M = np.zeros((len(int_length_pp_p_ebl_0),8))
for i in (np.arange(len(int_length_pp_p_ebl_0))) :
    M[i,0] = energy[i]
    M[i,1] = np.log10(int_length_pp_p_ebl_0[i])
    M[i,2] = np.log10(int_length_pp_p_ebl_05[i])
    M[i,3] = np.log10(int_length_pp_p_ebl_1[i])
    M[i,4] = np.log10(int_length_pp_p_ebl_2[i])
    M[i,5] = np.log10(int_length_pp_p_ebl_3[i])
    M[i,6] = np.log10(int_length_pp_p_ebl_5[i])
    M[i,7] = np.log10(int_length_pp_p_ebl_10[i])
path_save_data = "energy_loss_length-pair_production-ebl-p.txt"
f = open(path_save_data,"w")
row = "# Energy loss lenght for pair production with EBL photons (Dominguez 11) for protons \n"
f.write(row)
row = "# \n"
f.write(row)
row = "# Column 0: log_10 of energy (eV) \n"
f.write(row)
row = "# Column 1-7: log_10 of energy loss lengths (Mpc) for z=0, 0.5, 1, 2, 3, 5 and 10 \n"
f.write(row)
row = "# \n"
f.write(row)
row = "# \n"
f.write(row)
for i in (np.arange(len(int_length_pp_p_ebl_0))) :
    row = ""
    for j in (np.arange(8)) :
        row = row + str(M[i,j]) + " "
    row = row + "\n"
    f.write(row)
f.close()
"""

# Pion production with CMB
M = np.zeros((len(int_length_pi_p_cmb_0),8))
for i in (np.arange(len(int_length_pi_p_cmb_0))) :
    M[i,0] = energy[i]
    M[i,1] = np.log10(int_length_pi_p_cmb_0[i])
    M[i,2] = np.log10(int_length_pi_p_cmb_05[i])
    M[i,3] = np.log10(int_length_pi_p_cmb_1[i])
    M[i,4] = np.log10(int_length_pi_p_cmb_2[i])
    M[i,5] = np.log10(int_length_pi_p_cmb_3[i])
    M[i,6] = np.log10(int_length_pi_p_cmb_5[i])
    M[i,7] = np.log10(int_length_pi_p_cmb_10[i])
path_save_data = "interaction_length-pion_production-cmb-p.txt"
f = open(path_save_data,"w")
row = "# Interaction lenght for photopion production with CMB photons for protons \n"
f.write(row)
row = "# \n"
f.write(row)
row = "# Column 0: log_10 of energy (eV) \n"
f.write(row)
row = "# Column 1-7: log_10 of interaction lengths (Mpc) for z=0, 0.5, 1, 2, 3, 5 and 10 \n"
f.write(row)
row = "# \n"
f.write(row)
row = "# \n"
f.write(row)
for i in (np.arange(len(int_length_pi_p_cmb_0))) :
    row = ""
    for j in (np.arange(8)) :
        row = row + str(M[i,j]) + " "
    row = row + "\n"
    f.write(row)
f.close()

# Pion production with EBL 
M = np.zeros((len(int_length_pi_p_ebl_0),8))
for i in (np.arange(len(int_length_pi_p_ebl_0))) :
    M[i,0] = energy[i]
    M[i,1] = np.log10(int_length_pi_p_ebl_0[i])
    M[i,2] = np.log10(int_length_pi_p_ebl_05[i])
    M[i,3] = np.log10(int_length_pi_p_ebl_1[i])
    M[i,4] = np.log10(int_length_pi_p_ebl_2[i])
    M[i,5] = np.log10(int_length_pi_p_ebl_3[i])
    M[i,6] = np.log10(int_length_pi_p_ebl_5[i])
    M[i,7] = np.log10(int_length_pi_p_ebl_10[i])
path_save_data = "interaction_length-pion_production-ebl-p.txt"
f = open(path_save_data,"w")
row = "# Interaction lenght for pion production with EBL photons (Dominguez 11) for protons \n"
f.write(row)
row = "# \n"
f.write(row)
row = "# Column 0: log_10 of energy (eV) \n"
f.write(row)
row = "# Column 1-7: log_10 of interaction lengths (Mpc) for z=0, 0.5, 1, 2, 3, 5 and 10 \n"
f.write(row)
row = "# \n"
f.write(row)
row = "# \n"
f.write(row)
for i in (np.arange(len(int_length_pi_p_ebl_0))) :
    row = ""
    for j in (np.arange(8)) :
        row = row + str(M[i,j]) + " "
    row = row + "\n"
    f.write(row)
f.close()
