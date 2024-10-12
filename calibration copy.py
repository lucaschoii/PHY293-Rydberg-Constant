import fit_black_box as bb
import math
import numpy as np

def linear (m, x, b):
    return m * x + b

init_guess = (0, 1)
font_size = 20
xlabel = "(lambda - lambda_0)^-1"
ylabel = "y"
title = "Callibration"

lambda_0 = 286.0
lambda_0err = 2.0
wavelength = [447.1, 471.3, 492.2, 501.6, 587.6, 667.8, 434.0, 486.1, 656.3]
wav_err = [0.0000022, 0.0000024, 0.0000025, 0.000003, 0.000003, 0.000003, 0.0006, 0.0000024, 0.000007]


y = np.array([13.0, 11.85, 11.5, 11.25, 8.85, 7.5, 15.65, 12.15, 7.65])
x_inv = [w - lambda_0 for w in wavelength]
x = np.array([1.0 / x for x in x_inv])

yerr = np.array([0.15] * len(y))
xerr = [math.sqrt(wav_err[i]**2 + lambda_0err**2) / abs(wavelength[i] - lambda_0) for i in range(len(wavelength))]


(m, b), (merr, berr) = bb.plot_fit(linear, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size, title=title,
            xlabel=xlabel, ylabel=ylabel)



unknown_y = [7.0, 8.35, 8.65, 9.5, 10.65, 12.85, 14.15, 15.5, 16]
unknown_y_err = [0.15] * len(unknown_y)

unknown_lambda = [m / (y - b) + lambda_0 for y in unknown_y]

denom = [y - b for y in unknown_y]
denom_err = [math.sqrt(yerr**2 + berr**2) for yerr in unknown_y_err]

first_term_err = [m / denom[i] * math.sqrt((denom_err[i] / denom[i])**2 + (merr / m)**2) for i in range(len(denom))]
unknown_lambda_err = [math.sqrt(first_term_err[i]**2 + merr**2) for i in range(len(first_term_err))]

for i, l in enumerate(unknown_lambda):
    print(f"lambda_{i + 1} = {l} +/- {unknown_lambda_err[i]}")