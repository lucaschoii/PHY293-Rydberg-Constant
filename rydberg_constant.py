# 1 / lambda = R_H (1/2^2 - 1/n^2)
# R_H = 1 / lambda (1/2^2 - 1/n^2)
import math

h = 6.626070040 * 10**-34 # Js
c =  299792458            # m/s       
ev = 1.60218 * 10**-19    # J/eV


wavelength = [434.0 * 10**-9, 486.1 * 10**-9, 656.3 * 10**-9]
wav_err = [0.0006 * 10**-9, 0.0000024 * 10**-9, 0.000007 * 10**-9]

n = [5, 4, 3]

R_H = [1.0 / (wavelength[i] * (1/2**2 - 1/n[i]**2)) for i in range(len(wavelength))]
R_H_err = [R_H[i] * math.sqrt((wav_err[i] / wavelength[i])**2) for i in range(len(wavelength))]

weights = [1 / err**2 for err in R_H_err]
weighted_avg = sum([R_H[i] * weights[i] for i in range(len(R_H))]) / sum(weights)
weighted_avg_err = 1 / math.sqrt(sum(weights))

for i, r in enumerate(R_H):
    print(f"R_H_{i + 1} = {r}  +/- {R_H_err[i]} 1/m")

print(f"R_H_wav = {weighted_avg} +/- {weighted_avg_err} 1/m")

R_EH = weighted_avg * h * c / ev
R_EH_err = R_EH * weighted_avg_err / weighted_avg


print(f"R_EH = {R_EH} +- {R_EH_err} eV")