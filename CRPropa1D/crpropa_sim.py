from crpropa import *
import numpy as np

# Main class
sim = ModuleList()

# Propagation module
sim.add(SimplePropagation())

# Interaction modules
sim.add(ElectronPairProduction(CMB()))
sim.add(PhotoPionProduction(CMB()))
sim.add(NuclearDecay())
sim.add(Redshift())

# End conditon 
sim.add(MaximumTrajectoryLength(1e4*Mpc))

# Observer and output file
obs = Observer()
obs.add(ObserverPoint())
output = TextOutput("events.txt", Output.Event1D)
output.enable(output.RedshiftColumn)
output.enable(output.WeightColumn)
obs.onDetection(output)
sim.add(obs)

# Source class
source = Source()
d_max_com = redshift2ComovingDistance(3.0)
source.add(SourceUniform1D(0.0,d_max_com))
source.add(SourceRedshiftEvolution(0.0,0.0,3.0))
source.add(SourceParticleType(nucleusId(1,1)))
source.add(SourcePowerLawSpectrum(0.01*EeV,1e4*EeV,-1.0))
source.add(SourceDirection(Vector3d(-1.0,0.0,0.0)))

# Simulation run 
sim.setShowProgress(True)
sim.run(source,int(1e5))
output.close()

# run with python crpropa_sim.py 
