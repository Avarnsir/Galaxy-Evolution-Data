import numpy as np
import matplotlib.pyplot as plt

#Simulate Galaxy Dataset
np.random.seed(42)
num_galaxies = 100

sfr = np.random.uniform(0,10, num_galaxies) #SFR
morph_type = np.random.choice([1, 2], size = num_galaxies) #Morphological
local_density = np.random.uniform(0, 20, num_galaxies) #Local Density

avg_sfr_elliptical = np.mean(sfr[morph_type == 1])
avg_sfr_spiral = np.mean(sfr[morph_type == 2])
avg_density_high_sfr = np.mean(local_density[sfr > 5])

print(f"Average SFR for Elliptical Galaxies: {avg_sfr_elliptical:.2f}")
print(f"Average SFR for Spiral Galaxies: {avg_sfr_spiral:.2f}")
print(f"Average Local Density for High-SFR Galaxies: {avg_density_high_sfr:.2f}")

# Step 3: Create Scatter Plot
plt.figure(figsize=(10, 6))
colors = ['red' if mt == 1 else 'blue' for mt in morph_type]
plt.scatter(local_density, sfr, c=colors, alpha=0.7, label='Galaxies')
plt.colorbar(label='Morphological Type (Red=Elliptical, Blue=Spiral)')
plt.xlabel('Local Density (galaxies/Mpc³)')
plt.ylabel('Star Formation Rate (solar masses/year)')
plt.title('Galaxy Properties: Local Density vs. Star Formation Rate')
plt.grid(True)
plt.savefig('galaxy_plot.png')
plt.show()

