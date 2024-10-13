from calibration import calibrate, lambda_0, lambda_0err
import math

h = 6.626070040 * 10**-34 # Js
c =  299792458            # m/s       
ev = 1.60218 * 10**-19    # J/eV

m, b, merr, berr = calibrate(plot=False)

sodium_y = [8.85, 8.65]
sodium_y_err = [0.15] * len(sodium_y)

sodium_lambda = [m / (y - b) + lambda_0 for y in sodium_y]
sodium_lambda_err = [math.sqrt((merr / (y - b))**2 + (-m * sodium_y_err[i] / (y - b)**2)**2 + (m * berr / (y - b)**2)**2 + lambda_0err**2) for i, y in enumerate(sodium_y)]


for i, l in enumerate(sodium_lambda):
    print(f"sodium_lambda_{i + 1} = {l} +/- {sodium_lambda_err[i]}")

print()

separation = sodium_lambda[1] - sodium_lambda[0]
separation_err = math.sqrt(sum(s**2 for s in sodium_lambda_err))
print(f"separation, nm = {separation} +/- {separation_err}")

cm_inv_sep = 1 / (separation * 10**7)
cm_inv_sep_err = cm_inv_sep * separation_err / separation
print(f"separation, cm^-1 = {cm_inv_sep} +/- {cm_inv_sep_err}")

E_f = [h * c / (l * 10 ** -9) / ev for l in sodium_lambda]
E_f_err = [E_f[i] * sodium_lambda_err[i]/sodium_lambda[i] for i in range(len(sodium_lambda))]
separation_E = abs(E_f[1] - E_f[0])
separation_E_err = math.sqrt(sum(s**2 for s in E_f_err))
print(f"separation, eV = {separation_E} +/- {separation_E_err}")

sep = h * c / ev / (separation * 10**-9)
print(sep)






